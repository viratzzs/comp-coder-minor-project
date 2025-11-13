import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        current = a.copy()
        moves = []
        for i in range(n):
            if i == 0:
                continue
            if current[i] < current[i-1]:
                needed = current[i-1] - current[i]
                for _ in range(needed):
                    moves.append((i, i+1))
                    current[i-1] -= 1
                    current[i] += 1
        print(len(moves))
        for move in moves:
            print(move[0], move[1])

if __name__ == "__main__":
    main()