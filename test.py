from dotenv import load_dotenv
from datasets import load_dataset

load_dotenv()
ds = load_dataset("open-r1/codeforces-cots", "solutions_py", split="train")

print(ds)
#print(ds[0]['messages'][0]['content'])
print(ds[0]['messages'][1]['content'])
print(ds.features)