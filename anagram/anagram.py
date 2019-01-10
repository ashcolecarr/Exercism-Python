def find_anagrams(word, candidates):
    sorted_word = sorted(word.lower())

    anagrams = []
    for candidate in candidates:
        if sorted_word == sorted(candidate.lower()) and \
                candidate.lower() != word.lower():
            anagrams.append(candidate)

    return anagrams
