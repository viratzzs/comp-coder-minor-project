import math

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        if n ** 0.5 != int(n ** 0.5):
            results.append("No")
            continue
        
        r = int(n ** 0.5)
        if s[0] != '1' or s[-1] != '1':
            results.append("No")
            continue
        
        valid = True
        
        # Check rows
        for i in range(r):
            start = i * r
            end = start + r - 1
            if i == 0 or i == r - 1:
                continue
            if s[start] != '1' or s[end] != '1':
                valid = False
                break
            # Check inner elements
            for k in range(start + 1, end):
                if s[k] != '0':
                    valid = False
                    break
            if not valid:
                break
        
        if not valid:
            results.append("No")
            continue
        
        # Check columns
        for j in range(r):
            start_col = j + r
            end_col = (r - 2) * r + j
            if j == 0 or j == r - 1:
                continue
            if start_col > end_col:
                continue
            for k in range(start_col, end_col + 1, r):
                if s[k] != '0':
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            results.append("Yes")
        else:
            results.append("No")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()