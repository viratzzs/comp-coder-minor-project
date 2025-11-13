import sys
import collections

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
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
        bridges = []
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            bridges.append((u, v))
            idx += 2

        # BFS to compute minimal steps for Elsie to reach n
        from collections import deque
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        visited = [False] * (n + 1)
        q = deque()
        q.append(n)
        visited[n] = True
        while q:
            current = q.popleft()
            for u, v in bridges:
                if current == u:
                    if v == n:
                        dist[v] = min(dist[v], dist[current] + 1)
                        visited[v] = True
                        q.append(v)
                    else:
                        if not visited[v]:
                            dist[v] = min(dist[v], dist[current] + 1)
                            visited[v] = True
                            q.append(v)
                elif current == v:
                    if u == n:
                        dist[u] = min(dist[u], dist[current] + 1)
                        visited[u] = True
                        q.append(u)
                    else:
                        if not visited[u]:
                            dist[u] = min(dist[u], dist[current] + 1)
                            visited[u] = True
                            q.append(u)
        # Compute Bessie's steps
        bessie_dist = [float('inf')] * (n + 1)
        bessie_dist[n] = 0
        visited_bessie = [False] * (n + 1)
        q = deque()
        q.append(n)
        visited_bessie[n] = True
        while q:
            current = q.popleft()
            for u, v in bridges:
                if current == u:
                    if v == n:
                        bessie_dist[v] = min(bessie_dist[v], bessie_dist[current] + 1)
                        visited_bessie[v] = True
                        q.append(v)
                    else:
                        if not visited_bessie[v]:
                            bessie_dist[v] = min(bessie_dist[v], bessie_dist[current] + 1)
                            visited_bessie[v] = True
                            q.append(v)
                elif current == v:
                    if u == n:
                        bessie_dist[u] = min(bessie_dist[u], bessie_dist[current] + 1)
                        visited_bessie[u] = True
                        q.append(u)
                    else:
                        if not visited_bessie[u]:
                            bessie_dist[u] = min(bessie_dist[u], bessie_dist[current] + 1)
                            visited_bessie[u] = True
                            q.append(u)
        # Determine winner for each starting island
        res = []
        for s in range(1, n):
            if dist[s] <= bessie_dist[s]:
                res.append('1')
            else:
                res.append('0')
        results.append(''.join(res))

    print('\n'.join(results))

if __name__ == "__main__":
    main()