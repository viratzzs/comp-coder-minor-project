import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, m, k = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        s = data[idx]
        idx += 1
        last_end = -1
        count = 0
        i = 0
        while i < n:
            if i <= last_end:
                i += 1
                continue
            if s[i] == '0':
                count += 1
                last_end = i + k - 1
                i += k
            else:
                i += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    main()