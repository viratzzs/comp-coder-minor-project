import sys

def main():
    n = int(sys.stdin.readline())
    people_waiting = 0
    seats_available = 0
    for _ in range(n):
        parts = sys.stdin.readline().split()
        if parts[0] == 'P':
            p = int(parts[1])
            people_waiting += p
        else:
            b = int(parts[1])
            k = min(people_waiting, b)
            seats_available = b - k
            if seats_available > 0:
                print("YES")
            else:
                print("NO")
            people_waiting = people_waiting - k

if __name__ == "__main__":
    main()