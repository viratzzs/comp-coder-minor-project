t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        total += a[i] * (-1)**i
    print(total)