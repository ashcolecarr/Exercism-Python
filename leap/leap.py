def is_leap_year(year):
    if is_divisible(year, 4):
        if is_divisible(year, 100) and not is_divisible(year, 400):
            return False

        return True

    return False

def is_divisible(year, number):
    return year % number == 0
