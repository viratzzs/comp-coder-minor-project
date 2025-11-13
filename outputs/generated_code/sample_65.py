t = int(input())
for _ in range(t):
    s = input().strip()
    a = s[0]
    op = s[1]
    b = s[2]
    a_int = int(a)
    b_int = int(b)
    if (a_int < b_int and op == '<') or (a_int == b_int and op == '=') or (a_int > b_int and op == '>'):
        print(s)
    else:
        possible_ops = []
        # Check op changes
        if a_int > b_int:
            possible_ops.append(a + '>' + b)
        if a_int == b_int:
            possible_ops.append(a + '=' + b)
        if a_int < b_int:
            possible_ops.append(a + '<' + b)
        # Check first digit change
        possible_ops.append('0' + op + b)
        # Check third digit change
        new_third = a_int + 1
        if new_third <= 9:
            possible_ops.append(a + op + str(new_third))
        # Choose the first possible option
        print(possible_ops[0])