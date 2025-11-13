import argparse

from dotenv import load_dotenv
from pathlib import Path
from loguru import logger
from tqdm import tqdm
import json
import sys
load_dotenv()
sys.path.append(str(Path(__file__).parent.parent))

from utils.env_utils import (
    ModelHandler,
    DatasetHandler,
    CodeExtractor,
)

def setup_logging(log_file: str = "outputs/generation.log"):
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
    output_dir: str = "outputs",
    start_idx: int = 0,
    end_idx: int = None,
):
    """
    Args:
        model_name: HuggingFace model name or path
        adapter_path: Path to LoRA adapter (optional)
        output_dir: Directory to save outputs
        start_idx: Starting sample index (inclusive)
        end_idx: Ending sample index (exclusive, None for all)
    """
    logger.info("Initializing components...")

    # Create model-specific directory (using only model name, not org)
    model_dir_name = model_name.split("/")[-1]
    output_path = Path(output_dir) / model_dir_name
    code_dir = output_path / "generated_code"
    completions_dir = output_path / "completions"
    code_dir.mkdir(parents=True, exist_ok=True)
    completions_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directories: {output_path}")

    model_handler = ModelHandler(
        model_name=model_name,
        adapter_path=adapter_path,
    )

    dataset_handler = DatasetHandler(dataset_name="ViratChauhan/comp-coder-eval")
    code_extractor = CodeExtractor()

    #total_samples = len(dataset_handler)
    total_samples = 149
    if end_idx is None:
        end_idx = total_samples
    end_idx = min(end_idx, total_samples)

    logger.info(
        f"Processing samples {start_idx} to {end_idx-1} (total: {end_idx - start_idx})"
    )

    existing_indices = set()
    for filepath in code_dir.glob("sample_*.py"):
        try:
            idx = int(filepath.stem.split("_")[1])
            existing_indices.add(idx)
        except (ValueError, IndexError):
            logger.warning(f"Invalid filename: {filepath}")
    logger.info(f"Found {len(existing_indices)} existing generations")

    stats = {
        "total": 0,
        "skipped": 0,
        "generated": 0,
        "extracted": 0,
        "failed_extraction": 0,
    }

    samples_to_process = []
    for idx in range(start_idx, end_idx):
        stats["total"] += 1
        
        if idx in existing_indices:
            logger.info(f"Sample {idx}: Skipping (already generated)")
            stats["skipped"] += 1
            continue
        
        sample = dataset_handler.get_sample(idx)
        samples_to_process.append((idx, sample))
    
    logger.info(f"Will generate {len(samples_to_process)} new samples in batches of 50")
    
    batch_size = 50
    for batch_start in tqdm(range(0, len(samples_to_process), batch_size), desc="Processing batches"):
        batch_end = min(batch_start + batch_size, len(samples_to_process))
        batch = samples_to_process[batch_start:batch_end]
        
        batch_indices = [item[0] for item in batch]
        batch_prompts = [item[1]["prompt"] for item in batch]
        
        logger.info(f"Generating batch {batch_start//batch_size + 1}: samples {batch_indices[0]}-{batch_indices[-1]} ({len(batch)} samples)")
        
        try:
            generated_texts = model_handler.generate_code_batch(batch_prompts)
            
            for idx, generated_text in zip(batch_indices, generated_texts):
                try:
                    stats["generated"] += 1
                    logger.info(f"Sample {idx}: Generation complete ({len(generated_text)} chars)")
                    
                    completion_file = completions_dir / f"sample_{idx}.txt"
                    completion_file.write_text(generated_text, encoding="utf-8")
                    logger.debug(f"Sample {idx}: Saved completion")
                    
                    extracted_code = code_extractor.extract_code(generated_text)
                    
                    if extracted_code:
                        code_file = code_dir / f"sample_{idx}.py"
                        code_file.write_text(extracted_code, encoding="utf-8")
                        stats["extracted"] += 1
                        logger.info(f"Sample {idx}: Code extracted and saved ({len(extracted_code)} chars)")
                    else:
                        stats["failed_extraction"] += 1
                        logger.warning(f"Sample {idx}: Failed to extract code from generation")
                
                except Exception as e:
                    logger.error(f"Sample {idx}: Error during post-processing: {str(e)}")
                    logger.exception(e)
        
        except Exception as e:
            logger.error(f"Batch generation failed for indices {batch_indices[0]}-{batch_indices[-1]}: {str(e)}")
            logger.exception(e)

    logger.info("=" * 80)
    logger.info("Generation complete!")
    logger.info(f"Total samples processed: {stats['total']}")
    logger.info(f"Skipped (already generated): {stats['skipped']}")
    logger.info(f"Successfully generated: {stats['generated']}")
    logger.info(f"Successfully extracted: {stats['extracted']}")
    logger.info(f"Failed extraction: {stats['failed_extraction']}")
    logger.info("=" * 80)

    stats_file = Path(output_dir) / "generation_stats.json"
    with open(stats_file, "w") as f:
        json.dump(stats, f, indent=2)
    logger.info(f"Statistics saved to: {stats_file}")


def main():
    parser = argparse.ArgumentParser(description="Generate code solutions using vLLM")

    parser.add_argument(
        "--model",
        type=str,
        default="Qwen/Qwen3-1.7B",
        #required=True,
        help="HuggingFace model name or path",
    )

    parser.add_argument(
        "--adapter",
        type=str,
        #default=None,
        default="ViratChauhan/comp-coder-v1",
        help="Path to LoRA adapter (optional)",
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
        help="Starting sample index",
    )

    parser.add_argument(
        "--end-idx",
        type=int,
        default=None,
        help="Ending sample index (None for all)",
    )

    args = parser.parse_args()

    # Create model-specific directory for logs
    model_dir_name = args.model.split("/")[-1]
    log_dir = Path(args.output_dir) / model_dir_name
    log_dir.mkdir(parents=True, exist_ok=True)
    setup_logging(f"{log_dir}/generation.log")

    logger.info("Arguments:")
    for arg, value in vars(args).items():
        logger.info(f"  {arg}: {value}")

    generate_solutions(
        model_name=args.model,
        adapter_path=args.adapter,
        output_dir=args.output_dir,
        start_idx=args.start_idx,
        end_idx=args.end_idx,
    )


if __name__ == "__main__":
    main()
