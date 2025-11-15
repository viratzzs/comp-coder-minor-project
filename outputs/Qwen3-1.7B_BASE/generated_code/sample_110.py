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
        idx += 1
        s = data[idx]
        idx += 1
        if n % 2 == 1:
            # Need to delete one character
            # Check if after deleting one character, the string is alternating
            # Try deleting at position (n+1)//2
            new_s = s[:((n+1)//2)] + s[(((n+1)//2)+1):]
            even_replacements = 0
            for i in range(2, n, 2):
                if new_s[i-1] != new_s[0]:
                    even_replacements += 1
            odd_replacements = 0
            for i in range(1, n, 2):
                if new_s[i-1] != new_s[0]:
                    odd_replacements += 1
            total = even_replacements + odd_replacements
            results.append(str(1 + total))
        else:
            # Check if the string is alternating
            even_replacements = 0
            for i in range(2, n+1, 2):
                if s[i-1] != s[1]:
                    even_replacements += 1
            odd_replacements = 0
            for i in range(1, n+1, 2):
                if s[i-1] != s[0]:
                    odd_replacements += 1
            total = even_replacements + odd_replacements
            results.append(str(total))
    print('\n'.join(results))

if __name__ == "__main__":
    main()