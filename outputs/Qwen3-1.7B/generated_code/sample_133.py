import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        current_gold = 0
        count = 0
        for num in a:
            if num >= k:
                current_gold += num
            else:
                if num == 0:
                    if current_gold > 0:
                        current_gold -= 1
                        count += 1
        print(count)

if __name__ == "__main__":
    main()