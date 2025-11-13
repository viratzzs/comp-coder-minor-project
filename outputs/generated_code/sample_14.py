import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx+1])
        idx += 2
        x = list(map(int, data[idx:idx+n]))
        idx += n
        queries = list(map(int, data[idx:idx+q]))
        idx += q
        
        freq = defaultdict(int)
        for p in range(1, n):
            s = p * (n - p)
            len_p = x[p] - x[p-1] + 1
            freq[s] += len_p
        
        for k in queries:
            results.append(str(freq.get(k, 0)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()