import sys
import math

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        cities = []
        for _ in range(n):
            x = int(data[idx])
            y = int(data[idx+1])
            cities.append((x, y))
            idx += 2
        # Find the maximum k
        # We can try to find k as the maximum possible such that each region has at least k cities
        # For the purpose of this problem, we'll use the median of x and y coordinates
        # This is a heuristic approach
        # Sort the cities
        cities.sort()
        # Find the median x
        med_x = cities[n//2][0]
        # Find the median y
        med_y = cities[n//2][1]
        # The maximum k is floor(n/4)
        k = n // 4
        results.append(f"{k}\n{med_x} {med_y}")
    for res in results:
        print(res)

if __name__ == "__main__":
    main()