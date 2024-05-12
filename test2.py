import os
import time
import math
import random

BOARD_LEN = 20
board = [["." for _ in range(BOARD_LEN)] for _ in range(BOARD_LEN)] # create board


def get_sprites():
    p_loc = (random.randint(0, BOARD_LEN - 1), random.randint(0, BOARD_LEN - 1)) # player location
    o1_loc = (random.randint(0, BOARD_LEN - 1), random.randint(0, BOARD_LEN - 1)) # first o location
    o2_loc = (random.randint(0, BOARD_LEN - 1), random.randint(0, BOARD_LEN - 1)) # second o location

    board[p_loc[0]][p_loc[1]] = "x" # print player to board
    board[o1_loc[0]][o1_loc[1]] = "o" # print o1 to board
    board[o2_loc[0]][o2_loc[1]] = "o" # print o2 to board

    o_locs = [o1_loc, o2_loc] # location of o1 & o2
    return p_loc, o_locs


def print_b():
    os.system('cls' if os.name == 'nt' else 'clear') # clear board
    for j in range(len(board)): # print loop
        for i in board[j]:
            print(i, end=" ")
        print()


def move_p(p_loc, o_loc):
    y = p_loc[0]
    x = p_loc[1]
    wait = 0.2

    while y != o_loc[0] or x != o_loc[1]: 
        if y < o_loc[0]:
            board[y][x] = "."
            y += 1
            board[y][x] = "x"
            print_b()
            time.sleep(wait)
        if y > o_loc[0]:
            board[y][x] = "."
            y -= 1
            board[y][x] = "x"
            print_b()
            time.sleep(wait)
        if x < o_loc[1]:
            board[y][x] = "."
            x += 1
            board[y][x] = "x"
            print_b()
            time.sleep(wait)
        if x > o_loc[1]:
            board[y][x] = "."
            x -= 1
            board[y][x] = "x"
            print_b()
            time.sleep(wait)

def main():
    p_loc, o_locs = get_sprites() # get location of player location on o loactions
    print_b()

    for o in o_locs:
        move_p(p_loc, o)

main()