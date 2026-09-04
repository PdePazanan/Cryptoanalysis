# from collections import Counter


# def clean_text(text):

#     result = ""

#     for char in text.upper():

#         if char >= "A" and char <= "Z":
#             result += char

#     return result


# def create_quadgrams(text):

#     quadgrams = Counter()

#     for i in range(len(text) - 3):

#         quadgram = text[i:i + 4]
#         quadgrams[quadgram] += 1

#     return quadgrams


# with open("data/corpus.txt", "r", encoding="utf-8") as file:

#     text = file.read()


# text = clean_text(text)

# quadgrams = create_quadgrams(text)


# with open("data/quadgrams.txt", "w") as file:

#     for quadgram, count in quadgrams.most_common():

#         file.write(f"{quadgram} {count}\n")


# print("Quadgrams created.")
# print("Number of different quadgrams:", len(quadgrams))




from collections import Counter


def clean_text(text):

    result = ""

    for char in text.upper():

        if char >= "A" and char <= "Z":
            result += char

    return result


with open("data/corpus.txt", "r", encoding="utf-8") as file:

    text = clean_text(file.read())


trigrams = Counter()
quadgrams = Counter()


for i in range(len(text) - 2):

    trigram = text[i:i + 3]
    trigrams[trigram] += 1


for i in range(len(text) - 3):

    quadgram = text[i:i + 4]
    quadgrams[quadgram] += 1


with open("data/trigrams.txt", "w", encoding="utf-8") as file:

    for ngram, count in trigrams.most_common():

        file.write(f"{ngram} {count}\n")


with open("data/quadgrams.txt", "w", encoding="utf-8") as file:

    for ngram, count in quadgrams.most_common():

        file.write(f"{ngram} {count}\n")


print("N-grams created.")
print("Different trigrams:", len(trigrams))
print("Different quadgrams:", len(quadgrams))