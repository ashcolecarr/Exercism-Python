from collections import OrderedDict

class Allergies(object):
    _allergens = OrderedDict([('eggs', 1),
                              ('peanuts', 2),
                              ('shellfish', 4),
                              ('strawberries', 8),
                              ('tomatoes', 16),
                              ('chocolate', 32),
                              ('pollen', 64),
                              ('cats', 128)])

    def __init__(self, score):
        self._score = score

    def is_allergic_to(self, item):
        return self._score & self._allergens[item] == self._allergens[item]

    @property
    def lst(self):
        return [x for x in self._allergens.keys() if self.is_allergic_to(x)]
