from json import dumps
DIGITAL_NUMBERS = {dumps([' _ ', '| |', '|_|']): '0',
                   dumps(['   ', '  |', '  |']): '1',
                   dumps([' _ ', ' _|', '|_ ']): '2',
                   dumps([' _ ', ' _|', ' _|']): '3',
                   dumps(['   ', '|_|', '  |']): '4',
                   dumps([' _ ', '|_ ', ' _|']): '5',
                   dumps([' _ ', '|_ ', '|_|']): '6',
                   dumps([' _ ', '  |', '  |']): '7',
                   dumps([' _ ', '|_|', '|_|']): '8',
                   dumps([' _ ', '|_|', ' _|']): '9'}


def convert(input_grid):
    if len(input_grid) % 4 != 0 or \
            any([x for x in input_grid if len(x) % 3 != 0]):
        raise ValueError('Input must have a multiple of 4 lines '
                         'and a multiple of three columns.')

    converted_numbers = []
    for row in range(0, len(input_grid), 4):
        if row > 0:
            converted_numbers.append(',')
        for number in range(0, len(input_grid[0]), 3):
            current_number = [input_grid[row][number:number + 3],
                              input_grid[row + 1][number:number + 3],
                              input_grid[row + 2][number:number + 3]]
            converted_numbers.append(
                DIGITAL_NUMBERS.get(dumps(current_number), '?'))

    return ''.join(converted_numbers)
