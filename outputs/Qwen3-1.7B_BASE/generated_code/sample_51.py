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
        res = 0
        for i in range(n-1):
            if a[i] != a[i+1]:
                res += 1
        results.append(res)
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()