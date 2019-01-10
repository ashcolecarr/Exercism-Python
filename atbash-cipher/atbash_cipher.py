def encode(plain_text):
    alphabet = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
                'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
                'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
                's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
                'y': 'b', 'z': 'a'}

    grouping_count = 0
    cipher_text = []
    for text in plain_text:
        if not text.isalnum():
            continue

        cipher_text.append(alphabet[text.lower()]
                           if text.isalpha() else text)
        grouping_count += 1

        if grouping_count % 5 == 0:
            cipher_text.append(' ')

    return ''.join(cipher_text).strip()


def decode(ciphered_text):
    alphabet = {'z': 'a', 'y': 'b', 'x': 'c', 'w': 'd', 'v': 'e', 'u': 'f',
                't': 'g', 's': 'h', 'r': 'i', 'q': 'j', 'p': 'k', 'o': 'l',
                'n': 'm', 'm': 'n', 'l': 'o', 'k': 'p', 'j': 'q', 'i': 'r',
                'h': 's', 'g': 't', 'f': 'u', 'e': 'v', 'd': 'w', 'c': 'x',
                'b': 'y', 'a': 'z'}

    plain_text = []
    for text in ciphered_text:
        if not text.isalnum():
            continue

        plain_text.append(alphabet[text.lower()]
                          if text.isalpha() else text)

    return ''.join(plain_text)
