def on_square(integer_number):
    validate_values(integer_number)

    square_count = 1
    grains_on_square = 1
    while square_count < integer_number:
        grains_on_square = grains_on_square << 1
        square_count += 1

    return grains_on_square


def total_after(integer_number):
    validate_values(integer_number)

    return sum([2 ** x for x in range(integer_number)])


def validate_values(number):
    if number <= 0:
        raise ValueError('Number cannot be zero or negative.')
    elif number > 64:
        raise ValueError('Number cannot be greater than 64.')
