class Phone(object):
    def __init__(self, phone_number):
        numbers = ''.join([x for x in phone_number if x.isdigit()])
        if not 9 < len(numbers) < 12:
            raise ValueError('Phone number is invalid.')

        if len(numbers) == 11 and numbers[0] != '1':
            raise ValueError('Country code is invalid.')

        self.number = numbers[1:] if len(numbers) == 11 else numbers
        if int(self.number[0]) < 2:
            raise ValueError('Area code is invalid.')
        elif int(self.number[3]) < 2:
            raise ValueError('Exchange code is invalid.')

        self.area_code = self.number[0:3]

    def pretty(self):
        return '({0}) {1}-{2}'.format(self.number[0:3],
                                      self.number[3:6], self.number[6:])
