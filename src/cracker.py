import random
from cipher import decrypt, random_key
from scorer import score_text


def change_key(key):

    key = list(key)

    # On échange deux lettres au hasard.
    # Ça permet de tester une nouvelle clé proche de la précédente.
    a = random.randint(0, 25)
    b = random.randint(0, 25)

    key[a], key[b] = key[b], key[a]

    return "".join(key)


def crack(ciphertext, trigrams, quadgrams, iterations=10000, restarts=20):

    best_key = None
    best_score = -float("inf")

    # On recommence plusieurs fois avec une clé différente.
    # Ça évite de rester bloqué trop facilement sur une mauvaise solution.
    for restart in range(restarts):

        key = random_key()

        text = decrypt(ciphertext, key)
        score = score_text(text, trigrams, quadgrams)

        for i in range(iterations):

            new_key = change_key(key)

            new_text = decrypt(ciphertext, new_key)
            new_score = score_text(new_text, trigrams, quadgrams)

            # On garde la nouvelle clé seulement si elle donne
            # un texte qui ressemble davantage à de l'anglais.
            if new_score > score:

                key = new_key
                score = new_score

        if score > best_score:

            best_score = score
            best_key = key

            print(
                "New best score:",
                round(best_score, 2)
            )

    return best_key, best_score