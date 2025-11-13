import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        sorted_a = sorted(a)
        count = 0
        for i in range(n-1):
            if a[i] > a[i+1]:
                count += 1
        if count == 0:
            results.append("0")
        else:
            results.append(f"{count}")
            if n == 1:
                results.append("")
            else:
                res = []
                for i in range(n-1):
                    if i % 2 == 0:
                        res.append("R")
                    else:
                        res.append("D")
                results.append("".join(res))
    print("\n".join(results))

if __name__ == "__main__":
    main()