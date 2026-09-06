# Cryptoanalysis

## Introduction

Implémentation d'un algorithme de cryptanalyse sans connaissance préalable de la clé, basé sur l'analyse de fréquences de quadgrammes et une recherche locale de type hill climbing / simulated annealing. 
Détection automatique de la langue et évaluation de la qualité des clés candidates.
Ce projet permet donc d'encrypter ou de décrypter un message sans en connaitre la clé


```text
Cryptoanalysis/
├── README.md
├── src/
│   ├── cipher.py
│   ├── scorer.py
│   ├── cracker.py
│   └── main.py
├── data/
    └── quadgrams.txt
```

## Premiers test

Nous avons tout d'abord utilisé la méthode hill climbing


<img width="1365" height="807" alt="image" src="https://github.com/user-attachments/assets/61ea70c3-1b43-4997-81c3-8cd1e7bf4401" />

Quand le texte est assez court, notre algorithme a du mal à decoder le message, ci dessous un exemple avec un texte bien plus long, une solution a été trouvé.


<img width="1910" height="874" alt="image" src="https://github.com/user-attachments/assets/26c43501-490a-44e3-ad8b-9c9ad3de0417" />



## Modifications pour amelioration du dechiffrement

Ainsi, lorsque nous avons un long message il n'y a pas de soucis mais pour un message plus court, il est plus compliqué de déchiffrer, nous allons donc utiliser une attaque par motif de mots (word pattern attack)







### Sources

Test de Kasiski
