def make_diamond(letter):
    if letter == 'A':
        return letter + '\n'

    diamond = []
    outside_spaces_count = ord(letter) - ord('A')
    inside_spaces_count = 1

    current_letter = 'A'
    is_bottom_half = False
    while True:
        if current_letter == 'A':
            diamond.append('{0}{1}{0}'.format(' ' * outside_spaces_count, 'A'))
            if is_bottom_half:
                break
            else:
                current_letter = chr(ord(current_letter) + 1)
                outside_spaces_count -= 1
                continue

        diamond.append('{0}{1}{2}{1}{0}'
                       .format(' ' * outside_spaces_count,
                               current_letter, ' ' * inside_spaces_count))

        if current_letter == letter:
            is_bottom_half = True

        if is_bottom_half:
            current_letter = chr(ord(current_letter) - 1)
            outside_spaces_count += 1
            inside_spaces_count -= 2
        else:
            current_letter = chr(ord(current_letter) + 1)
            outside_spaces_count -= 1
            inside_spaces_count += 2

    return '\n'.join(diamond) + '\n'
