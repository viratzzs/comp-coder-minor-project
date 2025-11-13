import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        x = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        count = 0
        if x <= m:
            count += 1
        k = 1
        while True:
            t_val = x * k
            xor_val = t_val ^ x
            if xor_val <= m:
                count += 1
                k += 1
            else:
                break
        print(count)

if __name__ == "__main__":
    main()