import math
import random
from test2 import Coin


o1 = Coin()
o2 = Coin()
o3 = Coin()
o4 = Coin()

player = [0, 0]

points = [o1.location, o2.location, o3.location, o4.location]

listLength = len(points)
listRange = 200


print(points)


def find_dist(point):
    x_dist = player[0] - point[0]
    y_dist = player[1] - point[1]
    hyp = math.sqrt((x_dist**2 + y_dist**2))

    return hyp

def bubble_sort(list):
    for _ in range(len(list)):
        for num in range(len(list) - 1):
            if find_dist(list[num]) > find_dist(list[num + 1]):
                list[num], list[num + 1] = list[num + 1], list[num]
    return list

# def selection_sort(list):
#     for index in range(listLength):
#         for num in range(listLength - 1):
#             if find_dist(list[num]) < find_dist(list[num + 1]):
#                 list[index], list[num] = list[num], list[index]
#     return list
# print(selection_sort(points))


print(bubble_sort(points))