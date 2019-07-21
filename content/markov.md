Title: Les chaines de Markov
Slug: chaine-de-markov
Date: 2019-03-17 18:53:39
Modified: 2019-06-07 12:18:36
Tags: statistique,maths,café
Category:informatique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/stat_banner.jpg

Les chaines de Markov sont très populaire en bioinformatique pour l'analyse de séquences d'ADN. Vous en avez peut être déjà entendu parlé dans une de ses formes particulières : Les chaines de Markov caché ou HMM. Ces chaines sont des algorithmes pouvant générer des séquences (par exemple: A,C,C,G,T...) dont la probabilité d'apparition de chaque symbole depend uniquement du symbole précédent. Je me represente souvent une chaine de Markov comme une machine générant des symboles aléatoires (variable aléatoire) que l'on peut régler avec differents boutons pour ajuster la fréquence d'apparition des différents symboles. 
Dans ce billet, nous alons donc voir le fonctionnement des chaines de markov en utilisant l'ADN comme support et nous finirons par un exemple pratique en python. 

## Un dé à 4 faces

Imaginez un dé à 4 face sur lesquelles sont representé chaque base de l'ADN : A,C,G,T. Lancez ce dé plusieurs fois en notant chaque résultat.
Par exemple, au premier lancé, vous obtenez un A, au deuxième un T, au troisème un A, et ainsi de suite pour générer une longue séquence.
Si le dé n'est pas truqué, à chaque lancé, vous avez exactement une chance sur 4 d'obtenir chaques bases. Plus précisément, le résultat d'un lancé est indépendant des résultats précédants. La probabilité d'obtenir un A au 5ème lancé sera toujours de 1/4 peut importe les autres lancé.    
Une façon de representer ce tirage aléatoire est d'utiliser un graphe ou chaque noeuds represente les symboles ou état et les arrêtes les probabilités de transitions. Dans la figure ci-dessous, il y a 4 états (A,C,G,T) et 16 transitions toutes égal à 1 chance sur 4. Par exemple la probabilité d'obtenir un A suivi d'un C est de 0.25. un T suivi d'un autre T est de 0.25.
Pour générer une séquence, il suffit de partir d'un état au hasard, puis de faire une marche dans ce graphe en suivant les probabilité de transition et en notant les valeurs de chaques noeuds traversé. Le prochain noeuds à traverser dependra uniquement du noeud ou vous êtes. Vous lirez souvent que le futur depend uniquement du présent, jamais du passé. Une chaine de Markov ce n'est rien de plus que ça. 

<div class="figure">     <img src="../images/markov/markov1.png" />      <div class="legend">Chaine de Markov. Il y a 4 états (A,C,G,T) et 4x4=16 transitions possible toutes avec une probabilité de 1/4</div> </div>   



## Les paramètre chaine de Markov
Une chaine de Markov se défini donc par un nombre d'état E et une matrice de Transition T. Dans notre example, il y a 4 états (A,C,G,T) et 16 transitions toutes égales à 0.25 que l'on peut representer par une matrice 4x4. 
L'implementation en python peut s'écrire facilement en python ave numpy: 

```python
import numpy as np

def markov_chain(states , transitions, size = 10):
    """ generateur de Markov
        
        states (ndim=1): Liste des états possible ["A","C","G",T] 
        transitions (ndim=2): Matrice des transitions possibles 
     """ 
    
    # On verifie bien que les dimensions de la matrice de transitions 
    # correspondent à la dimensions de states 
    if states.shape * 2 != transitions.shape:
        raise AttributeError("La matrix transition n'est pas compatible avec states")
    
    # On choisi au hasard le premier symbole 
    current  = np.random.choice(states)

    for _ in range(size):
        # On récupère la position du symbole
        current_index = int(np.where(states == current)[0])
        # On récupère les transitions possible pour le symbole en cours
        current_transition = transitions[current_index]
        # On choisi au au hasard le prochain état en respectant les probabilités de transitions
        current = np.random.choice(states, p = current_transition)
        
        yield current


states = np.array(["A","C","G","T"])


transitions = np.array([
#      A     C    G     T
    [0.25, 0.25, 0.25, 0.25],  #A  
    [0.25, 0.25, 0.25, 0.25],  #C
    [0.25, 0.25, 0.25, 0.25],  #G
    [0.25, 0.25, 0.25, 0.25],  #T
])

print("".join(list(markov_chain(states, transitions, 50)))) 
# OUTPUT : CGGAGTAATAACTGCCATTTGAAGTCCGCATAGCAAGCTTGCAACGTTTA


transitions = np.array([
#      A     C    G     T
    [0.25, 0.25, 0.25, 0.25],  #A  
    [0.25, 0.25, 0.25, 0.25],  #C
    [0.01, 0.97, 0.01, 0.01],  #G
    [0.25, 0.25, 0.25, 0.25],  #T
])

# OUTPUT : GCATTCGCGCCTGCAAGCTCGCTCCGCCCATAGCGCGCCTATAGCCCAAG
```

