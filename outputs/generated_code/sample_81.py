t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 1:
        print(n)
        continue
    steps = 0
    while n > 0:
        current_power = 1
        x = 0
        while current_power * k <= n:
            current_power *= k
            x += 1
        steps += 1
        n -= current_power
    print(steps)