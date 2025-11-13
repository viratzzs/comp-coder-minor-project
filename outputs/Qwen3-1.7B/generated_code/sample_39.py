t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if y == x + 1:
        print("YES")
    else:
        delta = x - y + 1
        if delta >= 0 and delta % 9 == 0:
            print("YES")
        else:
            print("NO")