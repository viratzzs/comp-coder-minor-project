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
        a1 = list(map(int, data[idx:idx+n]))
        idx += n
        a2 = list(map(int, data[idx:idx+n]))
        idx += n
        sum_first = sum(a1)
        sum_second = sum(a2)
        a2_last = a2[-1]
        option1 = sum_first + a2_last
        option2 = a1[0] + sum_second
        result = max(option1, option2)
        results.append(str(result))
    print('\n'.join(results))

if __name__ == "__main__":
    main()