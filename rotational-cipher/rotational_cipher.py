def rotate(text, key):
    return ''.join([rotate_letter(x, key) if x.isalpha() else x for x in text])


def rotate_letter(letter, key):
    if ord(letter.upper()) + key > ord('Z'):
        return chr(ord(letter) - (26 - key))

    return chr(ord(letter) + key)
