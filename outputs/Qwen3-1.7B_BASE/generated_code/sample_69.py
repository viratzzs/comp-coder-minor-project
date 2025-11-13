import bisect

class SegmentTreeMaxL:
    def __init__(self, size):
        self.n = 1
        while self.n < size:
            self.n <<= 1
        self.size = self.n
        self.tree = [-float('inf')] * (2 * self.n)

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = max(self.tree[pos], value)
        while pos > 1:
            pos >>= 1
            self.tree[pos] = max(self.tree[2*pos], self.tree[2*pos+1])

    def query(self, l, r):
        res = -float('inf')
        l += self.n
        r += self.n
        while l <= r:
            if l % 2 == 1:
                res = max(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = max(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

class SegmentTreeMinR:
    def __init__(self, size):
        self.n = 1
        while self.n < size:
            self.n <<= 1
        self.size = self.n
        self.tree = [float('inf')] * (2 * self.n)

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = min(self.tree[pos], value)
        while pos > 1:
            pos >>= 1
            self.tree[pos] = min(self.tree[2*pos], self.tree[2*pos+1])

    def query(self, l, r):
        res = float('inf')
        l += self.n
        r += self.n
        while l <= r:
            if l % 2 == 1:
                res = min(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = min(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        users = []
        for _ in range(n):
            l = int(data[idx])
            r = int(data[idx+1])
            idx += 2
            users.append((l, r))
        # Sort by l, then by r
        users.sort(key=lambda x: (x[0], x[1]))
        # Collect all r values
        all_r = []
        for l, r in users:
            all_r.append(r)
        all_r = sorted(list(set(all_r)))
        # Build segment trees
        max_l_tree = SegmentTreeMaxL(len(all_r))
        min_r_tree = SegmentTreeMinR(len(all_r))
        answers = []
        for l, r in users:
            # Find compressed index of r
            idx_r = bisect.bisect_left(all_r, r)
            if idx_r < len(all_r) and all_r[idx_r] == r:
                max_l_tree.update(idx_r, l)
                min_r_tree.update(idx_r, r)
            else:
                pass
            # Query max_l_tree
            max_l = max_l_tree.query(idx_r, len(all_r) - 1)
            # Query min_r_tree
            min_r = min_r_tree.query(idx_r, len(all_r) - 1)
            if max_l == -float('inf') or min_r == float('inf'):
                answers.append(0)
            else:
                if max_l > min_r:
                    answers.append(0)
                else:
                    total = min_r - max_l + 1
                    overlap = max(0, min(min_r, r) - max(max_l, l) + 1)
                    answers.append(total - overlap)
        results.append(' '.join(map(str, answers)))
    print('\n'.join(results))

if __name__ == '__main__':
    main()