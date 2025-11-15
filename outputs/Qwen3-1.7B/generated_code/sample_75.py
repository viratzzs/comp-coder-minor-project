import sys
from collections import defaultdict

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        points = []
        for _ in range(n):
            x = int(input[ptr])
            y = int(input[ptr+1])
            points.append((x, y))
            ptr += 2
        total_tri = n * (n-1) * (n-2) // 6
        colinear = 0
        # Horizontal lines
        y0 = 0
        y1 = 1
        count_y0 = 0
        count_y1 = 0
        for x, y in points:
            if y == y0:
                count_y0 += 1
            elif y == y1:
                count_y1 += 1
        colinear += count_y0 * (count_y0 - 1) * (count_y0 - 2) // 6 if count_y0 >= 3 else 0
        colinear += count_y1 * (count_y1 - 1) * (count_y1 - 2) // 6 if count_y1 >= 3 else 0
        # Vertical lines
        x_counts = defaultdict(int)
        for x, y in points:
            x_counts[x] += 1
        colinear += sum(c * (c-1) * (c-2) // 6 for c in x_counts.values() if c >= 3)
        # Slope 1
        slope1 = defaultdict(int)
        for x, y in points:
            c = y - x
            slope1[c] += 1
        colinear += sum(c * (c-1) * (c-2) // 6 for c in slope1.values() if c >= 3)
        # Slope -1
        slope_minus1 = defaultdict(int)
        for x, y in points:
            c = x + y
            slope_minus1[c] += 1
        colinear += sum(c * (c-1) * (c-2) // 6 for c in slope_minus1.values() if c >= 3)
        results.append(total_tri - colinear)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()