from functools import reduce


def largest_product(series, size):
    if size > len(series):
        raise ValueError('Span cannot be longer than number sequence.')
    elif [x for x in series if not x.isdigit()]:
        raise ValueError('Sequence contains invalid character.')
    elif size < 0:
        raise ValueError('Span cannot be negative.')

    if size == 0:
        return 1

    max_product = 0
    for i, j in enumerate(series):
        substring = series[i:i + size]
        if len(substring) < size:
            break

        new_product = reduce(lambda x, y: int(x) * int(y), substring)
        if new_product > max_product:
            max_product = new_product

    return max_product
