import sys
import math

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        
        steps_x = 0
        if x != 0:
            steps_x = (x + k - 1) // k
        
        steps_y = 0
        if y != 0:
            steps_y = (y + k - 1) // k
        
        results.append(str(steps_x + steps_y))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()