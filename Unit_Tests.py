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
        print('Actual')
        print(actual_next_state1)
