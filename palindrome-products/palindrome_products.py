from itertools import product


def largest_palindrome(max_factor, min_factor):
    number_range = range(min_factor, max_factor + 1)
    if not number_range:
        raise ValueError('No numbers in range.')

    cartesian_product = {x for x in product(number_range, number_range)}
    products = [x[0] * x[1] for x in cartesian_product]
    maximum = max([x for x in products if str(x) == str(x)[::-1]])

    factors = [x for x in cartesian_product if x[0] * x[1] == maximum]

    return (maximum, factors)


def smallest_palindrome(max_factor, min_factor):
    number_range = range(min_factor, max_factor + 1)
    if not number_range:
        raise ValueError('No numbers in range.')

    cartesian_product = {x for x in product(number_range, number_range)}
    products = [x[0] * x[1] for x in cartesian_product]
    minimum = min([x for x in products if str(x) == str(x)[::-1]])

    factors = [x for x in cartesian_product if x[0] * x[1] == minimum]

    return (minimum, factors)
