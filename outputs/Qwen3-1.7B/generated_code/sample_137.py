import sys
from collections import deque
import heapq

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        m = int(input[ptr+1])
        h = int(input[ptr+2])
        ptr += 3
        horse_nodes = list(map(int, input[ptr:ptr+h]))
        ptr += h
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(input[ptr])
            v = int(input[ptr+1])
            w = int(input[ptr+2])
            adj[u].append((v, w))
            adj[v].append((u, w))
            ptr += 3
        # Check connectivity between 1 and n
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        while queue:
            u = queue.popleft()
            if u == n:
                break
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        if not visited[n]:
            print(-1)
            continue
        # Dijkstra for Marian
        def dijkstra(start, horse_set, adj, n):
            INF = float('inf')
            dist = [INF] * (n + 1)
            dist[start] = 0.0
            heap = [(0.0, start)]
            while heap:
                current_time, u = heapq.heappop(heap)
                if current_time > dist[u]:
                    continue
                for v, w in adj[u]:
                    if u in horse_set:
                        new_time = current_time + w / 2.0
                    else:
                        new_time = current_time + w
                    if new_time < dist[v]:
                        dist[v] = new_time
                        heapq.heappush(heap, (new_time, v))
            return dist
        horse_set = set(horse_nodes)
        dist_marian = dijkstra(1, horse_set, adj, n)
        dist_robins = dijkstra(n, horse_set, adj, n)
        min_time = float('inf')
        for v in range(1, n + 1):
            if dist_marian[v] != float('inf') and dist_robins[v] != float('inf'):
                current = max(dist_marian[v], dist_robins[v])
                if current < min_time:
                    min_time = current
        if min_time == float('inf'):
            print(-1)
        else:
            print(min_time)

if __name__ == "__main__":
    main()