import re

def extract_think_content(text):
    """Extracts content from within <think>...</think> tags."""
    pattern = r"<think>(.*?)</think>"
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        # group(1) contains the content captured by the first (and only)
        # parentheses group in the pattern.
        # .strip() removes any leading/trailing whitespace from the captured content.
        return match.group(1).strip()
    else:
        # logger.warning("Could not extract think content. Check completion format.") # Optional logging
        return None

def extract_contract_code(completion_text):
    """
    Extracts the Solidity contract code from the LLM completion.
    The contract code is expected between "[contract]" and "[test]" tags,
    within the <answer> block.
    """
    #pattern = r"<answer>.*?\[contract\]\s*(.*?)\s*</answer>"
    pattern = r"\[code\]\s*(.*?)\s*"
    match = re.search(pattern, completion_text, re.DOTALL)
    if match:
        code_content = match.group(1).strip()
        
        markdown_pattern = r"```(?:solidity)?\s*(.*?)\s*```"
        markdown_match = re.search(markdown_pattern, code_content, re.DOTALL)
        
        if markdown_match:
            code_content = markdown_match.group(1).strip()

        if code_content.startswith('(') and code_content.endswith(')'):
            code_content = code_content[1:-1].strip()
        
        
        return code_content
    else:
        # logger.warning("Could not extract contract code. Check completion format.") # Optional logging
        return None
