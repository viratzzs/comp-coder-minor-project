import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        size = 1
        while size < n:
            size <<= 1
        
        tree = [(0, 0)] * (2 * size)
        
        def build(node, start, end):
            if start == end:
                tree[node] = (a[start], 1)
            else:
                mid = (start + end) // 2
                build(2*node+1, start, mid)
                build(2*node+2, mid+1, end)
                left = tree[2*node+1]
                right = tree[2*node+2]
                if left[0] == right[0]:
                    tree[node] = (left[0], left[1] + right[1])
                else:
                    if left[0] > right[0]:
                        tree[node] = (left[0], left[1])
                    else:
                        tree[node] = (right[0], right[1])
        
        build(0, 0, n-1)
        
        def query(node, node_start, node_end, l, r):
            if node_end < l or node_start > r:
                return (0, 0)
            if l <= node_start and node_end <= r:
                return tree[node]
            mid = (node_start + node_end) // 2
            left = query(2*node+1, node_start, mid, l, r)
            right = query(2*node+2, mid+1, node_end, l, r)
            if left[0] == right[0]:
                return (left[0], left[1] + right[1])
            elif left[0] > right[0]:
                return (left[0], left[1])
            else:
                return (right[0], right[1])
        
        for __ in range(q):
            l = int(data[idx]) - 1
            r = int(data[idx+1]) - 1
            idx += 2
            max_val, count = query(0, 0, n-1, l, r)
            print("YES" if count % 2 == 0 else "NO")

if __name__ == "__main__":
    main()