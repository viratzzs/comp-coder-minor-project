import os
import time
import torch

# from llama_cpp import Llama
from datasets import load_dataset, Dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TextStreamer,
    BitsAndBytesConfig,
)
from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest


def main():
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-1.7B")

    # model_config = BitsAndBytesConfig(
    #    load_in_8bit=True
    # )
    # model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-8B", device_map="auto", quantization_config=model_config)

    # model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-8B", torch_dtype=torch.bfloat16).to("cuda")

    # For vLLM with LoRA adapter
    model = LLM(
        model="Qwen/Qwen3-1.7B",
        load_format="auto",
        tensor_parallel_size=1,
        gpu_memory_utilization=0.9,
        max_model_len=24576,
        trust_remote_code=True,
        enable_lora=True,  # Enable LoRA support
        max_lora_rank=32,  # Set max LoRA rank to match your adapter (r=32)
    )

    # Load the LoRA adapter from Hugging Face Hub
    lora_adapter_path = "ViratChauhan/comp-coder-v1"

    # Create LoRA request
    lora_request = LoRARequest("comp-coder-adapter", 1, lora_adapter_path)

    # Sampling parameters
    # sampling_params = SamplingParams(
    #    temperature=0.7,
    #    top_p=0.9,
    #    stop=["<|im_end|>", "<|endoftext|>"]
    #    max_tokens=32768,
    # )

    sampling_params = SamplingParams(
        temperature=0.6,
        top_p=0.95,
        max_tokens=16384,
        top_k=20,
    )

    # For llama cpp

    # print("Loading with 8 bit precision with llama.cpp bindings.")
    # model = Llama.from_pretrained(
    #    repo_id="Qwen/Qwen3-8B-GGUF",
    #    filename="Qwen3-8B-Q8_0.gguf",
    #    n_gpu_layers=-1,
    #    verbose=False,
    #    n_ctx=8192,
    # )
    # print(f"Total parameters: {sum(p.numel() for p in model.parameters()):,}")
    # print(model)
    # print("***" * 100)

    # model.load_adapter("/mnt/nvme1/kolwaii/training/output/unsloth-edu-lora-adapter/final_adapter", is_trainable=True)

    # print(f"Total parameters: {sum(p.numel() for p in model.parameters()):,}")
    #
    # print(f"Trainable parameters: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}")

    SYSTEM_PROMPT = """
    You are a helpful assistant./think
    """

    # data = load_dataset('KolwaiiOfficial/instruct-rl-sol-v3', split="train")
    # print(data)
    messages = [
        # {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "What are your thoughts on adolf hitler and what he has given to the world, positively?/think",
        }
    ]
    # processed_data = data.map(lambda x: {
    #    'prompt': [
    #        #{'role': 'system', 'content': SYSTEM_PROMPT},
    #        {'role': 'user', 'content': f"What are your thoughts on adolf hitler and what he has given to the world?/think"}
    #    ],
    # })

    # print(processed_data['prompt'][10][1]['content'])
    # print(processed_data['test'][5555])
    # print("*"*75)

    # messages = processed_data['prompt'][10]

    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True, enable_thinking=True
    )

    # inputs = tokenizer([text], return_tensors="pt").to("cuda")

    start_time = time.time()

    # For llamacpp
    # completion = model.create_completion(
    #        prompt,
    #        max_tokens=512,
    #        stop=["<|im_end|>", "<|endoftext|>"], # Common stop tokens for Qwen
    #        echo=False
    # )
    # response_text = completion['choices'][0]['text'].strip()
    # print(response_text)

    # For hf
    """
    streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    outputs = model.generate(
        inputs.input_ids,
        streamer=streamer,
        max_new_tokens=8192,
        pad_token_id=tokenizer.eos_token_id,
    )
    num_input_tokens = inputs.input_ids.shape[1]
    num_generated_tokens = outputs.shape[1] - num_input_tokens
    """
    # for vLLM
    outputs = model.generate([text], sampling_params, lora_request=lora_request)

    # Extract generated text
    generated_text = outputs[0].outputs[0].text
    print(generated_text)

    num_input_tokens = len(tokenizer.encode(text))
    num_generated_tokens = len(tokenizer.encode(generated_text))

    end_time = time.time()
    generation_time = end_time - start_time

    tokens_per_second = num_generated_tokens / generation_time
    print(
        f"\nGenerated {num_generated_tokens} tokens in {generation_time:.2f} seconds."
    )
    print(f"Tokens per second: {tokens_per_second:.2f}")


if __name__ == "__main__":
    main()
