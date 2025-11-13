import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort(reverse=True)
        max_element = a[0]
        remaining = a[1:]
        remaining.sort()
        if not remaining:
            min_remaining = 0
        else:
            min_remaining = remaining[0]
        sum_max = max_element * n
        sum_min = max_element + min_remaining * (n - 1)
        print(sum_max - sum_min)

if __name__ == "__main__":
    main()