t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if (a + 2 * b) % 2 != 0:
        print("NO")
    else:
        K = (a + 2 * b) // 2
        min_y = max(0, (K - a + 1) // 2)
        max_y = min(b, K // 2)
        if min_y <= max_y:
            print("YES")
        else:
            print("NO")