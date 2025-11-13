import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x, y = map(int, sys.stdin.readline().split())
        if y == x + 1:
            print("YES")
        else:
            diff = x - y + 1
            if diff >= 0 and diff % 9 == 0:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()