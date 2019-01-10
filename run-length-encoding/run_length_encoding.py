def decode(string):
    decoded = []

    digits = []
    for char in string:
        if char.isdigit():
            digits.append(char)
        else:
            decoded.append(char * (int(''.join(digits)) if digits else 1))
            digits.clear()

    return ''.join(decoded)


def encode(string):
    encoded = []

    letter_count = 1
    for i, j in enumerate(string):
        if i == len(string) - 1 or string[i] != string[i + 1]:
            encoded.append((str(letter_count) if letter_count > 1 else '') +
                           string[i])
            letter_count = 1
        else:
            letter_count += 1

    return ''.join(encoded)
