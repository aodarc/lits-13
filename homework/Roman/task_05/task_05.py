def sort_odd(in_data):
    loc_in_data = in_data

    # Get only odd variables
    odd_vars = [x for x in loc_in_data if x % 2 != 0]

    odd_vars.sort()

    loc_in_data = list(map((lambda x: (x % 2 and odd_vars.pop(0) or x)), loc_in_data))

    # Other, possible, not bad implementation:
    # for j, elem in enumerate(loc_in_data):
    #     if int(elem) % 2 != 0:
    #         loc_in_data[j] = odd_vars.pop(0)

    return loc_in_data


