import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        xc = int(data[idx])
        yc = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        if k == 1:
            results.append(f"{xc} {yc}")
        elif k == 2:
            results.append(f"{xc+1} {yc}")
            results.append(f"{xc-1} {yc}")
        else:
            results.append(f"{xc+1} {yc}")
            results.append(f"{xc-1} {yc+1}")
            results.append(f"{xc} {yc-1}")
            for _ in range(1, k-2):
                results.append(f"{xc} {yc}")
    print("\n".join(results))

if __name__ == "__main__":
    main()