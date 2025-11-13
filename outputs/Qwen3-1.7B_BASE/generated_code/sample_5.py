import sys
MOD = 998244353

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
        pairs = []
        for __ in range(n):
            l = int(data[idx])
            r = int(data[idx+1])
            pairs.append((l, r))
            idx += 2
        # Check if the current pairs form a valid sequence
        def is_valid(pairs):
            stack = []
            for l, r in pairs:
                if stack and stack[-1] < l:
                    stack.append(l)
                elif stack and stack[-1] > l:
                    stack.pop()
                elif not stack:
                    stack.append(l)
                else:
                    return False
            return True
        
        # Initial answer is C(n)
        # Catalan number C(n) = (2n)! / (n! * n! * 1) (mod MOD)
        def catalan(n):
            if n == 0:
                return 1
            return (2 * 2 * n - 1) * catalan(n - 1) % MOD
        
        # Precompute Catalan numbers up to n=5000
        max_n = 5000
        catalan_numbers = [0] * (max_n + 1)
        catalan_numbers[0] = 1
        for i in range(1, max_n + 1):
            catalan_numbers[i] = (2 * (2 * i - 1) * catalan_numbers[i - 1]) % MOD
        
        current = catalan_numbers[n]
        results.append(current)
        # For each step, check if the pairs form a valid sequence
        for i in range(1, n + 1):
            new_pairs = pairs[:i]
            if is_valid(new_pairs):
                current = catalan_numbers[n]
            else:
                current = 0
            results.append(current)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()