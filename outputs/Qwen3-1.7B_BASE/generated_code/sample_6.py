import sys

MOD = 998244353

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        pairs = []
        for __ in range(n):
            l = int(data[idx])
            r = int(data[idx+1])
            idx += 2
            pairs.append((l, r))
        
        # dp[i] is the number of valid sequences after the first i pairs
        dp = [1] * (n + 1)
        for i in range(1, n + 1):
            l_prev = pairs[i-2][1] if i > 1 else 0
            a = l_prev + 1
            # Calculate the number of valid (l, r) pairs for the i-th pair
            if a > 2 * n:
                dp[i] = 0
            else:
                m = 2 * n - a
                dp[i] = dp[i-1] * (m * (m + 1) // 2) % MOD
        
        results.append(dp[n] if n > 0 else 1)
    
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    main()