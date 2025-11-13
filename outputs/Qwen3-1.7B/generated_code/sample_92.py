import sys

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    cases = data[1:]
    
    for case in cases:
        n = len(case)
        if n % 3 != 0:
            print("NO")
            continue
        result = []
        prev = None
        valid = True
        for i in range(n):
            c = case[i]
            if c == '?':
                if prev is not None:
                    if prev == 'Y':
                        new_char = 'D'
                    elif prev == 'D':
                        new_char = 'X'
                    elif prev == 'X':
                        new_char = 'Y'
                    else:
                        new_char = 'Y'
                else:
                    new_char = 'Y'
            else:
                if prev is not None and c == prev:
                    valid = False
                    break
                new_char = c
            result.append(new_char)
            prev = new_char
        if not valid:
            print("NO")
            continue
        print("YES")
        print(''.join(result))
        steps = []
        for i in range(n):
            steps.append(f"{result[i]} 0")
        print("\n".join(steps))
        
solve()