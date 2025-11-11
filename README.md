# TODO
## Training stuff
- Create subset of openr1 dataset with 1000 samples (split of easy-medium-hard: 3-5-2, use dict to maintain range of problem ratings)
- Fix prompt and content util script
- Script to create and run generated code sequentially in environment
- Figure out how to use the i/o tests as a verifier
- Create prototype for rewards
- Read kalo's blog on RL before patching the train script
- Log training
- Patch up training script (2-3 epochs)

## Evals
- Setup humaneval (python only) or any other benchmark which is small and easy for base model and our model
- Take out 200-500 problems from the dataset for evals

## UI and API
- Host model on a server with live endpoint
- Streamlit UI which works with the UI with the req prompt
