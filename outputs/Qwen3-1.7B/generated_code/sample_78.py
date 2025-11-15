import sys

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
        idx += 3
        a = list(map(int, data[idx:idx+n]))
        idx += n
        queries = []
        for __ in range(q):
            l = int(data[idx])
            r = int(data[idx+1])
            queries.append((l, r))
            idx += 2
        # For each query, the array is of length k
        # So f(b) is 0 if there is a consecutive subarray of length k
        # Which is always true, so output 0
        for l, r in queries:
            results.append(0)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()