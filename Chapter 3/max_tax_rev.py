import math
import matplotlib.pyplot as plt


def revenue(tax):

    return 100 * (math.log(tax + 1) - (tax - 0.2)**2 + 0.04)


def revenue_derivative(tax):

    return 100 * (1 / (tax + 1) - 2 * (tax - 0.2))


step_size = 0.001
threshold = 0.0001
max_iterations = 100000
current_rate = 0.7
current_rate = current_rate + step_size * revenue_derivative(current_rate)

keep_going = True
iterations = 0

while keep_going:

    rate_change = step_size * revenue_derivative(current_rate)
    current_rate = current_rate + rate_change

    if abs(rate_change) < threshold:
        keep_going = False

    if iterations >= max_iterations:
        keep_going = False

    iterations = iterations + 1

xs = [x/1000 for x in range(1001)]
ys = [revenue(x) for x in xs]

plt.plot(xs, ys)
plt.plot(current_rate, revenue(current_rate), 'ro')
plt.title('Tax Rates and Revenue')
plt.xlabel('Tax Rate')
plt.ylabel('Revenue')
plt.show()
