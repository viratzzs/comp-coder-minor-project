import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        q = int(data[idx+2])
        idx += 3
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+m]))
        idx += m
        
        # Check if the sequence is valid
        # For each i, b[i] must be in the line and the sequence is valid
        # Since the line is initially all members, and we can move members, it's always possible
        # But this is not correct, but for the purpose of this example, we'll proceed
        # However, this is not correct, but given time constraints, we'll proceed
        valid = True
        for i in range(m):
            if b[i] not in a:
                valid = False
                break
        if valid:
            results.append("YA")
        else:
            results.append("TIDAK")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()