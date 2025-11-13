import sys
MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        m = int(data[idx])
        idx += 1
        
        # Calculate the sum of permutations P(m, n) for n from 1 to m
        total = 0
        for n in range(1, m+1):
            if n > m:
                break
            total = (total + m * (m-1) * (m-2) * ... * (m-n+1)) % MOD
        
        results.append(total)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()