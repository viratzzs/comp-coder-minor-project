t = input().strip()
n = len(t)
if n % 2 == 0:
    print("NO")
else:
    len_s = (n + 1) // 2
    s_candidate = t[:len_s]
    if t[len_s:] == s_candidate[1:]:
        print("YES")
        print(s_candidate)
    else:
        print("NO")