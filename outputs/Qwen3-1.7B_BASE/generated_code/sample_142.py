import sys

MOD = 10**9 + 7

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        if k == 1:
            results.append(n - 1)
        else:
            res = 1
            for i in range(1, k):
                res = res * (n - i) % MOD
            results.append(res)
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()