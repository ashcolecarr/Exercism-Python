def slices(series, length):
    if not series:
        raise ValueError('Empty series is not valid.')

    if length == 0:
        raise ValueError('Slice length cannot be zero.')
    elif length < 0:
        raise ValueError('Slice length cannot be negative.')
    elif len(series) < length:
        raise ValueError('Slice length is too large.')

    series_size = len(series)
    return [series[i:i + length] for i, j in enumerate(series)
            if i + length <= series_size]
