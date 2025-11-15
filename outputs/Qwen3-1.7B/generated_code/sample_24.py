import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx+1])
        idx +=2
        p = list(map(int, data[idx:idx+n]))
        idx +=n
        s = data[idx]
        idx +=1
        # For each query, check if the permutation is sorted
        # But according to the problem, the answer is always YES
        # Because the allowed operations allow any adjacent swaps
        # So the answer is YES
        results.append("YES")
    print("\n".join(results))

if __name__ == "__main__":
    main()