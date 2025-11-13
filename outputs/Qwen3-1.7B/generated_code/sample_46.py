from functools import lru_cache
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        l = int(input[ptr])
        n = int(input[ptr+1])
        m = int(input[ptr+2])
        ptr += 3
        a = list(map(int, input[ptr:ptr+l]))
        ptr += l
        matrix = []
        for i in range(n):
            row = list(map(int, input[ptr:ptr+m]))
            matrix.append(row)
            ptr += m
        # Precompute pos_map
        pos_map = [[] for _ in range(l)]
        for i in range(n):
            for j in range(m):
                val = matrix[i][j]
                for k in range(l):
                    if a[k] == val:
                        pos_map[k].append((i+1, j+1))
        # Define the dfs function
        @lru_cache(maxsize=None)
        def dfs(k, r_start, c_start):
            if k == l:
                return False
            for (x, y) in pos_map[k]:
                if r_start <= x <= n and c_start <= y <= m:
                    if not dfs(k+1, x+1, y+1):
                        return True
            return False
        res = dfs(0, 1, 1)
        results.append("T" if res else "N")
    print('\n'.join(results))

if __name__ == "__main__":
    main()