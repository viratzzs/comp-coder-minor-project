import re
import tempfile
import fcntl
import json
import subprocess
import functools
from pathlib import Path
from typing import Dict, List, Optional
from loguru import logger
from utils.env_utils import *
from utils.content_utils import *

LOCK_FILE = Path(CODE_ENV_PATH) / '.reward_lock'
def with_forge_lock(func):
    """Decorator to ensure sequential access to forge environment"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open(LOCK_FILE, 'w') as lock_file:
            try:
                fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
                return func(*args, **kwargs)
            finally:
                fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
    return wrapper

def count_xml(text) -> float:
    count = 0.0
    # stonks
    if text.count("<think>\n") == 1:
        count += 0.2
    if text.count("\n</think>\n") == 1:
        count += 0.2
    if text.count("<answer>\n") == 1:
        count += 0.2
    if text.count("\n[code]\n") == 1:
        count += 0.2
    #if text.count("\n[test]\n") == 1:
    #    count += 0.125
    if text.count("\n</answer>") == 1:
        count += 0.2
    
    # not stonks
    if text.count("\n<think>\n") > 1:
        count -= 0.2
    if text.count("\n</think>\n") > 1:
        count -= 0.2
    if text.count("\n<answer>\n") > 1:
        count -= 0.2
    if text.count("\n</answer>\n") > 1:
        count -= 0.2
    
    return count


# --------------- actual rewards -------------------------

def format_reward_func(completions, **kwargs) -> list[float]:    #1 now
    """Reward function that checks if the completion has a specific format. Formerly strict."""
    #pattern = r"^<think>(.*?)</think>\n\n<answer>(.*?)\[contract\](.*?)\[test\](.*?)</answer>$"
    #pattern = r"^<think>\n.*?\n</think>\n\n<answer>\n.*?\n\n\[contract\]\n.*?\n\n\[test\]\n.*?\n</answer>$"
    pattern = r"<think>\s*.*?\s*</think>\s*<answer>\s*.*?\s*\[code\]\s*.*?\s*</answer>$"
    #pattern = r"<think>\s*.*?\s*</think>\s*<answer>\s*.*?\s*\[contract\]\s*.*?\s*</answer>$"
    responses = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, r, flags=re.DOTALL) for r in responses] 
    return [1 if match else 0.0 for match in matches]
