import bisect

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        
        days = []
        milk = []
        
        for _ in range(n):
            d = int(data[idx])
            a = int(data[idx+1])
            idx += 2
            days.append(d)
            milk.append(a)
        
        available = 0
        count = 0
        
        for i in range(n):
            x = days[i]
            low = x - k + 1
            l = bisect.bisect_left(days, low)
            if l < n and days[l] <= x:
                d = days[l]
                available = max(available, milk[d - 1])
            
            if available >= m:
                count += 1
                available -= m
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()