import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        
        # dp[i][j] = True if Alice can force a win on segment i to j
        # Initialize dp
        dp = [[False] * n for _ in range(n)]
        
        # Base case: single boolean
        for i in range(n):
            if s[i] == '1':
                dp[i][i] = True
        
        # Fill dp for segments of length 2 to n
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Check all possible splits k in i < k < j
                can_win = False
                for k in range(i+1, j):
                    if dp[i][k] or dp[k][j]:
                        can_win = True
                        break
                dp[i][j] = can_win
        
        # Check if there exists a split where either left or right is lose
        win = False
        for i in range(1, n):
            if dp[0][i] or dp[i][n-1]:
                win = True
                break
        
        results.append("YES" if win else "NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()