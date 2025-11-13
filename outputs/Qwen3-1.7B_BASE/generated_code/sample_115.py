import sys
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factor(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors.append((i, count))
        i += 1
    if n > 1:
        factors.append((n, 1))
    return factors

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        d = int(data[idx+1])
        idx += 2
        if d % 2 == 0:
            results.append("")
            continue
        m = 9 * d
        if math.gcd(10, m) != 1:
            results.append("")
            continue
        phi_m = 6 * math.gcd(d, 10)
        factors = factor(phi_m)
        primes = [p for (p, _) in factors]
        primes = sorted(primes)
        for p in primes:
            if p > n:
                results.append(str(d))
                break
        else:
            # Compute product of 1..n mod phi_m
            if n >= phi_m + 1:
                results.append(str(d))
            else:
                product = 1
                for i in range(1, n+1):
                    product = product * i % phi_m
                if product == 0:
                    results.append(str(d))
                else:
                    mod = pow(10, product, m)
                    if mod == 1:
                        results.append(str(d))
    print("\n".join(results))

if __name__ == "__main__":
    main()