import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        if n == 1:
            print(0)
            continue
        # Check if there's at least one pair of equal adjacent elements
        has_equal = False
        for i in range(n):
            if a[i] == a[(i+1) % n]:
                has_equal = True
                break
        if has_equal:
            print(n - 1)
        else:
            print(n)

if __name__ == "__main__":
    main()