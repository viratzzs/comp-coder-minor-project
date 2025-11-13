import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, x = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        count_max = max(a)
        res = []
        for i in range(x, n+1):
            if i > count_max:
                res.append(str(count_max + 1))
            else:
                res.append(str(count_max))
        results.append(' '.join(res))
    print('\n'.join(results))

if __name__ == "__main__":
    main()