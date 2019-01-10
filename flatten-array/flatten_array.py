def flatten(iterable):
    if not iterable:
        return []

    if isinstance(iterable[0], list):
        return flatten(iterable[0]) + flatten(iterable[1:])
    else:
        if isinstance(iterable[0], int) or isinstance(iterable[0], str):
            return [iterable[0]] + flatten(iterable[1:])
        else:
            return flatten(iterable[1:])
