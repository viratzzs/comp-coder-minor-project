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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        unique_elements = []
        seen = set()
        for num in a:
            if num not in seen:
                seen.add(num)
                unique_elements.append(num)
        # Transform
        transformed = []
        for i in range(len(unique_elements)):
            if (i + 1) % 2 == 1:
                transformed.append(-unique_elements[i])
            else:
                transformed.append(unique_elements[i])
        results.append(f"{len(transformed)}\n{' '.join(map(str, transformed))}")
    print('\n'.join(results))

if __name__ == "__main__":
    main()