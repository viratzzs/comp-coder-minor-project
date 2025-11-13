import sys

def comb_mod2(a, b):
    if b == 0:
        return 1
    if a < b:
        return 0
    res = 1
    for i in range(60):
        if (b >> i) & 1 == 0:
            if (a >> i) & 1 == 0:
                return 0
    return 1

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        k = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        n = int(s, 2)
        pos = n // 2
        mod = 2
        if pos % 2 == 0:
            results.append(0)
            continue
        a = pos
        b = (n - pos)
        first_bit = (a >> 0) & 1
        second_bit = (b >> 0) & 1
        if first_bit == 0:
            if second_bit == 0:
                results.append(0)
            else:
                results.append(1)
        else:
            if second_bit == 1:
                results.append(1)
            else:
                results.append(0)
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()