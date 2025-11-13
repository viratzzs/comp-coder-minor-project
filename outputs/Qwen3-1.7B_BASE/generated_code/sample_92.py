import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        s = data[idx]
        idx += 1
        n = len(s)
        if n % 3 != 0:
            results.append("NO")
            continue
        
        k = n // 3
        possible_pairs = [('Y', 'D'), ('Y', 'X'), ('D', 'Y'), ('D', 'X'), ('X', 'Y'), ('X', 'D')]
        
        found = False
        for c1, c2 in possible_pairs:
            s_new = list(s)
            for i in range(2):
                if s[i] == '?':
                    if i == 0:
                        s_new[i] = c1
                    else:
                        s_new[i] = c2
            for i in range(2, n):
                if s[i] == '?':
                    if i % 2 == 0:
                        s_new[i] = c1
                    else:
                        s_new[i] = c2
            
            valid = True
            for i in range(1, n):
                if s_new[i] == s_new[i-1]:
                    valid = False
                    break
            
            if valid:
                results.append("YES")
                results.append(''.join(s_new))
                results.append('\n'.join(f"{c} 0" for c in s_new))
                found = True
                break
        
        if not found:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()