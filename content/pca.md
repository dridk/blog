Title: L'analyse en composante principale
Slug: lanalyse-en-composante-principale
Date: 2020-07-12 17:48:28
Modified: 2020-07-12 17:48:28
Tags: 
Category: informatique
Author: Sacha schutz
Status: Draft


L'analyse en composante principale ou PCA (e component analysis) est une méthode de réduction de dimension,largement utilisé en statistique descriptive pour visualiser sur un graphique à 2 ou 3 dimensions des données décrite sur plus de 3 dimensions. 
Dans ce billet, nous essayerons d'abord de comprendre le principe général avec l'exemple simple d'un passage de 2 dimensions à 1 dimensions. Les plus courageux pourront continuer à lire pour comprendre les mathématiques sous jacente et comment réaliser cette transformation en Python. 

## Tout commence avec un tableau
Chaque fois que je suis amené à analyser des données, mon première reflexe et d'identifier un tableau de donnée ou chaque ligne represente une observation et chaque colonne une variable décrivant l'observation.
Par exemple le tableau suivant, represente la taille et le poid chez 6 individus:

<div class="figure"><img src="../images/pca/table.png" /><div class="legend">
Tableau de données avec 6 observations et deux variables.
</div> 
</div>

Un façon de visualiser ces données sur un graphique est de considéré chaque observations comme un point ( ou vecteur ) dans un espace à deux dimensions décrivant les deux variables. On observe alors 2 groupes de points qui se ressemble. 


<div class="figure"><img src="../images/pca/2dplot.png" /><div class="legend">
Répresentation dans un espace à deux dimensions du tableau de données. Chaque observation est representé par un point.
Sont entouré, les groupes de points qui sont proche. 
De façon général, les M observations du tableau de données peuvent être vu comme des vecteurs dans un espace à N dimensions. L'ensemble formant une matrice de dimension NxM.
</div> 
</div>


En utilisant 3 variables, nous pourions faire un graphique à 3 dimensions. Mais avec plus de variable, et donc plus de dimensions cela devient problèmatique à répresenter.      
La solution à ce problème est la réduction de dimension en transformant par exemple un tableau à 100 variables vers un tableau à 2 ou 3 variables facillement representable graphiquement.   
Pour comprendre comment çela fonctionne, partons d'un cas simple. La réduction d'un tableau à  2 dimensions vers un tableau à 1 dimension. 

## Passage 2 dimensions à 1 dimension 
Reprenons notre graphique à 2 dimensions et essayons de le réduire à 1 dimensions. Pour cela, nous pouvons tracer un axe passant au mieux par tous les points. Puis faire la projection de chaque points sur cette axe. 
Cette axe ou composante principale, permet alors de representer les données sur un graphique à 1 dimension avec les deux groupes de points toujours visible.  

<div class="figure"><img src="../images/pca/pca2D.png" /><div class="legend">
Réduction de dimensions d'un espace à 2 dimensions vers in espace à 1 dimensions. 
L'information des 2 groupes de points est conservés. 
</div> 
</div>

Il y a cependant une perte d'information à prendre en compte comme l'illustre le graphique suivant. Plus les points sont corrélé entre eux, et plus l'information récupéré est grande. Gardez en tête qu'une réduction de dimension par PCA doit toujours être accompagné de la quantité d'information récupéré pour être interpretable.

<div class="figure"><img src="../images/pca/pca_information.png" /><div class="legend">
Réduction de dimensions d'un espace à 2 dimensions vers in espace à 1 dimensions. 
Dans les 3 exemples, la réduction de dimensions ammène aux même résultats. La différence est lié à la quantité d'information récupéré par la composante principale. Le premier graphique récupère que 40% de l'information tandisque la dernière récupère 90% de l'information.
</div> 
</div>

Une Analyse en composante principale c'est juste ça. Trouver les axes (ou composante principale) passants au mieux par l'ensemble des points. Dans notre cas, nous avons chercher un axe dans un espace 2D. Mais avec un peu d'abstraction de votre part, vous pouvez deviner qu'il est tout aussi possible de chercher 1,2 ou 3 axes passant au mieux parmis des points dans un espace à N dimensions. 
L'exemple suivant est obtenu à partir du j[eux de données iris](https://fr.wikipedia.org/wiki/Iris_de_Fisher) contenant 50 observations de fleurs et 4 variables. 

<div class="figure"><img src="../images/pca/iris.png" /><div class="legend">
Réduction d'un espace à 4 dimensions vers un espace à 2 dimensions.
</div> </div> 

Chacun des deux composante (P1 et P2) represente un axe passant au mieux par l'ensemble des points dans l'espace à 4 dimensions. Ces 2 axes sont orthogonaux dans l'espace 4D et sont accompagné du pourcentage d'information récupéré. En effet, le premiere axe passe au mieux par les points puis le deuxième axes récupère l'information non récupéré par le premier. Si la somme des deux pourcentage est proche de 100%, c'est que l'information de vos données se résume très bien dans un espace 2D.