En utilisant la même probabilité de 0.25 partout, on peut générer des séquence qui s'approche d'une distribution uniforme. Mais rien ne vous empeche maintenant de générer des séquences avec des distributions différentes. Il vous suffit de changer les probabilités de transition. Si vous voulez par exemple un générateur de séquence riche en GC, il suffit de mettre une plus grande probabilité pour la transition G donne C. 


## Apprentissage 
Si maintenant, au lieux de générer des séquences à partir d'une chaine de Markov nous faisions l'inverse. C'est à dire générer une chaine de Markov en observant des séquences. Il suffit de compter toutes les transitions possible d'une jeux de séquence pour en déduire le modèle ou profil.
En python cela peut s'écrire: 

```python
from itertools import product
from collections import Counter

def learn_transition(sequences):
    # Initilisation de la matrice de transition ( 4 * 4 )
    transitions = np.zeros(16).reshape(4,4)
    
    # pour faire le mapping entre les symboles et leurs positions dans la matrice
    base_maped = {"A":0, "C":1, "G":2,"T":3}

    # On parcours toutes les sequences
    for seq in sequences:
        # On parcours la séquence par 2 symboles
        for i in range(0,len(seq)-2):
            # On récupere la transition. ex: ["G","C"]
            transition = list(seq[i:i+2])
            # On récupère les coordonnées de la transition
            coord = tuple(map(base_maped.get, transition))
            # On incrémente cette transition 
            transitions[coord] += 1

    # On normalise la matrice pour avoir des probabilités 
    row_sums = transitions.sum(axis=1)
    transitions = np.divide(transitions,row_sums[:,np.newaxis])

    return transitions

# Attention à bien mettre tous les états (A,C,G,T) 
# Il y a bien 1 et 1 C 

seqs = [
"ATATCATATATATTTAT",
"ATATATATATATTTTAT",
"ATATATATATATTTTAT",
"ATATATATAGTATTTAT",
"ATATATATATAATTTAT"
]

transitions = learn_transition(seqs)
# on peut générer alors une séquence à partir de cette famille
print("".join(list(markov_chain(states, transitions, 17)))) 
# OUTPUT : TATATATATATTTATTA


```


## Prediction
Il est alors possible de calculer la probabilité pour qu'une nouvelle séquence appartiennent à ce modèle. Par exemple quel est la probabilité que la séquence ATTCG soit générer par une chaine de Markov connaissant sa matrice de transition $\theta$?
Etant donnée que la probabilité d'apparition d'un symbole depend uniquement du précédement, la probabilité peut s'écrire comme le produit de chaque transition: 
$$
p(ATTCG|\theta) = p(A) * p(T|A) * p(T|A) * p(T|T) * p(C|T) * p(G|C)
$$

Ou plus généralement : 

$$
P(S|\theta) = \prod_{0}^{n} p(S_{n}|S_{n-1}) 
$$

Et comme on préfère faire des additions que des multiplications, on préfère calculer la vraissemblance : 

$$
L_{\theta}(S) = \sum_{0}^{n} log(p(S_{n}|S_{n-1})) 
$$

## Convergence vers une distribution
Interessons nous maintenant à la distribution statistique des symboles sur le long terme. C'est à dire la fréquence d'apparition de chaque symbole après avoir générer une longue séquence. 


## Chaine de markov cachée
Une chaine de markov cachée est simplement une chaine de Markov ou certain des états sont caché. Plus préscisement ce sont des états autres que ceux présent dans la séquence. Reprenons notre dé et ajoutons un deuxième dé truqué contenant uniquement des G sur ces 4 faces. On lance toujours un seul dé pour générer une séquence. sauf que cette fois, à chaque lancé, il y a une chance sur 2 que nous changions de dé. La chaine de Markov peut être representé ainsi. 

<div class="figure">     <img src="../images/markov/hidden_markov.png" />      <div class="legend">Chaine de Markov</div> </div>   

Comme précédement, il est interessant de construire une chaine de Markov en apprenant à partir d'un jeux de séquence. Mais cette fois, les probabilités de transitionss cachés sont beaucoup plus difficile à calculé car non observé. 
On peut les estimer en cherchant les valeurs les plus vraissemblance. l'algorithme de xxx permet de résoudre ce problème. Il s'agit d'un algorithme d'esperance maximisation que nous avons déjà vu dans un autre billet. Notez aussi l'algorthme de Viterbi qui permet de générer une séquence caché...


# Représentation algébrique
Une chaine de Markov peut être défini par un vecteur d'état (A,C,G,T) et une matrice de transition M = [AA,AT,....]. 
L'interet d'un tel representation c'est de pouvoir calculer facilement la probabilité qu'une séquence soit générer par la chaine de Markov. 
Prenons la séquence = ACGTTT.
l'état 1 correspond au vecteur [1,0,0,0]. La probabilité des état 2 correspond au produit du vecteur d'état par la matrice de transition. très pratique !

## Propriété d'une chaine de Markov 




### Référence 
- [Super vidéo d'Aurélien Géron (en)](https://www.youtube.com/watch?v=ErfnhcEV1O8)
- [Une autre super vidéo (en)](https://www.youtube.com/watch?v=R4OlXb9aTvQ)
- [La théorie de l'information: L'origine de l'entropie](http://www.yann-ollivier.org/entropie/entropie1)

### Merci 
[@andhena](https://github.com/andhena)