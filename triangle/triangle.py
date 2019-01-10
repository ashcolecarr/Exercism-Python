def is_equilateral(sides):
    if all(x == 0 for x in sides):
        return False

    return len(set(sides)) == 1


def is_isosceles(sides):
    if violates_triangle_inequality(sides):
        return False

    return len(set(sides)) == 2 or is_equilateral(sides)


def is_scalene(sides):
    if violates_triangle_inequality(sides):
        return False

    return len(set(sides)) == 3


def violates_triangle_inequality(sides):
    sorted_sides = sorted(sides)
    if sorted_sides[0] + sorted_sides[1] < sorted_sides[2]:
        return True
