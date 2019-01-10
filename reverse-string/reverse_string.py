def reverse(text):
    reversedText = ''

    for i in range(len(text), 0, -1):
        reversedText += text[i - 1]

    return reversedText
