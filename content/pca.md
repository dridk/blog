Title: L'analyse en composante principale
Slug: lanalyse-en-composante-principale
Date: 2020-07-12 17:48:28
Modified: 2020-07-12 17:48:28
Tags: 
Category: informatique
Author: Sacha schutz
Status: Draft


L'analyse en composante principale ou PCA (e component analysis) est une méthode de réduction de dimension,largement utilisé en statistique descriptive pour representer sur un graphique à 2 ou 3 dimensions des données décrite sur plus de 3 dimensions. 
Dans ce billet, nous essayerons d'abord de comprendre le principe général avec l'exemple simple d'un passage de 2 dimensions à 1 dimensions. Les plus courageux pourront continuer à lire pour comprendre les mathématiques sous jacente et comment réaliser cette transformation en Python. 

## Tout commence avec un tableau
Chaque fois que je suis amené à analyser des données, mon première reflexe et d'identifier un tableau de donnée dont chaque ligne est une observation et chaque colonne une variable de l'observation. 
Par exemple le tableau suivant, represente la taille et le poid chez 10 individus. 

tableau

Il y a donc ici 10 observations et 2 variables quantitatives.
Un façon de visualiser ces données sur un graphique est de considéré chaque observations comme un point ( ou vecteur ) dans un espace défini par les 2 variables. On pourrait alors par exemple identifier deux groupes.

Graphique.

En rajoutant une troisième variable dans notre tableau, nous pourions faire un graphique à 3 dimensions. Mais avec plus de variables, et donc plus de dimensions, cela devient plus difficile. La solution à ce problème est la réduction de dimension en transformant par exemple un tableau à 100 variables vers un tableau à 2 ou 3 variables facillement representable graphiquement. 
Pour comprendre comment çela fonctionne, partons d'un cas simple. La réduction d'un tableau à  2 dimensions vers un tableau à 1 dimensions. 

## Passage 2D à 1D 
Reprenons notre graphique à 2 dimensions et essayons de le réduire à 1 dimensions. Pour cela, nous pouvons tracer un axe passant au mieux par tous les points. Puis faire la projection de chaque points sur cette axe. 
Cette axe ou composante, permet alors de representer les données sur un graphique à 1 dimension avec les deux groupes de points toujours visible. 

Graph 2D 1D 

Il y a cependant une perte d'information à prendre en compte comme l'illustre le graphique suivant. Plus les points sont corrélé entre eux, et plus l'information récupéré est grande. Gardez en tête qu'une réduction de dimension par PCA doit toujours être accompagné de la quantité d'information récupéré pour être interpretable.

Graph variance 


Une Analyse en composante principale c'est juste ça. Trouver les axes (ou composante principale) passants au mieux par l'ensemble des points. Dans notre cas, nous avons chercher un axe dans un espace 2D. Mais avec un peu d'abstraction de votre part, vous pouvez chercher 1,2 ou 3 axes passant au mieux parmis des points dans un espace à N dimensions. 
L'exemple classique suivant, est une réduction de dimension 4D en 2D obtenu à partir d'un tableau constitué de 100 observations et 4 propriété.


Chacun des deux composante (P1 et P2) represente un axe passant au mieux par l'ensemble des points dans l'espace à 4 dimensions. Ces 2 axes sont orthogonaux dans l'espace 4D et sont accompagné du pourcentage d'information récupéré. En effet, le premiere axe passe au mieux par les points puis le deuxième axes récupère l'information non récupéré par le premier. Si la somme des deux pourcentage est proche de 100%, c'est que l'information de vos données se résume très bien dans un espace 2D.

## Comprendre le calcul 
Pour les plus curieux, nous allons expliquer en détail comme trouver ces deux axes par le calcul à l'aide d'une interpretation géométrique.

### Matrice de covariance 
La variance d'une variable x, est la somme des écart à la moyenne au carré. 
Elle s'écrit : 
Variance = ... 

La covoariance entre deux variables indique la variance d'une variable x par rapport à une variable y. 

Covariance = ... 

Plus les variables x et y sont corrélé, plus la valeur absolu de la covariance est grande : 

shema ... 

La matrice de covariance de notre tableau de donnée s'obtient en calculant toutes les covariances des variables deux à deux . 

### Matrice de transformation
Précédement, nous avons vu qu'une observation dans le tableau de donnée peut être representé par un vecteur (ou un point) dans un espace à N dimensions. 
En multipliant ce vecteur par une matrice de dimension NxN, on obtient alors un nouveau vecteur. On peut s'imaginer cela comme la transformation (linéaire) d'un vecteur.

vnouvea =  v * M 

L'utilisation de ces matrices de transformation est largement utilisé en infographie pour réaliser des translations, des rotations et des redimensionnement d'object en 2 ou 3 dimensions. 

[ graph ]

Que se passe t'il si nous utilisons la matrice de covariance comme une matrice de transformation sur l'ensemble des points ? 

On obtient l'axe recherché ! 

Comment trouver cette axe par le calcul ?

### Vecteur propre et valeur propre 

Le vecteur propre d'une matrice de transformation est un vecteur qui ne change pas sa direction après transformation. Mais sa longueur (sa norme) peut changer d'un facteur indiqué par la valeur propre. 

 Ils sont défini par la relation suivante : 
Av = lamda v 

Par exemple, pour une matrice de transformation faisant une rotation, le vecteur propre est le centre de rotation. 
Avec la matrice de covariance, les vecteurs propres sont ceux correspondant aux axes recherchés et la valeur propre represente la quantité d'information récupéré par cette axe. 
Pour réaliser une analyse en composante principale, il faut donc trouver les vecteurs et valeurs propres de la matrice de covariance. C'est à dire résoudre l'equation suivante : 

Av = lamda v 
(A-lambdaI)x = 0

Je vous epargne la demonstration que vous pouvez retrouver ici. 
Essayons plutôt de faire notre PCA maison en python avec numpy

### PCA en Python

#### numpy


#### Avec sklearn

## Conclusion 
L'analyse en composante principale est une méthode parmi d'autre, de réduction de dimension. Il existe d'autre méthode avec chacune leurs avantage. Notaemmment les méthodes non linéaire comme t-SNE ou UMAP. 
sachez aussi que la PCA a d'autre application en informatique, notamment dans le traitement d'image et la réduction du bruit. En effet si vous faite une PCA puis si vous refaite l'inverse, alors vous supprimerez le bruit comme l'illustre l'image ci-dessous.

https://towardsdatascience.com/the-jewel-of-the-matrix-a-deep-dive-into-eigenvalues-eigenvectors-22f1c8da11fd

https://www.visiondummy.com/2014/04/geometric-interpretation-covariance-matrix/





## Autre application 
On peut faire autre chose, comme la compression 

## conclusion 
autres methodes 


