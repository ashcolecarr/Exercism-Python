def board(input_board_array):
    if not input_board_array or any([not x for x in input_board_array]):
        return input_board_array

    if len({len(x) for x in input_board_array}) > 1:
        raise ValueError('All rows in board must be of equal length.')
    elif any([[y for y in x
               if y != ' ' and y != '*' and not y.isdigit()]
              for x in input_board_array]):
        raise ValueError('Board contains an invalid character')

    output_board_array = []
    for i, x in enumerate(input_board_array):
        board_row = ''
        for j, y in enumerate(x):
            if y == '*':
                board_row += y
            else:
                mines = _get_mine_count((i, j), input_board_array)
                board_row += ' ' if mines == 0 else str(mines)

        output_board_array.append(board_row)

    return output_board_array


def _get_mine_count(position, input_board_array):
    mines = []
    # Scan all the adjacent tiles.
    for i, x in enumerate(input_board_array):
        for j, y in enumerate(x):
            if position[0] - 1 <= i <= position[0] + 1 and \
                    position[1] - 1 <= j <= position[1] + 1 and \
                    (i != position[0] or j != position[1]):
                mines.append(y)

    return mines.count('*')
