import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        if a >= b:
            print(a)
        else:
            if 2 * a >= b:
                print(a - max(0, b - a))
            else:
                print(0)

if __name__ == "__main__":
    main()