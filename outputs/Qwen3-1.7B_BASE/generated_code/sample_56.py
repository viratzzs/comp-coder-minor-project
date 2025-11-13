n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * n
total = 0

while total < k:
    found = False
    for i in range(n):
        max_c = (a[i] + b[i] - 1) // b[i]
        if c[i] < max_c:
            c[i] += 1
            total += 1
            found = True
            break
    if not found:
        break

print(' '.join(map(str, c)))