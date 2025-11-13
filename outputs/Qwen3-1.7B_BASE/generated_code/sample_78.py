import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, k, q = map(int, data[idx:idx+3])
        idx += 3
        a = list(map(int, data[idx:idx+n]))
        idx += n
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + (1 if a[i - 1] == 1 else 0)
        for __ in range(q):
            l = int(data[idx])
            idx += 1
            r = l + k - 1
            if prefix[r] - prefix[l - 1] >= 1:
                results.append(0)
            else:
                results.append(k)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()