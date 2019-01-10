from random import randint


class Cipher(object):
    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
                'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
                'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    inverse_alphabet = {v: k for k, v in alphabet.items()}

    def __init__(self, key=None):
        if key:
            self.key = ''.join([x.lower() for x in key if x.isalpha()])
        else:
            self.key = ''.join([self.inverse_alphabet[
                randint(0, len(self.alphabet) - 1)] for x in range(101)])

    def encode(self, text):
        cipher = []

        key_to_use = self._expand_key(text)

        for x, y in zip(key_to_use, text):
            cipher.append(self.inverse_alphabet[
                (self.alphabet[x] + self.alphabet[y]) % len(self.alphabet)])

        return ''.join(cipher)

    def decode(self, text):
        plaintext = []

        key_to_use = self._expand_key(text)

        for x, y in zip(key_to_use, text):
            plaintext.append(self.inverse_alphabet[
                (self.alphabet[y] - self.alphabet[x]) % len(self.alphabet)])

        return ''.join(plaintext)

    # Expand the key length to fit the text size.
    def _expand_key(self, text):
        if len(self.key) < len(text):
            repetitions = len(text) // len(self.key) + \
                1 if len(text) % len(self.key) > 0 else 0
            return self.key * repetitions
        else:
            return self.key
