import os
os.environ["HF_TOKEN"] = "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"
os.environ["HF_HOME"] = "/workspace/huggingface/cache/"

import re
import pandas as pd
from datasets import Dataset, load_dataset

ds = load_dataset("open-r1/codeforces", split="train")#.select(range(5000))

print(f"Sampled {len(ds)} rows from the dataset.")

count = 0
def is_valid(sample):
    global count
    if len(sample['description']) > 2400:
        return False
    
    if len(sample['test']) > 3000:
        return False

    #if "LiquidityPool.sol" in sample['test']:
    #    if count > 1000:
    #        return False
    #    count += 1

    return True
    
#print(len(ds[-1]['problem']))

ds = ds.filter(is_valid)
ds = ds.shuffle(seed=42)
print(f"Found {len(ds)} samples after filtering.")

ds.push_to_hub(repo_id="KolwaiiOfficial/instruct-rl-sol-v3")
#ds.push_to_hub(repo_id="KolwaiiOfficial/instruct-rl-sol-v3-hard")