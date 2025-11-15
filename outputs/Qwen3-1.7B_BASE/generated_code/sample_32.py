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
        x = []
        y = []
        for _ in range(n):
            xi = int(data[idx])
            yi = int(data[idx+1])
            x.append(xi)
            y.append(yi)
            idx += 2
        s_x = [0] * (n+1)
        s_y = [0] * (n+1)
        for i in range(1, n+1):
            s_x[i] = s_x[i-1] + x[i-1]
            s_y[i] = s_y[i-1] + y[i-1]
        sum_overlap = 0
        for i in range(n-1):
            dx = s_x[i+1] - s_x[i]
            dy = s_y[i+1] - s_y[i]
            if dx * dx + dy * dy == m * m:
                sum_overlap += 2 * (dx + dy)
        perimeter = 4 * m * n - 2 * sum_overlap
        results.append(str(perimeter))
    print('\n'.join(results))

if __name__ == "__main__":
    main()