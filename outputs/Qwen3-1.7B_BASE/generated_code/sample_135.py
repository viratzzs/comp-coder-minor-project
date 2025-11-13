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
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        if n == 1:
            results.append("-1")
            continue
        S = sum(a)
        m = max(a)
        sorted_other = sorted([x for x in a if x != m])
        k = (n + 1) // 2
        if len(sorted_other) < k:
            results.append("-1")
            continue
        low = 0
        high = 10**12
        answer = -1
        while low <= high:
            mid = (low + high) // 2
            T = (S + mid) / (2 * n)
            count = bisect.bisect_left(sorted_other, T)
            if count > n / 2:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        results.append(str(answer) if answer != -1 else "-1")
    print("\n".join(results))

if __name__ == "__main__":
    main()