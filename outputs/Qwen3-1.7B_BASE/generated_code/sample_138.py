import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, c = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        total = sum(ai for ai in a if ai >= 0)
        results.append(total)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()