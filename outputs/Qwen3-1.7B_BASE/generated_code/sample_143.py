import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        s = set(a)
        dp = defaultdict(int)
        max_len = 0
        for x in s:
            current = x
            count = 1
            while True:
                next_x = current + 1
                if next_x in s:
                    if count < k:
                        current = next_x
                        count += 1
                    else:
                        break
                elif current in s:
                    current = x
                    count += 1
                else:
                    break
            max_len = max(max_len, count)
        results.append(str(max_len))
    print('\n'.join(results))

if __name__ == '__main__':
    main()