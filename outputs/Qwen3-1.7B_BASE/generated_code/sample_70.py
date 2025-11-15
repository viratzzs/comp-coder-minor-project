import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))
    edges = []
    for i in range(2, len(data), 2):
        edges.append((int(data[i]), int(data[i+1])))
    
    from collections import defaultdict
    value_to_nodes = defaultdict(list)
    for i in range(2*n):
        value = a[i]
        value_to_nodes[value].append(i+1)
    
    selected = []
    for val in range(1, n+1):
        if val not in value_to_nodes:
            continue
        nodes = value_to_nodes[val]
        if len(nodes) == 1:
            selected.append(nodes[0])
            continue
        selected.append(nodes[0])
    
    print(len(selected))
    print(' '.join(map(str, selected)))

main()