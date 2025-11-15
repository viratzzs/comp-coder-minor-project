import sys

def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    m = int(input[1])
    r = list(map(int, input[2:2+n]))
    
    strength = 0
    intelligence = 0
    passes = 0
    
    for i in range(n):
        if r[i] == 0:
            # Spend on strength or intelligence; choose strength first
            strength += 1
        else:
            if r[i] < 0:
                # Strength check
                if strength < -r[i]:
                    strength += 1
                    passes += 1
                else:
                    passes += 1
            else:
                # Intelligence check
                if intelligence < r[i]:
                    intelligence += 1
                    passes += 1
                else:
                    passes += 1
    print(passes)

if __name__ == "__main__":
    main()