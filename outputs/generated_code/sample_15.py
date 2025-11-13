import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x_c, y_c, k = map(int, sys.stdin.readline().split())
        if k == 1:
            print(x_c, y_c)
        elif k == 2:
            print(x_c + 1, y_c + 1)
            print(x_c - 1, y_c - 1)
        else:
            res = []
            for i in range(k):
                if i < k - 1:
                    x = x_c + i
                    y = y_c + i
                else:
                    x = x_c - ((k - 2) * (k - 1)) // 2
                    y = y_c - ((k - 2) * (k - 1)) // 2
                res.append((x, y))
            for x, y in res:
                print(x, y)

if __name__ == "__main__":
    main()