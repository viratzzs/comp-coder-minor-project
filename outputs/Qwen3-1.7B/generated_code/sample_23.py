import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        count_1 = s.count('1')
        count_0 = n - count_1
        if count_1 > count_0:
            if (n - 1) % 2 == 1:
                results.append("YES")
            else:
                results.append("NO")
        else:
            if (n - 1) % 2 == 0:
                results.append("YES")
            else:
                results.append("NO")
    print('\n'.join(results))

if __name__ == "__main__":
    main()