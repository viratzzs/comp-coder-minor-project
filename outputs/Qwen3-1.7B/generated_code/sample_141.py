q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    # Calculate the minimum steps
    # Case 1: build s and t directly
    case1 = len(s) + len(t)
    # Case 2: copy once, then build the rest
    # If s is longer than t, then copy s to t and build the rest of s
    # Or vice versa
    if len(s) < len(t):
        case2 = len(s) + 1 + (len(t) - len(s))
    elif len(t) < len(s):
        case2 = len(t) + 1 + (len(s) - len(t))
    else:
        case2 = len(s) + 1  # if they are equal, copy once and build the rest of one
    # The minimum of case1 and case2
    min_steps = min(case1, case2)
    print(min_steps)