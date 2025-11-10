import os

os.environ["HF_HOME"] = "/workspace/huggingface/cache/"
#os.environ["VLLM_MAX_MODEL_LEN"] = "19000"
os.environ["WANDB_PROJECT"] = "comp-coder"

# Launch script with accelerate instead
# CUDA_VISIBLE_DEVICES=0,1 accelerate launch grpo-qwen3-8b.py 
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"
#os.environ["WORLD_SIZE"] = "1"
#os.environ["RANK"] = "0"
#os.environ["LOCAL_RANK"] = "0"
#os.environ["MASTER_ADDR"] = "localhost"
#os.environ["MASTER_PORT"] = "12355"
 
import torch

from datasets import load_dataset, Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, TextStreamer
from peft import LoraConfig
from vllm import SamplingParams
from trl import GRPOConfig, GRPOTrainer
from loguru import logger

from rewards import *


SYSTEM_PROMPT = """
You are an expert Python developer. Generate correct Python code.
First, analyze the requirements in <think> tags with your reasoning, design choices, and implementation approach. 
Afterwards, reason about how to generate the code that passes all given unit tests and compiles successfully.

Then provide your solution in <answer> tags using this exact format:

<answer>
A brief description of your solution. 

[code]
// your code here

</answer>

## Guidelines:
- Implement all functionalities by yourself and don't use any external libraries
"""

def get_sol_data(split = "train") -> Dataset:
    data = load_dataset('KolwaiiOfficial/instruct-rl-sol-v3', split=split)#.select(range(1000))
    data = data.map(lambda x: {
        'prompt': [
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': f"{x['problem']}\n\nUnit tests:\n{x['test']}"}
        ],
        'test': x['test']
    })
    return data

dataset = get_sol_data()

model_name = "Qwen/Qwen3-8B"

output_dir="outputs/comp-coder-v1"
run_name="comp-coder-v1"

if __name__ == "__main__":
    # 45k samples * 2 epochs * 2 generations = 180k samples
    # 180k / (2 batch size * 8 gradient accumulation * 2 workers) = 5624 steps (for 2 gpus)
    # 180k / (2 batch size * 8 gradient accumulation * 8 workers) = 1406 steps (for 8 gpus)
    # 180k / (2 batch size * 2 gradient accumulation * 8 workers) = 5624 steps (for 8 gpus)
    # UPDATED: 40k samples * 1 epoch * 2 generations = 80k samples
    # 80k / (2 batch size * 4 gradient accumulation * 8 workers) = 1250 steps (for 8 gpus)
    # 18k * 2 epochs * 2 generations = 72k samples
    # 72k / (2 batch size * 8 gradient accumulation * 4 workers) = 1125 steps (for 4 gpus)
    training_args = GRPOConfig(
        #importance_sampling_level="sequence", # GSPO implementation by Qwen team
        loss_type="bnpo",
        #beta=0.1,
        #epsilon=0.2,
        output_dir=output_dir,
        run_name=run_name,
        use_vllm=True,
        vllm_mode="colocate",
        repetition_penalty=1.05,
        #vllm_mode="server",
        vllm_gpu_memory_utilization=0.51,
        learning_rate=2e-5,
        temperature=0.7,
        top_p=0.95,
        top_k=-1,
        min_p=0.0,
        #weight_decay = 0.05, #exp
        warmup_ratio = 0.1,
        lr_scheduler_type='cosine',
        bf16=True,
        use_liger_loss=True,  # liger only supports token level sampling, so incompatible with GSPO(sequence level sampling)
        logging_steps=1,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,
        num_generations=2,
        max_prompt_length=4000,
        max_completion_length=16000,
        num_train_epochs=2,
        save_steps=100,
        # to prevent RTE: expected to mark a variable ready only once, add this in startup: --ddp_find_unused_parameters False
        gradient_checkpointing=True,
        ddp_find_unused_parameters=False,
        report_to="wandb",
        push_to_hub=True,
        #generation_kwargs={},
        wandb_log_unique_prompts=True,
    )

    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "down_proj", "gate_proj"],
        task_type="CAUSAL_LM",
        lora_dropout=0.05,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
    )#.to("cuda")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    
    trainer = GRPOTrainer(
        #model=model_name, # for vllm server mode
        model=model,
        processing_class=tokenizer,
        reward_funcs=[
            #xmlcount_reward_func,
            #format_reward_func,
            #reward_long_cot_chains,
            #reward_compilation,
            #reward_test_quality,
            #reward_test_passing,
        ],
        args=training_args,
        train_dataset=dataset,
        peft_config=peft_config
    )
    
    #trainer.train(resume_from_checkpoint="/workspace/training-mvp/src/code-rl/outputs/Qwen8B-RL/checkpoint-600")
    trainer.train()

    repo_name = "ViratChauhan/comp-coder-v1"

    trainer.save_model(f"{output_dir}/final_model")

    logger.info("Saving LoRA adapters...")
    if hasattr(trainer.model, 'save_pretrained'):
        trainer.model.save_pretrained(f"{output_dir}/final_lora")
    else:
        logger.warning("Warning: Could not save LoRA adapters separately")
    
    try:
        trainer.model.push_to_hub(
            repo_name,
            commit_message="push model",
            private=True,
        )
        
        trainer.tokenizer.push_to_hub(
            repo_name,
            commit_message="push tokenizer",
        )
        
        logger.success(f"Model successfully pushed to: https://huggingface.co/{repo_name}")
    except Exception as e:
        logger.error(f"Error pushing to hub: {e}")
        logger.info("Model saved locally in:", f"{output_dir}/final_model")
        logger.info("LoRA adapters saved in:", f"{output_dir}/final_lora")
