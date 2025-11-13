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
        d = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        jobs = []
        for __ in range(k):
            l = int(data[idx])
            r = int(data[idx+1])
            jobs.append((l, r))
            idx += 2
        # Compute events for brother's x (max count)
        events = [0] * (n + 2)
        for l, r in jobs:
            a_i = max(1, l - d + 1)
            b_i = min(n - d + 1, r)
            if a_i <= n - d + 1:
                events[a_i] += 1
                events[b_i + 1] -= 1
        max_count = 0
        best_x = 0
        current_sum = 0
        for x in range(1, n - d + 2):
            current_sum += events[x]
            if current_sum > max_count:
                max_count = current_sum
                best_x = x
            elif current_sum == max_count:
                if x < best_x:
                    best_x = x
        # Compute events for mother's y (min count)
        events = [0] * (n + 2)
        for l, r in jobs:
            a_i = max(1, l - d + 1)
            b_i = min(n - d + 1, r)
            if a_i <= n - d + 1:
                events[a_i] += 1
                events[b_i + 1] -= 1
        min_count = float('inf')
        best_y = 0
        current_sum = 0
        for x in range(1, n - d + 2):
            current_sum += events[x]
            if current_sum < min_count:
                min_count = current_sum
                best_y = x
            elif current_sum == min_count:
                if x < best_y:
                    best_y = x
        results.append(f"{best_x} {best_y}")
    print('\n'.join(results))

if __name__ == "__main__":
    main()