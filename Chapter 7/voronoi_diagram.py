import pylab as pl
from matplotlib import collections as mc

point = [0.2, 0.8]

triangle = [[0.2, 0.8], [0.5, 0.2], [0.8, 0.7]]


def points_to_triangle(point1, point2, point3):

    triangle = [list(point1), list(point2), list(point3)]

    return triangle


def gen_lines(list_points, itinerary):

    lines = []

    for j in range(len(itinerary) - 1):

        lines.append([list_points[itinerary[j]], list_points[itinerary[j + 1]]])

    return lines


def plot_triangle_simple(triangle, name):

    fig, ax = pl.subplots()

    xs = [triangle[0][0], triangle[1][0], triangle[2][0]]
    ys = [triangle[0][1], triangle[1][1], triangle[2][1]]

    itin = [0, 1, 2, 0]

    lines = gen_lines(triangle, itin)

    lc = mc.LineCollection(gen_lines(triangle, itin), linewidths=2)

    ax.add_collection(lc)

    ax.margins(0.1)
    pl.scatter(xs, ys)
    pl.savefig(str(name), + '.png')
    pl.close()


plot_triangle_simple(points_to_triangle((0.2, 0.8), (0.5, 0.2), (0.8, 0.7)), 'tri')
