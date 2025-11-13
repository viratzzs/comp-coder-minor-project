import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        if len(s) % 2 == 0:
            print(s)
        else:
            print(-1)

if __name__ == "__main__":
    main()