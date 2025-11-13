import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        if len(s) == 1:
            print(-1)
        else:
            found = False
            for i in range(len(s) - 1):
                if s[i] == s[i+1]:
                    print(s[i:i+2])
                    found = True
                    break
            if not found:
                print(s[0:2])

if __name__ == "__main__":
    main()