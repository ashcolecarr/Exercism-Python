import math


def sieve(limit):
    if limit < 2:
        return []

    prime_candidates = [False, False] + [True] * (limit - 1)
    for i in range(2, int(math.sqrt(limit)) + 1):
        if prime_candidates[i]:
            for j in [i ** 2 + y * i for y in range(0, limit + 1)
                      if i ** 2 + y * i <= limit]:
                prime_candidates[j] = False

    return [i for i, j in enumerate(prime_candidates) if j]
