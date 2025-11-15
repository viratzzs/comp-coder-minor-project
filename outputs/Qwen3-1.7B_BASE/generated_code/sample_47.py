import sys
from functools import lru_cache

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        l = int(data[idx])
        n = int(data[idx+1])
        m = int(data[idx+2])
        idx += 3
        a = list(map(int, data[idx:idx+l]))
        idx += l
        b = []
        for _ in range(n):
            row = list(map(int, data[idx:idx+m]))
            b.append(row)
            idx += m
        # Precompute positions for each a[i]
        pos = [[] for _ in range(l)]
        for i in range(l):
            for r in range(n):
                for c in range(m):
                    if b[r][c] == a[i]:
                        pos[i].append((r, c))
        # Memoization cache
        @lru_cache(maxsize=None)
        def dfs(i, r, c):
            if i > l:
                return False
            if r+1 > n or c+1 > m:
                return True  # submatrix is empty, current player wins
            for r_prime in range(r+1, n+1):
                for c_prime in range(c+1, m+1):
                    if dfs(i+1, r_prime, c_prime):
                        return True
            return False
        # Check if there's a position in pos[0] that allows Tsovak to win
        result = False
        for r, c in pos[0]:
            if dfs(0, r, c):
                result = True
                break
        print("T" if result else "N")

if __name__ == "__main__":
    main()