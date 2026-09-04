import random

from cipher import decrypt, random_key
from scorer import score_text

def change_key(key):

    key = list(key)

    # On échange simplement deux lettres de la clé.
    # C'est notre petite modification à chaque étape.
    a = random.randint(0, 25)
    b = random.randint(0, 25)

    key[a], key[b] = key[b], key[a]

    return "".join(key)


def crack(ciphertext, quadgrams, iterations=20000):

    key = random_key()

    plaintext = decrypt(ciphertext, key)
    best_score = score_text(plaintext, quadgrams)

    best_key = key

    for i in range(iterations):

        new_key = change_key(key)

        new_text = decrypt(ciphertext, new_key)
        new_score = score_text(new_text, quadgrams)

        if new_score > best_score:

            key = new_key
            best_score = new_score
            best_key = new_key

    return best_key, best_score