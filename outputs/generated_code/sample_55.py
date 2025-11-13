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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        a.sort()
        res = []
        for x in a:
            is_add = True
            for y in res:
                if x % y == 0:
                    is_add = False
                    break
            if is_add:
                res.append(x)
        results.append((len(res), res))
    for size, subset in results:
        print(size)
        print(' '.join(map(str, subset)))

if __name__ == "__main__":
    main()