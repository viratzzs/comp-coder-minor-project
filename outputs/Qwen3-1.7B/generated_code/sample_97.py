import sys
import math

def get_divisors(x):
    divisors = set()
    for i in range(1, int(math.isqrt(x)) + 1):
        if x % i == 0:
            divisors.add(i)
            divisors.add(x // i)
    return divisors

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        x = int(data[index])
        m = int(data[index + 1])
        index += 2
        divisors = get_divisors(x)
        count = 0
        for d in divisors:
            y = x ^ d
            if 1 <= y <= m and y != x:
                count += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == "__main__":
    main()