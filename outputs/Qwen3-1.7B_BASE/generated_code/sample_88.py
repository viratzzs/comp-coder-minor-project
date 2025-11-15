import sys
import bisect

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
        cities.sort()
        best_min = 0
        best_x = 0
        best_y = 0
        for k in range(1, n):
            first_group = cities[:k]
            second_group = cities[k:]
            max_x_first = first_group[-1][0]
            max_x_second = second_group[0][0]
            x0 = max_x_first
            sorted_y1 = sorted(y for x, y in first_group)
            sorted_y2 = sorted(y for x, y in second_group)
            A = k // 2
            B = 2 * A - k
            if not (0 <= B <= len(second_group)):
                continue
            y0_first = sorted_y1[A]
            y0_second = sorted_y2[B]
            count1 = A
            count2 = B + (k - A)
            count3 = B + (len(second_group) - B)
            count4 = B + (len(second_group) - B)
            current_min = min(count1, count2, count3, count4)
            if current_min > best_min:
                best_min = current_min
                best_x = max_x_first
                best_y = y0_first
        results.append(f"{best_min}\n{best_x} {best_y}")
    print("\n".join(results))

if __name__ == "__main__":
    main()