def saddle_points(matrix):
    if len({len(x) for x in matrix}) > 1:
        raise ValueError('Ragged matrices are not allowed.')

    saddle_points = set()

    for (row_index, row) in enumerate(matrix):
        maximum = max(row)
        for (column_index, column) in enumerate(row):
            if column == maximum:
                minimum = min([x[column_index] for x in matrix])
                if maximum == minimum:
                    saddle_points.add((row_index, column_index))

    return saddle_points
