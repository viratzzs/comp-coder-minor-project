import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        n = int(input[ptr])
        m = int(input[ptr+1])
        ptr +=2
        strings = []
        for _ in range(n):
            s = input[ptr]
            strings.append(s)
            ptr +=1
        max_diff = 0
        for s in strings:
            count = 0
            current_pos = 0
            for c in s:
                if current_pos < 5:
                    if c == 'n' and current_pos == 0:
                        current_pos += 1
                    elif c == 'a' and current_pos == 1:
                        current_pos += 1
                    elif c == 'r' and current_pos == 2:
                        current_pos += 1
                    elif c == 'e' and current_pos == 3:
                        current_pos += 1
                    elif c == 'k' and current_pos == 4:
                        current_pos += 1
            total_letters_in_5 = sum(1 for c in s if c in {'n', 'a', 'r', 'e', 'k'})
            if current_pos >= 5:
                contribution = 5 - (total_letters_in_5 - current_pos)
            else:
                contribution = current_pos - total_letters_in_5
            max_diff = max(max_diff, contribution)
        results.append(str(max_diff))
    print('\n'.join(results))

if __name__ == "__main__":
    main()