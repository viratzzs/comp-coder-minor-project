import re
import subprocess
import tempfile
from dotenv import load_dotenv
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from loguru import logger
from datasets import load_dataset
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest
load_dotenv()

class ModelHandler:
    """Handles model loading and code generation using vLLM."""
    
    def __init__(
        self,
        model_name: str,
        adapter_path: Optional[str] = None,
    ):
        self.model_name = model_name
        self.adapter_path = adapter_path
        
        logger.info(f"Loading model with vLLM: {model_name}")
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        self.model = LLM(
            model=model_name,
            load_format="auto",
            tensor_parallel_size=1,
            gpu_memory_utilization=0.9,
            max_model_len=24576,
            trust_remote_code=True,
            enable_lora=adapter_path is not None,
            max_lora_rank=32 if adapter_path else None,
        )
        
        self.lora_request = None
        if adapter_path:
            logger.info(f"Loading LoRA adapter: {adapter_path}")
            self.lora_request = LoRARequest("adapter", 1, adapter_path)
        
        self.sampling_params = SamplingParams(
            temperature=0.6,
            top_p=0.95,
            min_p=0,
            max_tokens=24576,
            top_k=20,
        )
        
        logger.info("Model loaded successfully")
    
    def generate_code(self, prompt: str) -> str:
        """Generate code from a single prompt."""
        try:
            text = self.tokenizer.apply_chat_template(
                [{"role": "user", "content": prompt}],
                tokenize=False,
                add_generation_prompt=True,
            )
        except:
            text = prompt
        
        outputs = self.model.generate(
            [text],
            self.sampling_params,
            lora_request=self.lora_request,
        )
        
        generated_text = outputs[0].outputs[0].text
        
        return generated_text
    
    def generate_code_batch(self, prompts: List[str]) -> List[str]:
        """Generate code from multiple prompts in batch."""
        texts = []
        for prompt in prompts:
            try:
                text = self.tokenizer.apply_chat_template(
                    [{"role": "user", "content": prompt}],
                    tokenize=False,
                    add_generation_prompt=True,
                )
            except:
                text = prompt
            texts.append(text)
        
        outputs = self.model.generate(
            texts,
            self.sampling_params,
            lora_request=self.lora_request,
        )
        
        generated_texts = [output.outputs[0].text for output in outputs]
        
        return generated_texts


class DatasetHandler:
    """Handles dataset loading and management."""
    
    def __init__(self, dataset_name: str = "comp-coder-eval"):
        """
        Args:
            dataset_name: HuggingFace dataset name
        """
        self.dataset_name = dataset_name
        logger.info(f"Loading dataset: {dataset_name}")
        self.dataset = load_dataset(dataset_name, split="test")
        logger.info(f"Dataset loaded: {len(self.dataset)} samples")
    
    def get_sample(self, idx: int) -> Dict[str, Any]:
        """Get a single sample from the dataset."""
        return self.dataset[idx]
    
    def __len__(self) -> int:
        """Get the number of samples in the dataset."""
        return len(self.dataset)
    
    def __iter__(self):
        """Iterate over the dataset."""
        return iter(self.dataset)


class CodeExtractor:
    """Extracts Python code from generated text."""
    
    @staticmethod
    def extract_code(generated_text: str) -> Optional[str]:
        """
        Extract Python code from markdown code blocks.
        
        Args:
            generated_text: Generated text containing code
            
        Returns:
            Extracted code or None if no code found
        """
        # Pattern to match ```python ... ``` or ``` ... ```
        patterns = [
            r'```python\s*\n(.*?)```',
            r'```\s*\n(.*?)```',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, generated_text, re.DOTALL)
            if matches:
                # Return the last code block (usually the complete solution)
                code = matches[-1].strip()
                logger.debug(f"Extracted code block ({len(code)} chars)")
                return code
        
        logger.warning("No code block found in generated text")
        return None


class CodeExecutor:
    """Executes Python code and validates outputs."""
    
    @staticmethod
    def check_syntax(code: str) -> Tuple[bool, Optional[str]]:
        """
        Check if code compiles without syntax errors.
        
        Args:
            code: Python code to check
            
        Returns:
            Tuple of (compiles: bool, error_message: Optional[str])
        """
        try:
            compile(code, '<string>', 'exec')
            return True, None
        except SyntaxError as e:
            return False, str(e)
    
    @staticmethod
    def run_code(
        code: str,
        test_input: str,
        timeout: int = 5,
    ) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Run code with given input and return output.
        
        Args:
            code: Python code to execute
            test_input: Input to provide to the code
            timeout: Timeout in seconds
            
        Returns:
            Tuple of (success: bool, output: Optional[str], error: Optional[str])
        """
        # Create a temporary file with the code
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        try:
            # Run the code with subprocess
            result = subprocess.run(
                ['python', temp_file],
                input=test_input,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            
            # Clean up
            Path(temp_file).unlink()
            
            if result.returncode == 0:
                return True, result.stdout, None
            else:
                return False, None, result.stderr
                
        except subprocess.TimeoutExpired:
            Path(temp_file).unlink()
            return False, None, "Timeout expired"
        except Exception as e:
            Path(temp_file).unlink()
            return False, None, str(e)
    
    @staticmethod
    def compare_outputs(actual: str, expected: str) -> bool:
        """
        Compare actual and expected outputs.
        
        Args:
            actual: Actual output from code execution
            expected: Expected output
            
        Returns:
            True if outputs match, False otherwise
        """
        # Normalize whitespace and line endings
        actual_normalized = actual.strip().replace('\r\n', '\n')
        expected_normalized = expected.strip().replace('\r\n', '\n')
        
        return actual_normalized == expected_normalized
    
    @staticmethod
    def evaluate_sample(
        code: str,
        test_cases: List[Dict[str, str]],
        timeout: int = 5,
    ) -> Tuple[bool, int, int, List[Dict[str, Any]]]:
        """
        Evaluate code against all test cases.
        
        Args:
            code: Python code to evaluate
            test_cases: List of test cases with 'input' and 'output' keys
            timeout: Timeout per test case in seconds
            
        Returns:
            Tuple of (all_passed: bool, passed_count: int, total_count: int, results: List[Dict])
        """
        results = []
        passed_count = 0
        total_count = len(test_cases)
        
        for i, test_case in enumerate(test_cases):
            test_input = test_case['input']
            expected_output = test_case['output']
            
            success, actual_output, error = CodeExecutor.run_code(
                code, test_input, timeout
            )
            
            if success:
                passed = CodeExecutor.compare_outputs(actual_output, expected_output)
                if passed:
                    passed_count += 1
                
                results.append({
                    'test_index': i,
                    'success': True,
                    'passed': passed,
                    'actual_output': actual_output,
                    'expected_output': expected_output,
                    'error': None,
                })
            else:
                results.append({
                    'test_index': i,
                    'success': False,
                    'passed': False,
                    'actual_output': None,
                    'expected_output': expected_output,
                    'error': error,
                })
        
        all_passed = passed_count == total_count
        return all_passed, passed_count, total_count, results

