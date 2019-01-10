from collections import Counter
from re import sub


def word_count(phrase):
    # Account for text sequence where whitespace may not be the separator.
    cleaned_phrase = ''.join([' ' if x == ',' or x == '_' else x
                             for x in phrase])

    cleaned_phrase = sub("(\s'|'\s)", ' ', cleaned_phrase)
    cleaned_phrase = ''.join([x for x in cleaned_phrase.lower()
                             if x.isalnum() or x.isspace() or x == "'"])

    words = cleaned_phrase.split()

    return dict(Counter(words))
