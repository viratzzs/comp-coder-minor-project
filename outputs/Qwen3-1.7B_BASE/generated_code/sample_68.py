import math

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        
        m = 1
        while True:
            s = m * (m + 1) * (m - 1) // 3
            if s >= k and m * (m + 1) // 2 <= n:
                results.append(str(m))
                break
            m += 1
            if m > int(math.sqrt(2 * n)) + 1:
                break
        else:
            results.append("-1")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()