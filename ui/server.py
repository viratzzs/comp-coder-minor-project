import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from pyngrok import ngrok
from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest

load_dotenv()
ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN"))

app = FastAPI(title="Comp Coder API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Loading vLLM model with LoRA adapter...")
llm = LLM(
    model="Qwen/Qwen3-1.7B",
    enable_lora=True,
    max_lora_rank=32,
    trust_remote_code=True,
    gpu_memory_utilization=0.9,
    max_model_len=16384,
)

lora_request = LoRARequest(
    lora_name="comp-coder",
    lora_int_id=1,
    lora_path="ViratChauhan/comp-coder-v1"
)

print("Model loaded successfully!")

class SolveRequest(BaseModel):
    problem: str
    #system_prompt: str = None
    #temperature: float = 0.2
    max_tokens: int = 512

class SolveResponse(BaseModel):
    output: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/solve", response_model=SolveResponse)
async def solve(request: SolveRequest):
    """
    Generate solution for competitive programming problem using vLLM with LoRA adapter.
    """
    SYSTEM_PROMPT = """
    You are an experienced Python developer specializing in solving competitive programming problems. Assist the user with all inquiries.
    """
    prompt = f"{SYSTEM_PROMPT}\n\n{request.problem}"
    
    sampling_params = SamplingParams(
        temperature=0.6,
        top_p=0.95,
        min_p=0,
        max_tokens=request.max_tokens,
    )
    
    outputs = llm.generate(
        prompts=[prompt],
        sampling_params=sampling_params,
        lora_request=lora_request
    )
    
    output_text = outputs[0].outputs[0].text
    
    return SolveResponse(output=output_text)

if __name__ == "__main__":
    public_url = ngrok.connect(8001)
    print(f"\n{'='*60}")
    print(f"Public URL: {public_url.public_url}")
    print(f"Set COLAB_ENDPOINT to: {public_url.public_url}/solve")
    print(f"{'='*60}\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8001)