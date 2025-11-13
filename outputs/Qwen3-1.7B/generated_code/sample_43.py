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
        m = int(data[idx+1])
        q = int(data[idx+2])
        idx +=3
        teachers = list(map(int, data[idx:idx+m]))
        idx += m
        queries = list(map(int, data[idx:idx+q]))
        idx += q
        for a in queries:
            min_dist = min(abs(a - teachers[0]), abs(a - teachers[1]))
            results.append(str(min_dist))
    print('\n'.join(results))

if __name__ == "__main__":
    main()