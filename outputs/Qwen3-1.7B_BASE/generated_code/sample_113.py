import bisect
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        a.sort()
        m = (n + 1) // 2
        for __ in range(q):
            x = int(data[idx])
            idx += 1
            L = bisect.bisect_left(a, x)
            if m <= L:
                results.append(str(a[m-1]))
            else:
                res = 0
                for i in range(L, n):
                    res = a[i] % x
                    if i == m - L - 1:
                        break
                results.append(str(res))
    print('\n'.join(results))

if __name__ == '__main__':
    main()