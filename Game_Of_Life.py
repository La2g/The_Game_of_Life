import random
from pprint import pprint


def random_state(board_width, board_height):
    """This function creates a board of the size specified by board_with and board_height, in this board
    all cells state are randomized, meaning all values are 0 or 1 (dead or alive).
    """
    board = []

    for h in range(0, board_height):
        width_list = []
        for w in range(0, board_width):
            random_number = random.random()  # generates a random value for each row.
            if random_number >= 0.5:
                width_list.append(1)
            else:
                width_list.append(0)
        board.append(width_list)

    return board


def render_board(board_state):
    """This functions takes a board state and renders the board in the terminal.
    The board state is a list with each cell state (dead or alive)."""
    board_height = len(board_state)
    board_width = len(board_state[0])

    print('----------------')
    for h in range(board_height):
        print('# ', end=" ")
        for w in range(board_width):
            print(board_state[h][w], end=" ")  # 'end' Changes print behaviour so no new line after each print.
        print(' #', end=" ")
        print()  # Enters new line.
    print('----------------')


def next_board_state(board_state):
    """This function take a board state an calculate the next state of the board based on the following four rules:
    1 - Any live cell with 0 or 1 live neighbors becomes dead
    2 - Any live cell with 2 or 3 live neighbors stays alive
    3 - Any live cell with more than 3 live neighbors becomes dead
    4 - Any dead cell with exactly 3 live neighbors becomes alive"""
    board_height = len(board_state)
    board_width = len(board_state[0])

    def check_neighbor_state:
        for h in range(board_height):
            for w in range(board_width):
                if board_state[h][w] == 0:
                    if board_state[h][w + 1] == 1:
                        if board_state[h + 1][w] == 1:
                            if board_state[h + 1][w + 1] == 1:
                                board_state[h][w] = 1
                if board_state[h][w] == 1:
                    if board_state[h][w + 1] == 1:
                        if board_state[h + 1][w] == 1:
                            board_state[h][w] = 1





















render_board(random_state(5, 5))
