import math


def merging(left, right):

    new_cab = []

    while min(len(left), len(right)) > 0:

        if left[0] > right[0]:

            to_insert = right.pop(0)

            new_cab.append(to_insert)

        elif left[0] <= right[0]:

            to_insert = left.pop(0)

            new_cab.append(to_insert)

    if len(left) > 0:

        for i in left:

            new_cab.append(i)

    if len(right) > 0:

        for i in right:

            new_cab.append(i)

    return new_cab


def mergesort(cabinet):

    new_cab = []

    if len(cabinet) == 1:

       new_cab = cabinet

    else:

       left = mergesort(cabinet[:math.floor(len(cabinet)/2)])

       right = mergesort(cabinet[math.floor(len(cabinet)/2):])

       new_cab = merging(left, right)

    return new_cab


cabinet = [4, 1, 3, 2, 6, 3, 18, 2, 9, 7, 3, 1, 2.5, -9]

new_cabinet = mergesort(cabinet)

print(new_cabinet)
