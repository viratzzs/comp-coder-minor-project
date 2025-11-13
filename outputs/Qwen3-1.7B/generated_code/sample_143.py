import bisect
from collections import Counter

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, k = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        freq = Counter(a)
        unique = sorted(freq.keys())
        s = unique
        # Compute prefix sums
        prefix = [0] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            prefix[i] = prefix[i-1] + freq[s[i-1]]
        max_sum = 0
        for x in s:
            current = x
            l = 1
            while current + 1 in freq:
                current += 1
                l += 1
            max_possible_m = min(k, l)
            for m in range(1, max_possible_m + 1):
                i = bisect.bisect_left(s, x)
                if i + m > len(s):
                    break
                current_sum = prefix[i + m] - prefix[i]
                if current_sum > max_sum:
                    max_sum = current_sum
        print(max_sum)

if __name__ == "__main__":
    main()