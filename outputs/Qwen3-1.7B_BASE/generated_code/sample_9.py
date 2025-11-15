import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, m, v = map(int, data[idx:idx+3])
        idx += 3
        a = list(map(int, data[idx:idx+n]))
        idx += n
        total = sum(a)
        if total < (m + 1) * v:
            results.append("-1")
        else:
            results.append(str(total - m * v))
    print('\n'.join(results))

if __name__ == "__main__":
    main()