t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print("0")
    elif n == 2:
        print("01")
    else:
        print("0" + "1" * (n - 1))