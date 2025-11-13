t = int(input())
for _ in range(t):
    n = int(input())
    lines = [input().strip() for _ in range(n)]
    result = []
    for line in reversed(lines):
        for i in range(4):
            if line[i] == '#':
                result.append(str(i + 1))
                break
    print(' '.join(result))