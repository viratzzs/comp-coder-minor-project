import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        if n == 2:
            print(0)
        else:
            print(n)

if __name__ == "__main__":
    main()