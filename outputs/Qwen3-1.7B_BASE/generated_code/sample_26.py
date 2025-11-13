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
        n = int(data[idx])
        q = int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Precompute length[i] for each i
        length = [1] * n
        for i in range(n-2, -1, -1):
            if a[i] == a[i+1]:
                length[i] = length[i+1] + 1
            else:
                length[i] = 1
        
        # Precompute emptyable[i] for each i
        emptyable = [False] * (n + 1)  # 1-based
        emptyable[n] = True
        for i in range(n-1, 0, -1):
            if length[i] >= 1 and emptyable[i + length[i]]:
                emptyable[i] = True
            else:
                emptyable[i] = False
        
        # Process queries
        for __ in range(q):
            l = int(data[idx])
            r = int(data[idx+1])
            idx += 2
            found = False
            for i in range(l, r+1):
                if length[i] >= 1 and emptyable[i + length[i]]:
                    found = True
                    break
            results.append("YES" if found else "NO")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()