import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, m = int(data[idx]), int(data[idx + 1])
        idx += 2
        strings = []
        for _ in range(n):
            s = data[idx]
            idx += 1
            strings.append(s)
        # Precompute n_contribution and c_contribution for each string
        n_contrib = []
        c_contrib = []
        for s in strings:
            # Compute n_contribution
            n_count = 0
            i = 0
            while i < len(s):
                if s[i] == 'n':
                    n_count += 1
                    i += 1
                    if n_count == 5:
                        break
                elif s[i] == 'a':
                    n_count += 1
                    i += 1
                    if n_count == 5:
                        break
                elif s[i] == 'r':
                    n_count += 1
                    i += 1
                    if n_count == 5:
                        break
                elif s[i] == 'e':
                    n_count += 1
                    i += 1
                    if n_count == 5:
                        break
                elif s[i] == 'k':
                    n_count += 1
                    i += 1
                    if n_count == 5:
                        break
                else:
                    i += 1
            n_contrib.append(n_count)
            # Compute c_contribution
            c_count = 0
            for ch in s:
                if ch in {'n', 'a', 'r', 'e', 'k'}:
                    c_count += 1
            c_contrib.append(c_count)
        # Compute the total difference
        total = 0
        for i in range(n):
            if n_contrib[i] > 0 and c_contrib[i] < n_contrib[i]:
                total += (n_contrib[i] - c_contrib[i])
        results.append(total)
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()