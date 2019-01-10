def sum_of_multiples(limit, multiples):
    unique_multiples = set()

    for multiple in multiples:
        unique_multiples.update({x for x in range(0, limit, multiple)})

    return sum(unique_multiples)
