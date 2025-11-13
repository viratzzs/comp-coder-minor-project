import sys

def count_valid_y(x, m):
    # Count divisors of x in [1, m]
    divisors = 0
    for i in range(1, m + 1):
        if x % i == 0:
            divisors += 1
    # Count multiples of x in [1, m]
    multiples = m // x
    # Subtract 1 to account for overlap (y = x)
    return multiples + divisors - 1

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x, m = map(int, sys.stdin.readline().split())
        print(count_valid_y(x, m))

if __name__ == "__main__":
    main()