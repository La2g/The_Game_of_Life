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
    new_state = board_state
    board_height = len(new_state)
    board_width = len(new_state[0])

    for h in range(0, board_height):
        for w in range(0, board_width):
            neighbor_sum = 0
            current_cell_value = board_state[h][w]
            for x in range(-1, 2):
                for y in range(-1, 2):
                    # If x and y equals 0 it means it's checking the value of the current cell
                    # not that of a neighbor.
                    if x == 0 and y == 0:
                        pass
                    # If a list index is negative it check the cell at the other side of the board
                    # which doesn't count as a neighbor cell.
                    elif (h + x) < 0 or (w + y) < 0:
                        pass
                    else:
                        try:
                            neighbor_sum = neighbor_sum + board_state[h + x][w + y]
                        except IndexError:
                            pass
            # A cell state only matters for rule 2, so if cell is alive:
            if current_cell_value == 1:
                # If cell has 2 or 3 live neighbors, it stays alive. Rule 2.
                if neighbor_sum == 2 or neighbor_sum == 3:
                    new_state[h][w] = 1
            # If cell have 0 or just 1 live neighbors, it dies. Rule 1.
            if neighbor_sum == 0 or neighbor_sum == 1:
                new_state[h][w] = 0
            # If cell has more than 3 live neighbors, it dies. Rule 3.
            elif neighbor_sum > 3:
                new_state[h][w] = 0
            # If cell has 3 live neighbors it becomes alive. Rule 4.
            elif neighbor_sum == 3:
                new_state[h][w] = 1
            # If cell is dead and has only 2 alive neighbors, it stays dead. Rule 2.
            else:
                new_state[h][w] = 0

    return new_state


board = random_state(3, 3)
render_board(board)
new_board = next_board_state(board)
render_board(new_board)
