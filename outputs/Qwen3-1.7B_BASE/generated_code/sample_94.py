import sys
import bisect

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        a.sort()
        total = sum(a)
        if total >= k:
            results.append(1)
            continue
        res = 0
        for i in range(n):
            res += a[i]
            if res >= k:
                break
        results.append(res)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()