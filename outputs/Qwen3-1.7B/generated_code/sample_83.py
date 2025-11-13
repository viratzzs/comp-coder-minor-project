import sys

class DSU:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [1] * (size + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        m = int(input[ptr + 1])
        ptr += 2
        dsu = DSU(n)
        for _ in range(m):
            a = int(input[ptr])
            d = int(input[ptr + 1])
            k = int(input[ptr + 2])
            ptr += 3
            for j in range(1, k + 1):
                x = a + (j - 1) * d
                y = a + j * d
                dsu.union(x, y)
        roots = set()
        for i in range(1, n + 1):
            roots.add(dsu.find(i))
        print(len(roots))

if __name__ == "__main__":
    main()