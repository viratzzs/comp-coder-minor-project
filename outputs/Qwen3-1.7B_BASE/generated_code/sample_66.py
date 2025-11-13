import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        a.sort(reverse=True)
        min_coins = float('inf')
        for m in range(1, n+1):
            current_sum = sum(a[:m])
            if current_sum == k:
                min_coins = min(min_coins, 0)
            elif current_sum < k:
                coins_needed = k - current_sum
                min_coins = min(min_coins, coins_needed)
        results.append(str(min_coins))
    print('\n'.join(results))

if __name__ == '__main__':
    main()