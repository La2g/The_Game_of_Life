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


render_board(random_state(5, 5))
