import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        participants = []
        for _ in range(n):
            a = int(data[idx])
            b = int(data[idx+1])
            s = int(data[idx+2])
            participants.append((a, b, s))
            idx += 3
        cities = []
        for _ in range(m):
            k = int(data[idx])
            q = list(map(int, data[idx+1:idx+1+k]))
            cities.append((k, q))
            idx += 1 + k
        # Sort cities by the number of participants in non-decreasing order
        cities.sort(key=lambda x: x[0])
        possible = True
        for idx_c in range(m):
            k_i, q_i = cities[idx_c]
            if idx_c + 1 > k_i:
                possible = False
                break
        if not possible:
            results.append("-1")
            continue
        # Generate the output
        total_problems = m * (m + 1) // 2
        results.append(f"{total_problems}")
        for i in range(1, m + 1):
            start = i
            end = 2 * i
            for j in range(start, end):
                results.append(f"0 {j}")
    print("\n".join(results))

if __name__ == "__main__":
    main()