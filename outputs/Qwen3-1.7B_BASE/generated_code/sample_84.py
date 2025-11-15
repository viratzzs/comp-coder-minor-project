MOD = 10**9 + 7
inv_1e4 = pow(10000, MOD - 2, MOD)

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
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        p = list(map(int, data[idx:idx+n]))
        idx += n
        
        b = [1 if ai % 2 == 1 else 0 for ai in a]
        
        T = 0
        sum_sq = 0
        
        for i in range(n):
            term = (p[i] * inv_1e4) % MOD
            term = (term * b[i]) % MOD
            T = (T + term) % MOD
            sum_sq = (sum_sq + (term * term) % MOD) % MOD
        
        T_sq = (T * T) % MOD
        E = (T_sq + T - sum_sq) % MOD
        results.append(E)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()