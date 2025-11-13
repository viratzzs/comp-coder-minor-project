import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    lcm = a * b // g
    T = max(a, b)
    max_r = min(a - 1, b - 1)
    min_m = float('inf')
    for r in range(0, max_r + 1):
        numerator = T - r
        if numerator <= 0:
            k = 0
        else:
            k = (numerator + lcm - 1) // lcm
        m_candidate = r + k * lcm
        if m_candidate < min_m:
            min_m = m_candidate
    print(min_m)