import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    n = int(data[idx])
    idx += 1

    a = list(map(int, data[idx:idx + n]))
    idx += n
    b = list(map(int, data[idx:idx + n]))
    idx += n

    prefix_a = [0] * (n + 1)
    prefix_b = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]

    g = [0] * (n + 1)
    for i in range(1, n + 1):
        g[i] = prefix_a[i] + b[i - 1]

    max_prefix = [0] * (n + 2)
    max_suffix = [0] * (n + 2)

    max_g_r_plus_b_r = -float('inf')
    min_g_l_minus_b_l = float('inf')
    for i in range(1, n + 1):
        if i == 1:
            current_max_g_r_plus_b_r = g[i] + b[i - 1]
            current_min_g_l_minus_b_l = g[0] - b[0]
        else:
            current_max_g_r_plus_b_r = max(max_g_r_plus_b_r, g[i] + b[i - 1])
            current_min_g_l_minus_b_l = min(min_g_l_minus_b_l, g[i - 1] - b[i - 1])
        max_prefix[i] = current_max_g_r_plus_b_r - current_min_g_l_minus_b_l
        max_g_r_plus_b_r = current_max_g_r_plus_b_r
        min_g_l_minus_b_l = current_min_g_l_minus_b_l

    max_g_r_plus_b_r = -float('inf')
    min_g_l_minus_b_l = float('inf')
    for i in range(n, 0, -1):
        if i == n:
            current_max_g_r_plus_b_r = g[i] + b[i - 1]
            current_min_g_l_minus_b_l = g[i - 1] - b[i - 1]
        else:
            current_max_g_r_plus_b_r = max(max_g_r_plus_b_r, g[i] + b[i - 1])
            current_min_g_l_minus_b_l = min(min_g_l_minus_b_l, g[i + 1] - b[i + 1])
        max_suffix[i] = current_max_g_r_plus_b_r - current_min_g_l_minus_b_l
        max_g_r_plus_b_r = current_max_g_r_plus_b_r
        min_g_l_minus_b_l = current_min_g_l_minus_b_l

    max_total = -float('inf')
    current_max_P = -float('inf')
    for j in range(1, n + 1):
        if j == 1:
            current_max_P = max_prefix[1]
        else:
            current_max_P = max(current_max_P, max_prefix[j - 1])
        current_candidate = current_max_P + max_suffix[j]
        if current_candidate > max_total:
            max_total = current_candidate

    print(max_total)

if __name__ == "__main__":
    main()