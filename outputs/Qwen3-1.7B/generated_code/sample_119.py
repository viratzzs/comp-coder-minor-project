import sys
from itertools import combinations

MOD = 998244353

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    q = int(input[ptr])
    ptr += 1
    a = list(map(int, input[ptr:ptr + n]))
    ptr += n
    for _ in range(q):
        l = int(input[ptr])
        ptr += 1
        r = int(input[ptr])
        ptr += 1
        segment = a[l-1:r]
        m = len(segment)
        has_zero = 0 in segment
        if has_zero:
            t = 1
        else:
            freq = {}
            for num in segment:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
            has_duplicates = any(v >= 2 for v in freq.values())
            if has_duplicates:
                t = 2
            else:
                s = set(segment)
                found = False
                for i in range(m):
                    for j in range(i+1, m):
                        x = segment[i] ^ segment[j]
                        if x in s:
                            found = True
                            break
                    if found:
                        break
                if found:
                    t = 3
                else:
                    if m >= 4:
                        found = False
                        for combo in combinations(segment, 4):
                            if (combo[0] ^ combo[1] ^ combo[2] ^ combo[3]) == 0:
                                found = True
                                break
                        if found:
                            t = 4
                    else:
                        t = -1
        if t == -1:
            print(-1)
        else:
            max_k = m - t
            if max_k < 0:
                print(-1)
            else:
                if t == 1:
                    ways = segment.count(0)
                elif t == 2:
                    ways = 0
                    freq = {}
                    for num in segment:
                        if num in freq:
                            freq[num] += 1
                        else:
                            freq[num] = 1
                    count = 0
                    for v in freq.values():
                        count += (v * (v - 1)) // 2
                    ways = count
                elif t == 3:
                    s = set(segment)
                    count = 0
                    for i in range(m):
                        for j in range(i+1, m):
                            x = segment[i] ^ segment[j]
                            if x in s:
                                count += 1
                    ways = count
                else:
                    ways = 0
                print(max_k, ways % MOD)

if __name__ == "__main__":
    main()