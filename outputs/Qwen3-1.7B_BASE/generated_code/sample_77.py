import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] + a[i-1]
        for __ in range(q):
            l = int(data[idx])
            r = int(data[idx+1])
            idx += 2
            total = r - l + 1
            full_cycles = total // n
            remainder = total % n
            sum_a = prefix[n]
            if remainder > 0:
                sum_part = prefix[remainder]
            else:
                sum_part = 0
            results.append(str(full_cycles * sum_a + sum_part))
    print('\n'.join(results))

if __name__ == "__main__":
    main()