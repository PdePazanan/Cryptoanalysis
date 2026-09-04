import string
import random

alphabet = string.ascii_uppercase


def encrypt(text, key):
    result = ""

    for c in text.upper():
        if c in alphabet:
            pos = alphabet.index(c)
            result += key[pos]
        else:
            result += c

    return result


def decrypt(text, key):
    result = ""

    for c in text.upper():
        if c in alphabet:
            pos = key.index(c)
            result += alphabet[pos]
        else:
            result += c

    return result


def random_key():
    letters = list(alphabet)
    random.shuffle(letters)
    return "".join(letters)