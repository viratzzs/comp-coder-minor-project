import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    from collections import defaultdict

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        adj = [[] for _ in range(n + 1)]
        for __ in range(n - 1):
            u = int(data[idx])
            v = int(data[idx + 1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2

        # Compute total_d for each node
        total_d = [defaultdict(int) for _ in range(n + 1)]
        visited = [False] * (n + 1)

        def dfs(u, parent):
            visited[u] = True
            for v in adj[u]:
                if v != parent:
                    dfs(v, u)
                    for d in range(1, 100):
                        total_d[u][d] += total_d[v][d - 1]

        dfs(1, -1)

        # Compute the contribution for each node
        res = 0
        for l in range(1, n + 1):
            total_l = defaultdict(int)
            for d in range(1, 100):
                total_l[d] += total_d[l][d]
            for d1 in range(1, 100):
                for d2 in range(1, 100):
                    a = d1
                    b = d2
                    if a == b:
                        val = 2 * a - 1
                    else:
                        val = max(a - 1, b - 1)
                    res += val * total_l[d1] * total_l[d2]

        print(res)

if __name__ == "__main__":
    main()