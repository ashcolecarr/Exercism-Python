def transpose(input_lines):
    if not input_lines:
        return ''

    max_lines = max([len(x) for x in input_lines.splitlines()])

    transposed_lines = [[] for x in range(max_lines)]
    for i, row in enumerate(input_lines.splitlines()):
        for j, char in enumerate(row):
            while len(transposed_lines[j]) < i:
                transposed_lines[j].append(' ')

            transposed_lines[j].append(char)

    return '\n'.join(''.join(x) for x in transposed_lines)
