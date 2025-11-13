import sys
import math
import bisect

MOD = 10**9 + 7

def factorize(x):
    factors = {}
    while x % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        x //= 2
    i = 3
    while i*i <= x:
        while x % i == 0:
            factors[i] = factors.get(i, 0) + 1
            x //= i
        i += 2
    if x > 1:
        factors[x] = 1
    return factors

def solve():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        d = int(data[idx + 2])
        idx += 3
        total = 0
        for x in range(1, n + 1):
            xk = x ** k
            if xk == 0:
                continue
            factors = factorize(xk)
            m = 1
            for p in factors:
                a = factors[p]
                m *= (k * a + 1)
            total = (total + pow(m, d, MOD)) % MOD
        results.append(total)
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()