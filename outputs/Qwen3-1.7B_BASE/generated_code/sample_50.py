import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        grid = []
        for _ in range(n):
            grid.append(data[idx])
            idx += 1
        
        visited = [[False]*m for _ in range(n)]
        ans = 0
        
        def dfs(i, j):
            if visited[i][j]:
                return False
            visited[i][j] = True
            if grid[i][j] == '?':
                return True
            if grid[i][j] == 'U' and i == 0:
                return False
            if grid[i][j] == 'D' and i == n-1:
                return False
            if grid[i][j] == 'L' and j == 0:
                return False
            if grid[i][j] == 'R' and j == m-1:
                return False
            
            if grid[i][j] == 'U':
                if dfs(i-1, j):
                    return True
            elif grid[i][j] == 'D':
                if dfs(i+1, j):
                    return True
            elif grid[i][j] == 'L':
                if dfs(i, j-1):
                    return True
            elif grid[i][j] == 'R':
                if dfs(i, j+1):
                    return True
            
            return False
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '?':
                    if not visited[i][j]:
                        if dfs(i, j):
                            ans += 1
                else:
                    if not visited[i][j]:
                        if dfs(i, j):
                            ans += 1
        
        results.append(ans)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()