import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        x = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        count = 0
        for d in range(1, x+1):
            if x % d == 0 or ((x ^ d) % d == 0):
                y = x ^ d
                if 1 <= y <= m:
                    count += 1
        results.append(count)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()