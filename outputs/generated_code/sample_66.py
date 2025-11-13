import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort(reverse=True)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] + a[i-1]
        min_coins = float('inf')
        for m in range(1, n + 1):
            if prefix[m] <= k:
                coins = k - prefix[m]
                if coins < min_coins:
                    min_coins = coins
        print(min_coins)

if __name__ == "__main__":
    main()