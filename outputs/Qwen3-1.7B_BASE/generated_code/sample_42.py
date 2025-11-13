t = int(input())
for _ in range(t):
    n = int(input())
    vowels = ['a', 'e', 'i', 'o', 'u']
    base = n // 5
    remainder = n % 5
    counts = [base + 1] * remainder + [base] * (5 - remainder)
    s = ''.join([v * c for v, c in zip(vowels, counts)])
    print(s)