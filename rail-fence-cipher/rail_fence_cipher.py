from math import ceil


def encode(message, rails):
    fence = [[] for x in range(rails)]

    is_going_down = True
    rail_index = 0
    for i, char in enumerate(message):
        fence[rail_index].append(char)

        if rail_index == rails - 1:
            is_going_down = False
        elif rail_index == 0:
            is_going_down = True

        if is_going_down:
            rail_index += 1
        else:
            rail_index -= 1

    return ''.join([''.join(x) for x in fence])


def decode(encoded_message, rails):
    cycle = (rails * 2) - 2
    total_cycles = len(encoded_message) / cycle
    top_row = ceil(total_cycles)
    middle_row = int(total_cycles * 2)

    fence = [[] for x in range(rails)]
    fence[0] += encoded_message[0:top_row]
    position = top_row
    for x in range(1, rails):
        fence[x] += encoded_message[position:position + middle_row]
        position += middle_row

    row = 0
    is_going_down = True
    plain_text = []
    while True:
        if not fence[row]:
            break

        plain_text.append(fence[row].pop(0))
        if row == len(fence) - 1:
            is_going_down = False
        elif row == 0:
            is_going_down = True

        if is_going_down:
            row += 1
        else:
            row -= 1

    return ''.join(plain_text)
