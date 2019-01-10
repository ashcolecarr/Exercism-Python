def hey(phrase):
    text = phrase.strip()

    if not(text):
        # Nothing said
        return 'Fine. Be that way!'

    if(is_yelling(text)):
        # Was the yell a question or a statement?
        if(text[-1] == '?'):
            return 'Calm down, I know what I\'m doing!'

        return 'Whoa, chill out!'

    if(text[-1] == '?'):
        return 'Sure.'

    return 'Whatever.'


def is_yelling(phrase):
    letters = ''.join([x for x in phrase if x.isalpha()])
    # Won't be yelling if there are no letters.
    if not(letters):
        return False

    return all([x.isupper() for x in letters])
