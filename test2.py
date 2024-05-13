import os
import time
import math
import random

BOARD_LEN = 20
board = [["." for _ in range(BOARD_LEN)] for _ in range(BOARD_LEN)] # create board
p_loc = [random.randint(0, BOARD_LEN - 1), random.randint(0, BOARD_LEN - 1)] # player location
board[p_loc[0]][p_loc[1]] = "x" # print player to board


class Coin():
    """Coins are the objective of the program. \n
    Automatically creates coin location and adds it to board"""

    def __init__(self):
        self.location = (random.randint(0, BOARD_LEN - 1), random.randint(0, BOARD_LEN - 1))
        board[self.location[0]][self.location[1]] = "o"        


def print_board():
    os.system('cls' if os.name == 'nt' else 'clear') # clear board
    for j in range(len(board)): # print loop
        for i in board[j]:
            print(i, end=" ")
        print()


def move_p(o_loc):
    wait = 0.2

    while p_loc[0] != o_loc[0] or p_loc[1] != o_loc[1]:
        if p_loc[0] < o_loc[0]:
            board[p_loc[0]][p_loc[1]] = "."
            p_loc[0] += 1
            board[p_loc[0]][p_loc[1]] = "x"
            print_board()
            time.sleep(wait)
        if p_loc[0] > o_loc[0]:
            board[p_loc[0]][p_loc[1]] = "."
            p_loc[0] -= 1
            board[p_loc[0]][p_loc[1]] = "x"
            print_board()
            time.sleep(wait)
        if p_loc[1] < o_loc[1]:
            board[p_loc[0]][p_loc[1]] = "."
            p_loc[1] += 1
            board[p_loc[0]][p_loc[1]] = "x"
            print_board()
            time.sleep(wait)
        if p_loc[1] > o_loc[1]:
            board[p_loc[0]][p_loc[1]] = "."
            p_loc[1] -= 1
            board[p_loc[0]][p_loc[1]] = "x"
            print_board()
            time.sleep(wait)


def main():
    o1 = Coin()
    o2 = Coin()
    o3 = Coin()
    o4 = Coin()

    coins = (o1, o2, o3, o4)

    for coin in coins:
        move_p(coin.location)

    print_board()

main()