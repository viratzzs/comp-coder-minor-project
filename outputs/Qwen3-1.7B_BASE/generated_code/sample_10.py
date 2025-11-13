import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    def compute_next_smaller(p):
        n = len(p)
        next_smaller = [None] * (n + 1)
        stack = []
        for i in range(n, 0, -1):
            while stack and p[stack[-1]] <= p[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            else:
                next_smaller[i] = None
            stack.append(i)
        return next_smaller
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        q = list(map(int, data[idx:idx + n]))
        idx += n
        k = list(map(int, data[idx:idx + n]))
        idx += n
        j = list(map(int, data[idx:idx + n]))
        idx += n
        
        next_q = compute_next_smaller(q)
        next_k = compute_next_smaller(k)
        next_j = compute_next_smaller(j)
        
        next_reachable = [None] * (n + 1)
        for x in range(1, n + 1):
            candidates = []
            if next_q[x] is not None:
                candidates.append((next_q[x], 'q'))
            if next_k[x] is not None:
                candidates.append((next_k[x], 'k'))
            if next_j[x] is not None:
                candidates.append((next_j[x], 'j'))
            if not candidates:
                next_reachable[x] = None
            else:
                next_reachable[x] = min(candidates, key=lambda x: x[0])
        
        path = []
        current = 1
        while current < n:
            if next_reachable[current] is None:
                results.append("NO")
                break
            path.append(current)
            current = next_reachable[current][0]
        else:
            results.append("YES")
            results.append(len(path))
            for i in range(len(path) - 1):
                x = path[i]
                y = path[i + 1]
                results.append(f"{next_reachable[x][1]} {y}")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()