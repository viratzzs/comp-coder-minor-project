import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx+1])
        idx +=2
        a = list(map(int, data[idx:idx+n]))
        idx +=n
        queries = list(map(int, data[idx:idx+q]))
        idx +=q
        for x in queries:
            new_a = []
            for num in a:
                if num < x:
                    new_a.append(num)
                else:
                    new_a.append(num % x)
            new_a.sort()
            median = new_a[(n+1)//2 -1]
            results.append(str(median))
    print('\n'.join(results))

if __name__ == "__main__":
    main()