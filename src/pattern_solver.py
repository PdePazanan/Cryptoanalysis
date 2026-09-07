import sys
import time
import random
from collections import Counter
from scorer import clean_words

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def load_wordlist(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip().upper() for line in f if line.strip().isalpha()]


def word_pattern(word):
    mapping = {}
    pattern = []
    next_id = 0
    for char in word:
        if char not in mapping:
            mapping[char] = chr(ord("A") + next_id)
            next_id += 1
        pattern.append(mapping[char])
    return "".join(pattern)


def build_pattern_index(wordlist):
    index = {}
    for word in wordlist:
        p = word_pattern(word)
        index.setdefault(p, []).append(word)
    return index


def solve_word_patterns(ciphertext, wordlist, pattern_index=None,
                         max_solutions=10, max_nodes=2_000_000):

    if pattern_index is None:
        print("Construction de l'index des motifs...")
        pattern_index = build_pattern_index(wordlist)

    cipher_words = clean_words(ciphertext)
    counts = Counter(cipher_words)
    distinct_words = list(set(cipher_words))

    candidates_by_word = {
        w: pattern_index.get(word_pattern(w), [])
        for w in distinct_words
    }

    # Affiche tout de suite combien de candidats a chaque mot :
    # ça permet de voir immédiatement si un mot bloque tout
    # (0 candidat) ou si un mot va faire exploser la recherche
    # (des milliers de candidats).
    print("Mots distincts à résoudre :")
    for w in sorted(distinct_words, key=lambda w: len(candidates_by_word[w])):
        print(f"  {w} (x{counts[w]})  ->  {len(candidates_by_word[w])} candidats")

    solutions = []
    nodes_explored = 0
    start_time = time.time()

    def backtrack(remaining_words, cipher_to_plain, plain_to_cipher, depth):
        nonlocal nodes_explored
        nodes_explored += 1

        if nodes_explored % 2000 == 0:
            elapsed = time.time() - start_time
            sys.stdout.write(
                f"\rRecherche en cours...  "
                f"Noeuds explorés: {nodes_explored}  "
                f"Profondeur: {depth}/{len(distinct_words)}  "
                f"Solutions trouvées: {len(solutions)}  "
                f"Temps: {elapsed:.0f}s   "
            )
            sys.stdout.flush()

        if nodes_explored >= max_nodes:
            return

        if len(solutions) >= max_solutions:
            return

        if not remaining_words:
            solutions.append(dict(cipher_to_plain))
            return

        # HEURISTIQUE MRV : on choisit le mot restant qui a
        # le MOINS de candidats compatibles avec le mapping actuel,
        # pas juste le plus fréquent. Ça élague l'arbre bien plus vite.
        best_word = None
        best_candidates = None

        for w in remaining_words:
            compatible = []
            for candidate in candidates_by_word[w]:
                ok = True
                for c_char, p_char in zip(w, candidate):
                    if cipher_to_plain.get(c_char, p_char) != p_char:
                        ok = False
                        break
                    if plain_to_cipher.get(p_char, c_char) != c_char:
                        ok = False
                        break
                if ok:
                    compatible.append(candidate)

            if best_candidates is None or len(compatible) < len(best_candidates):
                best_word = w
                best_candidates = compatible

            if len(compatible) == 0:
                return  # cul-de-sac : ce mot n'a plus aucun candidat viable

        next_remaining = [w for w in remaining_words if w != best_word]

        for candidate in best_candidates:
            new_pairs = []
            for c_char, p_char in zip(best_word, candidate):
                if c_char not in cipher_to_plain:
                    new_pairs.append((c_char, p_char))
                    cipher_to_plain[c_char] = p_char
                    plain_to_cipher[p_char] = c_char

            backtrack(next_remaining, cipher_to_plain, plain_to_cipher, depth + 1)

            for c_char, p_char in new_pairs:
                del cipher_to_plain[c_char]
                del plain_to_cipher[p_char]

            if len(solutions) >= max_solutions or nodes_explored >= max_nodes:
                break

    backtrack(distinct_words, {}, {}, 0)

    sys.stdout.write("\n")
    if nodes_explored >= max_nodes:
        print(f"Arrêt après {max_nodes} noeuds explorés (limite de sécurité atteinte).")

    return solutions


def mapping_to_key(cipher_to_plain):
    key = [None] * 26

    for cipher_letter, plain_letter in cipher_to_plain.items():
        plain_idx = ALPHABET.index(plain_letter)
        key[plain_idx] = cipher_letter

    used = set(cipher_to_plain.keys())
    remaining = [c for c in ALPHABET if c not in used]
    random.shuffle(remaining)

    r = 0
    for i in range(26):
        if key[i] is None:
            key[i] = remaining[r]
            r += 1

    return "".join(key)