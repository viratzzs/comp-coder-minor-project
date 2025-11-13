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
        k = int(data[idx+1])
        q = int(data[idx+2])
        idx += 3
        
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        for __ in range(q):
            l = int(data[idx])
            r = int(data[idx+1])
            idx += 2
            
            a_l = a[l-1]
            a_r = a[r-1]
            
            if a_l == a_r:
                a_l = a_r
            else:
                pass
            
            current_max = a_l
            current_min = a_l
            count_max = 1
            count_min = 1
            overlap = 0
            
            if current_max == current_min:
                overlap = count_max
            
            sum_total = k - (count_max + count_min - overlap)
            
            for j in range(l + k - 1, r + 1):
                a_j = a[j-1]
                
                new_max = max(current_max, a_j)
                new_min = min(current_min, a_j)
                
                new_count_max = count_max
                new_count_min = count_min
                
                if a_j == new_max:
                    new_count_max += 1
                if a_j == new_min:
                    new_count_min += 1
                
                if new_max == new_min:
                    overlap_new = new_count_max
                else:
                    overlap_new = 0
                
                count_new = new_count_max + new_count_min - overlap_new
                sum_total += k - count_new
                
                current_max, current_min = new_max, new_min
                count_max, count_min = new_count_max, new_count_min
            
            results.append(sum_total)
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()