from functools import reduce
from math import sqrt


def classify(number):
    if number < 1:
        raise ValueError('Number must be 1 or greater.')

    # Aliquot sum does not include the number itself.
    aliquot_sum = sum(_factors(number)) - number
    if aliquot_sum > number:
        return 'abundant'
    elif aliquot_sum < number:
        return 'deficient'
    else:
        return 'perfect'


def _factors(number):
    step = 2 if number % 2 else 1
    return set(reduce(list.__add__,
                      ([x, number // x] for x in
                       range(1, int(sqrt(number)) + 1, step)
                       if number % x == 0)))
