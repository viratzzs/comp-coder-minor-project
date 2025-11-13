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
        n, m, k = map(int, data[idx:idx+3])
        idx += 3
        s = data[idx]
        idx += 1
        count = 0
        i = 0
        while i < n:
            if s[i] == '0':
                # Apply operation on i to i + k - 1
                count += 1
                i += k
            else:
                i += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == "__main__":
    main()