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
        total = sum(a)
        current_sum = 0
        count = 0
        for i in range(n):
            current_sum += a[i]
            if current_sum == total:
                count += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    main()