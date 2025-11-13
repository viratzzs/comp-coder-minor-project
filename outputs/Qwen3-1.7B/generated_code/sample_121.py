import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, x = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        residues = set()
        for num in a:
            residues.add(num % x)
        # Find the smallest non-negative integer not in residues
        m = 0
        while m in residues:
            m += 1
        results.append(str(m))
    print('\n'.join(results))

if __name__ == '__main__':
    main()