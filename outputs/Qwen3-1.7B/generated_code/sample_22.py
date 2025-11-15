import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if n == 1:
            print('0')
        else:
            print('0' * (n-1) + '1')

if __name__ == "__main__":
    main()