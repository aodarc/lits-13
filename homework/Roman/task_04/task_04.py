def count_holes(in_data):
    if isinstance(in_data, float):
        return 'ERROR'

    if not isinstance(in_data, int) and not str(in_data).isdigit():
        return 'ERROR'

    # Use dictionary to avoid if else
    d = {
        '9': 1,
        '8': 2,
        '7': 0,
        '6': 1,
        '5': 0,
        '4': 1,
        '3': 0,
        '2': 0,
        '1': 0,
        '0': 1,
        '-': 0
    }

    cnt = 0
    for number in str(in_data):
        cnt += d.get(number)

    return cnt

