import sys
import math

def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    a = int(data[1])
    b = int(data[2])
    
    # Calculate sum of row GCDs
    sum_rows = 0
    for i in range(1, n + 1):
        sum_rows += math.gcd(i, a)
    
    # Calculate sum of column GCDs
    sum_cols = 0
    for j in range(1, n + 1):
        sum_cols += math.gcd(j, b)
    
    # Total number of down steps
    total_down = 2 * n - 2
    
    # Sort rows by their GCD with a
    sorted_rows = sorted(range(1, n + 1), key=lambda x: math.gcd(x, a))
    sum_down_rows = sorted_rows[0] * total_down
    
    # Sort columns by their GCD with b
    sorted_cols = sorted(range(1, n + 1), key=lambda x: math.gcd(x, b))
    sum_down_cols = sorted_cols[0] * total_down
    
    # Total cost is sum of row contributions + column contributions
    print(sum_rows + sum_cols + sum_down_rows + sum_down_cols)

if __name__ == "__main__":
    main()