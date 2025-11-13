import sys
import math

def count_good_subarrays(test_cases):
    results = []
    for case in test_cases:
        n, a = case
        odd_count = 0
        for i in range(n):
            odd_count += 1
        # Now compute even_count
        even_count = 0
        m = 2
        while m <= n:
            for i in range(n - m + 1):
                sub = a[i:i+m]
                sorted_sub = sorted(sub)
                if sorted_sub[m//2 - 1] == sorted_sub[m//2]:
                    even_count += 1
            m += 2
        total = odd_count + even_count
        results.append(total)
    return results

def main():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    test_cases = []
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        a = list(map(int, input[idx:idx + n]))
        idx += n
        test_cases.append((n, a))
    results = count_good_subarrays(test_cases)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()