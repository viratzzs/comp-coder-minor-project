import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        total = 0
        for i in range(n):
            if i % 2 == 0:
                total += a[i]
            else:
                total -= a[i]
        print(total)

if __name__ == "__main__":
    main()