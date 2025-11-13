import sys

def contains_seven(num):
    return '7' in str(num)

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if '7' in str(n):
            print(0)
            continue
        found = False
        for k in range(1, 20):
            # Check if adding 10^k - 1 (k 9s) gives a 7
            s = 10**k - 1
            m = n + s
            if contains_seven(m):
                print(k)
                found = True
                break
        if not found:
            print(20)

if __name__ == "__main__":
    solve()