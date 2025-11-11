from dotenv import load_dotenv
import re
import pandas as pd
from datasets import Dataset, load_dataset
load_dotenv()

ds = load_dataset("open-r1/codeforces", "verifiable-prompts", split="test")#.select(range(5000))

print(f"Sampled {len(ds)} rows from the dataset.")
print(ds)
#print(ds[0]['rating'])

count = 0
def is_valid(sample):
    global count
    if sample['language'] == 'cpp':
        return False
    if sample['rating'] is None:
        return False
    return True

ds = ds.filter(is_valid)
columns_to_keep = ['prompt', 'rating', 'tags', 'official_tests']
columns_to_remove = [col for col in ds.column_names if col not in columns_to_keep]
ds = ds.remove_columns(columns_to_remove)
print(f"Found {len(ds)} samples after filtering.")

ds.push_to_hub(repo_id="ViratChauhan/comp-coder-eval")