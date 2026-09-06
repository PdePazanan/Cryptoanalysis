# import random
# import math
# from cipher import decrypt, random_key
# from scorer import score_text


# # SEULEMENT HILL CLIMBING
# def change_key(key):

#     key = list(key)

#     # On échange deux lettres au hasard.
#     # Ça permet de tester une nouvelle clé proche de la précédente.
#     a = random.randint(0, 25)
#     b = random.randint(0, 25)

#     key[a], key[b] = key[b], key[a]

#     return "".join(key)


# def crack(ciphertext, trigrams, quadgrams, iterations=20000, restarts=20):

#     best_key = None
#     best_score = -float("inf")

#     # On recommence plusieurs fois avec une clé différente.
#     # Ça évite de rester bloqué trop facilement sur une mauvaise solution.
#     for restart in range(restarts):

#         key = random_key()

#         text = decrypt(ciphertext, key)
#         score = score_text(text, trigrams, quadgrams)

#         for i in range(iterations):

#             new_key = change_key(key)

#             new_text = decrypt(ciphertext, new_key)
#             new_score = score_text(new_text, trigrams, quadgrams)

#             # On garde la nouvelle clé seulement si elle donne
#             # un texte qui ressemble davantage à de l'anglais.
#             if new_score > score:

#                 key = new_key
#                 score = new_score

#         if score > best_score:

#             best_score = score
#             best_key = key

#             print(
#                 "New best score:",
#                 round(best_score, 2)
#             )

#     return best_key, best_score






import sys
import time
import random
from cipher import decrypt, random_key
from scorer import score_text

SPINNER = "|/-\\"


def change_key(key):
    key = list(key)
    a = random.randint(0, 25)
    b = random.randint(0, 25)
    key[a], key[b] = key[b], key[a]
    return "".join(key)


def crack(ciphertext, trigrams, quadgrams, iterations=20000, restarts=20):

    best_key = None
    best_score = -float("inf")
    start_time = time.time()

    for restart in range(restarts):

        key = random_key()
        text = decrypt(ciphertext, key)
        score = score_text(text, trigrams, quadgrams)

        for i in range(iterations):

            new_key = change_key(key)
            new_text = decrypt(ciphertext, new_key)
            new_score = score_text(new_text, trigrams, quadgrams)

            if new_score > score:
                key = new_key
                score = new_score

            # Affichage toutes les 200 itérations (pas à chaque itération :
            # écrire dans le terminal a un coût, ça ralentirait le calcul)
            if i % 200 == 0:
                elapsed = time.time() - start_time
                spin = SPINNER[(i // 200) % len(SPINNER)]
                sys.stdout.write(
                    f"\r{spin} Restart {restart + 1}/{restarts}  "
                    f"Iteration {i}/{iterations}  "
                    f"Current score: {round(score, 1)}  "
                    f"Best score: {round(best_score, 1)}  "
                    f"time: {elapsed:.0f}s   "
                )
                sys.stdout.flush()

        if score > best_score:
            best_score = score
            best_key = key
            sys.stdout.write("\n")  # on quitte la ligne de progression avant d'imprimer
            print("New best score:", round(best_score, 2))

    sys.stdout.write("\n")
    return best_key, best_score

