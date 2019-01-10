class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(y) for y in x.split()]
                       for x in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        return [x[index] for x in self.matrix]
