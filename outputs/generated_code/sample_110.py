import sys
from collections import Counter

def main():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        s = input[idx]
        idx += 1
        if n % 2 == 0:
            even_positions = [s[i] for i in range(0, n, 2)]
            odd_positions = [s[i] for i in range(1, n, 2)]
            is_alter = True
            if len(even_positions) > 0:
                if not all(c == even_positions[0] for c in even_positions):
                    is_alter = False
            if len(odd_positions) > 0:
                if not all(c == odd_positions[0] for c in odd_positions):
                    is_alter = False
            if is_alter:
                results.append(0)
            else:
                even_freq = Counter(even_positions)
                max_even = max(even_freq.values())
                steps_even = len(even_positions) - max_even
                odd_freq = Counter(odd_positions)
                max_odd = max(odd_freq.values())
                steps_odd = len(odd_positions) - max_odd
                results.append(steps_even + steps_odd)
        else:
            min_ops = float('inf')
            for i in range(n):
                new_s = s[:i] + s[i+1:]
                m = n - 1
                if m % 2 != 0:
                    continue
                even_positions_new = [new_s[j] for j in range(0, m, 2)]
                odd_positions_new = [new_s[j] for j in range(1, m, 2)]
                even_freq_new = Counter(even_positions_new)
                max_even_new = max(even_freq_new.values())
                steps_even_new = len(even_positions_new) - max_even_new
                odd_freq_new = Counter(odd_positions_new)
                max_odd_new = max(odd_freq_new.values())
                steps_odd_new = len(odd_positions_new) - max_odd_new
                total_steps = steps_even_new + steps_odd_new
                if total_steps < min_ops:
                    min_ops = total_steps
            results.append(1 + min_ops)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()