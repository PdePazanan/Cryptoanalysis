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
│   └── quadgrams.txt
└── examples/
    └── encrypted.txt
```

## Premiers test

Nous avons tout d'abord utilisé la méthode hill climbing


<img width="1365" height="807" alt="image" src="https://github.com/user-attachments/assets/61ea70c3-1b43-4997-81c3-8cd1e7bf4401" />


### Sources

Test de Kasiski
