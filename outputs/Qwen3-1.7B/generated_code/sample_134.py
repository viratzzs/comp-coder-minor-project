t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = n - k + 1
    count = (n + 1) // 2 - (a // 2)
    print("YES" if count % 2 == 0 else "NO")