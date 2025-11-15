import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        l = int(data[idx])
        n = int(data[idx+1])
        m = int(data[idx+2])
        idx +=3
        a = list(map(int, data[idx:idx+l]))
        idx += l
        b = []
        for _ in range(n):
            row = list(map(int, data[idx:idx+m]))
            idx += m
            b.append(row)
        
        positions = [[] for _ in range(l)]
        for i in range(l):
            for r in range(n):
                for c in range(m):
                    if b[r][c] == a[i]:
                        positions[i].append((r, c))
        
        # Initialize DP table
        dp = [[[False for _ in range(m)] for __ in range(n)] for ___ in range(l+1)]
        
        for i in range(l, 0, -1):
            for r in range(n):
                for c in range(m):
                    min_r = min(r for (r_, c_) in positions[i-1] if r_ >= r and r_ <= n-1)
                    max_r = max(r for (r_, c_) in positions[i-1] if r_ >= r and r_ <= n-1)
                    min_c = min(c for (r_, c_) in positions[i-1] if c_ >= c and c_ <= m-1)
                    max_c = max(c for (r_, c_) in positions[i-1] if c_ >= c and c_ <= m-1)
                    
                    if min_r >= r and max_r <= n-1 and min_c >= c and max_c <= m-1:
                        for (r_, c_) in positions[i-1]:
                            if r_ >= r and r_ <= n-1 and c_ >= c and c_ <= m-1:
                                if not dp[i][r_+1][c_+1]:
                                    dp[i-1][r][c] = True
                                    break
        
        results.append("T" if dp[0][0][0] else "N")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()