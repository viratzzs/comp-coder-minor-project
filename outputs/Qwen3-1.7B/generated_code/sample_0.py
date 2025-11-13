t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if l == 1:
        if r >= 2:
            res = 1 + (r - 2)
        else:
            res = 1
    else:
        res = r - l
    print(res)