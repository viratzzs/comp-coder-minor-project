import math

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        k = int(data[index+1])
        index += 2
        S = n * k + n * (n - 1) // 2
        i0 = (1 - 2 * k) / 2
        candidates = set()
        candidates.add(1)
        candidates.add(n)
        candidates.add(int(math.floor(i0)))
        candidates.add(int(math.ceil(i0)))
        min_x = float('inf')
        for i in candidates:
            if 1 <= i <= n:
                P_i = i * k + i * (i - 1) // 2
                val = abs(2 * P_i - S)
                if val < min_x:
                    min_x = val
        results.append(str(min_x))
    print('\n'.join(results))

if __name__ == "__main__":
    main()