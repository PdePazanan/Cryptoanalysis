import math


def load_ngrams(filename):

    ngrams = {}

    with open(filename, "r", encoding="utf-8") as file:

        for line in file:

            parts = line.split()

            if len(parts) != 2:
                continue

            ngram = parts[0]
            count = int(parts[1])

            ngrams[ngram] = count

    total = sum(ngrams.values())

    for ngram in ngrams:

        probability = ngrams[ngram] / total
        ngrams[ngram] = math.log10(probability)

    return ngrams


def clean_text(text):

    result = ""

    for char in text.upper():

        if char >= "A" and char <= "Z":
            result += char

    return result


def score_ngrams(text, ngrams, size):

    text = clean_text(text)

    score = 0

    for i in range(len(text) - size + 1):

        ngram = text[i:i + size]

        if ngram in ngrams:
            score += ngrams[ngram]

        else:
            score -= 10

    return score


def score_text(text, trigrams, quadgrams):

    trigram_score = score_ngrams(
        text,
        trigrams,
        3
    )

    quadgram_score = score_ngrams(
        text,
        quadgrams,
        4
    )

    # Les quadgrams sont plus précis,
    # donc on leur donne plus de poids.

    return (
        0.3 * trigram_score
        + 0.7 * quadgram_score
    )