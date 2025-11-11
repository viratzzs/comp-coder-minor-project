# Comp Coder v1
This repository contains the code for training a competitive programming llm using distillation from Deepseek R1. the base model used is qwen3-1.7B and the distillation is done by performing Supervised Fine Tuning(SFT) on 5 responses per problem by the larger R1 model. The dataset is https://huggingface.co/datasets/open-r1/codeforces-cots and we are using the python subset which contains a total of nearly 10k training samples.

## TODO 
### Training stuff (SFT distillation)
- Use codeforces-cots dataset.
- launch training :) (ongoing)

### Training stuff (RL)
- Create subset of openr1 dataset with 1000 samples (split of easy-medium-hard: 3-5-2, use dict to maintain range of problem ratings)
- Fix prompt and content util script
- Script to create and run generated code sequentially in environment
- Figure out how to use the i/o tests as a verifier
- Create prototype for rewards
- Read kalo's blog on RL before patching the train script
- Log training
- Patch up training script (2-3 epochs)

### Evals
- Setup eval (python only) or any other benchmark which is small and easy for base model and our model (DONE, though need to setup environment for it to run)
- Take out 200-500 problems from the dataset for evals

### UI and API
- Host model on a server with live endpoint
- Streamlit UI which works with the UI with the req prompt
