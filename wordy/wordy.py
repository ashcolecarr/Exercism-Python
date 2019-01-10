from re import findall
ERROR_MESSAGE = 'Question is not in a valid format.'


def calculate(question):
    terms = findall('((-?\d+)(\s[a-zA-Z]+(\s[a-zA-Z]+)?)?)+', question)

    operations_queue = []
    for x in terms:
        operations_queue.append(x[1])
        if x[2]:
            operations_queue.append(x[2].strip())

    if not operations_queue:
        raise ValueError(ERROR_MESSAGE)

    result = int(operations_queue[0])
    operation = ''
    # Numbers and operations should alternate.
    for x in operations_queue[1:]:
        if x.isdigit() and not operation:
            raise ValueError(ERROR_MESSAGE)

        if not operation:
            operation = x
        else:
            result = conduct_operation(result, operation, int(x))
            operation = ''

    # Is a number missing off the end?
    if operation:
        raise ValueError(ERROR_MESSAGE)

    return result


def conduct_operation(result, operation, term):
    if operation == 'plus':
        return result + term
    elif operation == 'minus':
        return result - term
    elif operation == 'multiplied by':
        return result * term
    elif operation == 'divided by':
        return result // term
    else:
        raise ValueError(ERROR_MESSAGE)
