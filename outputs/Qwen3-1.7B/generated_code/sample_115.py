t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    res = [1]
    if n >= 3:
        res.append(3)
    else:
        if d % 3 == 0:
            res.append(3)
    if d % 5 == 0:
        res.append(5)
    if n >= 3:
        res.append(7)
    else:
        if n == 2 and d % 7 == 0:
            res.append(7)
    if n >= 6:
        res.append(9)
    else:
        if n == 5:
            if d % 3 == 0:
                res.append(9)
        elif n == 4:
            if d % 3 == 0:
                res.append(9)
        elif n == 3:
            if d % 3 == 0:
                res.append(9)
        elif n == 2:
            if d % 9 == 0:
                res.append(9)
    res.sort()
    print(' '.join(map(str, res)))