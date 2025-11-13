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
        x = int(data[idx + 1])
        idx += 2
        a = list(map(int, data[idx:idx + n]))
        idx += n
        s = set(a)
        for i in range(n + 1):
            if i not in s:
                results.append(str(i))
                break
        else:
            results.append(str(n))
    print('\n'.join(results))

if __name__ == "__main__":
    main()