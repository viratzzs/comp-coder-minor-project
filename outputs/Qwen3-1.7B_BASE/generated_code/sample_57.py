import sys
from collections import Counter

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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        x_values = a
        y_values = a
        
        # Process x_values
        freq_x = Counter(x_values)
        distinct_x = [x for x in freq_x if freq_x[x] >= 2]
        if not distinct_x:
            x_diff = 0
        else:
            max_x_diff = 0
            for i in range(len(distinct_x)):
                for j in range(i + 1, len(distinct_x)):
                    current_diff = distinct_x[i] - distinct_x[j]
                    if current_diff > max_x_diff:
                        max_x_diff = current_diff
            x_diff = max_x_diff
        
        # Process y_values
        freq_y = Counter(y_values)
        distinct_y = [y for y in freq_y if freq_y[y] >= 2]
        if not distinct_y:
            y_diff = 0
        else:
            max_y_diff = 0
            for i in range(len(distinct_y)):
                for j in range(i + 1, len(distinct_y)):
                    current_diff = distinct_y[i] - distinct_y[j]
                    if current_diff > max_y_diff:
                        max_y_diff = current_diff
            y_diff = max_y_diff
        
        # Determine output
        if x_diff == 0 and y_diff == 0:
            results.append("YES")
            results.append("0 0 0 0 0 0 0 0")
        elif x_diff == 0:
            results.append("YES")
            results.append("0 0 0 0 0 0 0 0")
        elif y_diff == 0:
            results.append("YES")
            results.append("0 0 0 0 0 0 0 0")
        else:
            results.append("YES")
            x1 = distinct_x[0]
            x2 = distinct_x[1]
            y1 = distinct_y[0]
            y2 = distinct_y[1]
            results.append(f"{x1} {y1} {x1} {y2} {x2} {y1} {x2} {y2}")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()