"""
Utility functions for model loading, code generation, extraction, and test execution.
"""

import re
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from loguru import logger
from datasets import load_dataset
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel


class ModelHandler:
    """Handles model loading and code generation."""
    
    def __init__(
        self,
        model_name: str,
        adapter_path: Optional[str] = None,
        max_seq_length: int = 24576,
        device: str = "cuda" if torch.cuda.is_available() else "cpu",
    ):
        """
        Initialize the model handler.
        
        Args:
            model_name: HuggingFace model name or path
            adapter_path: Path to LoRA adapter (optional)
            max_seq_length: Maximum sequence length
            device: Device to load model on
        """
        self.model_name = model_name
        self.adapter_path = adapter_path
        self.max_seq_length = max_seq_length
        self.device = device
        
        logger.info(f"Loading model: {model_name}")
        logger.info(f"Max sequence length: {max_seq_length}")
        logger.info(f"Device: {device}")
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        # Load base model
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
            device_map="auto",
            trust_remote_code=True,
        )
        
        # Load adapter if provided
        if adapter_path:
            logger.info(f"Loading LoRA adapter from: {adapter_path}")
            self.model = PeftModel.from_pretrained(self.model, adapter_path)
            self.model = self.model.merge_and_unload()
            logger.info("Adapter loaded and merged")
        
        self.model.eval()
        logger.info("Model loaded successfully")
    
    def generate_code(
        self,
        prompt: str,
        max_new_tokens: int = 2048,
        temperature: float = 0.7,
        top_p: float = 0.95,
        do_sample: bool = True,
    ) -> str:
        """
        Generate code from a prompt.
        
        Args:
            prompt: Input prompt
            max_new_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            top_p: Nucleus sampling parameter
            do_sample: Whether to use sampling
            
        Returns:
            Generated text
        """
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=self.max_seq_length - max_new_tokens,
        ).to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                do_sample=do_sample,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )
        
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Remove the prompt from the generated text
        if generated_text.startswith(prompt):
            generated_text = generated_text[len(prompt):].strip()
        
        return generated_text


class DatasetHandler:
    """Handles dataset loading and management."""
    
    def __init__(self, dataset_name: str = "comp-coder-eval"):
        """
        Initialize the dataset handler.
        
        Args:
            dataset_name: HuggingFace dataset name
        """
        self.dataset_name = dataset_name
        logger.info(f"Loading dataset: {dataset_name}")
        self.dataset = load_dataset(dataset_name, split="train")
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


class FileManager:
    """Manages file storage for generated code and completions."""
    
    def __init__(self, base_dir: str = "outputs"):
        """
        Initialize file manager.
        
        Args:
            base_dir: Base directory for outputs
        """
        self.base_dir = Path(base_dir)
        self.code_dir = self.base_dir / "generated_code"
        self.completions_dir = self.base_dir / "completions"
        
        # Create directories
        self.code_dir.mkdir(parents=True, exist_ok=True)
        self.completions_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Output directories created: {self.base_dir}")
    
    def save_completion(self, idx: int, completion: str) -> Path:
        """
        Save the complete model generation.
        
        Args:
            idx: Sample index
            completion: Complete generated text
            
        Returns:
            Path to saved file
        """
        filepath = self.completions_dir / f"sample_{idx}.txt"
        filepath.write_text(completion, encoding='utf-8')
        logger.debug(f"Saved completion to: {filepath}")
        return filepath
    
    def save_code(self, idx: int, code: str) -> Path:
        """
        Save extracted code.
        
        Args:
            idx: Sample index
            code: Extracted Python code
            
        Returns:
            Path to saved file
        """
        filepath = self.code_dir / f"sample_{idx}.py"
        filepath.write_text(code, encoding='utf-8')
        logger.debug(f"Saved code to: {filepath}")
        return filepath
    
    def load_code(self, idx: int) -> Optional[str]:
        """
        Load generated code for a sample.
        
        Args:
            idx: Sample index
            
        Returns:
            Code content or None if file doesn't exist
        """
        filepath = self.code_dir / f"sample_{idx}.py"
        if filepath.exists():
            return filepath.read_text(encoding='utf-8')
        return None
    
    def get_all_generated_indices(self) -> List[int]:
        """
        Get list of all sample indices that have generated code.
        
        Returns:
            List of sample indices
        """
        indices = []
        for filepath in self.code_dir.glob("sample_*.py"):
            try:
                idx = int(filepath.stem.split('_')[1])
                indices.append(idx)
            except (ValueError, IndexError):
                logger.warning(f"Invalid filename: {filepath}")
        
        return sorted(indices)
