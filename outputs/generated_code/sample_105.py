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
        sorted_a = sorted(a)
        if sorted_a == a:
            results.append("0")
            continue
        # Generate two paths
        path1 = "RRDD" * (n-1)
        path2 = "DRDD" * (n-1)
        results.append("2")
        results.append(path1)
        results.append(path2)
    print("\n".join(results))

if __name__ == "__main__":
    main()