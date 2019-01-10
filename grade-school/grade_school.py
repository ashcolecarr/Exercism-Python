class School(object):
    def __init__(self):
        self.__students = []

    def add_student(self, name, grade):
        self.__students.append((grade, name))

    def roster(self):
        return [y for (x, y) in
                sorted(self.__students, key=lambda x: (x[0], x[1]))]

    def grade(self, grade_number):
        return sorted([y for (x, y) in self.__students if x == grade_number])
