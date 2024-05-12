import random
import os

board_len = 10
board = [["." for _ in range(board_len)] for _ in range(board_len)]
p_x, p_y = 5, 5

def coords_gen(): # generate random coords for o spots
    x_coords, y_coords = [random.randint(0, board_len - 1) for _ in range(5)], [random.randint(0, board_len - 1) for _ in range(5)]
    for q in range(5):
        board[y_coords[q]][x_coords[q]] = "o"
    return x_coords, y_coords


def print_board(board): # function to print the board
    os.system('cls' if os.name == 'nt' else 'clear') # clear board
    for j in range(len(board)):
        for i in board[j]:
            print(i, end=" ")
        print()

def run_game(y_coords, x_coords, p_y, p_x): # game loop
    score = 0
    while True:
        command = input().lower()
        if command == "down" and p_y < (board_len - 1):
            board[p_y][p_x] = "."
            p_y += 1
        elif command == "up" and p_y > 0:
            board[p_y][p_x] = "."
            p_y -= 1
        elif command == "right" and p_x < (board_len - 1):
            board[p_y][p_x] = "."
            p_x += 1
        elif command == "left" and p_x > 0:
            board[p_y][p_x] = "."
            p_x -= 1
        elif command == "exit":
            print("exit successful")
            break

        for w in range(len(x_coords)):
            if p_y == y_coords[w] and p_x == x_coords[w]:
                board[y_coords[w]][x_coords[w]] = "."
                score += 1

        # after player moves
        board[p_y][p_x] = "x"
        print_board(board)
        print("score:", score)
        if score == 5:
            print("you win!")
            break

def main():
    # game variables
    
    board[p_y][p_x] = "x"

    x_coords, y_coords = coords_gen() # generate o spot coords
    print_board(board)
    run_game(y_coords, x_coords, p_y, p_x)
main()