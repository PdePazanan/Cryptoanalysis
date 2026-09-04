import math


def load_quadgrams(filename):
    quadgrams = {}

    with open(filename, "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) != 2:
                continue

            quadgrams[parts[0]] = int(parts[1])

    total = sum(quadgrams.values())

    # On travaille avec les log-probabilités pour éviter
    # de multiplier plein de nombres très petits.
    for q in quadgrams:
        quadgrams[q] = math.log10(quadgrams[q] / total)

    return quadgrams


def score_text(text, quadgrams):

    text = ""

    for c in text.upper():
        if c.isalpha():
            text += c

    score = 0

    for i in range(len(text) - 3):

        quadgram = text[i:i + 4]

        if quadgram in quadgrams:
            score += quadgrams[quadgram]
        else:
            # Un groupe de lettres jamais vu dans le corpus
            # est probablement très peu probable.
            score -= 10

    return score