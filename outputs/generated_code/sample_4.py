import sys
import bisect

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        adj = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u = int(input[ptr])
            v = int(input[ptr+1])
            adj[u].append(v)
            adj[v].append(u)
            ptr += 2
        depth = [0] * (n + 1)
        subtree_depths = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        def dfs(u, parent):
            visited[u] = True
            for v in adj[u]:
                if v != parent:
                    dfs(v, u)
                    subtree_depths[u].append(depth[v])
            subtree_depths[u].append(depth[u])
            depth[u] = depth[parent] + 1 if parent != 0 else 0
        dfs(1, 0)
        children = [[] for _ in range(n + 1)]
        def build_children(u, parent):
            for v in adj[u]:
                if v != parent:
                    children[u].append(v)
                    build_children(v, u)
        build_children(1, 0)
        total = 0
        for l in range(1, n+1):
            children_l = children[l]
            for i in range(len(children_l)):
                for j in range(i+1, len(children_l)):
                    list1 = [d - depth[l] for d in subtree_depths[children_l[i]]]
                    list2 = [d - depth[l] for d in subtree_depths[children_l[j]]]
                    list1.sort()
                    list2.sort()
                    m = len(list1)
                    k = len(list2)
                    prefix = [0] * (k + 1)
                    for i in range(k):
                        prefix[i+1] = prefix[i] + list2[i]
                    sum_min = 0
                    for a in list1:
                        idx = bisect.bisect_left(list2, a)
                        sum_min += prefix[idx] + (k - idx) * a
                    contribution = 2 * sum_min - m * k
                    total += contribution
        print(total)

if __name__ == "__main__":
    main()