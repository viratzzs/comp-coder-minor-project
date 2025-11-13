t = input().strip()
n = len(t)
for k in range(1, n):
    if t[:k] == t[k:][0:k]:
        print("YES")
        print(t[k:])
        exit()
print("NO")