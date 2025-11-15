import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        adj = []
        for _ in range(n):
            adj.append(data[idx])
            idx += 1
        in_degree = [0] * (n + 1)
        edges = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i < j and adj[i-1][j-1] == '1':
                    edges[i].append(j)
                    in_degree[j] += 1
        queue = deque()
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)
        topo_order = []
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v in edges[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        p = [0] * (n + 1)
        for i in range(1, n + 1):
            p[i] = topo_order[i-1]
        results.append(' '.join(map(str, p[1:n+1])))
    print('\n'.join(results))

if __name__ == "__main__":
    main()