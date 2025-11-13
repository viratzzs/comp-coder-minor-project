t = input().strip()

if len(t) < 2:
    print("NO")
else:
    for n in range(1, len(t) + 1):
        m = len(t)
        for k in range(n):
            if 2 * n - k != m:
                continue
            s_candidate = t[:n]
            if s_candidate + s_candidate[k:] == t:
                print("YES")
                print(s_candidate)
                exit()
    print("NO")