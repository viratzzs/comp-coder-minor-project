import sys
MOD = 998244353

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        if m == 0:
            if n == 0:
                results.append(1)
            else:
                results.append(1)
            continue
        segments = []
        for __ in range(m):
            l = int(data[idx])
            r = int(data[idx + 1])
            segments.append((l, r))
            idx += 2
        segments.sort()
        first_l = segments[0][0]
        last_r = segments[-1][1]
        sum_inside = 0
        for a, b in segments:
            sum_inside += 2 * (b - a)
        sum_outside = (n - last_r) + (first_l - 1)
        sum_outside = max(0, sum_outside)
        product = 1
        for a, b in segments:
            product = product * 2 * (b - a) % MOD
        ans = product * sum_outside % MOD
        results.append(ans)
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()