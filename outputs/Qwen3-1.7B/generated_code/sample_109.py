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
        p = list(map(int, data[idx:idx+n]))
        idx += n
        s = data[idx]
        idx += 1
        visited = [False] * n
        res = [0] * n
        for i in range(n):
            if not visited[i]:
                current = i
                cycle = []
                while not visited[current]:
                    visited[current] = True
                    cycle.append(current)
                    current = p[current] - 1
                count = 0
                for idx_in_cycle in cycle:
                    if s[idx_in_cycle] == '0':
                        count += 1
                for idx_in_cycle in cycle:
                    res[idx_in_cycle] = count
        results.append(' '.join(map(str, res)))
    print('\n'.join(results))

if __name__ == "__main__":
    main()