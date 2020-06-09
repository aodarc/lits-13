def check_symmetry(in_data):
    # Format string at begging
    # Make all lower case and remove white spaces
    loc_str = str(in_data).lower().replace(' ', '')

    # Compare two cuts, second with reverse direction.
    # Since reverse direction starts from -1 need subtract 1 from final index
    str_length = len(loc_str)
    if loc_str[:] == loc_str[::-1]:
        print('YES')
    else:
        print('NO')
