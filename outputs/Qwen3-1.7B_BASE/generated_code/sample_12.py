import sys
input = sys.stdin.read

def main():
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
        if m == 0:
            if any(x == 0 for x in a):
                results.append("YES")
            else:
                results.append("NO")
            continue
        if a[0] == m:
            results.append("YES")
            continue
        max_val = a[0]
        S = {a[0]}
        found = False
        for i in range(1, n):
            new_max = max_val
            new_set = set()
            for x in S:
                new_val_add = x + a[i]
                if new_val_add <= m and new_val_add > new_max:
                    new_max = new_val_add
                new_set.add(new_val_add)
                new_val_mul = x * a[i]
                if new_val_mul <= m and new_val_mul > new_max:
                    new_max = new_val_mul
                new_set.add(new_val_mul)
            if new_max == m:
                found = True
                results.append("YES")
                break
            if new_max > m:
                results.append("NO")
                break
            max_val = new_max
            S = new_set
        if not found:
            results.append("NO")
    print('\n'.join(results))

if __name__ == "__main__":
    main()