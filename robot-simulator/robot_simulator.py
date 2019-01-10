# Globals for the bearings
# Change the values as you see fit
EAST = 90
NORTH = 0
WEST = 270
SOUTH = 180


class Robot(object):
    bearing = NORTH
    _x = 0
    _y = 0
    coordinates = (0, 0)

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self._x = x
        self._y = y
        self.coordinates = (self._x, self._y)

    def turn_left(self):
        self.bearing = (self.bearing - 90) % 360

    def turn_right(self):
        self.bearing = (self.bearing + 90) % 360

    def advance(self):
        if self.bearing == NORTH:
            self._y += 1
        elif self.bearing == SOUTH:
            self._y -= 1
        elif self.bearing == EAST:
            self._x += 1
        elif self.bearing == WEST:
            self._x -= 1

        self.coordinates = (self._x, self._y)

    def simulate(self, commands):
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'A':
                self.advance()
