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
        intervals = []
        for _ in range(n):
            l = int(data[idx])
            r = int(data[idx + 1])
            intervals.append((l, r))
            idx += 2
        events = []
        for l, r in intervals:
            events.append((l, 1))
            events.append((r + 1, -1))
        events.sort(key=lambda x: (x[0], x[1]))
        current_count = 0
        max_count = 0
        for x, delta in events:
            if delta == 1:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            else:
                current_count -= 1
        results.append(max_count)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()