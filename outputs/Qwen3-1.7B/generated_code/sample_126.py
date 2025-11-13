import sys
import heapq

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
        s = list(map(int, data[idx:idx+p]))
        idx += p
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            w = int(data[idx+2])
            graph[u].append((v, w))
            graph[v].append((u, w))
            idx += 3
        
        # For each required house, compute the minimal maximum latency to any node
        d = [0] * (p)
        for i in range(p):
            # Dijkstra's algorithm to find the minimal maximum latency
            dist = [float('inf')] * (n+1)
            dist[s[i]] = 0
            heap = [(0, s[i])]
            while heap:
                current_dist, u = heapq.heappop(heap)
                if current_dist > dist[u]:
                    continue
                for v, w in graph[u]:
                    new_dist = max(current_dist, w)
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(heap, (new_dist, v))
            d[i] = dist[s[i]]
        
        # Prepare the results
        res = [0] * n
        for k in range(1, n+1):
            total = 0
            for i in range(k):
                total += d[i]
            res[k-1] = total
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()