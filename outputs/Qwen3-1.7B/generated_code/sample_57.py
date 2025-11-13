import sys
from collections import Counter

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        freq = Counter(a)
        unique_x = list(freq.keys())
        unique_y = list(freq.keys())
        if len(unique_x) < 2:
            results.append("NO")
            continue
        has_two_x = False
        for x in unique_x:
            if freq[x] >= 2:
                has_two_x = True
                break
        if not has_two_x:
            results.append("NO")
            continue
        max_val = max(a)
        min_val = min(a)
        if freq[max_val] >= 2 and freq[min_val] >= 2:
            results.append("YES")
            results.append(f"{min_val} {min_val} {max_val} {max_val} {min_val} {min_val} {max_val} {max_val}")
        else:
            results.append("NO")
    print("\n".join(results))

if __name__ == "__main__":
    main()