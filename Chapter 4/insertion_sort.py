# import random
# import matplotlib.pyplot as plt


def insert_cabinet(cabinet, to_insert):

    check_location = len(cabinet) - 1

    insert_location = 0

    global step_counter

    while check_location >= 0:

        step_counter += 1

        if to_insert > cabinet[check_location]:

            insert_location = check_location + 1

            check_location = - 1

        check_location = check_location - 1

    step_counter += 1

    cabinet.insert(insert_location, to_insert)

    return cabinet


def insertion_sort(cabinet):

    new_cabinet = []

    global step_counter

    while len(cabinet) > 0:

        step_counter += 1

        to_insert = cabinet.pop(0)

        new_cabinet = insert_cabinet(new_cabinet, to_insert)

    return new_cabinet


size_of_cab = 10
cabinet = [8, 4, 6, 1, 2, 5, 3, 7]

step_counter = 0

sorted_cabinet = insertion_sort(cabinet)

print(step_counter)

# Something is wrong here. Need to come back and fix some bugs to finish the code
