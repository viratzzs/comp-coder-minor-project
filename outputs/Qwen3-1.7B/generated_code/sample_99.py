import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        S = list(map(int, input[ptr:ptr+m]))
        ptr += m
        max_val = max(S)
        if S.count(max_val) > 1:
            print(-1)
            continue
        if n == 1:
            print(max_val)
            continue
        if m < n:
            print(-1)
            continue
        sorted_S = sorted(S, reverse=True)
        res = [max_val]
        for i in range(1, n):
            if not sorted_S:
                print(-1)
                break
            res.append(sorted_S[0])
            sorted_S.pop(0)
        else:
            print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()