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
        m = int(data[idx+1])
        q = int(data[idx+2])
        idx += 3
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+m]))
        idx += m
        if Counter(a) == Counter(b):
            results.append("YA")
        else:
            results.append("TIDAK")
    print("\n".join(results))

if __name__ == "__main__":
    main()