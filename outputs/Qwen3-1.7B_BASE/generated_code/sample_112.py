import sys

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
        if n == 1:
            results.append("1" if a[0] == 0 else "0")
        else:
            s = sum(a)
            results.append(str(max(0, s - n)))
    print('\n'.join(results))

if __name__ == "__main__":
    main()