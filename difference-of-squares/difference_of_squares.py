from functools import reduce


def square_of_sum(count):
    return (reduce(lambda x, y: x + y, list(range(1, count + 1)))) ** 2


def sum_of_squares(count):
    return reduce(lambda x, y: x + y, map(lambda x: x ** 2, (range(1, count + 1))))


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
