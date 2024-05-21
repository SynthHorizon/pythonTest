import os
import time
import math
import random

BOARD_LEN = 20
board = [["." for _ in range(BOARD_LEN)] for _ in range(BOARD_LEN)] # create board
p_loc = [random.randint(0, BOARD_LEN - 1), random.randint(0, BOARD_LEN - 1)] # player location
player = "x"
board[p_loc[0]][p_loc[1]] = player # print player to board

class Coin():
    """Coins are the objective of the program. \n
    Automatically creates coin location and adds it to board"""

    def __init__(self):
        self.location = [random.randint(0, BOARD_LEN - 1), random.randint(0, BOARD_LEN - 1)]
        board[self.location[0]][self.location[1]] = "o"


def print_board():
    os.system('cls' if os.name == 'nt' else 'clear') # clear board
    for j in range(len(board)): # print loop
        for i in board[j]:
            print(i, end=" ")
        print()


def find_dist(point):
    x_dist = p_loc[0] - point[0]
    y_dist = p_loc[1] - point[1]
    hyp = math.sqrt((x_dist**2 + y_dist**2))

    return hyp


def bubble_sort(list):
    for _ in range(len(list)):
        for num in range(len(list) - 1):
            if find_dist(list[num]) < find_dist(list[num + 1]):
                list[num], list[num + 1] = list[num + 1], list[num]
    return list


def move_p(coins):

    wait = 0.1
    num_of_coins = len(coins)
    i = 0

    coins = bubble_sort(coins)

    while i < num_of_coins:
        while p_loc[0] != coins[num_of_coins - 1][0] or p_loc[1] != coins[num_of_coins - 1][1]:

            if p_loc[0] < coins[num_of_coins - 1][0]:
                board[p_loc[0]][p_loc[1]] = "."
                p_loc[0] += 1
                board[p_loc[0]][p_loc[1]] = player
                print_board()
                time.sleep(wait)

            if p_loc[0] > coins[num_of_coins - 1][0]:
                board[p_loc[0]][p_loc[1]] = "."
                p_loc[0] -= 1
                board[p_loc[0]][p_loc[1]] = player
                print_board()
                time.sleep(wait)

            if p_loc[1] < coins[num_of_coins - 1][1]:
                board[p_loc[0]][p_loc[1]] = "."
                p_loc[1] += 1
                board[p_loc[0]][p_loc[1]] = player
                print_board()
                time.sleep(wait)

            if p_loc[1] > coins[num_of_coins - 1][1]:
                board[p_loc[0]][p_loc[1]] = "."
                p_loc[1] -= 1
                board[p_loc[0]][p_loc[1]] = player
                print_board()
                time.sleep(wait)

        coins.remove(coins[num_of_coins - 1])
        coins = bubble_sort(coins)
        num_of_coins = len(coins)

    return p_loc


def main():
    o1 = Coin()
    o2 = Coin()
    o3 = Coin()
    o4 = Coin()

    coins = [o1.location, o2.location, o3.location, o4.location]

    move_p(coins)
main()