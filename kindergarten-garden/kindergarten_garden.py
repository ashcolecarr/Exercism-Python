import collections


class Garden(object):
    _plants = {
        'V': 'Violets',
        'R': 'Radishes',
        'C': 'Clover',
        'G': 'Grass'
    }

    _default_students = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

    _plants_per_student = 2

    def __init__(self, diagram, students=None):
        class_students = sorted(students if students is not None
                                else self._default_students)

        plant_rows = diagram.split()

        self._student_plants = collections.defaultdict(list)
        for (idx, student) in enumerate(class_students):
            for row in plant_rows:
                self._student_plants[student] += (
                    row[idx * self._plants_per_student:idx *
                        self._plants_per_student +
                        self._plants_per_student]
                )

    def plants(self, student):
        return [self._plants[x] for x in self._student_plants[student]]
