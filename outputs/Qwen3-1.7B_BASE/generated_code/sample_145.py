import sys
import math
MOD = 998244353

def main():
    n, m = map(int, sys.stdin.readline().split())
    s1 = n * m
    s_other = 0
    if s1 != n * m:
        s_other = n * m - s1
    k = (n * m) // 2
    if k < 0 or k > n * m:
        print(0)
        return

    def comb(n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return math.comb(n, k)

    total = (comb(s1 + s_other, k) - comb(s_other, k)) // 2
    s_other_lower = min(s_other, m)
    if s_other_lower >= k:
        total = (total - comb(s_other_lower, k) // 2) % MOD
    else:
        total = total % MOD
    print(total % MOD)

if __name__ == "__main__":
    main()