import sys
from collections import deque

MOD = 998244353
inv_2 = pow(2, MOD - 2, MOD)

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        adj = [[] for _ in range(n + 1)]
        for __ in range(n - 1):
            x = int(input[ptr])
            y = int(input[ptr + 1])
            adj[x].append(y)
            adj[y].append(x)
            ptr += 2
        parent = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        q = deque()
        q.append(1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    children[u].append(v)
                    q.append(v)
        f = [0] * (n + 1)
        f[1] = 1
        stack = [(1, False)]
        while stack:
            node, processed = stack.pop()
            if not processed:
                stack.append((node, True))
                for child in reversed(children[node]):
                    stack.append((child, False))
            else:
                if node == 1:
                    pass
                else:
                    if len(children[node]) == 0:
                        f[node] = 0
                    else:
                        sum_children = 0
                        for child in children[node]:
                            sum_children += f[child]
                        sum_adj = (sum_children + f[parent[node]]) % MOD
                        min_children = float('inf')
                        for child in children[node]:
                            if f[child] < min_children:
                                min_children = f[child]
                        min_adj = min(min_children, f[parent[node]])
                        f[node] = (sum_adj + min_adj) * inv_2 % MOD
        res = [str(f[i]) for i in range(1, n + 1)]
        print(' '.join(res))

if __name__ == "__main__":
    main()