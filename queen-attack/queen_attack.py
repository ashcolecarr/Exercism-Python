class Queen(object):
    def __init__(self, row, column):
        if row < 0 or row > 7 or column < 0 or column > 7:
            raise ValueError('Queen cannot be placed outside the board.')

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and \
                self.column == another_queen.column:
            raise ValueError('Queens cannot occupy the same position.')

        # Verify orthogonal movement.
        if self.row == another_queen.row or \
                self.column == another_queen.column:
            return True

        # Verify diagonal movement.
        northeast = southeast = southwest = \
            northwest = self.row, self.column

        for x in range(8):
            northeast = northeast[0] + 1, northeast[1] - 1
            southeast = southeast[0] - 1, southeast[1] - 1
            southwest = southwest[0] - 1, southwest[1] + 1
            northwest = northwest[0] + 1, northwest[1] + 1

            if northeast == (another_queen.row, another_queen.column) or \
                    southeast == (another_queen.row, another_queen.column) or \
                    southwest == (another_queen.row, another_queen.column) or \
                    northwest == (another_queen.row, another_queen.column):
                return True

        return False
