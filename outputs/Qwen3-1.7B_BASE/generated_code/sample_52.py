import sys
import math
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
        m = int(data[idx+1])
        k = int(data[idx+2])
        idx +=3
        scrolls = set()
        for __ in range(k):
            r = int(data[idx])
            b = int(data[idx+1])
            idx +=2
            scrolls.add((r, b))
        # Initialize dp
        dp = [[0]*(m+2) for _ in range(n+2)]
        # Fill dp in reverse order
        for r in range(n, -1, -1):
            for b in range(m, -1, -1):
                if r + b == 0:
                    dp[r][b] = 0
                    continue
                pr = r / (r + b)
                ps = b / (r + b)
                val = 0
                if (r+1, b) in scrolls:
                    val += pr * 2
                else:
                    val += pr
                if (r, b+1) in scrolls:
                    val += ps * 2
                else:
                    val += ps
                dp[r][b] = val
        results.append(dp[0][0])
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()