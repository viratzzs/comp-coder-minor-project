import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        l = int(data[idx])
        r = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        current_S = list(range(l, r+1))
        answer = 0
        while current_S:
            x = None
            for x_candidate in current_S:
                if r // x_candidate >= k:
                    x = x_candidate
                    break
            if x is None:
                break
            answer += 1
            current_S.remove(x)
        results.append(str(answer))
    print('\n'.join(results))

if __name__ == "__main__":
    main()