import sys

def is_subset(a, b):
    for i in range(len(a)):
        if a[i] < b[i]:
            return False
    return True

def is_superset(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx +=2
        A = []
        for i in range(n):
            row = int(data[idx])
            A.append(row)
            idx +=1
        B = []
        for i in range(n):
            row = int(data[idx])
            B.append(row)
            idx +=1
        # Row check
        valid = True
        for i in range(n):
            if not is_subset(A[i], B[i]):
                valid = False
                break
        if not valid:
            results.append("No")
            continue
        # Column check
        valid = True
        for j in range(m):
            if not is_superset(A, B[j]):
                valid = False
                break
        if valid:
            results.append("Yes")
        else:
            results.append("No")
    print('\n'.join(results))

if __name__ == "__main__":
    main()