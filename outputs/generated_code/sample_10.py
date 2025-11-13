import sys

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
        q = list(map(int, data[idx:idx+n]))
        idx += n
        k = list(map(int, data[idx:idx+n]))
        idx += n
        j = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Check if there's a path from 1 to n
        # Use BFS to find the path
        from collections import deque
        visited = [False] * (n + 1)
        queue = deque()
        queue.append(1)
        visited[1] = True
        path = []
        found = False
        while queue:
            x = queue.popleft()
            if x == n:
                found = True
                break
            # Check for each player
            for player in [q, k, j]:
                max_y = -1
                for y in range(x + 1, n + 1):
                    if player[y - 1] > player[x - 1]:
                        max_y = y
                        break
                if max_y > x:
                    queue.append(max_y)
                    visited[max_y] = True
        if found:
            results.append("YES")
            # Reconstruct the path
            path = []
            current = n
            while current != 1:
                for player in [q, k, j]:
                    for y in range(current + 1, n + 1):
                        if player[y - 1] > player[current - 1]:
                            path.append((player, y))
                            current = y
                            break
            k_trades = len(path)
            print("YES")
            print(k_trades)
            for trade in path:
                print(f"{trade[0]} {trade[1]}")
        else:
            results.append("NO")
    for res in results:
        print(res)

if __name__ == "__main__":
    main()