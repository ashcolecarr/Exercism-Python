def triplets_with_sum(sum_of_triplet):
    return set([(a, b, (sum_of_triplet - (a + b)))
                for a in range(1, sum_of_triplet // 3 + 1)
                for b in range(a + 1, sum_of_triplet // 2 + 1)
                if (sum_of_triplet - (a + b)) * (sum_of_triplet - (a + b)) ==
                a * a + b * b])


def triplets_in_range(range_start, range_end):
    # Not sure what this is for. It doesn't appear to factor
    # in any of the tests and is not called for by the problem description.
    pass


def is_triplet(triplet):
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2
