def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        if n % 2 == 0:
            k = n // 2
            first_part = [1, 1] + list(range(2, k + 1))
            second_part = list(range(k - 1, 0, -1))
            results.append(' '.join(map(str, first_part + second_part)))
        else:
            k = (n - 1) // 2
            first_part = [1, 1] + list(range(2, k + 1))
            second_part = [k + 1] + list(range(k, 0, -1))
            results.append(' '.join(map(str, first_part + second_part)))
    print('\n'.join(results))

if __name__ == '__main__':
    main()