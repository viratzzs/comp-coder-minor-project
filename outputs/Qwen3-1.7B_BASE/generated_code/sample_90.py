import sys
import heapq
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        n, m = int(data[idx]), int(data[idx+1])
        idx += 2
        participants = []
        for _ in range(n):
            a = int(data[idx])
            b = int(data[idx+1])
            s = int(data[idx+2])
            participants.append((a, b, s))
            idx += 3
        cities = []
        for _ in range(m):
            k = int(data[idx])
            q = list(map(int, data[idx+1:idx+1+k]))
            cities.append((k, q))
            idx += 1 + k
        # Sort cities by the number of participants in descending order
        cities.sort(key=lambda x: -x[0])
        # Assign topics and difficulties
        topics = []
        difficulties = []
        for city in cities:
            k, q = city
            # Find the minimum a and b for participants with s = t
            min_a = float('inf')
            min_b = float('inf')
            for idx_q in q:
                a, b, s = participants[idx_q-1]
                if s == t:
                    if a < min_a:
                        min_a = a
                    if b < min_b:
                        min_b = b
            t = len(topics) + 1
            difficulty = min(min_a, min_b)
            topics.append(t)
            difficulties.append(difficulty)
        # Output
        p = sum(k for k, q in cities)
        results.append(f"{p}\n")
        for i in range(p):
            results[-1] += f"{difficulties[i]} {topics[i]}\n"
    print("\n".join(results))

if __name__ == "__main__":
    main()