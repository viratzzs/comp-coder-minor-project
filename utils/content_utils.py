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
    pattern = r"<answer>.*?\[contract\]\s*(.*?)\s*</answer>"
    #pattern = r"<answer>.*?\[contract\]\s*(.*?)</answer>"
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

def extract_test_code(completion_text):
    """
    Extracts the Solidity test code from the LLM completion.
    The test code is expected between "[test]" and "</answer>" tags,
    within the <answer> block.
    """
    pattern = r"<answer>.*?\[contract\].*?\[test\]\s*(.*?)\s*</answer>"
    match = re.search(pattern, completion_text, re.DOTALL)
    if match:
        code_content = match.group(1).strip()
        
        markdown_pattern = r"```(?:solidity)?\s*(.*?)\s*```"
        markdown_match = re.search(markdown_pattern, code_content, re.DOTALL)
        
        if markdown_match:
            code_content = markdown_match.group(1).strip()

        # Remove surrounding parentheses if they exist
        if code_content.startswith('(') and code_content.endswith(')'):
            code_content = code_content[1:-1].strip()
        
        
        return code_content
    else:
        # logger.warning("Could not extract test code. Check completion format.") # Optional logging
        return None

def extract_contract_name_from_test(test_code: str) -> str:
    """Extract contract name from test import statement"""
    
    patterns = [
        r'import\s+["\']\.\.\/src\/(\w+)\.sol["\']', 
        
        r'import\s+.*?from\s+["\']\.\.\/src\/(\w+)\.sol["\']|import\s+["\']\.\.\/src\/(\w+)\.sol["\']', 
        # Named imports: import { ... } from "../src/FileName.sol";
        r'import\s*\{[^}]*\}\s*from\s*["\'][^"\']*\/(\w+)\.sol["\']',
        
        # Direct imports: import "../src/FileName.sol";
        r'import\s*["\'][^"\']*\/(\w+)\.sol["\']',
        
        # Wildcard imports: import * as Name from "../src/FileName.sol";
        r'import\s*\*\s*as\s*\w+\s*from\s*["\'][^"\']*\/(\w+)\.sol["\']',
        
        # Default imports: import ContractName from "...";
        r'import\s+(\w+)\s+from\s*["\'][^"\']*\.sol["\']',
    ]
    
    excluded_names = {'Test', 'console', 'Script', 'Vm'}
    
    for pattern in patterns:
        match = re.search(pattern, test_code, re.IGNORECASE)
        if match:
            contract_name = match.group(1)
            # Only return if it's not an excluded testing utility
            if contract_name not in excluded_names:
                return contract_name
    
    return "Contract"