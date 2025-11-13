import sys

t = input().strip()
n = len(t)

if n % 2 == 0:
    print("NO")
else:
    for L in range((n + 1) // 2, n):
        k = 2 * L - n
        if 1 <= k <= L - 1:
            s = t[:L]
            if t == s + s[k:]:
                print("YES")
                print(s)
                sys.exit()
    print("NO")