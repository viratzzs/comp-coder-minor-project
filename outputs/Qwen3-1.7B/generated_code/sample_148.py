import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        l = int(data[index])
        r = int(data[index+1])
        k = int(data[index+2])
        index += 3
        m = r // k
        if m >= l:
            results.append(str(m - l + 1))
        else:
            results.append("0")
    print('\n'.join(results))

if __name__ == "__main__":
    main()