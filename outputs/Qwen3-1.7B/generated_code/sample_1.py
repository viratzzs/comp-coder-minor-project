import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, l, r = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        original_sum = sum(a[l-1:r])
        segment = a[l-1:r]
        max_segment = max(segment)
        outside = []
        for i in range(n):
            if i < l-1 or i >= r:
                outside.append(a[i])
        if len(outside) > 0:
            min_outside = min(outside)
            change = min_outside - max_segment
            minimal_sum = original_sum + change
        else:
            minimal_sum = original_sum
        print(minimal_sum)

if __name__ == "__main__":
    main()