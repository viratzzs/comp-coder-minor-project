import sys
MOD = 10**9 + 7

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    n_list = list(map(int, data[1:t*2:2]))
    k_list = list(map(int, data[2:t*2:2]))
    
    # Precompute factorials and inverse factorials up to max n
    max_n = max(n_list)
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
    for i in range(max_n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    results = []
    for i in range(t):
        n = n_list[i]
        k = k_list[i]
        if k > n:
            results.append(0)
        else:
            res = fact[n] * inv_fact[k] % MOD
            res = res * inv_fact[n - k] % MOD
            results.append(res)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()