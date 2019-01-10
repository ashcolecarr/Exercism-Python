from re import match


def translate(text):
    words = text.split()

    return ' '.join([pig_latinize(x) for x in words])


def pig_latinize(word):
    vowels = set({'a', 'e', 'i', 'o', 'u'})

    groups = match('(\w*?(qu)?)([aeiouy]\w*)', word)
    if word[0] in vowels:
        return word + 'ay'
    elif (word[0] == 'y' or word[0] == 'x'):
        if word[1] not in vowels:
            return word + 'ay'
        else:
            return word[1:] + word[0] + 'ay'
    else:
        return groups.group(3) + groups.group(1) + 'ay'
