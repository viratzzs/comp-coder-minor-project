import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        n = int(data[i])
        count = 0
        while n > 3:
            n = n // 4
            count += 1
        results.append(2 ** count)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()