from random import randint, seed


class Robot(object):
    def __init__(self):
        self.name = ''.join([chr(randint(65, 90)) for x in range(2)] +
                            [str(randint(0, 9)) for x in range(3)])

    def reset(self):
        seed()
        self.__init__()
