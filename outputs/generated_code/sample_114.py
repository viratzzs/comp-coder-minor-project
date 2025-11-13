import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        count = 0
        while n > 3:
            n = n // 4
            count += 1
        print(2 ** count)

if __name__ == "__main__":
    main()