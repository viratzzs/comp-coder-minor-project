from collections import defaultdict
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    a = []
    for _ in range(n):
        a.append(int(data[idx]))
        idx += 1
    
    freq = defaultdict(int)
    for x in a:
        freq[x] += 1
    
    T = 0
    for x in a:
        T += (freq[x] * (freq[x] - 1)) // 2
    
    last = T
    
    q = int(data[idx])
    idx += 1
    
    for _ in range(q):
        type_q = int(data[idx])
        idx += 1
        
        if type_q == 1:
            p_prime = int(data[idx])
            idx += 1
            x_prime = int(data[idx])
            idx += 1
            
            p = ((p_prime + last) % n) + 1
            x = ((x_prime + last) % n) + 1
            
            if a[p-1] == x:
                print(0)
                last = T
                continue
            
            old_val = a[p-1]
            new_val = x
            
            count_old = freq[old_val]
            count_new = freq[new_val]
            
            T += (- (count_old - 1) + count_new)
            freq[old_val] -= 1
            freq[new_val] += 1
            a[p-1] = new_val
            
            last = T
        else:
            l_prime = int(data[idx])
            idx += 1
            r_prime = int(data[idx])
            idx += 1
            
            l = ((l_prime + last) % n) + 1
            r = ((r_prime + last) % n) + 1
            
            if l > r:
                l, r = r, l
            
            S = (r - l + 1) * (r - l) // 2
            answer = S - T
            print(answer)
            last = answer

if __name__ == "__main__":
    main()