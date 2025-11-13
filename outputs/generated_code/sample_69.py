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
        users = []
        for _ in range(n):
            l = int(data[idx])
            r = int(data[idx + 1])
            users.append((l, r))
            idx += 2
        res = []
        for i in range(n):
            l_i, r_i = users[i]
            predictors = []
            for j in range(n):
                if j != i and users[j][0] <= l_i and users[j][1] >= r_i:
                    predictors.append(users[j])
            if not predictors:
                res.append(0)
                continue
            max_l = max(x[0] for x in predictors)
            min_r = min(x[1] for x in predictors)
            if max_l > min_r:
                res.append(0)
            else:
                overlap = max(0, min(min_r, r_i) - max(max_l, l_i) + 1)
                count = (min_r - max_l + 1) - overlap
                res.append(count)
        results.append(' '.join(map(str, res)))
    print('\n'.join(results))

if __name__ == "__main__":
    main()