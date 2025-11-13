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
        c = list(map(int, data[idx:idx + n]))
        idx += n
        
        even_count = 0
        odd_count = 0
        
        for color in c:
            if c.count(color) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        results.append(even_count + odd_count)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()