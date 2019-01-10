def is_isogram(string):
    letters = [x for x in string.lower() if x.isalpha()]

    letters_set = set(letters)

    return len(letters) == len(letters_set)
