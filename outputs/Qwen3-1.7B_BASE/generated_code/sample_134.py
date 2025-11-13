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
        a = n - k + 1
        b = n
        if a > b:
            results.append("YES")
        else:
            count = (b + 1) // 2 - (a // 2)
            if count % 2 == 0:
                results.append("YES")
            else:
                results.append("NO")
    print("\n".join(results))

if __name__ == "__main__":
    main()