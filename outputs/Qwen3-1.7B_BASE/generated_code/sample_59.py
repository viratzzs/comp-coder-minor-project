import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    p = list(map(int, data[idx:idx + m]))
    idx += m
    
    a = []
    for _ in range(n):
        row = list(map(int, data[idx:idx + n]))
        a.append(row)
        idx += n
    
    INF = -10**18
    dp_prev = [[INF] * n for _ in range(n)]
    dp_prev[0][0] = 0
    
    best_c = [[-1] * n for _ in range(n)]
    
    for j in range(m):
        current_p = p[j]
        current_P = 0
        dp_current = [[INF] * n for _ in range(n)]
        best_c_current = [[-1] * n for _ in range(n)]
        
        for r in range(n):
            for R in range(n):
                if dp_prev[r][R] == INF:
                    continue
                # Try all possible c_j not equal to r
                for c in range(n):
                    if c == r:
                        continue
                    if current_p != r:
                        if current_P > R:
                            new_r = current_p
                            new_R = current_P
                            new_P = 0
                            new_score = dp_prev[r][R] + a[c][j]
                            if new_score > dp_current[new_r][new_R]:
                                dp_current[new_r][new_R] = new_score
                                best_c_current[new_r][new_R] = c
                    else:
                        if current_P + 1 > R:
                            new_r = current_p
                            new_R = current_P + 1
                            new_P = 0
                            new_score = dp_prev[r][R] + a[c][j]
                            if new_score > dp_current[new_r][new_R]:
                                dp_current[new_r][new_R] = new_score
                                best_c_current[new_r][new_R] = c
        dp_prev = dp_current
        best_c = best_c_current
    
    max_score = INF
    best_r = -1
    best_R = -1
    
    for r in range(n):
        for R in range(n):
            if dp_prev[r][R] > max_score:
                max_score = dp_prev[r][R]
                best_r = r
                best_R = R
    
    if max_score == INF:
        print(-1)
    else:
        print(best_c[best_r][best_R])
        
if __name__ == "__main__":
    main()