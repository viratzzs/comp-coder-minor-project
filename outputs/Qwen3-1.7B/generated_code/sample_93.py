t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a >= b:
        print(a)
    else:
        x = max(0, b - a)
        if x > a:
            print(0)
        else:
            if x <= b // 2:
                ans = b - 2 * x
                print(ans if ans >= 0 else 0)
            else:
                print(0)