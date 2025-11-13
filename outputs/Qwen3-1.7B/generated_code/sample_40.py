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
        total = sum(a)
        if total % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
    print('\n'.join(results))

if __name__ == "__main__":
    main()