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
        squares = []
        for _ in range(n):
            x, y = int(data[idx]), int(data[idx+1])
            idx += 2
            squares.append((x, y))
        count = 0
        for i in range(n):
            x1, y1 = squares[i]
            for j in range(i+1, n):
                x2, y2 = squares[j]
                # Check if squares i and j are adjacent
                # Horizontal adjacency: x2 == x1 + m - 1 and y2 == y1
                if x2 == x1 + m - 1 and y2 == y1:
                    count += 1
                # Vertical adjacency: x1 == x2 and y1 == y2 + m - 1
                elif x1 == x2 and y1 == y2 + m - 1:
                    count += 1
        perimeter = 4 * m * n - 2 * count * m
        results.append(perimeter)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()