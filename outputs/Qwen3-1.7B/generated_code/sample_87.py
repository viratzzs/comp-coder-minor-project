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
        i = 0
        while i < n - 1:
            if a[i] > a[i+1]:
                # Perform the operation
                a[i] += 1
                a.append(a[i])
                del a[i]
            else:
                i += 1
        results.append(' '.join(map(str, a)))
    print('\n'.join(results))

if __name__ == "__main__":
    main()