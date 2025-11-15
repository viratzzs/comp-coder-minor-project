import sys

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.data = data
        self.tree = [None] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = {
                'max_subarray': data[i],
                'max_prefix': data[i],
                'max_suffix': data[i],
                'total_sum': data[i],
                'start': i,
                'end': i
            }
        for i in range(self.size - 1, 0, -1):
            left = self.tree[2 * i]
            right = self.tree[2 * i + 1]
            left_max_sub = left['max_subarray']
            right_max_sub = right['max_subarray']
            left_max_suffix = left['max_suffix']
            right_max_prefix = right['max_prefix']
            combined = left_max_suffix + right_max_prefix
            current_max_sub = max(left_max_sub, right_max_sub, combined)
            left_max_prefix = left['max_prefix']
            right_max_prefix = right['max_prefix']
            left_total_sum = left['total_sum']
            combined_prefix = left_total_sum + right_max_prefix
            current_max_prefix = max(left_max_prefix, combined_prefix)
            left_max_suffix = left['max_suffix']
            right_max_suffix = right['max_suffix']
            right_total_sum = right['total_sum']
            combined_suffix = right_total_sum + left_max_suffix
            current_max_suffix = max(right_max_suffix, combined_suffix)
            current_total_sum = left['total_sum'] + right['total_sum']
            self.tree[i] = {
                'max_subarray': current_max_sub,
                'max_prefix': current_max_prefix,
                'max_suffix': current_max_suffix,
                'total_sum': current_total_sum,
                'start': left['start'] if current_max_sub == left_max_sub else right['start'] if current_max_sub == right_max_sub else (left['end'] + 1 if current_max_sub == combined else -1),
                'end': left['end'] if current_max_sub == left_max_sub else right['end'] if current_max_sub == right_max_sub else (left['end'] if current_max_sub == combined else -1)
            }

    def query_range(self, l, r):
        def _query(node, node_l, node_r, l, r):
            if node_r < l or node_l > r:
                return (0, -1, -1)
            if l <= node_l and node_r <= r:
                return self.tree[node], node_l, node_r
            mid = (node_l + node_r) // 2
            left_res = _query(2 * node, node_l, mid, l, r)
            right_res = _query(2 * node + 1, mid + 1, node_r, l, r)
            if left_res[0] == 0 and right_res[0] == 0:
                return (0, -1, -1)
            if left_res[0] == 0:
                return right_res
            if right_res[0] == 0:
                return left_res
            # Combine the results
            if left_res[0] > right_res[0]:
                return left_res
            else:
                return right_res
        res = _query(1, 0, self.size - 1, l, r)
        return res

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    a = list(map(int, input[ptr:ptr + n]))
    ptr += n
    b = list(map(int, input[ptr:ptr + n]))
    ptr += n
    c = [a[i] + b[i] for i in range(n)]
    st = SegmentTree(c)
    q = int(input[ptr])
    ptr += 1
    for _ in range(q):
        query_type = input[ptr]
        ptr += 1
        if query_type == '1':
            p = int(input[ptr]) - 1
            ptr += 1
            x = int(input[ptr])
            ptr += 1
            a[p] = x
        elif query_type == '2':
            p = int(input[ptr]) - 1
            ptr += 1
            x = int(input[ptr])
            ptr += 1
            b[p] = x
        elif query_type == '3':
            l = int(input[ptr]) - 1
            ptr += 1
            r = int(input[ptr]) - 1
            ptr += 1
            # Query the max subarray in [l, r]
            max_sub, start, end = st.query_range(l, r)
            if max_sub == 0:
                print(0)
                continue
            # Find max_left in [l, start-1]
            max_left = -float('inf')
            current = 0
            for i in range(l, start):
                current = max(c[i], current + c[i])
                if current > max_left:
                    max_left = current
            # Find max_right in [end+1, r]
            max_right = -float('inf')
            current = 0
            for i in range(end + 1, r + 1):
                current = max(c[i], current + c[i])
                if current > max_right:
                    max_right = current
            if max_left == -float('inf') and max_right == -float('inf'):
                print(max_sub)
            else:
                print(max_sub + max_left + max_right)

if __name__ == "__main__":
    main()