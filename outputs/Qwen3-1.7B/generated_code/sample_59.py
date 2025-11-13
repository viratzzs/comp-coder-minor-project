import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    a = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        a.append(row)
    
    current_ruling = None
    power_levels = [0] * n
    result = []
    
    for j in range(m):
        required_p = p[j]
        possible_cj = []
        for c in range(1, n + 1):
            if c == current_ruling:
                continue
            new_power = list(power_levels)
            new_power[c - 1] += 1
            max_power = max(new_power)
            new_ruling = None
            for i in range(n):
                if new_power[i] == max_power:
                    new_ruling = i + 1
                    break
            if new_ruling == required_p:
                possible_cj.append((c, a[c - 1][j]))
        
        if not possible_cj:
            print(-1)
            return
        
        best_c = None
        best_score = -1
        for c, score in possible_cj:
            if score > best_score:
                best_score = score
                best_c = c
        
        # Update power_levels and current_ruling
        new_power = list(power_levels)
        new_power[best_c - 1] += 1
        max_power = max(new_power)
        new_ruling = None
        for i in range(n):
            if new_power[i] == max_power:
                new_ruling = i + 1
                break
        power_levels = new_power
        current_ruling = new_ruling
        result.append(best_c)
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()