import sys
import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

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
        h = int(data[idx+2])
        idx +=3
        horses = list(map(int, data[idx:idx+h]))
        idx += h
        graph = [[] for _ in range(n+1)]
        for __ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            w = int(data[idx+2])
            graph[u].append((v, w))
            graph[v].append((u, w))
            idx +=3
        d1 = dijkstra(n, graph, 1)
        dn = dijkstra(n, graph, n)
        min_time = float('inf')
        for v in range(1, n+1):
            if v in horses:
                time_marian = min(d1[v], d1[v] + dn[v]/2)
                time_marian += dn[v]/2
                time_robin = min(dn[v], dn[v] + d1[v]/2)
                time_robin += d1[v]/2
            else:
                time_marian = d1[v] + dn[v]/2
                time_robin = dn[v] + d1[v]/2
            if time_marian == time_robin:
                if time_marian < min_time:
                    min_time = time_marian
        if min_time != float('inf'):
            results.append(str(min_time))
        else:
            results.append('-1')
    print('\n'.join(results))

if __name__ == '__main__':
    main()