import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = []
        for i in range(n):
            if i % 2 == 0:
                a.append(1)
            else:
                a.append(2)
        print(' '.join(map(str, a)))

if __name__ == "__main__":
    main()