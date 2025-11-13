import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    a = list(map(int, data[idx:idx + n]))
    idx += n
    q = int(data[idx])
    idx += 1
    last = 0
    for _ in range(q):
        type_q = int(data[idx])
        if type_q == 1:
            p_prime = int(data[idx + 1])
            x_prime = int(data[idx + 2])
            idx += 3
            p = ((p_prime + last) % n) + 1
            x = ((x_prime + last) % n) + 1
            a[p - 1] = x
        else:
            l_prime = int(data[idx + 1])
            r_prime = int(data[idx + 2])
            idx += 3
            l = ((l_prime + last) % n) + 1
            r = ((r_prime + last) % n) + 1
            if l > r:
                l, r = r, l
            start = l - 1
            end = r
            count = defaultdict(int)
            for i in range(start, end):
                count[a[i]] += 1
            total_pairs = (r - l + 1) * (r - l) // 2
            same_pairs = 0
            for c in count.values():
                same_pairs += c * (c - 1) // 2
            print(total_pairs - same_pairs)
            last = same_pairs

if __name__ == "__main__":
    main()