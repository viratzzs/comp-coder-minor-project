import sys
import math
from collections import defaultdict

MOD = 998244353

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
        adj = [[] for _ in range(n + 1)]
        for __ in range(n - 1):
            x = int(data[idx])
            y = int(data[idx + 1])
            adj[x].append(y)
            adj[y].append(x)
            idx += 2
        
        # Compute escape probabilities for each node v (1 <= v <= n)
        # Special case: root node v=1 has escape probability 1
        escape = [0] * (n + 1)
        escape[1] = 1
        
        # Process nodes in a way that allows us to compute escape probabilities for all nodes
        # This is a placeholder for the actual implementation logic
        # Placeholder for the correct DP approach
        for v in range(2, n + 1):
            # Placeholder logic for the escape probability
            # This part needs to be filled with the actual recursive logic
            # For the purpose of this example, we assume a simple model
            escape[v] = 1  # Placeholder
        
        results.append(' '.join(map(str, escape[1:n + 1])))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()