import sys
import math

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        
        T = n * k + (n - 1) * n // 2
        if T % 2 == 0:
            D = (2 * k - 1) ** 2 + 4 * T
            sqrt_D = int(math.isqrt(D))
            if sqrt_D * sqrt_D != D:
                results.append(0)
                continue
            i = (-(2 * k - 1) + sqrt_D) // 2
            if 1 <= i <= n:
                results.append(0)
                continue
            else:
                results.append(min(abs(2 * k - T), abs(2 * T - T)))
        else:
            low = 1
            high = n
            min_val = float('inf')
            while low <= high:
                mid = (low + high) // 2
                current = mid * mid + (2 * k - 1) * mid - T
                if current == 0:
                    results.append(0)
                    break
                val = abs(current)
                if val < min_val:
                    min_val = val
                if current < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                results.append(min_val)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()