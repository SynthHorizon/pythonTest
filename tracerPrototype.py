import os
import time
import math
import random

BOARD_LEN = 20
board = [["." for _ in range(BOARD_LEN)] for _ in range(BOARD_LEN)]


y, x = random.randint(0, BOARD_LEN - 1), random.randint(0, BOARD_LEN - 1)
y1, x1 = random.randint(0, BOARD_LEN - 1), random.randint(0, BOARD_LEN - 1)
y2, x2 = random.randint(0,  - 1), random.randint(0, BOARD_LEN - 1)


p = board[y][x] = "x"
o1 = board[y1][x1] = "o"
o2 = board[y2][x2] = "o"


def print_b():
    os.system('cls' if os.name == 'nt' else 'clear') # clear board
    for j in range(len(board)):
        for i in board[j]:
            print(i, end=" ")
        print()


def get_dist(o_y, o_x):
    dist_y = (y - o_y)
    dist_x = (x - o_x)
    distance = math.sqrt(dist_x**2 + dist_y**2)
    return distance


wait = 0.2

while y != y1 or x != x1:
    if y < y1:
        board[y][x] = "."
        y += 1
        board[y][x] = "x"
        print_b()
        time.sleep(wait)
    elif y > y1:
        board[y][x] = "."
        y -= 1
        board[y][x] = "x"
        print_b()
        time.sleep(wait)
    elif x < x1:
        board[y][x] = "."
        x += 1
        board[y][x] = "x"
        print_b()
        time.sleep(wait)
    elif x > x1:
        board[y][x] = "."
        x -= 1
        board[y][x] = "x"
        print_b()
        time.sleep(wait)


while y != y2 or x != x2:
    if y < y2:
        board[y][x] = "."
        y += 1
        board[y][x] = "x"
        print_b()
        time.sleep(wait)
    elif y > y2:
        board[y][x] = "."
        y -= 1
        board[y][x] = "x"
        print_b()
        time.sleep(wait)
    elif x < x2:
        board[y][x] = "."
        x += 1
        board[y][x] = "x"
        print_b()
        time.sleep(wait)
    elif x > x2:
        board[y][x] = "."
        x -= 1
        board[y][x] = "x"
        print_b()
        time.sleep(wait)