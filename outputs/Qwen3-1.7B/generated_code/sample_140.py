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
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        for __ in range(q):
            l = int(data[idx])
            r = int(data[idx+1])
            idx += 2
            sub = a[l-1:r]
            sub.sort(reverse=True)
            sum_odd = 0
            sum_even = 0
            for i in range(len(sub)):
                if i % 2 == 0:
                    sum_odd += sub[i]
                else:
                    sum_even += sub[i]
            if sum_even >= sum_odd:
                results.append("YES")
            else:
                results.append("NO")
    print('\n'.join(results))

if __name__ == "__main__":
    main()