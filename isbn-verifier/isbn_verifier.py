def verify(isbn):
    parsedIsbn = [x for x in isbn if x.isnumeric() or x == 'X']

    # ISBN should be exactly ten numbers
    # and can have an X only in the final position.
    if len(parsedIsbn) != 10 or isXInFinalPositionOnly(parsedIsbn):
        return False

    isbnNumbers = [int(x) if x != 'X' else 10 for x in parsedIsbn]

    return calculate(isbnNumbers) == 0


def calculate(isbnNumbers):
    countDown = 10
    isbnSum = 0

    for num in isbnNumbers:
        isbnSum += countDown * num
        countDown -= 1

    return isbnSum % 11


def isXInFinalPositionOnly(parsedIsbn):
    locationX = (''.join(parsedIsbn)).find('X')

    return locationX != -1 and locationX < 9
