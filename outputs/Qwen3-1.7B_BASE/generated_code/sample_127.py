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
        
        edges = []
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            w = int(data[idx+2])
            edges.append((u-1, v-1, w))
            idx += 3
        
        # Compute minimal max latency for each required house
        min_latency = [0] * (n)
        for i in range(p):
            s_i = s[i]
            dist = [float('inf')] * n
            dist[s_i] = 0
            heap = [(0, s_i)]
            while heap:
                d, u = heapq.heappop(heap)
                if d > dist[u]:
                    continue
                for v, w in edges:
                    if v == u:
                        continue
                    new_d = max(d, w)
                    if new_d < dist[v]:
                        dist[v] = new_d
                        heapq.heappush(heap, (new_d, v))
            min_latency[i] = dist[s_i]
        
        # Sort required houses by their min_latency in descending order
        sorted_s = sorted(s, key=lambda x: min_latency[s.index(x)], reverse=True)
        
        # For each k from 1 to n, the sum of first k min_latencies
        for k in range(1, n+1):
            total = sum(min_latency[i] for i in sorted_s[:k])
            results.append(str(total))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()