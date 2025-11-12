import os
from dotenv import load_dotenv
import torch
from datasets import load_dataset, Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, TrainingArguments
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig
load_dotenv()

model_name = "Qwen/Qwen3-1.7B"
output_dir="outputs/comp-coder-v1"
run_name="comp-coder-v1"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

def get_sol_data(split="train") -> Dataset:
    data = load_dataset('open-r1/codeforces-cots', "solutions_py", split=split)
    
    def build_text(example):
        full_messages = [
            {"role": "user", "content": example['messages'][0]['content']},
            {"role": "assistant", "content": example['messages'][1]['content']}
        ]
        text = tokenizer.apply_chat_template(full_messages, tokenize=False, add_generation_prompt=False)
        return {"text": text}
    
    data = data.map(build_text)
    # Keep only the text column to avoid conflicts with prompt/completion detection
    data = data.select_columns(['text'])
    return data

if __name__ == "__main__":
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    dataset = get_sol_data()

    print(dataset.column_names)
    print(dataset[0])
    training_args = SFTConfig(
        output_dir=output_dir,
        run_name=run_name,
        learning_rate=2e-5,
        weight_decay=0.1,
        warmup_ratio=0.1,
        lr_scheduler_type='cosine',
        bf16=True,
        logging_steps=1,
        per_device_train_batch_size=8,
        gradient_accumulation_steps=8,
        num_train_epochs=1,
        save_steps=1250,
        save_total_limit=2,
        gradient_checkpointing=True,
        dataset_text_field="text",
        packing=False,
        ddp_find_unused_parameters=False,
        report_to="wandb",
        #use_liger_kernel=True,
        #max_seq_length=4096,
    )

    peft_config = LoraConfig(
        r=32,
        lora_alpha=64,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "down_proj", "gate_proj"],
        task_type="CAUSAL_LM",
        lora_dropout=0.05,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        # quantization_config=bnb_config,
        dtype=torch.bfloat16,
        #use_cache=False if training_args.gradient_checkpointing else True,
        trust_remote_code=True,
    )
    
    if training_args.gradient_checkpointing:
        model.gradient_checkpointing_enable()

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        peft_config=peft_config,
        processing_class=tokenizer,
        #formatting_func=formatting_func,
    )

    print("Starting SFT training...")
    trainer.train()

    final_save_path = os.path.join(output_dir, "final_model_adapters")
    trainer.save_model(final_save_path)
    print(f"LoRA adapters saved to: {final_save_path}")

    repo_name = "ViratChauhan/comp-coder-v1"
    try:
        print(f"Pushing model adapters to Hugging Face Hub: {repo_name}")
        trainer.model.push_to_hub(
            repo_name,
            commit_message="Final SFT LoRA adapters for Solidity code generation",
            private=True,
            safe_serialization=True
        )
        
        print(f"Pushing tokenizer to Hugging Face Hub: {repo_name}")
        trainer.tokenizer.push_to_hub(
            repo_name,
            commit_message="Tokenizer for SFT trained model",
            private=True,
        )
        print(f"Model and tokenizer successfully pushed to: https://huggingface.co/{repo_name}")
    except Exception as e:
        print(f"Error pushing to hub: {e}")
        print(f"Model adapters saved locally in: {final_save_path}")

    print("SFT script finished.")