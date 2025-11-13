import os


from rewards import *
from utils.content_utils import *
from datasets import load_dataset


def calculate_reward(completion, test):
    """Calculate total weighted reward"""
    rewards = {}
    print(completion)

    if completion:
        # rewards['xmlcount_reward_func'] = xmlcount_reward_func(completion)[0]
        rewards["format_reward_func"] = format_reward_func(completion)[0]
        # rewards['long_cot_chains'] = reward_long_cot_chains(completion)[0]
        # rewards['compilation'] = reward_compilation(completion)[0]
        # rewards['vulnerability'] = reward_vulnerability_analysis(completion, test)[0]
        # rewards['test_passing'] = reward_test_passing(completion, test)[0]
        # rewards['test_quality'] = reward_test_quality(completion)[0]

    # print(rewards)
    total_reward = sum(rewards[key] for key in rewards)
    rewards["total"] = total_reward

    return rewards


def main():
    data = load_dataset("KolwaiiOfficial/instruct-rl-sol-v3", split="train")
    processed_data = data.map(
        lambda x: {
            "prompt": [
                #            {'role': 'system', 'content': SYSTEM_PROMPT},
                {"role": "user", "content": x["problem"]}
            ],
            "test": x["test"],
        }
    )

    print(processed_data["prompt"][10][0]["content"])
    # print(processed_data['test'][1])

    completion = [[{"content": ""}]]
    with open("data.txt", "r") as f:
        completion[0][0]["content"] = f.read()

    # print(completion[0][0]['content'])
    # completion[0][0]['content'] = reasoning + "\n[contract]" + contract_code + "\n[test]" + test_code + "\n</answer>"

    rewards = calculate_reward(completion, processed_data["test"][10])
    print("=== REWARD BREAKDOWN ===")
    for key, value in rewards.items():
        print(f"{key}: {value:.3f}")

    return rewards


if __name__ == "__main__":
    main()
