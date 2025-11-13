import sys

def main():
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
        total_sum = sum(a)
        threshold = total_sum / (2 * n)
        original_C = 0
        for num in a:
            if num < threshold:
                original_C += 1
        required_new_C = (n + 1) // 2
        if original_C > required_new_C:
            results.append(0)
            continue
        max_val = max(a)
        if max_val < threshold:
            # Need to find x such that (max_val + x) < threshold
            # new_C = original_C - 1 + (max_val + x < threshold)
            # required_new_C = (n + 1) // 2
            # So, we need original_C - 1 + (1 if (max_val + x) < threshold else 0) > required_new_C
            # => (max_val + x) < threshold must be >= (required_new_C - original_C + 1)
            required = required_new_C - original_C + 1
            if required <= 0:
                results.append(-1)
            else:
                # x must be such that max_val + x < threshold
                # x_min is the minimal x where max_val + x < threshold
                # since max_val < threshold, x can be 0
                # but we need to check if adding x makes the new_C >= required_new_C
                # new_C = original_C - 1 + 1 = original_C
                # which is original_C >= required_new_C?
                # No, because original_C <= required_new_C
                # So, we need to find x such that (max_val + x) < threshold
                # and original_C - 1 + 1 > required_new_C
                # which is original_C > required_new_C
                # but original_C is <= required_new_C
                # So, this is not possible
                # Wait, no. required_new_C is (n + 1) // 2
                # original_C is <= required_new_C
                # So, new_C is original_C - 1 + (1 if ... )
                # So, if original_C - 1 + 1 = original_C > required_new_C?
                # No, because original_C <= required_new_C
                # So, this is not possible
                # So, no solution
                results.append(-1)
        else:
            # max_val >= threshold
            required = required_new_C - original_C
            if required <= 0:
                results.append(0)
            else:
                # need (max_val + x) < threshold
                # but max_val >= threshold, so max_val + x >= threshold
                # so (max_val + x) < threshold is false
                # new_C = original_C + 0 = original_C
                # which is <= required_new_C
                # so no solution
                results.append(-1)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()