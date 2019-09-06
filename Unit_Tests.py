from Game_Of_Life import next_board_state

if __name__ == "__main__":
    # Test 1: dead cells with no live neighbors should stay dead.
    init_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    expected_next_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    actual_next_state1 = next_board_state(init_state1)

    if expected_next_state1 == actual_next_state1:
        print('Passed 1')
    else:
        print('Failed 1!')
        print('Expected:')
        print(expected_next_state1)
        print('Actual:')
        print(actual_next_state1)

    # Test 2: dead cells with exactly 3 neighbors should come alive.
    init_state2 = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    expected_next_state2 = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    actual_next_state2 = next_board_state(init_state2)

    if expected_next_state2 == actual_next_state2:
        print('Passed 2')
    else:
        print('Failed 2!')
        print('Expected:')
        print(expected_next_state2)
        print('Actual:')
        print(actual_next_state2)

    # Test 3: any live cell with more than 3 live neighbors dies.
    init_state3 = [
        [1, 0, 1],
        [0, 1, 1],
        [1, 0, 0]
    ]
    expected_next_state3 = [
        [1, 0, 1],
        [0, 0, 1],
        [0, 0, 0]
    ]
    actual_next_state3 = next_board_state(init_state2)

    if expected_next_state3 == actual_next_state3:
        print('Passed 3')
    else:
        print('Failed 3!')
        print('Expected:')
        print(expected_next_state3)
        print('Actual:')
        print(actual_next_state3)
