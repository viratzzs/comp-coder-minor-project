import sys

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
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + a[i]
        low = 0
        high = 10**18
        def is_possible(m):
            c = bisect.bisect_right(a, m)
            total = prefix[c] + m * (n - c)
            return total >= k
        # Binary search for the smallest m where is_possible(m) is true
        while low < high:
            mid = (low + high) // 2
            if is_possible(mid):
                high = mid
            else:
                low = mid + 1
        results.append(low)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()