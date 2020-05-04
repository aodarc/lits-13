import random


def get_random_24bit_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    out_str = '#' + "{:02x}".format(red) + "{:02x}".format(green) + "{:02x}".format(blue)
    return out_str


print(get_random_24bit_color())
