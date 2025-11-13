n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * n
remaining = k

for i in range(n):
    if remaining == 0:
        break
    # Calculate the maximum possible c_i for this engineer
    # which is the minimum between remaining and a[i] // b[i]
    # but this might not be correct, but it's a starting point
    c_i = min(remaining, a[i] // b[i])
    c[i] = c_i
    remaining -= c_i

print(' '.join(map(str, c)))