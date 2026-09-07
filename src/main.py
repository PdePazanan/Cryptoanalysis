import sys

from cipher import encrypt, decrypt, random_key
from scorer import clean_words, load_ngrams, score_text
from cracker import crack
from pattern_solver import load_wordlist, solve_word_patterns, mapping_to_key
from cracker import crack, refine_from_key


def print_title():

    print()
    print("=" * 60)
    print("            SUBSTITUTION CIPHER CRACKER")
    print("=" * 60)
    print("||                                                        ||")


def encrypt_message():
    
    message = input("|| Message à encrypter: ")
    print("||                                                        ||")

    key = random_key()

    encrypted = encrypt(message, key)

    print("||                                                        ||")
    print("|| message encrypté:                                      ||")
    print("||", encrypted)

    print("||                                                        ||")
    print("|| Key:                                                   ||")
    print("||", key,"                            ||" )
    print("|| ABCDEFGHIJKLMNOPQRSTUVWXYZ                             ||")
    print("||                                                        ||")
    print("=" * 60)


def decrypt_message():

    print("|| Collez le message encrypté.                            ||")
    print("|| Appuyez sur ENTER quand vous avez terminé.             ||")
    print("||                                                        ||")
    print()

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    ciphertext = " ".join(lines)

    # if len(ciphertext) < 20:

    #     print()
    #     print("The message is probably too short.")
    #     print("Try using a longer text.")
    #     return

    print("||                                                         ||")
    print("|| chargement des statistiques linguistiques...            ||")

    trigrams = load_ngrams(
        "data/english_trigrams.txt"
    )

    quadgrams = load_ngrams(
        "data/english_quadgrams.txt"
    )
    
    print("|| Nombres de trigrams:", len(trigrams), "                             ||")
    print("|| Nombres de quadgrams:", len(quadgrams), "                           ||")

    print( "|| Test score:",score_text("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG and eat his food",trigrams,quadgrams),"                       ||")
    
    word_count = len(clean_words(ciphertext))
    print(f"Nombre de mots détectés : {word_count}")
    
    if word_count <35:
    
        print("Tentative par motifs de mots (dictionnaire)...")
        
        wordlist = load_wordlist("data/words.txt")
        solutions = solve_word_patterns(ciphertext, wordlist)
        
        if solutions:
            print(f"{len(solutions)} solution(s) trouvée(s) par motifs.")
            print("Affinage de chaque solution par recuit simulé...")

            best_key = None
            best_score = -float("inf")

            for i, mapping in enumerate(solutions):
                candidate_key = mapping_to_key(mapping)

                # on part de cette clé (déjà partiellement correcte)
                # au lieu d'une clé 100% aléatoire, pour finir le travail
                refined_key, refined_score = refine_from_key(
                    ciphertext, candidate_key, trigrams, quadgrams, iterations=3000
                )

                print(f"  Candidat {i + 1}/{len(solutions)} affiné — score: {round(refined_score, 2)}")

                if refined_score > best_score:
                    best_score = refined_score
                    best_key = refined_key

            plaintext = decrypt(ciphertext, best_key)

            print()
            print("=" * 50)
            print("RESULT (motifs de mots + affinage)")
            print("=" * 50)
            print()
            print("Recovered key:")
            print(best_key)
            print()
            print("Score:")
            print(round(best_score, 2))
            print()
            print("Decrypted message:")
            print()
            print(plaintext)
            print()
            print("=" * 50)
            return

    else :
        print("Assez de mots, recherche statistique par trigrams et quadgrams...")
        

        print("|| Starting cryptanalysis...                                        ||")
        print("||                                                                  ||")

        key, score = crack(ciphertext,trigrams,quadgrams,iterations=20000,restarts=15)

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
        print("||    1 - Encrypter un message                            ||")
        print("||    2 - Decrypter un message                            ||")
        print("||    3 - Quitter                                         ||")

        print("||                                                        ||")

        choice = input("|| Choice:"   )  
        print("||                                                        ||")
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