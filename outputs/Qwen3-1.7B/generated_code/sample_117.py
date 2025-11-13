import math
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        l = int(data[index])
        r = int(data[index+1])
        G = int(data[index+2])
        index += 3
        
        a_min = (l + G - 1) // G
        b_max = r // G
        
        if a_min > b_max:
            results.append("-1 -1")
            continue
        
        if math.gcd(a_min, b_max) == 1:
            results.append(f"{a_min} {b_max}")
        else:
            found = False
            for a in range(a_min, b_max + 1):
                if math.gcd(a, b_max) == 1:
                    results.append(f"{a} {b_max}")
                    found = True
                    break
            if not found:
                results.append("-1 -1")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()