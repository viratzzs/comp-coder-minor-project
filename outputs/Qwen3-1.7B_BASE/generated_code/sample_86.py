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
        
        a1 = list(map(int, data[idx:idx + n]))
        idx += n
        
        a2 = list(map(int, data[idx:idx + n]))
        idx += n
        
        option1 = a1[0] + sum(a1[1:]) + a2[-1]
        option2 = a1[0] + a2[0] + sum(a2[1:])
        
        results.append(str(max(option1, option2)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()