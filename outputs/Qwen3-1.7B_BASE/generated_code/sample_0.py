import sys
import math

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        l = int(data[idx])
        r = int(data[idx+1])
        idx += 2
        a = 0
        if l <= 1 <= r:
            a += 1
        if l == r == 1:
            a += 1
        if r < 2:
            a = 0
        else:
            a += max(0, r - max(l, 2))
        results.append(a)
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()