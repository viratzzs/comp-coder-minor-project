import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx + 1])
        idx += 2
        
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        s = list(data[idx])
        idx += n
        
        possible = False
        for i in range(1, n):
            if s[i] in ('L', 'R'):
                possible = True
                break
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()