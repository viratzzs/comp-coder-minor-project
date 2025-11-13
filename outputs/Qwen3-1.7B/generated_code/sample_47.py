import sys
from functools import lru_cache

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        l = int(input[ptr])
        n = int(input[ptr+1])
        m = int(input[ptr+2])
        ptr += 3
        a = list(map(int, input[ptr:ptr+l]))
        ptr += l
        matrix = []
        for _ in range(n):
            row = list(map(int, input[ptr:ptr+m]))
            matrix.append(row)
            ptr += m
        
        # Preprocess positions for each element
        positions = {}
        for i in range(l):
            pos_list = []
            for r in range(n):
                for c in range(m):
                    if matrix[r][c] == a[i]:
                        pos_list.append((r+1, c+1))  # 1-based indexing
            positions[i] = pos_list
        
        @lru_cache(maxsize=None)
        def can_win(i, r, c):
            if i >= l:
                # Base case: check if current submatrix has any positions for a[l-1]
                if l == i:
                    for (r_p, c_p) in positions[l-1]:
                        if r_p >= r and r_p <= n and c_p >= c and c_p <= m:
                            return True
                    return False
                else:
                    return False
            current_a = a[i]
            pos_list = positions[i]
            if not pos_list:
                return False
            for (r_p, c_p) in pos_list:
                if r_p >= r and r_p <= n and c_p >= c and c_p <= m:
                    next_r = r_p + 1
                    next_c = c_p + 1
                    if not can_win(i+1, next_r, next_c):
                        return True
            return False
        
        result = can_win(0, 1, 1)
        print("T" if result else "N")

if __name__ == "__main__":
    solve()