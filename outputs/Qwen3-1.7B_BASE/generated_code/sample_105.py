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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        if a == sorted(a):
            results.append("0")
            continue
        # Generate n paths, each with 4 steps: R, D, R, D
        steps = []
        for i in range(n):
            steps.append("R")
            steps.append("D")
            steps.append("R")
            steps.append("D")
        results.append("4")
        results.append("".join(steps))
    print("\n".join(results))

if __name__ == "__main__":
    main()