import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 2
    records = list(map(int, data[idx:idx+n]))
    idx += n

    strength = 0
    intelligence = 0
    passes = 0
    current_index = 0

    while current_index < n:
        if records[current_index] == 0:
            count_s = 0
            count_i = 0
            for i in range(current_index + 1, n):
                if records[i] < 0:
                    count_s += 1
                elif records[i] > 0:
                    count_i += 1
            if count_s > count_i:
                strength += 1
            elif count_i > count_s:
                intelligence += 1
            else:
                if strength >= intelligence:
                    strength += 1
                else:
                    intelligence += 1
            current_index += 1
        elif records[current_index] < 0:
            required = -records[current_index]
            if strength >= required:
                strength += required
                passes += 1
            current_index += 1
        else:
            required = records[current_index]
            if intelligence >= required:
                intelligence += required
                passes += 1
            current_index += 1

    print(passes)

if __name__ == "__main__":
    main()