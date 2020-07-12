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
Chaque fois que je suis amené à analyser des données, mon première reflexe et d'identifier un tableau de donnée dont chaque ligne est une observation et chaque colonne une propriété de l'observation. 
Par exemple le tableau suivant, represente la taille et le poid chez 10 individus. 

tableau

Il y a donc ici 10 observations et 2 propriétés quantitatives.
Un façon de visualiser ces données sur un graphique est de considéré chaque observations comme un point ( ou vecteur ) dans un espace défini par les 2 propriétés. On pourra alors identifier facilement deux groupes.

Graphique.

En rajoutant une troisième propriété dans notre tableau, nous pourions faire un graphique à 3 dimensions. Mais avec plus de propriété, et donc plus de dimensions, cela devient plus difficile. La solution à ce problème est la réduction de dimension en transformant par exemple un tableau à 100 colonnes vers un tableau à 2 colonnes. 
Pour comprendre comment çela fonctionne, partons d'un cas simple. La réduction de 2 dimensions à 1 dimensions. 

## Passage 2D à 1D 
Reprenons notre graphique à 2 dimensions et essayons de le réduire à 1 dimensions. Pour cela, nous pouvons tracer un axe passant au mieux par tous les points. Puis faire la projection des ces points sur cette axe. 
Cette axe ou composante, permet alors de representer les données sur un graphique à 1 dimension avec les deux groupes de points toujours visible. 

Graph 2D 1D 

Il y a cependant une perte d'information à prendre en compte comme l'illustre le graphique suivant. Plus les points sont corrélé entre eux, et plus l'information récupéré est grande. Gardez en tête qu'une réduction de dimension par PCA doit toujours être accompagné de la quantité d'information récupéré pour être interpretable.

Graph variance 


Une Analyse en composante principale c'est juste ça. Trouver les axes (ou composante principale) passants au mieux par l'ensemble des points. Dans notre cas, nous avons chercher un axe dans un espace 2D. Mais avec un peu d'abstraction de votre part, vous pouvez chercher 1,2 ou 3 axes passant au mieux parmis des points dans un espace à N dimensions. 
L'exemple classique suivant, est une réduction de dimension 4D en 2D obtenu à partir d'un tableau constitué de 100 observations et 4 propriété.


Chacun des deux composante (P1 et P2) represente un axe passant au mieux par l'ensemble des points dans l'espace à 4 dimensions. Ces 2 axes sont orthogonaux dans l'espace 4D et sont accompagné du pourcentage d'information récupéré. En effet, le premiere axe passe au mieux par les points puis le deuxième axes récupère l'information non récupéré par le premier. Si la somme des deux pourcentage est proche de 100%, c'est que l'information de vos données se résume très bien dans un espace 2D.

## Comprendre le calcul 
Pour les plus curieux, nous allons expliquer en détail comme trouver ces deux axes par le calcul avec un peu d'algèbre linéaire... ou plutôt de la géométrie. 

### Matrice de transformation
Précédement, nous avons vu qu'une observation peut être définit par un point ou vecteur dans un espace à N dimensions. Ce vecteur peut être déplacer ou plutôt transformer en le multipliant par une matrice NxN. 

vnouvea =  v * M 

En infographie, on utilise beaucoup ces matrices pour faire des transformations géométrique. Les figures suivante, vous montre les transformations usuel de 4 vecteurs après multiplication par une matrice. 

[ graph ]

### Matrice de covariance 
La variance d'une variable x , est la somme des écart à la moyenne au carré. 
La covariance c'est .... 

La matrice de covariance de notre tableau de donnée s'obtient en calculant toutes les covariances deux à deux . 

Que se passe t'il si nous utilisons cette matrice de covariance comme une matrice de transformation sur l'ensemble des points ? 
Je vous fait un programme : 

On obtient l'axe recherché ! 

### Vecteur propre et valeur propre 

Av = lamda v 
Sur l'animation précédente , quels sont les point qui ne bouge pas après transformation ? Ceux qui sont déjà sur l'axe ? 
Et bien les vecteurs propres d'une matrice de transformation sont les vecteurs qui ne bouge pas après transformation. Ces vecteurs définissent ainsi l'axe recherché. Quand à la valeur propre, il represente la norme du vecteur et correspond à la quantité d'information récupéré  . 

### Calcul 


### En python 
#### A la main 


#### Avec une sklearn 









## Autre application 
On peut faire autre chose, comme la compression 

## conclusion 
autres methodes 


