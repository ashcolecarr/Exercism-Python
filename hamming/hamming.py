def distance(strand_a, strand_b):
    if(len(strand_a) != len(strand_b)):
        raise ValueError('DNA strands must be of equal length.')

    distanceCount = 0

    for a, b in zip(strand_a, strand_b):
        if(a != b):
            distanceCount += 1

    return distanceCount
