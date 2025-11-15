import sys
from collections import defaultdict

MOD = 998244353

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    q = int(data[idx])
    idx += 1
    a = list(map(int, data[idx:idx+n]))
    idx += n
    
    def compute_xor(l, r):
        xor_val = 0
        for i in range(l-1, r):
            xor_val ^= a[i]
        return xor_val
    
    for _ in range(q):
        l = int(data[idx])
        idx += 1
        r = int(data[idx])
        idx += 1
        if l > r:
            print(-1)
            continue
        segment = a[l-1:r]
        total_elements = r - l + 1
        x = compute_xor(l, r)
        if x == 0:
            k = min(r - l, total_elements - 1)
            print(k, 1)
            continue
        max_k = min(r - l, total_elements - 1)
        found = False
        for k in range(max_k, -1, -1):
            dp = [set() for _ in range(k+1)]
            dp[0].add(0)
            for a_i in segment:
                new_dp = [set() for _ in range(k+1)]
                for i in range(k+1):
                    for x_val in dp[i]:
                        new_x = x_val ^ a_i
                        if new_x <= 50:
                            new_dp[i+1].add(new_x)
                for i in range(k+1):
                    dp[i] = new_dp[i]
            if x in dp[k]:
                print(k, 1)
                found = True
                break
        if not found:
            print(-1)

if __name__ == "__main__":
    main()