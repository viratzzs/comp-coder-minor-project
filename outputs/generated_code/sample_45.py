import sys
import math
from math import gcd

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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Compute original GCDs
        def compute_gcd(arr):
            res = arr[0]
            for num in arr[1:]:
                res = math.gcd(res, num)
            return res
        
        original_gcd_a = compute_gcd(a)
        original_gcd_b = compute_gcd(b)
        original_sum = original_gcd_a + original_gcd_b
        max_sum = original_sum
        count = 0
        
        # Precompute prefix and suffix GCDs for a and b
        prefix_a = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_a[i] = math.gcd(prefix_a[i-1], a[i-1])
        
        suffix_a = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            suffix_a[i] = math.gcd(suffix_a[i+1], a[i])
        
        prefix_b = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_b[i] = math.gcd(prefix_b[i-1], b[i-1])
        
        suffix_b = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            suffix_b[i] = math.gcd(suffix_b[i+1], b[i])
        
        # Iterate all possible l and r
        for l in range(n):
            for r in range(l, n):
                # Compute subarray_b[l..r]
                subarray_b = 0
                for i in range(l, r+1):
                    subarray_b = math.gcd(subarray_b, b[i])
                # Compute subarray_a[l..r]
                subarray_a = 0
                for i in range(l, r+1):
                    subarray_a = math.gcd(subarray_a, a[i])
                
                # Compute new_a_gcd
                g1 = prefix_a[l]
                g2 = suffix_a[r]
                new_a_gcd = math.gcd(g1, g2)
                new_a_gcd = math.gcd(new_a_gcd, subarray_b)
                
                # Compute new_b_gcd
                g3 = prefix_b[l]
                g4 = suffix_b[r]
                new_b_gcd = math.gcd(g3, g4)
                new_b_gcd = math.gcd(new_b_gcd, subarray_a)
                
                current_sum = new_a_gcd + new_b_gcd
                if current_sum > max_sum:
                    max_sum = current_sum
                    count = 1
                elif current_sum == max_sum:
                    count += 1
        
        results.append(f"{max_sum} {count}")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()