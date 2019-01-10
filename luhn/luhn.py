class Luhn(object):
    def __init__(self, card_num):
        self._number = card_num

    def is_valid(self):
        candidate_number = self._number.replace(' ', '')

        if [x for x in candidate_number if not x.isdigit()]:
            return False
        elif len([x for x in candidate_number if x.isdigit()]) == 1:
            return False

        digits = [self.double_digit(int(j)) if i % 2 == 1 else int(j)
                  for i, j in enumerate(candidate_number[::-1])]

        return sum(digits) % 10 == 0

    def double_digit(self, digit):
        doubled_digit = digit << 1

        return doubled_digit - 9 if doubled_digit > 9 else doubled_digit
