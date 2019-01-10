VERSES = ['the house that Jack built.',
          'the malt that lay in ',
          'the rat that ate ',
          'the cat that killed ',
          'the dog that worried ',
          'the cow with the crumpled horn that tossed ',
          'the maiden all forlorn that milked ',
          'the man all tattered and torn that kissed ',
          'the priest all shaven and shorn that married ',
          'the rooster that crowed in the morn that woke ',
          'the farmer sowing his corn that kept ',
          'the horse and the hound and the horn that belonged to ']


def recite(start_verse, end_verse):
    verses = []
    for x in range(start_verse, end_verse + 1):
        verses.append('This is ' + get_verses(x - 1))

    return verses


def get_verses(current_verse):
    if current_verse == 0:
        return VERSES[current_verse]

    return VERSES[current_verse] + get_verses(current_verse - 1)
