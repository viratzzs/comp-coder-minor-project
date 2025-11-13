import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        p = int(data[idx+2])
        idx += 3
        
        pow2 = [pow(2, i, p) for i in range(n)]
        prev = [0] * (k + 1)
        prev[0] = 1
        
        for i in range(1, k + 1):
            curr = [0] * (k + 1)
            for s in range(k + 1):
                if s < 0:
                    continue
                for l in range(n):
                    if s - l >= 0:
                        curr[s] = (curr[s] + prev[s - l] * pow2[l]) % p
            prev = curr
        
        results.append(prev[k] % p)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()