MOD = 10**9 + 7

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    sum_a_sq = sum(x * x for x in a)
    numerator = (sum_a * sum_a - sum_a_sq) % MOD
    denominator = n * (n - 1) % MOD
    inv_denominator = pow(denominator, MOD - 2, MOD)
    result = (numerator * inv_denominator) % MOD
    print(result)