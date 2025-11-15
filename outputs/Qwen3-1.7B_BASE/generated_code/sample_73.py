import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    for _ in range(n):
        line = sys.stdin.readline().strip()
        for i in range(4):
            if line[i] == '#':
                print(i + 1)
                break