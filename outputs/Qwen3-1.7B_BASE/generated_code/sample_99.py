import sys
import math

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, m = int(data[idx]), int(data[idx + 1])
        idx += 2
        S = list(map(int, data[idx:idx + m]))
        idx += m
        if 1 in S:
            results.append("-1")
            continue
        S.sort(reverse=True)
        selected = []
        for x in S:
            if x in selected:
                continue
            valid = True
            for y in selected:
                if x == y:
                    valid = False
                    break
                if x == y:
                    valid = False
                    break
                if x != y:
                    if x == y:
                        valid = False
                        break
                if x % y == 0:
                    valid = False
                    break
            if valid:
                selected.append(x)
        if not selected:
            results.append("-1")
        else:
            results.append(" ".join(map(str, selected)))
    print("\n".join(results))

if __name__ == "__main__":
    main()