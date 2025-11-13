import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n, m = int(input[idx]), int(input[idx+1])
        idx += 2
        a = list(map(int, input[idx:idx+n]))
        idx += n
        graph = [[] for _ in range(n+1)]  # 1-based
        for _ in range(m):
            u = int(input[idx])
            v = int(input[idx+1])
            graph[u].append(v)
            idx += 2
        
        # Build reverse graph for reachability check
        reverse_graph = [[] for _ in range(n+1)]
        for u in range(1, n+1):
            for v in graph[u]:
                reverse_graph[v].append(u)
        
        # Determine nodes that must be in S
        S = []
        for u in range(1, n+1):
            visited = [False] * (n+1)
            queue = deque()
            queue.append(u)
            visited[u] = True
            found = False
            while queue:
                current = queue.popleft()
                if current != u:
                    found = True
                for neighbor in reverse_graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            if not found:
                S.append(u)
        
        remaining = [i for i in range(1, n+1) if i not in S]
        selected = []
        
        while remaining:
            max_count = -1
            best_node = None
            for node in remaining:
                visited = [False] * (n+1)
                queue = deque()
                queue.append(node)
                visited[node] = True
                count = 0
                while queue:
                    current = queue.popleft()
                    count += 1
                    for neighbor in graph[current]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                if count > max_count:
                    max_count = count
                    best_node = node
            selected.append(best_node)
            # Remove all nodes reachable from best_node
            visited = [False] * (n+1)
            queue = deque()
            queue.append(best_node)
            visited[best_node] = True
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            remaining = [node for node in remaining if not visited[node]]
        
        total = 0
        for node in S:
            total += a[node-1]
        for node in selected:
            total += a[node-1]
        print(total)

if __name__ == "__main__":
    main()