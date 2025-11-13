import sys
import math

MOD = 998244353

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    n, m = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        edges[u].append(v)
        edges[v].append(u)
    
    # Precompute maximum distance from each node
    max_dist = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    def dfs(u, parent):
        visited[u] = True
        max_dist[u] = 0
        for v in edges[u]:
            if v != parent:
                dfs(v, u)
                max_dist[u] = max(max_dist[u], max_dist[v] + 1)
    
    dfs(1, -1)
    
    # For each node, compute forbidden set {1, 2, ..., max_dist[u] + 1}
    forbidden = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        forbidden[u] = list(range(1, max_dist[u] + 2))
    
    # Count the number of valid values for each node
    def count_valid_values(u):
        # Forbidden values are those divisible by any number in forbidden[u]
        # So valid values are those not divisible by any number in forbidden[u]
        cnt = 0
        for v in range(1, m + 1):
            valid = True
            for d in forbidden[u]:
                if v % d == 0:
                    valid = False
                    break
            if valid:
                cnt += 1
        return cnt
    
    # Compute the product of valid values for each node
    result = 1
    for u in range(1, n + 1):
        result = result * count_valid_values(u) % MOD
    
    print(result)

if __name__ == "__main__":
    main()