import math
import numpy as np
import matplotlib.pylab as pl
import matplotlib.collections as mc

random_seed = 1729

np.random.seed(random_seed)

N = 40

x = np.random.rand(N)
y = np.random.rand(N)

points = zip(x, y)
cities = list(points)

# j = 10
# point = [0.5, 0.5]
# distance = math.sqrt((point[0] - cities[j][0]) ** 2 + (point[1] - cities[j][1]) ** 2)

itinerary = list(range(0, N))


def gen_lines(cities, itinerary):

    lines = []

    for j in range(0, len(itinerary) - 1):

        lines.append([cities[itinerary[j]], cities[itinerary[j + 1]]])

    return lines


def how_far(lines):

    distance = 0

    for j in range(0, len(lines)):

        distance += math.sqrt(abs(lines[j][1][0] - lines[j][0][0]) ** 2 + abs(lines[j][1][1] - lines[j][0][1]) ** 2)

    return distance


def find_nearest(cities, idx, nnitinerary):

    point = cities[idx]
    min_distance = float('inf')
    min_idx = - 1

    for j in range(0, len(cities)):

        distance = math.sqrt((point[0] - cities[j][0]) ** 2 + (point[1] - cities[j][1]) ** 2)

        if distance < min_distance and distance > 0 and j not in nnitinerary:

            min_distance = distance

            min_idx = j

    return min_idx


def donn(cities, N):

    nnitinerary = [0]

    for j in range(0, N - 1):

        next = find_nearest(cities, nnitinerary[len(nnitinerary) - 1], nnitinerary)

        nnitinerary.append(next)

    return nnitinerary


def plot_itinerary(cities, itin, plot_title, the_name):

    lc = mc.LineCollection(gen_lines(cities, itin), linewidths=2)

    fig, ax = pl.subplots()

    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)

    pl.scatter(x, y)
    pl.title(plot_title)
    pl.xlabel('X Coordinate')
    pl.ylabel('Y Coordinate')
    pl.savefig(str(the_name) + '.png')
    pl.close()


total_distance = how_far(gen_lines(cities, itinerary))

plot_itinerary(cities, donn(cities, N), 'TSP - Nearest Neighbor', 'figure3')

print(how_far(gen_lines(cities, donn(cities, N))))
