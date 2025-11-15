import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    skill = []
    for _ in range(n):
        skill.append(input[idx])
        idx += 1
    
    for x in range(1, m + 1):
        current = []
        for i in range(n):
            if skill[i][x-1] == '1':
                current.append(i)
        found = False
        for s in range(x, x + m):
            if s > m:
                s -= m
            all_not = True
            for p in current:
                if skill[p][s-1] == '1':
                    all_not = False
                    break
            if all_not:
                continue
            else:
                new_current = []
                for p in current:
                    if skill[p][s-1] == '1':
                        new_current.append(p)
                current = new_current
                if len(current) == 1:
                    print(current[0] + 1)
                    found = True
                    break
        if not found:
            print(current[0] + 1)

if __name__ == "__main__":
    main()