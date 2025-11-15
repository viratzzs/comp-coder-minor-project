import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        a.sort()
        result = [a[0]]
        remaining = a[1:]
        while remaining:
            if len(remaining) == 1:
                result.append(remaining[0])
                break
            if len(remaining) % 2 == 0:
                result.append(remaining[-1])
                remaining = remaining[:-1]
            else:
                result.append(remaining[-1])
                remaining = remaining[:-1]
                result.append(remaining[0])
                remaining = remaining[1:]
        score = 0
        for i in range(len(result)):
            if i == 0:
                current_max = result[i]
                current_min = result[i]
            else:
                current_max = result[i]
                current_min = result[i-1] if i > 0 else result[0]
            score += current_max - current_min
        results.append(score)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()