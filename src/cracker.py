import random
import math
from cipher import decrypt, random_key
from scorer import score_text


# SEULEMENT HILL CLIMBING
def change_key(key):

    key = list(key)

    # On échange deux lettres au hasard.
    # Ça permet de tester une nouvelle clé proche de la précédente.
    a = random.randint(0, 25)
    b = random.randint(0, 25)

    key[a], key[b] = key[b], key[a]

    return "".join(key)


def crack(ciphertext, trigrams, quadgrams, iterations=20000, restarts=20):

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


# def change_key(key):
#     key = list(key)
#     a = random.randint(0, 25)
#     b = random.randint(0, 25)
#     while b == a:
#         b = random.randint(0, 25)  # évite un swap inutile
#     key[a], key[b] = key[b], key[a]
#     return "".join(key)





# def crack(ciphertext, trigrams, quadgrams, iterations=20000, restarts=30):
#     best_key = None
#     best_score = -float("inf")

#     for restart in range(restarts):
#         key = random_key()
#         text = decrypt(ciphertext, key)
#         score = score_text(text, trigrams, quadgrams)

#         current_key, current_score = key, score

#         for i in range(iterations):
#             # Température décroissante : accepte plus de "mauvais" coups au début
#             temperature = max(0.01, 1 - i / iterations)

#             new_key = change_key(current_key)
#             new_text = decrypt(ciphertext, new_key)
#             new_score = score_text(new_text, trigrams, quadgrams)

#             delta = new_score - current_score

#             if delta > 0 or random.random() < math.exp(delta / (temperature * 50)):
#                 current_key = new_key
#                 current_score = new_score

#                 if current_score > score:
#                     key, score = current_key, current_score

#         if score > best_score:
#             best_score = score
#             best_key = key
#             print("New best score:", round(best_score, 2))

#     return best_key, best_score


