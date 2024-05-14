import math

points = [(1, 2), (2, 3), (4, 3)]

player = [5, 4]

def find_dist(point):
    x_dist = player[0] - point[0]
    y_dist = player[1] - point[1]

    hyp = math.sqrt((x_dist**2 + y_dist**2))

    return hyp




print(find_dist(points[0]))