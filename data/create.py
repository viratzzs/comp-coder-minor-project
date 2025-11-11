import os
from dotenv import load_dotenv
import re
import pandas as pd
from datasets import Dataset, load_dataset

load_dotenv()

ds = load_dataset("open-r1/codeforces", "verifiable-prompts", split="train")#.select(range(5000))

print(f"Sampled {len(ds)} rows from the dataset.")

count = 0
def is_valid(sample):
    global count
    if sample['language'] == 'cpp':
        return False
    
    if int(sample['rating']) >= 1600:
        return False
    
    if len(sample['prompt']) > 4000:
        return False
    
    #if len(sample['official_tests']) > 1000:
    #    return False

    return True
    
#print(len(ds[-1]['problem']))

ds = ds.filter(is_valid)
ds = ds.shuffle(seed=42)
print(f"Found {len(ds)} samples after filtering.")

#ds.push_to_hub(repo_id="ViratChauhan/comp-coder-rl")