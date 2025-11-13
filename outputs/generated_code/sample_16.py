import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        p = list(map(int, input[idx:idx+n]))
        idx += n
        available = list(range(1, n+1))
        q = []
        for val in p:
            # Find the smallest available number not equal to val
            for num in available:
                if num != val:
                    q.append(num)
                    available.remove(num)
                    break
            else:
                # If all available are equal to val, choose the smallest one
                # but this is not possible since available is a permutation
                # so this should not happen
                q.append(available[0])
                available.remove(available[0])
        results.append(' '.join(map(str, q)))
    print('\n'.join(results))

if __name__ == "__main__":
    main()