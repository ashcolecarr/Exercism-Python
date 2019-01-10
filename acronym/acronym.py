def abbreviate(words):
    split_words = ''.join([' ' if x == '-' else x for x in words]).split()

    return ''.join([x[0].upper() for x in split_words])
