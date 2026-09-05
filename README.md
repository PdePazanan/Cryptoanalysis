# Cryptoanalysis

Implémentation d'un algorithme de cryptanalyse sans connaissance préalable de la clé, basé sur l'analyse de fréquences de quadgrammes et une recherche locale de type hill climbing / simulated annealing. Détection automatique de la langue et évaluation de la qualité des clés candidates.

Ce projet permet d'encrypter ou de décrypter un message



substitution-cipher-cracker/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── cipher.py
│   ├── scorer.py
│   ├── cracker.py
│   └── main.py
│
├── data/
│   └── quadgrams.txt
│
└── examples/
    └── encrypted.txt


## Premiers test

Nous avons tout d'abord utilisé la méthode hill climbing

    
### Sources

Test de Kasiski
