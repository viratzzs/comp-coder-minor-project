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
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        x = None
        for i in range(n):
            if a[i] not in (-1, 1):
                x = a[i]
                break
        
        if x is None:
            # No x, generate all possible subarray sums of the normal elements
            m = n
            dp = {0}
            for i in range(m):
                new_dp = set()
                for s in dp:
                    new_dp.add(s + 1)
                    new_dp.add(s - 1)
                dp = new_dp
            combined = set(dp)
            combined.add(0)
            combined = sorted(combined)
            results.append(len(combined))
            results.append(' '.join(map(str, combined)))
        else:
            # x is found, generate all possible subarray sums of the normal elements
            m = n - 1
            dp = {0}
            for i in range(m):
                new_dp = set()
                for s in dp:
                    new_dp.add(s + 1)
                    new_dp.add(s - 1)
                dp = new_dp
            combined = set(dp)
            combined.add(0)
            combined = sorted(combined)
            added = [s + x for s in combined]
            combined = set(combined + added)
            combined = sorted(combined)
            results.append(len(combined))
            results.append(' '.join(map(str, combined)))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()