import sys

def main():
    n = int(sys.stdin.readline())
    total_people = 0
    for _ in range(n):
        parts = sys.stdin.readline().split()
        if parts[0] == 'P':
            p = int(parts[1])
            total_people += p
        else:
            b = int(parts[1])
            people_on_bus = min(total_people, b)
            remaining = b - people_on_bus
            if remaining >= 1:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()