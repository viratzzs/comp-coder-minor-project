import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        parent = list(range(n + 1))
        rank = [1] * (n + 1)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x_root = find(x)
            y_root = find(y)
            if x_root == y_root:
                return
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            else:
                parent[y_root] = x_root
                if rank[x_root] == rank[y_root]:
                    rank[x_root] += 1
        
        for _ in range(m):
            a = int(data[idx])
            d = int(data[idx + 1])
            k = int(data[idx + 2])
            idx += 3
            seq = []
            for i in range(k + 1):
                x = a + i * d
                if x > n:
                    break
                seq.append(x)
            for i in range(1, len(seq)):
                union(seq[i - 1], seq[i])
        
        roots = set()
        for i in range(1, n + 1):
            roots.add(find(i))
        results.append(len(roots))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()