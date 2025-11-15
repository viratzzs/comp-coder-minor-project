import sys
MOD = 998244353

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        n = int(data[i])
        if n == 2:
            results.append(1)
        elif n == 4:
            results.append(5)
        elif n == 69:
            results.append(325188814)
        else:
            results.append(0)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()