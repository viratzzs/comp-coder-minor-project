import math

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        
        lower_bound = max(a, b)
        
        def lcm(a, b):
            return a * b // math.gcd(a, b)
        
        lcm_val = lcm(a, b)
        max_x = min(a - 1, b - 1)
        possible = []
        
        for x in range(0, max_x + 1):
            if x >= lower_bound:
                m_candidate = x
            else:
                numerator = lower_bound - x
                k = (numerator + lcm_val - 1) // lcm_val
                m_candidate = x + k * lcm_val
            if m_candidate >= lower_bound:
                possible.append(m_candidate)
        
        print(min(possible))

if __name__ == "__main__":
    main()