import math
import matplotlib.pyplot as plt


def income(edu_years):

    return math.sin((edu_years - 10.6) * (2 * math.pi / 4)) + (edu_years - 11) / 2


def income_derivative(edu_years):

    return math.cos((edu_years - 10.6) * (2 * math.pi / 4)) + 1/2


threshold = 0.0001
max_iterations = 100000

current_edu = 12.5
step_size = 0.001

keep_going = True
iterations = 0

while keep_going:

    edu_change = step_size * income_derivative(current_edu)

    current_edu = current_edu + edu_change

    if abs(edu_change) < threshold:
        keep_going = False

    if iterations >= max_iterations:
        keep_going = False

    iterations = iterations + 1

xs = [11 + x / 100 for x in list(range(901))]
ys = [income(x) for x in xs]

plt.plot(xs, ys)
plt.plot(current_edu, income(current_edu), 'ro')
plt.title('Education and Income')
plt.xlabel('Years of Education')
plt.ylabel('Lifetime Income')
plt.show()
