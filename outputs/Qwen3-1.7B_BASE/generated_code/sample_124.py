import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        C = []
        for _ in range(n):
            row = list(map(int, data[idx:idx+m]))
            C.append(row)
            idx += m
        # Compute prefix sums for current day
        prefix_current = [0] * (m + 1)
        for i in range(1, m + 1):
            prefix_current[i] = prefix_current[i - 1] + C[i - 1][i - 1]
        # Compute max_prefix_ge and min_prefix_le
        max_prefix_ge = [0] * (m + 1)
        min_prefix_le = [0] * (m + 1)
        max_prefix_ge[1] = prefix_current[1]
        min_prefix_le[0] = 0
        for i in range(2, m + 1):
            max_prefix_ge[i] = max(max_prefix_ge[i - 1], prefix_current[i])
            min_prefix_le[i] = min(min_prefix_le[i - 1], prefix_current[i])
        # Initialize for day 1
        current_max_profit = max_prefix_ge[1]
        current_a_prev = 1
        current_b_prev = m
        # Process each day
        for i in range(2, n + 1):
            b_prev = current_b_prev
            a_prev = current_a_prev
            # Compute case1: l >= b_prev + 1
            if b_prev + 1 <= m:
                case1 = max_prefix_ge[b_prev + 1] - min_prefix_le[a_prev]
            else:
                case1 = 0
            # Compute case2: l >= b_prev
            if b_prev <= m:
                case2 = max_prefix_ge[b_prev] - min_prefix_le[a_prev - 1]
            else:
                case2 = 0
            current_max_profit = max(case1, case2)
            current_a_prev = a_prev
            current_b_prev = b_prev
        results.append(current_max_profit)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()