import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    q = int(data[idx])
    idx += 1
    a = [0] * n
    results = []
    for _ in range(q):
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1
        if a[x-1] > a[y-1]:
            if a[x-1] >= 1:
                results.append('x-')
            else:
                results.append('x+')
        else:
            if a[y-1] >= 1:
                results.append('y-')
            else:
                results.append('y+')
        results.append('\n')
    print(''.join(results))

if __name__ == "__main__":
    main()