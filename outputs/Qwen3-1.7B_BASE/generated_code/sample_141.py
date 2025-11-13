import sys
from collections import deque

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        s = sys.stdin.readline().strip()
        t = sys.stdin.readline().strip()
        visited = set()
        queue = deque()
        queue.append(( "", "" , 0 ))
        visited.add( ( "", "" ) )
        found = False
        while queue:
            a, b, steps = queue.popleft()
            if a == s and b == t:
                print(steps)
                found = True
                break
            for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                new_a1 = a + c
                new_b1 = b
                if (new_a1, new_b1) not in visited:
                    visited.add( (new_a1, new_b1) )
                    queue.append( (new_a1, new_b1, steps + 1) )
                new_a2 = a
                new_b2 = b + c
                if (new_a2, new_b2) not in visited:
                    visited.add( (new_a2, new_b2) )
                    queue.append( (new_a2, new_b2, steps + 1) )
                new_a3 = a
                new_b3 = a
                if (new_a3, new_b3) not in visited:
                    visited.add( (new_a3, new_b3) )
                    queue.append( (new_a3, new_b3, steps + 1) )
        if not found:
            print(-1)

if __name__ == "__main__":
    main()