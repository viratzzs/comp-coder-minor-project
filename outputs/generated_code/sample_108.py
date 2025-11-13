import math

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if l == r:
        print(1)
        continue
    k = r - l
    s = math.sqrt(8 * k + 1)
    n = int((s + 1) // 2)
    print(n)