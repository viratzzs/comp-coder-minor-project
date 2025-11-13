import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        if a == sorted(a):
            print(0)
        else:
            print(2)
            print('R' * (n-1) + 'D' * (n-1))
            print('D' * (n-1) + 'R' * (n-1))

if __name__ == "__main__":
    main()