def transform(legacy_data):
    new_data = {}

    for key, value in legacy_data.items():
        for letter in value:
            new_data.update({letter.lower(): key})

    return new_data
