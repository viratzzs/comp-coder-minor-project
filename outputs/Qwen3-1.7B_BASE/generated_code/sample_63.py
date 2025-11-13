import sys

def main():
    n = int(sys.stdin.readline())
    total = (18 + 21 + 25) * n
    max_contribution = 60
    min_planks = total // max_contribution
    if n == 1:
        min_planks += 1
    print(min_planks)

if __name__ == "__main__":
    main()