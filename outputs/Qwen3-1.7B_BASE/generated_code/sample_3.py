import sys
import bisect

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + m]))
        idx += m
        
        a.sort()
        b.sort()
        
        max_a = a[-1] - a[0]
        max_b = b[-1] - b[0]
        
        k_max = (n + m) // 3
        
        f = []
        for k in range(1, k_max + 1):
            if max_a >= max_b:
                x = min(k, n)
                y = max(k - x, 0)
                f.append(x * max_a + y * max_b)
            else:
                y = min(k, m)
                x = max(k - y, 0)
                f.append(x * max_b + y * max_a)
        
        results.append(f)
    
    print(len(results))
    if len(results) > 0:
        for res in results:
            print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()