import sys
import math

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    h = 0
    a = 0
    total = 0
    print(total)
    for _ in range(q):
        t = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        if t == 1:
            h += 1
            contribution = min(h * (h + a), v)
            total += contribution
        else:
            a += 1
            contribution = min(h * (h + a), v)
            total += contribution
        print(total)

if __name__ == "__main__":
    main()