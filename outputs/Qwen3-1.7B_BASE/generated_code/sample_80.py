import sys
import math
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    LOG = 20
    LOG_TABLE = [0] * (1 << LOG)
    for i in range(2, 1 << LOG):
        LOG_TABLE[i] = LOG_TABLE[i // 2] + 1
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        q = int(data[idx + 2])
        idx += 3
        a = list(map(int, data[idx:idx + n]))
        idx += n
        freq = [0] * (n + 2)
        c = [0] * (n + 2)
        for i in range(1, k + 1):
            freq[a[i - 1]] += 1
        for i in range(1, n - k + 1):
            current = a[i]
            cnt = freq[current]
            c[i] = k - cnt
            if i > 1:
                freq[a[i - 1]] -= 1
            if i + k <= n:
                freq[a[i + k]] += 1
        log_table = [0] * (n + 2)
        for i in range(2, n + 2):
            log_table[i] = log_table[i // 2] + 1
        st = [[0] * (LOG + 1) for _ in range(n + 2)]
        for i in range(1, n + 1):
            st[i][0] = c[i]
        for j in range(1, LOG + 1):
            for i in range(1, n + 1 - (1 << j) + 1):
                st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
        res = []
        for _ in range(q):
            l = int(data[idx])
            r = int(data[idx + 1])
            idx += 2
            if r - k + 1 < l:
                res.append(0)
                continue
            length = r - l + 1
            j = LOG_TABLE[length]
            if j > LOG:
                j = LOG
            i = l + (1 << j) - 1
            min_val = min(st[i][j], st[r - (1 << j) + 1][j])
            res.append(min_val)
        print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()