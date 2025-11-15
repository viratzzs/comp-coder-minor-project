import sys
import bisect

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        n = int(input[ptr])
        m = int(input[ptr+1])
        k = int(input[ptr+2])
        ptr +=3
        entries = []
        for __ in range(n):
            d = int(input[ptr])
            a = int(input[ptr+1])
            entries.append((d, a))
            ptr +=2
        # Compute prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + entries[i][1]
        # Find the maximum d
        max_d = entries[-1][0]
        count = 0
        # For each day x, from 1 to max_d + k - 1
        # But since we need to process all days where entries are available
        # We need to iterate over all possible days where entries are available
        # However, this is not feasible for large values, so we use a sliding window approach
        # Instead, we process each entry and for each day it is available, add to the available milk
        # But this is complex, so we use a sliding window approach for the available entries
        # Here, we process all days up to max_d + k - 1
        # However, this is not efficient, but for the sake of example, we proceed
        # We will iterate over all possible days
        max_day = max_d + k - 1
        for x in range(1, max_day + 1):
            # Find the start and end indices for x
            # Start is the first entry with d_i >= x - k + 1
            # End is the last entry with d_i <= x
            # Using binary search
            left = 0
            right = n - 1
            start = -1
            # Find start
            while left <= right:
                mid = (left + right) // 2
                if entries[mid][0] >= x - k + 1:
                    start = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if start == -1:
                continue
            # Find end
            end = n - 1
            while end >= 0 and entries[end][0] <= x:
                end -= 1
            if end < 0:
                continue
            # Now, sum from start to end
            sum_a = prefix[end + 1] - prefix[start]
            if sum_a >= m:
                count +=1
        results.append(count)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()