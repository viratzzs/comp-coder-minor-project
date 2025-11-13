import sys
import bisect
from collections import defaultdict

def build_sparse_table(a, n):
    log_table = [0] * (n + 1)
    for i in range(2, n + 1):
        log_table[i] = log_table[i // 2] + 1
    st = [[0] * n for _ in range(log_table[n] + 1)]
    for i in range(n):
        st[0][i] = a[i]
    for k in range(1, log_table[n] + 1):
        for i in range(n - (1 << k) + 1):
            st[k][i] = max(st[k-1][i], st[k-1][i + (1 << (k-1))])
    return st, log_table

def query_max(st, log_table, l, r):
    if l > r:
        return -1
    k = log_table[r - l + 1]
    return max(st[k][l], st[k][r - (1 << k) + 1])

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
        max_n = n
        st, log_table = build_sparse_table(a, max_n)
        freq = defaultdict(list)
        for i in range(n):
            freq[a[i]].append(i)
        answer = 0
        for x in freq:
            S = freq[x]
            k = len(S)
            for i in range(k):
                j = S[i] + 1
                if j in freq[x]:
                    answer += (S[i] + 1) * (n - j)
                else:
                    low = S[i] + 1
                    high = n
                    res = S[i] + 1
                    while low <= high:
                        mid = (low + high) // 2
                        if mid > n:
                            break
                        l = S[i] + 1
                        r = mid - 1
                        if r < l:
                            break
                        current_max = query_max(st, log_table, l, r)
                        if current_max <= x:
                            res = mid
                            low = mid + 1
                        else:
                            high = mid - 1
                    if res > S[i] + 1:
                        answer += (S[i] + 1) * (n - res)
        results.append(answer)
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()