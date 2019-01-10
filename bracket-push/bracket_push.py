def is_paired(input_string):
    enclosures = []

    for x in input_string:
        if x in '({[':
            enclosures.append(x)
        elif x in ')}]':
            # Can't have closing enclosure before an opening one.
            if not enclosures:
                return False

            enclosure = enclosures.pop(-1)
            if x == ')' and enclosure != '(':
                return False
            elif x == '}' and enclosure != '{':
                return False
            elif x == ']' and enclosure != '[':
                return False

    return True if not enclosures else False
