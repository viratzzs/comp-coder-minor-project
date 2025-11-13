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
        gold = 0
        count = 0
        for x in a:
            if x >= k:
                gold += x
            if x == 0 and gold >= 1:
                count += 1
                gold -= 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == "__main__":
    main()