## Comprendre le calcul 
Pour les plus curieux, nous allons expliquer en détail comme trouver ces deux axes par le calcul à l'aide d'une interpretation géométrique.

### Transformation linéaire

En multipliant un vecteur (un point) par une matrice on obtient un nouveau vecteur. Autrement dit, on déplace le point vers un autre endroit. 

equation
v' = v * M

Des matrices particulière, appelé matrice de transformation, sont largement utilisé en infographie pour réaliser des translations, des rotations ou des redimensionnement en 2 ou en 3 dimensions. 
Par exemple, dans le cas ci-dessous, les 4 vecteurs définissant le carré sont transformé par la matrice de transformation M . Je vous invite à tester en ligne les differences transformation possible. 

### Vecteur propre et valeur propre 

Le vecteur propre d'une matrice de transformation est un vecteur qui ne change pas sa direction après transformation. Quand à la valeur propre, elle indique le facteur d'elongation de ce vecteur après transformation. 
Dans l'exemple, ci-dessus, la transformation à 2 deux vecteurs propres ... 

<center>Pour trouver les vecteurs et valeurs propres de la matrice A:</center>

$$ A = \begin{bmatrix}
a & b \\ 
c & d 
\end{bmatrix}
$$

<center>Il faut donc résoudre l'equation suivante</center>

$$A\vec{v} = \lambda \vec{v}$$

<center>Ce qui revient à résoudre : </center>

$$(A-\lambda I) \vec{v} = \vec{0}$$

<center>Cette equation admet des solution(s) $\lambda$ si :</center> 

$$det(A-\lambda I) = 0 $$

<center>C'est à dire : </center>
$$ det (\begin{bmatrix}
a - \lambda & b \\ 
c & d - \lambda
\end{bmatrix}) = 0
$$

<center>Pour trouver $\lambda$ Il suffit donc de résoudre : </center>

$$
(a - \lambda)(c - \lambda) - bc = 0
$$

En remplacant lambda dans l'equation d'origine, ou trouve alors les vecteurs propres associés. 

### Matrice de covariance 
**La variance** d'une variable x, informe de la dispersion des données autour de la moyenne. C'est la moyenne de tous les écarts à la moyenne.
Elle s'écrit : 

$$var(x) = \frac{1}{N} \sum_{i=0}^{n} (x-\bar{x})^{2}$$

Dans notre tableau, la variance de la taille et du poids sont respectivement de 328.5 et 238.

**La covoariance** entre deux variables indique la variance d'une variable x par rapport à une variable y. Elle indique le dégrés de corrélation entre deux variable. Elle s'écrit :

$$cov(x,y) = \frac{1}{N} \sum_{i=0}^{n} (x_i - \bar{x})(y_i - \bar{y})$$

Plus les variables x et y sont corrélé, plus la valeur absolu de la covariance est grande : 

<div class="figure"><img src="../images/pca/cov.png" /><div class="legend">

</div> </div> 

**La matrice de covariance** est une matrice carré contenant l'ensemble des covariance entre variable pris 2 à 2. 

$$M = \begin{bmatrix}
cov(x,x) & cov(x,y) \\ 
cov(y,x) & cov(y,y) 
\end{bmatrix}$$

Avec notre tableau des 6 individus et 2 variables, nous obtenons : 

<div class="figure"><img src="../images/pca/cov_df.png" /><div class="legend">
</div> </div> 



### Trouver les axes 

Les vecteurs propres de la matrice de covariance sont les axes recherches. 
La valeurs propre indique la quantité d'information récupéré. 

array([528.89387928,  37.67278739])

array([[ 0.76953573, -0.63860376],
       [ 0.63860376,  0.76953573]])

### Projection des vecteurs sur les axes 

Il suffit maintenant de projeter les points sur le vecteur choisi à l'aide de l'equation suivante : ...



## En Python 

### avec numpy 

#### Avec sklearn




## Conclusion 
L'analyse en composante principale est une méthode parmi d'autre, de réduction de dimension. Il existe d'autre méthode avec chacune leurs avantage. Notaemmment les méthodes non linéaire comme t-SNE ou UMAP. 
sachez aussi que la PCA a d'autre application en informatique, notamment dans le traitement d'image et la réduction du bruit. En effet si vous faite une PCA puis si vous refaite l'inverse, alors vous supprimerez le bruit comme l'illustre l'image ci-dessous.

https://towardsdatascience.com/the-jewel-of-the-matrix-a-deep-dive-into-eigenvalues-eigenvectors-22f1c8da11fd

https://www.visiondummy.com/2014/04/geometric-interpretation-covariance-matrix/


https://medium.com/@kyasar.mail/pca-principal-component-analysis-729068e28ec8


## Autre application 
On peut faire autre chose, comme la compression 

## conclusion 
autres methodes 


