import math

sorted_cab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(sorted_cab, looking_for):

    guess = math.floor(len(sorted_cab) / 2)

    upper_bound = len(sorted_cab)

    lower_bound = 0

    if sorted_cab[guess] > looking_for:

        upper_bound = guess

        guess = math.floor((guess + lower_bound) / 2)

    if sorted_cab[guess] < looking_for:

        lower_bound = guess

        guess = math.floor((guess + upper_bound) / 2)

    return guess


print(binary_search(sorted_cab, 8))
