MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        p = list(map(int, input[ptr:ptr+n]))
        ptr += n
        
        sum_p_a = 0
        sum_p_a_squared = 0
        sum_p_p_a_squared = 0
        
        for i in range(n):
            ai = a[i]
            pi = p[i]
            sum_p_a = (sum_p_a + pi * ai) % MOD
            sum_p_a_squared = (sum_p_a_squared + pi * (ai * ai)) % MOD
            sum_p_p_a_squared = (sum_p_p_a_squared + (pi * pi) * (ai * ai)) % MOD
        
        # Compute numerator
        term1 = (sum_p_a_squared * 10000) % MOD
        term2 = (sum_p_a * sum_p_a) % MOD
        term3 = sum_p_p_a_squared % MOD
        numerator = (term1 + term2 - term3) % MOD
        
        # Compute denominator
        denominator = (10000 * 10000) % MOD
        inv_denominator = pow(denominator, MOD-2, MOD)
        
        ans = (numerator * inv_denominator) % MOD
        print(ans)

if __name__ == "__main__":
    main()