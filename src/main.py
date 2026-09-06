import sys

from cipher import encrypt, decrypt, random_key
# from scorer import load_quadgrams, score_text
from scorer import load_ngrams, score_text
from cracker import crack


def print_title():

    print()
    print("=" * 50)
    print("       SUBSTITUTION CIPHER CRACKER")
    print("=" * 50)
    print("||                                              ||")


def encrypt_message():
    
    message = input("|| Message to encrypt: ")
    print("||                                              ||")

    key = random_key()

    encrypted = encrypt(message, key)

    print("||                                              ||")
    print("|| Encrypted message:                           ||")
    print("||", encrypted)

    print("||                                              ||")
    print("|| Key:                                         ||")
    print("||", key,"                  ||" )
    print("|| ABCDEFGHIJKLMNOPQRSTUVWXYZ                   ||")
    print("||                                              ||")
    print("=" * 50)


def decrypt_message():

    print("|| Paste the encrypted message.                 ||")
    print("|| Press ENTER on an empty line when finished.  ||")
    print("||                                              ||")
    print()

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    ciphertext = " ".join(lines)

    if len(ciphertext) < 20:

        print()
        print("The message is probably too short.")
        print("Try using a longer text.")
        return

    print()
    print("Loading language statistics...")

    trigrams = load_ngrams(
        "data/english_trigrams.txt"
    )

    quadgrams = load_ngrams(
        "data/english_quadgrams.txt"
    )
    
    print("Number of trigrams:", len(trigrams))
    print("Number of quadgrams:", len(quadgrams))

    print(
        "Test score:",
        score_text(
            "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG and eat his food",
            trigrams,
            quadgrams
        )
    )

    print("Starting cryptanalysis...")
    print()

    key, score = crack(ciphertext,trigrams,quadgrams,iterations=20000,restarts=20)

    plaintext = decrypt(ciphertext, key)

    print()
    print("=" * 50)
    print("RESULT")
    print("=" * 50)

    print()
    print("Recovered key:")
    print(key)

    print()
    print("Score:")
    print(round(score, 2))

    print()
    print("Decrypted message:")
    print()

    print(plaintext)

    print()
    print("=" * 50)


def main():

    while True:

        print_title()
        print("||    1 - Encrypt a message                     ||")
        print("||    2 - Decrypt a message                     ||")
        print("||    3 - Quit                                  ||")

        print("||                                              ||")

        choice = input("|| Choice:"   )  
        print("||                                              ||")
        if choice == "1":

            encrypt_message()

        elif choice == "2":

            decrypt_message()

        elif choice == "3":

            print("Goodbye.")
            sys.exit()

        else:

            print("Unknown option.")


if __name__ == "__main__":
    main()