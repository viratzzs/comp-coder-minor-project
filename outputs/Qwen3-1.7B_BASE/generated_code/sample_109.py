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
        p = list(map(int, data[idx:idx + n]))
        idx += n
        s = data[idx]
        idx += 1
        visited = [False] * (n + 1)
        F = [0] * (n + 1)
        for i in range(1, n + 1):
            if not visited[i]:
                current = i
                cycle_nodes = []
                while not visited[current]:
                    visited[current] = True
                    cycle_nodes.append(current)
                    current = p[current - 1]
                count_black = sum(1 for x in cycle_nodes if s[x - 1] == '0')
                for node in cycle_nodes:
                    F[node] = count_black
        results.append(' '.join(map(str, F[1:])))
    print('\n'.join(results))

if __name__ == "__main__":
    main()