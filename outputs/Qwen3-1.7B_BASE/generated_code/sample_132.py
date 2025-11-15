import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        print(n)

if __name__ == "__main__":
    main()