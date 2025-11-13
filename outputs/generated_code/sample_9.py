import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        n = int(input[ptr])
        m = int(input[ptr+1])
        v = int(input[ptr+2])
        ptr += 3
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        total_sum = sum(a)
        if total_sum < m * v:
            results.append(-1)
            continue
        sum_m = 0
        current_sum = 0
        index = 0
        possible = True
        for i in range(m):
            while index < n and current_sum < v:
                current_sum += a[index]
                index += 1
            if index >= n:
                possible = False
                break
            sum_m += current_sum
            current_sum = 0
        if not possible:
            results.append(-1)
        else:
            results.append(total_sum - sum_m)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()