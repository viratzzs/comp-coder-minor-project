import sys
import math

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, k, q = map(int, data[idx:idx+3])
        idx +=3
        a = list(map(int, data[idx:idx+n]))
        idx +=n
        # Precompute max_freq for all intervals of length k
        max_freq = [0]*n
        from collections import defaultdict
        freq = defaultdict(int)
        current_max = 0
        for i in range(k):
            freq[a[i]] += 1
            if freq[a[i]] > current_max:
                current_max = freq[a[i]]
            max_freq[i] = current_max
        # Now slide the window
        for i in range(k, n):
            # Remove a[i-k]
            freq[a[i-k]] -= 1
            if freq[a[i-k]] == 0:
                current_max = 0
            else:
                current_max = max(freq.values())
            # Add a[i]
            freq[a[i]] += 1
            if freq[a[i]] > current_max:
                current_max = freq[a[i]]
            max_freq[i] = current_max
        # Compute prefix sums
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + max_freq[i]
        # Process queries
        for __ in range(q):
            l = int(data[idx])
            r = int(data[idx+1])
            idx +=2
            # The number of intervals is r -k +1 - l +1
            # But the query is for i from l to r-k+1
            # So the number of intervals is r -k +1 - l +1 = r - l + 2 -k
            # But need to check if r >= l +k-1
            # For each i in l to r-k+1, inclusive
            # The sum is sum (k - max_freq[i]) for i in [l, r-k+1]
            # So compute the sum
            if r -k +1 < l:
                results.append(0)
            else:
                start = l
                end = r -k +1
                total = (end - start +1) * k - (prefix[end] - prefix[start-1])
                results.append(total)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()