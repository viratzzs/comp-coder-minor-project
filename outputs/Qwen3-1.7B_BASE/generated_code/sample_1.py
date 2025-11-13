import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        l = int(data[idx + 1])
        r = int(data[idx + 2])
        idx += 3
        a = list(map(int, data[idx:idx + n]))
        idx += n
        elements_in_segment = a[l-1:r]
        elements_in_set = set(elements_in_segment)
        elements_not_in_segment = [x for x in a if x not in elements_in_set]
        original_sum = sum(elements_in_segment)
        if not elements_not_in_segment:
            results.append(str(original_sum))
        else:
            max_val = max(elements_in_segment)
            min_rest = min(elements_not_in_segment)
            results.append(str(original_sum - max_val + min_rest))
    print('\n'.join(results))

if __name__ == "__main__":
    main()