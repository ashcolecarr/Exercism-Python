MAIN_VERSE = 'On the {0} day of Christmas my true love gave to me: '
ORDINALS = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth',
            6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth',
            11: 'eleventh', 12: 'twelfth'}
GIFTS = ['twelve Drummers Drumming, ', 'eleven Pipers Piping, ',
         'ten Lords-a-Leaping, ', 'nine Ladies Dancing, ',
         'eight Maids-a-Milking, ', 'seven Swans-a-Swimming, ',
         'six Geese-a-Laying, ', 'five Gold Rings, ', 'four Calling Birds, ',
         'three French Hens, ', 'two Turtle Doves, ',
         'and a Partridge in a Pear Tree.']


def recite(start_verse, end_verse):
    verses = []

    for x in range(start_verse, end_verse + 1):
        verse = MAIN_VERSE.format(ORDINALS[x])
        if x == 1:
            verse += GIFTS[-1][4:]
        else:
            verse += ''.join(GIFTS[len(GIFTS) - x:])

        verses.append(verse)

    return verses
