def append(xs, ys):
    return xs + ys


def concat(lists):
    return foldl(lambda x, y: x + y, lists, [])


def filter_clone(function, xs):
    filtered = []

    for x in xs:
        if function(x):
            filtered += [x]

    return filtered


def length(xs):
    return foldl(lambda x, y: x + y, map_clone(lambda x: 1, xs), 0)


def map_clone(function, xs):
    mapped = []

    for x in xs:
        mapped += [function(x)]

    return mapped


def foldl(function, xs, acc):
    result = acc

    for x in xs:
        result = function(result, x)

    return result


def foldr(function, xs, acc):
    result = acc

    for x in reverse(xs):
        result = function(x, result)

    return result


def reverse(xs):
    backwards = []

    for i in range(length(xs) - 1, -1, -1):
        backwards += [xs[i]]

    return backwards
