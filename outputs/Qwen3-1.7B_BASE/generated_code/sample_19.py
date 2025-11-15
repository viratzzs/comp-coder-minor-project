import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, x = int(data[idx]), int(data[idx + 1])
        idx += 2
        a = list(map(int, data[idx:idx + n]))
        idx += n
        max_val = n
        res = max_val - 1
        results.append(res)
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()