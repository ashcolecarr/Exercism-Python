from math import sqrt


def prime_factors(natural_number):
    prime_factors = []

    # Get a list of factors.
    factors = [2] if natural_number % 2 == 0 else []
    factors += [x for x in range(3, int(sqrt(natural_number)) + 1, 2)
                if natural_number % x == 0]

    # Using straightforward trial division.
    trialed_number = natural_number
    idx = 0
    while idx < len(factors):
        if trialed_number % factors[idx] == 0:
            prime_factors.append(factors[idx])
            trialed_number //= factors[idx]
        else:
            idx += 1

    # A prime factor could still be left.
    if trialed_number > 1:
        prime_factors.append(trialed_number)

    return prime_factors
