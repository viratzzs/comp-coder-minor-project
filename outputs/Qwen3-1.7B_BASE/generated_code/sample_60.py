import sys

def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    participants = []
    idx = 2
    for _ in range(n):
        s = data[idx]
        idx += 1
        skills = set()
        for j in range(m):
            if s[j] == '1':
                skills.add(j)
        participants.append(skills)
    
    for x in range(1, m + 1):
        current_set = set(range(n))
        for k in range(m):
            sport = (x + k) % m
            new_set = set()
            for i in current_set:
                if sport in participants[i]:
                    new_set.add(i)
            current_set = new_set
        if len(current_set) == 1:
            print(current_set.pop())
        else:
            print(0)

if __name__ == "__main__":
    main()