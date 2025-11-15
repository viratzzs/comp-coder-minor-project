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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        freq = Counter(a)
        max_freq = max(freq.values())
        results.append(n - max_freq)
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()