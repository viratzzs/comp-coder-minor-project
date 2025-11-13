import sys
import math

MOD = 10**9 + 7

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    max_n = 500
    max_k = 500
    dp = [[0] * (max_k + 1) for _ in range(max_n + 1)]
    dp[0][0] = 1
    for i in range(1, max_n + 1):
        for j in range(1, max_k + 1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j - i]
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        if k < 0:
            print(0)
            continue
        if n > max_n or k > max_k:
            print(0)
            continue
        print(dp[n][k] % MOD)

if __name__ == "__main__":
    main()