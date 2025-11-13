import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, m = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        if n == 1:
            if a[0] == m:
                results.append("YES")
            else:
                results.append("NO")
            continue
        possible = set()
        possible.add(a[0])
        found = False
        for i in range(1, n):
            new_possible = set()
            for val in possible:
                new_add = val + a[i]
                if new_add <= m:
                    new_possible.add(new_add)
                new_mul = val * a[i]
                if new_mul <= m:
                    new_possible.add(new_mul)
            possible = new_possible
            if m in possible:
                found = True
                break
        if found:
            results.append("YES")
        else:
            results.append("NO")
    print('\n'.join(results))

if __name__ == "__main__":
    main()