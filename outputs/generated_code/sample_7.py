import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, a, b = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        current_x, current_y = 0, 0
        visited = set()
        visited.add((current_x, current_y))
        found = False
        for i in range(2 * n):
            move = s[i % n]
            if move == 'N':
                current_y += 1
            elif move == 'S':
                current_y -= 1
            elif move == 'E':
                current_x += 1
            elif move == 'W':
                current_x -= 1
            if (current_x, current_y) == (a, b):
                print("YES")
                found = True
                break
            if (current_x, current_y) in visited:
                print("NO")
                found = True
                break
            visited.add((current_x, current_y))
        if not found:
            print("NO")

if __name__ == "__main__":
    main()