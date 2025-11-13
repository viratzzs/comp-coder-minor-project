import sys
import math
from collections import defaultdict

def input():
    return sys.stdin.readline()

def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_prefix_gcd(a, n):
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = compute_gcd(prefix[i - 1], a[i - 1])
    return prefix

def get_suffix_gcd(a, n):
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = compute_gcd(suffix[i + 1], a[i])
    return suffix

def get_divisors(x):
    if x == 0:
        return []
    divisors = set()
    i = 1
    while i * i <= x:
        if x % i == 0:
            divisors.add(i)
            divisors.add(x // i)
        i += 1
    return divisors

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if n == 0:
            print(0, 0)
            continue
        prefix_a = get_prefix_gcd(a, n)
        suffix_a = get_suffix_gcd(a, n)
        max_d_b = 0
        for num in b:
            max_d_b = compute_gcd(max_d_b, num)
        if max_d_b == 0:
            print(0, 0)
            continue
        divisors_b = get_divisors(max_d_b)
        possible_d_b = set()
        for d in divisors_b:
            found = False
            for num in b:
                if num % d == 0:
                    found = True
                    break
            if found:
                possible_d_b.add(d)
        possible_d_a = set()
        for i in range(1, n + 1):
            d = compute_gcd(prefix_a[i - 1], suffix_a[i])
            possible_d_a.add(d)
        intersection = possible_d_a & possible_d_b
        if not intersection:
            print(0, 0)
            continue
        max_d = max(intersection)
        print(2 * max_d, 0)

if __name__ == "__main__":
    main()