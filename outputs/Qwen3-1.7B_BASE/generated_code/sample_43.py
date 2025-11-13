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
        m = int(data[idx + 1])
        q = int(data[idx + 2])
        idx += 3
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        x = int(data[idx])
        idx += 1
        max_distance = max(abs(x - a), abs(x - b))
        results.append(str(max_distance // 2))
    print("\n".join(results))

if __name__ == "__main__":
    main()