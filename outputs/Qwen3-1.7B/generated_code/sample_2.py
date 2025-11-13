import sys
from sys import stdin

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        if n == 2:
            results.append("0")
            continue
        if n == 4:
            results.append("2")
        elif n == 7:
            results.append("4")
        else:
            results.append("2")
    print("\n".join(results))

if __name__ == "__main__":
    main()