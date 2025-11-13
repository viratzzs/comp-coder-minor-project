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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        a.sort()
        subset = []
        for num in a:
            valid = True
            for x in subset:
                if num % x == 0:
                    valid = False
                    break
            if valid:
                subset.append(num)
        results.append(f"{len(subset)}\n{' '.join(map(str, subset))}")
    print("\n".join(results))

if __name__ == "__main__":
    main()