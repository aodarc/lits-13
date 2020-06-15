import string


def convert_n_to_m(x, n: int, m: int):
    """Calculates representation of x in base m.

    in case x can't be represented as number or row,
    or x can't be represented in base n returns False

    Arguments:
    x -- an input, integer or string with base n
    n -- base for an input x, where 1 <= n <= 36
    m -- base for returned value, where 1 <= m <= 36

    """

    if isinstance(x, float):
        return 'False'

    if isinstance(x, list):
        in_string = str(x)[1:-1]
    else:
        in_string = str(x)

    dict_key = list(string.digits)
    dict_key.extend(list(string.ascii_uppercase))
    dict_val = list(range(0, 37))

    forward_dict = {f: i for i, f in enumerate(dict_key)}

    reverse_dict = {i: f for i, f in enumerate(dict_key)}

    # Transfer input value into BASE10
    dec_val = 0
    cnt = 0
    for i in in_string[::-1]:
        if forward_dict.get(i) >= n:
            return 'False'
        dec_val += forward_dict.get(i) * (n ** cnt)
        cnt += 1

    # Calculate maximum required power, cnt will represent max required power
    cnt = 1
    stage = 1
    while stage < dec_val:
        cnt += 1
        stage = m ** cnt
    cnt -= 1

    # Calculate output value with given BASE m
    out_str = ''
    residual = dec_val
    for i in range(cnt, -1, -1):
        mult = 1
        while residual >= mult * (m ** i):
            mult += 1
        residual -= (mult - 1) * (m ** i)
        out_str += reverse_dict.get(mult-1)

    return out_str

