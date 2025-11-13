import argparse
from pathlib import Path
from loguru import logger
from tqdm import tqdm
import json
import sys

sys.path.append(str(Path(__file__).parent.parent))

from utils.env_utils import (
    DatasetHandler,
    CodeExecutor,
)


def setup_logging(log_file: str = "outputs/evaluation.log"):
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    logger.add(
        log_file,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        level="DEBUG",
    )
    logger.info("=" * 80)
    logger.info("Starting evaluation script")
    logger.info("=" * 80)


def evaluate_solutions(
    dataset_name: str = "comp-coder-eval",
    output_dir: str = "outputs",
    timeout: int = 5,
    start_idx: int = 0,
    end_idx: int = None,
):
    """
    Evaluate all generated code solutions.

    Args:
        dataset_name: HuggingFace dataset name
        output_dir: Directory containing generated code
        timeout: Timeout per test case in seconds
        start_idx: Starting sample index (inclusive)
        end_idx: Ending sample index (exclusive, None for all)
    """
    # Initialize components
    logger.info("Initializing components...")

    dataset_handler = DatasetHandler(dataset_name=dataset_name)
    code_executor = CodeExecutor()

    # Setup paths
    output_path = Path(output_dir)
    code_dir = output_path / "generated_code"

    # Get all generated code indices
    generated_indices = []
    if code_dir.exists():
        for filepath in code_dir.glob("sample_*.py"):
            try:
                idx = int(filepath.stem.split("_")[1])
                generated_indices.append(idx)
            except (ValueError, IndexError):
                logger.warning(f"Invalid filename: {filepath}")
        generated_indices = sorted(generated_indices)

    logger.info(f"Found {len(generated_indices)} generated solutions")

    # Filter by range
    total_samples = len(dataset_handler)
    if end_idx is None:
        end_idx = total_samples
    end_idx = min(end_idx, total_samples)

    # Filter indices within range
    indices_to_evaluate = [
        idx for idx in generated_indices if start_idx <= idx < end_idx
    ]

    logger.info(
        f"Evaluating {len(indices_to_evaluate)} solutions in range [{start_idx}, {end_idx})"
    )

    # Statistics
    stats = {
        "total_samples": len(indices_to_evaluate),
        "compiled": 0,
        "failed_compilation": 0,
        "passed_all_tests": 0,
        "failed_some_tests": 0,
        "total_test_cases": 0,
        "passed_test_cases": 0,
    }

    # Detailed results for each sample
    detailed_results = []

    # Process each sample
    for idx in tqdm(indices_to_evaluate, desc="Evaluating solutions"):
        try:
            # Load generated code
            code_file = code_dir / f"sample_{idx}.py"
            if not code_file.exists():
                logger.warning(f"Sample {idx}: Code file not found, skipping")
                continue

            code = code_file.read_text(encoding="utf-8")

            # Get sample from dataset
            sample = dataset_handler.get_sample(idx)
            test_cases = sample["official_tests"]

            logger.info(f"Sample {idx}: Evaluating {len(test_cases)} test case(s)")

            # Check syntax/compilation
            compiles, syntax_error = code_executor.check_syntax(code)

            if not compiles:
                stats["failed_compilation"] += 1
                logger.warning(f"Sample {idx}: Failed to compile - {syntax_error}")

                detailed_results.append(
                    {
                        "sample_index": idx,
                        "compiles": False,
                        "syntax_error": syntax_error,
                        "passed_all_tests": False,
                        "passed_test_count": 0,
                        "total_test_count": len(test_cases),
                        "test_results": [],
                    }
                )
                continue

            stats["compiled"] += 1
            logger.debug(f"Sample {idx}: Code compiled successfully")

            # Run all test cases
            all_passed, passed_count, total_count, test_results = (
                code_executor.evaluate_sample(
                    code=code,
                    test_cases=test_cases,
                    timeout=timeout,
                )
            )

            stats["total_test_cases"] += total_count
            stats["passed_test_cases"] += passed_count

            if all_passed:
                stats["passed_all_tests"] += 1
                logger.info(f"Sample {idx}: PASSED all {total_count} test case(s)")
            else:
                stats["failed_some_tests"] += 1
                logger.warning(
                    f"Sample {idx}: FAILED - passed {passed_count}/{total_count} test case(s)"
                )

            # Store detailed results
            detailed_results.append(
                {
                    "sample_index": idx,
                    "compiles": True,
                    "syntax_error": None,
                    "passed_all_tests": all_passed,
                    "passed_test_count": passed_count,
                    "total_test_count": total_count,
                    "test_results": test_results,
                }
            )

            # Log individual test results
            for test_result in test_results:
                test_idx = test_result["test_index"]
                if test_result["success"]:
                    if test_result["passed"]:
                        logger.debug(f"Sample {idx}, Test {test_idx}: PASSED")
                    else:
                        logger.debug(
                            f"Sample {idx}, Test {test_idx}: FAILED (output mismatch)"
                        )
                else:
                    logger.debug(
                        f"Sample {idx}, Test {test_idx}: ERROR - {test_result['error']}"
                    )

        except Exception as e:
            logger.error(f"Sample {idx}: Error during evaluation: {str(e)}")
            logger.exception(e)

    # Calculate metrics
    compile_at_1 = (
        (stats["compiled"] / stats["total_samples"] * 100)
        if stats["total_samples"] > 0
        else 0
    )
    pass_at_1 = (
        (stats["passed_all_tests"] / stats["total_samples"] * 100)
        if stats["total_samples"] > 0
        else 0
    )

    # Log final statistics
    logger.info("=" * 80)
    logger.info("Evaluation complete!")
    logger.info("=" * 80)
    logger.info(f"Total samples evaluated: {stats['total_samples']}")
    logger.info(f"Compiled successfully: {stats['compiled']}")
    logger.info(f"Failed compilation: {stats['failed_compilation']}")
    logger.info(f"Passed all tests: {stats['passed_all_tests']}")
    logger.info(f"Failed some tests: {stats['failed_some_tests']}")
    logger.info(f"Total test cases run: {stats['total_test_cases']}")
    logger.info(f"Test cases passed: {stats['passed_test_cases']}")
    logger.info("=" * 80)
    logger.info(f"compile@1: {compile_at_1:.2f}%")
    logger.info(f"pass@1: {pass_at_1:.2f}%")
    logger.info("=" * 80)

    # Prepare results
    results = {
        "metrics": {
            "compile@1": compile_at_1,
            "pass@1": pass_at_1,
        },
        "statistics": stats,
        "detailed_results": detailed_results,
    }

    # Save results
    results_file = Path(output_dir) / "evaluation_results.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2)
    logger.info(f"Results saved to: {results_file}")

    # Also save a summary file
    summary_file = Path(output_dir) / "evaluation_summary.txt"
    with open(summary_file, "w") as f:
        f.write("=" * 80 + "\n")
        f.write("EVALUATION SUMMARY\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Dataset: {dataset_name}\n")
        f.write(f"Total samples evaluated: {stats['total_samples']}\n\n")
        f.write(f"Compiled successfully: {stats['compiled']}\n")
        f.write(f"Failed compilation: {stats['failed_compilation']}\n")
        f.write(f"Passed all tests: {stats['passed_all_tests']}\n")
        f.write(f"Failed some tests: {stats['failed_some_tests']}\n\n")
        f.write(f"Total test cases run: {stats['total_test_cases']}\n")
        f.write(f"Test cases passed: {stats['passed_test_cases']}\n\n")
        f.write("=" * 80 + "\n")
        f.write("METRICS\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"compile@1: {compile_at_1:.2f}%\n")
        f.write(f"pass@1: {pass_at_1:.2f}%\n\n")

    logger.info(f"Summary saved to: {summary_file}")

    return results


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Evaluate generated code solutions")

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
        help="Directory containing generated code",
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=5,
        help="Timeout per test case in seconds",
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
        "--log-file",
        type=str,
        default="outputs/evaluation.log",
        help="Path to log file",
    )

    args = parser.parse_args()

    # Setup logging
    setup_logging(args.log_file)

    # Log arguments
    logger.info("Arguments:")
    for arg, value in vars(args).items():
        logger.info(f"  {arg}: {value}")

    # Evaluate solutions
    evaluate_solutions(
        dataset_name=args.dataset,
        output_dir=args.output_dir,
        timeout=args.timeout,
        start_idx=args.start_idx,
        end_idx=args.end_idx,
    )


if __name__ == "__main__":
    main()
