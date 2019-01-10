MAX = 999999999999
NUMBER_WORDS = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
                40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
                80: 'eighty', 90: 'ninety', 100: 'hundred',
                1000: 'thousand', 1000000: 'million', 1000000000: 'billion'}


def say(number):
    if number < 0 or number > MAX:
        raise ValueError('Number is outside of accepted range.')
    elif number == 0:
        return NUMBER_WORDS[0]

    reversed_number = str(int(number))[::-1]
    number_chunks = [int(reversed_number[i:i + 3][::-1]) for i, j in
                     enumerate(reversed_number) if i % 3 == 0]

    number_words = []
    number_place = 1
    for chunk in number_chunks:
        translated_number = translate_number(chunk)
        number_words.append(
            '{0}{1}'.format(translated_number, ' ' + NUMBER_WORDS[number_place]
                            if number_place > 1 and
                            len(translated_number) > 0 else ''))
        number_place *= 1000

    return ' '.join(number_words[::-1]).strip()


def translate_number(number):
    if number == 0:
        return ''

    number_words = []

    and_text = ''
    if number >= 100:
        number_words.append('{0} {1} '.format(NUMBER_WORDS[number // 100],
                                              NUMBER_WORDS[100]))
        and_text = 'and '

    # Get the tens-place number.
    tens_number = number % 100
    if tens_number > 0 and tens_number < 20:
        number_words.append('{0}{1}'.format(and_text,
                                            NUMBER_WORDS[tens_number]))
    elif tens_number >= 20 and tens_number < 100:
        number_words.append('{0}{1}'
                            .format(and_text,
                                    NUMBER_WORDS[(tens_number // 10) * 10]))
        if tens_number % 10 != 0:
            number_words.append('-{0}'.format(NUMBER_WORDS[tens_number % 10]))

    return ''.join(number_words)
