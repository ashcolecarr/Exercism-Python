from collections import Counter


[NONE, ONE_PAIR, TWO_PAIRS, THREE_OF_A_KIND, STRAIGHT, FLUSH,
 FULL_HOUSE, FOUR_OF_A_KIND, STRAIGHT_FLUSH, ROYAL_FLUSH] = range(10)


def best_hands(hands):
    scores = [determine_hand(x) for x in hands]

    return [hands[scores.index(max(scores))]]


def convert_card_value(card_value):
    if card_value == 'T':
        return 10
    elif card_value == 'J':
        return 11
    elif card_value == 'Q':
        return 12
    elif card_value == 'K':
        return 13
    elif card_value == 'A':
        return 14
    else:
        return int(card_value)


def determine_hand(hand):
    card_values = [convert_card_value(x[0]) for x in hand.split()]
    card_suits = [x[1] for x in hand.split()]

    card_values.sort()
    same_values = len(set(card_values))
    # If every card is of the same suit, it is some kind of flush.
    if len(set(card_suits)) == 1:
        return determine_flush_type(card_values, same_values)

    # Check if values are consecutive,
    # but not of the same suit, i.e. a Straight.
    if same_values == 5 and card_values[4] - card_values[0] == 4:
        return STRAIGHT

    values_count = Counter(card_values)
    if same_values == 2:
        # If there are 4 of the same value, then it's Four of a Kind.
        if 4 in values_count.values():
            return FOUR_OF_A_KIND
        # Otherwise, it must be a Full House.
        else:
            return FULL_HOUSE
    elif same_values == 3:
        # If there are 3 of the same value, then it's Three of a Kind.
        if 3 in values_count.values():
            return THREE_OF_A_KIND
        # Otherwise, it must be Two Pairs.
        else:
            return TWO_PAIRS
    elif same_values == 4:
        # Only One Pair
        return ONE_PAIR

    # No winning hand.
    return NONE


def determine_flush_type(card_values, same_values):
    # Are the values consecutive?
    if same_values == 5 and card_values[4] - card_values[0] == 4:
        # Royal Flush
        if card_values[0] == 10 and card_values[4] == 14:
            return ROYAL_FLUSH
        # Straight Flush
        else:
            return STRAIGHT_FLUSH
    # Flush
    else:
        return FLUSH
