ACTIONS = ['wink', 'double blink', 'close your eyes', 'jump']
INVERTED = {'wink': 0, 'double blink': 1, 'close your eyes': 2, 'jump': 3}


def handshake(code):
    binary_code = bin(code)[2:]
    actions = [ACTIONS[i] for i, j in enumerate(binary_code[::-1])
               if j == '1' and i < 4]
    return actions if code < 16 else actions[::-1]


def secret_code(actions):
    # Is the list of actions in reverse order?
    is_reversed = INVERTED[actions[0]] > \
        INVERTED[actions[-1]]

    padded_actions = ['1' if x in actions else '0' for x in ACTIONS[::-1]]
    if is_reversed:
        padded_actions = ['1'] + padded_actions

    return int(''.join(padded_actions), 2)
