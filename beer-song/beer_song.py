def recite(start, take=1):
    song = []
    for x in range(start, start - take, -1):
        verses = get_verses(x)
        song.append(verses[0])
        song.append(verses[1])

        if x > (start - take) + 1:
            song.append('')

    return song


def get_verses(number):
    first_verse = '{0} bottle{1} of beer on the wall, {0} bottle{1} of beer.'
    second_verse = \
        'Take {0} down and pass it around, {1} bottle{2} of beer on the wall.'
    zero_verse = \
        'No more bottles of beer on the wall, no more bottles of beer.'
    final_verse = \
        'Go to the store and buy some more, 99 bottles of beer on the wall.'

    if number > 2:
        return (first_verse.format(number, 's'),
                second_verse.format('one', number - 1, 's'))
    elif number == 2:
        return (first_verse.format(number, 's', number),
                second_verse.format('one', number - 1, ''))
    elif number == 1:
        return (first_verse.format(number, ''),
                second_verse.format('it', 'no more', 's'))
    else:
        return (zero_verse, final_verse)
