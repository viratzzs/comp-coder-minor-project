t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a % 2 != 0:
        print("NO")
    else:
        target = (a + 2 * b) // 2
        lower = max(0, (target - a + 1) // 2)
        upper = min(b, target // 2)
        print("YES" if lower <= upper else "NO")