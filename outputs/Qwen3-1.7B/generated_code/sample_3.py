import sys
import math

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+m]))
        idx += m
        
        # Compute max differences for a and b
        a_sorted = sorted(a)
        b_sorted = sorted(b)
        max_a = a_sorted[-1] - a_sorted[0]
        max_b = b_sorted[-1] - b_sorted[0]
        
        # Compute k_max
        total_points = n + m
        k_max = (total_points) // 3
        if n >= 2:
            k_max = min(k_max, (n * (n-1) // 2) + (m * (m-1) // 2))
        
        # Compute f(x)
        f_list = []
        for x in range(1, k_max + 1):
            if x == 1:
                f_val = max(max_a, max_b)
            else:
                f_val = max(max_a, max_b)
            f_list.append(f_val)
        
        # Prepare output
        if k_max == 0:
            results.append("")
        else:
            results.append(str(k_max))
            results.append(' '.join(map(str, f_list)))
    
    # Print results
    for res in results:
        if res:
            print(res)

if __name__ == "__main__":
    main()