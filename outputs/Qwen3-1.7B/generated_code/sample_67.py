import sys
from collections import Counter

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        c = list(map(int, sys.stdin.readline().split()))
        count = Counter(c)
        total = 0
        for color, freq in count.items():
            if freq % 2 == 1:
                total += 2
            else:
                total += 1
        print(total)

if __name__ == "__main__":
    main()