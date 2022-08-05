import math


def continued_fraction_decimal(x, error_tolerance, length_tolerance):

    output = []

    first_term = int(x)
    leftover = x - int(x)

    output.append(first_term)

    error = leftover

    while error > error_tolerance and len(output) < length_tolerance:

        next_term = math.floor(1 / leftover)

        leftover = 1 / leftover - next_term

        output.append(next_term)

        error = abs(get_number(output) - x)

    return output


def get_number(continued_fraction):

    index = -1
    number = continued_fraction[index]

    while abs(index) < len(continued_fraction):

        next = continued_fraction[index - 1]
        number = 1 / number + next
        index -= 1

    return number


print(continued_fraction_decimal(1.4142135623730951, 0.00001, 100))
