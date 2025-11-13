t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    s = input().strip()
    current_x, current_y = 0, 0
    path = set()
    for i in range(2 * n):
        if i < n:
            direction = s[i]
            if direction == 'N':
                current_y += 1
            elif direction == 'E':
                current_x += 1
            elif direction == 'S':
                current_y -= 1
            elif direction == 'W':
                current_x -= 1
            path.add((current_x, current_y))
        else:
            direction = s[i - n]
            if direction == 'N':
                current_y += 1
            elif direction == 'E':
                current_x += 1
            elif direction == 'S':
                current_y -= 1
            elif direction == 'W':
                current_x -= 1
            path.add((current_x, current_y))
    if (a, b) in path:
        print("YES")
    else:
        print("NO")