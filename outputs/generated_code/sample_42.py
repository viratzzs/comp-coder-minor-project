t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print('a')
    elif n == 2:
        print('ae')
    else:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = vowels[:n-1] + [vowels[0]]
        print(''.join(s))