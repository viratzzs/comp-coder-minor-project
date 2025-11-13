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
        
        # Process from right to left
        i = n - 1
        while i >= 0:
            j = i - 1
            while j >= 0 and a[j] <= a[i]:
                j -= 1
            if j >= 0:
                # Move a[j] to the end
                a = a[:j] + [a[i]] + a[j+1:i] + a[i+1:]
            i -= 1
        
        results.append(' '.join(map(str, a)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()