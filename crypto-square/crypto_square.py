from math import sqrt, ceil


def encode(plain_text):
    if not plain_text:
        return ''

    normalized_text = ''.join([x.lower() for x in plain_text if x.isalnum()])

    # The rectangle to use will always have columns >= rows
    # and columns - rows <= 1
    column_count = ceil(sqrt(len(normalized_text)))

    rectangle = []
    for x in range(0, len(normalized_text), column_count):
        rectangle.append(normalized_text[x:x + column_count])

    if len(rectangle[-1]) < column_count:
        rectangle[-1] += (' ' * (column_count - len(rectangle[-1])))

    cipher_text = []
    for i, column in enumerate(rectangle[0]):
        for j, row in enumerate(rectangle):
            cipher_text.append(rectangle[j][i])
        if i < len(rectangle[0]) - 1:
            cipher_text.append(' ')

    return ''.join(cipher_text)
