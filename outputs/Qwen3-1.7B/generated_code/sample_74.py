import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x, y, k = map(int, sys.stdin.readline().split())
        if x == 0 and y == 0:
            print(1)
        else:
            if x == 0:
                m_x = 1
            else:
                m_x = 2 * ((x + k - 1) // k) - 1
            if y == 0:
                m_y = 1
            else:
                m_y = 2 * ((y + k - 1) // k)
            print(max(m_x, m_y))

if __name__ == "__main__":
    main()