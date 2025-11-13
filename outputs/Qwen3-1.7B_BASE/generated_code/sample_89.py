import sys
from collections import deque

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
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        adj = [[] for _ in range(n+1)]
        for __ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            idx += 2
        # Predecessors
        predecessors = [[] for _ in range(n+1)]
        for u in range(1, n+1):
            for v in adj[u]:
                predecessors[v].append(u)
        # Topological sort
        in_degree = [0]*(n+1)
        for u in range(1, n+1):
            for v in adj[u]:
                in_degree[v] += 1
        queue = deque()
        for u in range(1, n+1):
            if in_degree[u] == 0:
                queue.append(u)
        top_order = []
        while queue:
            u = queue.popleft()
            top_order.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        S = set()
        for u in top_order:
            if u not in S:
                if S.intersection(predecessors[u]):
                    continue
                else:
                    S.add(u)
        all_in_S = True
        for u in range(1, n+1):
            if u not in S:
                all_in_S = False
                break
        if all_in_S:
            sum_a = sum(a[i-1] for i in S)
            results.append(sum_a)
        else:
            results.append(-1)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()