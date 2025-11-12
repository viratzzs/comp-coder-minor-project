"""
Script to generate code solutions from prompts using a language model.
Handles generation, extraction, and storage of code.
"""

import argparse
from pathlib import Path
from loguru import logger
from tqdm import tqdm
import json
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.model_utils import (
    ModelHandler,
    DatasetHandler,
    CodeExtractor,
    FileManager,
)


def setup_logging(log_file: str = "outputs/generation.log"):
    """Setup logging configuration."""
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    logger.add(
        log_file,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        level="DEBUG",
    )
    logger.info("=" * 80)
    logger.info("Starting code generation script")
    logger.info("=" * 80)


def generate_solutions(
    model_name: str,
    adapter_path: str = None,
    dataset_name: str = "comp-coder-eval",
    output_dir: str = "outputs",
    start_idx: int = 0,
    end_idx: int = None,
    max_new_tokens: int = 2048,
    temperature: float = 0.7,
    top_p: float = 0.95,
    skip_existing: bool = True,
):
    """
    Generate code solutions for all samples in the dataset.
    
    Args:
        model_name: HuggingFace model name or path
        adapter_path: Path to LoRA adapter (optional)
        dataset_name: HuggingFace dataset name
        output_dir: Directory to save outputs
        start_idx: Starting sample index (inclusive)
        end_idx: Ending sample index (exclusive, None for all)
        max_new_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        top_p: Nucleus sampling parameter
        skip_existing: Whether to skip samples that already have generated code
    """
    # Initialize components
    logger.info("Initializing components...")
    
    model_handler = ModelHandler(
        model_name=model_name,
        adapter_path=adapter_path,
    )
    
    dataset_handler = DatasetHandler(dataset_name=dataset_name)
    file_manager = FileManager(base_dir=output_dir)
    code_extractor = CodeExtractor()
    
    # Determine range
    total_samples = len(dataset_handler)
    if end_idx is None:
        end_idx = total_samples
    end_idx = min(end_idx, total_samples)
    
    logger.info(f"Processing samples {start_idx} to {end_idx-1} (total: {end_idx - start_idx})")
    
    # Get existing generated indices if skipping
    existing_indices = set()
    if skip_existing:
        existing_indices = set(file_manager.get_all_generated_indices())
        logger.info(f"Found {len(existing_indices)} existing generations")
    
    # Statistics
    stats = {
        'total': 0,
        'skipped': 0,
        'generated': 0,
        'extracted': 0,
        'failed_extraction': 0,
    }
    
    # Process each sample
    for idx in tqdm(range(start_idx, end_idx), desc="Generating solutions"):
        stats['total'] += 1
        
        # Skip if already generated
        if skip_existing and idx in existing_indices:
            logger.info(f"Sample {idx}: Skipping (already generated)")
            stats['skipped'] += 1
            continue
        
        try:
            # Get sample
            sample = dataset_handler.get_sample(idx)
            prompt = sample['prompt']
            
            logger.info(f"Sample {idx}: Generating solution...")
            logger.debug(f"Sample {idx}: Prompt length: {len(prompt)} chars")
            
            # Generate code
            generated_text = model_handler.generate_code(
                prompt=prompt,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
            )
            
            stats['generated'] += 1
            logger.info(f"Sample {idx}: Generation complete ({len(generated_text)} chars)")
            
            # Save complete generation
            file_manager.save_completion(idx, generated_text)
            logger.debug(f"Sample {idx}: Saved complete generation")
            
            # Extract code
            extracted_code = code_extractor.extract_code(generated_text)
            
            if extracted_code:
                # Save extracted code
                file_manager.save_code(idx, extracted_code)
                stats['extracted'] += 1
                logger.info(f"Sample {idx}: Code extracted and saved ({len(extracted_code)} chars)")
            else:
                stats['failed_extraction'] += 1
                logger.warning(f"Sample {idx}: Failed to extract code from generation")
        
        except Exception as e:
            logger.error(f"Sample {idx}: Error during generation: {str(e)}")
            logger.exception(e)
    
    # Log final statistics
    logger.info("=" * 80)
    logger.info("Generation complete!")
    logger.info(f"Total samples processed: {stats['total']}")
    logger.info(f"Skipped (already generated): {stats['skipped']}")
    logger.info(f"Successfully generated: {stats['generated']}")
    logger.info(f"Successfully extracted: {stats['extracted']}")
    logger.info(f"Failed extraction: {stats['failed_extraction']}")
    logger.info("=" * 80)
    
    # Save statistics
    stats_file = Path(output_dir) / "generation_stats.json"
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
    logger.info(f"Statistics saved to: {stats_file}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate code solutions from prompts using a language model"
    )
    
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="HuggingFace model name or path",
    )
    
    parser.add_argument(
        "--adapter",
        type=str,
        default=None,
        help="Path to LoRA adapter (optional)",
    )
    
    parser.add_argument(
        "--dataset",
        type=str,
        default="comp-coder-eval",
        help="HuggingFace dataset name",
    )
    
    parser.add_argument(
        "--output-dir",
        type=str,
        default="outputs",
        help="Directory to save outputs",
    )
    
    parser.add_argument(
        "--start-idx",
        type=int,
        default=0,
        help="Starting sample index (inclusive)",
    )
    
    parser.add_argument(
        "--end-idx",
        type=int,
        default=None,
        help="Ending sample index (exclusive, None for all)",
    )
    
    parser.add_argument(
        "--max-new-tokens",
        type=int,
        default=2048,
        help="Maximum tokens to generate",
    )
    
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Sampling temperature",
    )
    
    parser.add_argument(
        "--top-p",
        type=float,
        default=0.95,
        help="Nucleus sampling parameter",
    )
    
    parser.add_argument(
        "--no-skip-existing",
        action="store_true",
        help="Regenerate even if code already exists",
    )
    
    parser.add_argument(
        "--log-file",
        type=str,
        default="outputs/generation.log",
        help="Path to log file",
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.log_file)
    
    # Log arguments
    logger.info("Arguments:")
    for arg, value in vars(args).items():
        logger.info(f"  {arg}: {value}")
    
    # Generate solutions
    generate_solutions(
        model_name=args.model,
        adapter_path=args.adapter,
        dataset_name=args.dataset,
        output_dir=args.output_dir,
        start_idx=args.start_idx,
        end_idx=args.end_idx,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_p=args.top_p,
        skip_existing=not args.no_skip_existing,
    )


if __name__ == "__main__":
    main()
