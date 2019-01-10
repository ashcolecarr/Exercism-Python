def is_armstrong(number):
    number_size = len(str(number))
    return sum([int(x) ** number_size
                for x in list(str(number))]) == number
