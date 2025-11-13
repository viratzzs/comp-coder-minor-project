import sys
import math

MOD = 998244353

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        
        scrolls = []
        for __ in range(k):
            r = int(data[idx])
            b = int(data[idx+1])
            scrolls.append((r, b))
            idx += 2
        
        # Initialize dp table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base case: no red rubies or blue sapphires
        for r in range(n + 1):
            for b in range(m + 1):
                if r == 0 or b == 0:
                    dp[r][b] = 0
        
        # Fill the dp table
        for r in range(n + 1):
            for b in range(m + 1):
                if r == 0 or b == 0:
                    continue
                prob_red = (r * 1.0) / (n + m)
                prob_blue = (b * 1.0) / (n + m)
                
                # Check if current state matches any scroll
                current_matches = False
                for (r_i, b_i) in scrolls:
                    if r == r_i and b == b_i:
                        current_matches = True
                        break
                if current_matches:
                    dp[r][b] = (dp[r][b] + prob_red * dp[r-1][b] * 2 + prob_blue * dp[r][b-1] * 2) % MOD
                else:
                    dp[r][b] = (dp[r][b] + prob_red * dp[r-1][b] + prob_blue * dp[r][b-1]) % MOD
        
        print(dp[n][m] % MOD)

if __name__ == "__main__":
    main()