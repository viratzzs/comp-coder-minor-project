import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    q = int(data[idx])
    idx += 1
    for i in range(1, q + 1):
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1
        if i % 2 == 1:
            print(f'y+')
        else:
            print(f'x+')

if __name__ == "__main__":
    main()