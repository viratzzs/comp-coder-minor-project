import sys
import heapq
from collections import defaultdict

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
        p = int(data[idx+2])
        idx += 3
        required = list(map(int, data[idx:idx+p]))
        idx += p
        # Build the graph
        edges = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            w = int(data[idx+2])
            idx += 3
            edges[u].append((v, w))
            edges[v].append((u, w))
        # Precompute distances from each required house to all servers
        # Using BFS for each required house
        distance = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for s in required:
            dist = [float('inf')] * (n + 1)
            dist[s] = 0
            queue = [s]
            while queue:
                u = queue.pop(0)
                for v, w in edges[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        queue.append(v)
            for u in range(1, n+1):
                distance[s][u] = dist[u]
        # Build priority queues for each required house
        pq = []
        for s in required:
            heap = []
            for u in range(1, n+1):
                if distance[s][u] != float('inf'):
                    heapq.heappush(heap, (distance[s][u], u))
            pq.append(heap)
        selected = set()
        total = 0
        k = 0
        while k < n and pq:
            dist, u = heapq.heappop(pq)
            if u not in selected:
                selected.add(u)
                k += 1
                total += dist
        results.append(total)
    print(' '.join(map(str, results)))

if __name__ == "__main__":
    main()