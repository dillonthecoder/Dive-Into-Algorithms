import math


def square_root(x, y, error_tolerance):

    our_error = error_tolerance * 2

    while our_error > error_tolerance:

        z = x / y
        y = (y + z) / 2

        our_error = y ** 2 - x

    return y


print(square_root(5, 1, 0.000000000000001))
print(math.sqrt(5))
