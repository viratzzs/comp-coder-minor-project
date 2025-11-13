import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        INF = -10**18
        dp = [[INF] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n):
            for k in range(0, i + 2):
                if k == 0:
                    dp[i][k] = 0
                else:
                    option1 = dp[i-2][k-1] if (i-2) >= 0 else INF
                    option2 = dp[i-1][k] if (i-1) >= 0 else INF
                    dp[i][k] = max(option1, option2)
        res = INF
        for k in range(0, n):
            if dp[n-1][k] + k > res:
                res = dp[n-1][k] + k
        print(res)
        
if __name__ == "__main__":
    main()