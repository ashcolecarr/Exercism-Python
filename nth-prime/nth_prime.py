def nth_prime(positive_number):
    if positive_number < 1:
        raise ValueError('Prime position must be one or greater.')

    if positive_number == 1:
        return 2
    elif positive_number == 2:
        return 3

    # All primes have the form 6(n) +/- 1 except 2 and 3
    primeCount = 2
    candidateCount = 1
    finalPrime = 0

    while primeCount < positive_number:
        if isPrime(6 * candidateCount - 1):
            primeCount += 1
            if primeCount == positive_number:
                finalPrime = 6 * candidateCount - 1

        if isPrime(6 * candidateCount + 1):
            primeCount += 1
            if primeCount == positive_number:
                finalPrime = 6 * candidateCount + 1

        candidateCount += 1

    return finalPrime


def isPrime(n):
    if n < 2:
        return False
    elif n % 2 == 0:
        return n == 2

    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2

    return True
