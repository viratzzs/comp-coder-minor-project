import heapq

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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        unique_elements = sorted(set(a))
        available = set(unique_elements)
        min_heap = unique_elements.copy()
        heapq.heapify(min_heap)
        max_heap = []
        for num in unique_elements:
            heapq.heappush(max_heap, -num)
        
        result = []
        for i in range(n):
            if i % 2 == 0:
                while min_heap and min_heap[0] not in available:
                    heapq.heappop(min_heap)
                if not min_heap:
                    break
                selected = heapq.heappop(min_heap)
                result.append(selected)
                available.remove(selected)
            else:
                while max_heap and -max_heap[0] not in available:
                    heapq.heappop(max_heap)
                if not max_heap:
                    break
                selected = -heapq.heappop(max_heap)
                result.append(selected)
                available.remove(selected)
        
        results.append(len(result))
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()