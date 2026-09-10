# Cryptoanalysis

## Introduction

Implémentation d'un algorithme de cryptanalyse sans connaissance préalable de la clé, basé sur l'analyse de fréquences de quadgrammes et une recherche locale de type hill climbing / simulated annealing. 
Ce projet permet donc d'encrypter ou de décrypter un message sans en connaitre la clé. Il y a 26 lettres dans l'alphabet, il existe donc 26! ≈ 4×10²⁶ clés possibles.


Ofobi wybxsxq, dro aesod dygx gkuoc loxokdr k zkvo cui. Lsbnc mbycc dro byypdyzc, grsvo zoyzvo rebbi dygkbn gybu, cmryyv, kxn cwkvv knfoxdeboc. Sx dro moxdbkv zkbu, mrsvnbox vkeqr locsno yvn dbooc, kxn k lkuob yzoxc rsc gkbw cryz xokb dro caekbo. Loiyxn dro ryecoc, qboox rsvvc cebbyexn dro dygx vsuo k qoxdvo gkvv. Xylyni uxygc grkd dro xog nki gsvv lbsxq, led ofobiyxo mkbbsoc k vsddvo ryzo


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


## Fonctionnement 

Notre fichier scorer.py va mesurer la vraisemblance du texte déchiffré avec un vrai texte anglais, pour chercher intelligemment et non juste pas force brut.

### Quadrams

En comptant les quadrigrammes sur un immense corpus de texte anglais réel, on obtient une distribution de probabilité : "TION" est fréquent, "QXZK" n'existe quasiment jamais. load_ngrams charge ces fréquences et les convertit en log-probabilités. Ensuite, score_ngrams parcourt le texte déchiffré fenêtre par fenêtre

### Hill Climbing

Nous allons utiliser le hill climbing, pour dechiffrer un code, voici le fonctionnement :
1- Initialement on part avec une clé aléatoire, déchiffrer, noter le score.
2- Échanger deux lettres de la clé au hasard (change_key), redéchiffrer, renoter.
3- Si le nouveau score est meilleur, garder cette clé (hill-climbing)
4- Risque : rester bloqué sur un "sommet local" (clé imparfaite mais le score ne s'ameliore pas). Solution : Recul simulé, accepte un score moins bon Pour s'en échapper,ça permet de sortir des pièges locaux en début de recherche, puis de se stabiliser en fin de recherche.
5- Les restarts relancent tout le processus depuis plusieurs clés aléatoires différentes, et on garde la meilleure trouvée sur l'ensemble — utile car un seul run peut malgré tout se retrouver bloqué.

### Limite de cette méthode

Le scoring par n-grams est une méthode statistique et demande donc beaucoup de données. Pour un texte court, il sera bien plus difficile de le déchiffrer. Pour cela une méthode utile peut etre le solveur par pattern : 2 mots chiffrés identiques doivent correspondre au même mot. En comparant la structure de répétition des lettres de chaque mot chiffré à un dictionnaire anglais, puis en résolvant les contraintes de cohérence lettre-à-lettre entre tous les mots simultanément (backtracking), on retrouve la clé même avec très peu de texte — c'est même le cas où cette méthode brille le plus, à l'inverse du scoring statistique.





## Test


<img width="1365" height="807" alt="image" src="https://github.com/user-attachments/assets/61ea70c3-1b43-4997-81c3-8cd1e7bf4401" />

Quand le texte est assez court, notre algorithme a du mal à decoder le message, ci dessous un exemple avec un texte bien plus long, une solution a été trouvé.


<img width="1910" height="874" alt="image" src="https://github.com/user-attachments/assets/26c43501-490a-44e3-ad8b-9c9ad3de0417" />



