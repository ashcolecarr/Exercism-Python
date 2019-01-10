def is_pangram(sentence):
    ALPHABET_LENGTH = 26

    letters = sentence.lower()

    onlyLetters = set(map(lambda x: x if (str.isalpha(x)) else '', letters))

    return len(''.join(onlyLetters)) == ALPHABET_LENGTH
