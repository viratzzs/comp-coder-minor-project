import math
import sys

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
        s = data[idx]
        idx += 1
        r = int(math.isqrt(n))
        if r * r != n:
            results.append("No")
            continue
        valid = True
        for i in range(r):
            start = i * r
            end = start + r
            row = s[start:end]
            if row[0] != '1' or row[-1] != '1':
                valid = False
                break
        results.append("Yes" if valid else "No")
    print("\n".join(results))

if __name__ == "__main__":
    main()