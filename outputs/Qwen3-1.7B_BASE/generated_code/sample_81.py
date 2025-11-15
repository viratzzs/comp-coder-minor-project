import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        if k == 1:
            if n == 1:
                results.append(1)
            else:
                results.append(n)
        else:
            count = 0
            while n > 0:
                x = 0
                while True:
                    if pow(k, x) > n:
                        break
                    x += 1
                count += 1
                n -= pow(k, x - 1)
            results.append(count)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()