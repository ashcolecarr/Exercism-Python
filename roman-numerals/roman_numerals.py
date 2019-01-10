def numeral(number):
    if number > 3000 or number <= 0:
        raise ValueError('Number must be between 1 and 3000.')

    numerals = 'IVXXLCCDMM'

    # Split number into its components.
    number_places = [int(x) for x in str(number)[::-1]]

    roman_numeral = ''
    for i, number in enumerate(number_places):
        roman_numeral += generate_numeral(
            number, numerals[i * 3:i * 3 + 3])[::-1]

    return roman_numeral[::-1]


def generate_numeral(number, numerals):
    if number == 0:
        return ''
    elif number <= 3:
        return numerals[0] * number
    elif number == 4:
        return numerals[0] + numerals[1]
    elif number == 5:
        return numerals[1]
    elif number >= 6 and number <= 8:
        return numerals[1] + (numerals[0] * (number - 5))
    elif number == 9:
        return numerals[0] + numerals[2]
