import sys
import bisect

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Compute median m
        a_sorted = sorted(a)
        m = a_sorted[n//2]
        next_higher = [0] * n
        count = 0
        for i in range(n):
            if a_sorted[i] == m:
                count += 1
                if i < n-1 and a_sorted[i+1] > m:
                    next_higher[i] = a_sorted[i+1]
                else:
                    next_higher[i] = m
        # Group elements
        group1 = []
        group2 = []
        for i in range(n):
            if a[i] == m:
                group1.append((a[i], next_higher[i]))
            else:
                group2.append((a[i], m))
        # Compute contributions for group1 and group2
        max_contribution1 = 0
        if group1:
            max_contribution1 = max(a[i] + next_higher[i] for a, next_higher in group1)
        max_contribution2 = 0
        if group2:
            max_contribution2 = max(a[i] + m for a, m in group2)
        # Apply min(k, len(group1)) increments to group1
        x = min(k, len(group1))
        max_contribution = max(max_contribution1 + x, max_contribution2 + x)
        results.append(max_contribution)
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()