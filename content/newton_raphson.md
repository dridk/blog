Title: L'algorithme de Newton-Raphson
Slug: newton-raphson
Date: 2018-10-21 12:32:39
Modified: 2018-10-21 12:32:39
Tags: algorithme, machine learning
Category: informatique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/ia_banner.jpg

La méthode de de Newton-Raphson est une méthode algorithmique pour trouver la racine d'une fonction. C'est à dire trouver x tel que f(x) = 0. Cette méthode est d'une simplicité déconcernante et n'importe qui à l'aide d'un crayon et d'une règle pourrait reproduire l'algorithme sur une feuille de papier. 
Dans ce billet, nous verons comment réaliser cette algorithme de façon géométrique puis algorithmique. Puis pour faire suite au billet précédent sur la descente en gradient, nous verrons comment utiliser la méthode de Newton-raphson dans une regression linéaire.

## Trouver la racine d'une fonction cubique

Prenons une fonction cubique, par exemple $f(x) = x^3  +3$  et traçon la courbe sur un repère cartésien.

<div class="figure">
    <img src="../images/newton_raphson/cubic.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses au point rouge. Nous voulons trouver les coordonnées de ce point par une méthode algorithmique</div> </div>   

La méthode de Newton-Raphson nous permet de trouver le point x de la courbe tel que f(x) = 0. C'est à dire le point de la courbe qui coupe l'axe des abcisses. Bien sur, nous pourrions simplement résoudre l'équation et trouver x. Mais parfois, les fonctions sont plus complexe et il n'existe aucune solution analytique. La méthode de Newton-Raphson nous permet d'y remédier de par un algorithme itératif décrit ci-dessous:

### Representation géométrique 
Choissisons un point au hasard A sur l'axe des abcsisses. 
Par exemple A=(2.5, 0).

<div class="figure">
    <img src="../images/newton_raphson/test0-1.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>   


Puis trouvons le point A' comme étant la projection de A par la fonction cubique. C'est à dire le point A'=(2.5, f(2.5)).

<div class="figure">
    <img src="../images/newton_raphson/test0-2.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>   


Enfin, traçons la tangente de la courbe au point A'. Cette tangente est une droite qui couple l'axe des abscisses au point B.

<div class="figure">
    <img src="../images/newton_raphson/test0-3.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>   

A partir du point B, il suffit de recommencer les même étape qu'avec le point A. Chercher B', tracer la tangente en B' puis trouver le point C et ainsi de suite... Vous verez alors rapidement, qu'en 7 itéartions, les points convergent vers la racine (autour de -1.44) comme illustré dans l'animation ci-dessous: 

<div class="figure">
    <img src="../images/newton_raphson/anim.gif" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>  

### Representation algébrique 
Maintenant que vous visualisez comment trouver la racine d'une fonction en utilisant la méthode de Newton-Raphson, voyons comme la calculer. Quelque notion de math vu au lycée suffirons:

#### Equation de la tangente au point A'
La tangente en un point d'une fonction f(x) ayant pour dérivé f'(x) est une droite d'équation $y=f'(a)(x-a) + f(a)$ avec «a» les coordonnées de A sur l'axe des abscisses. Dans notre cas, l'équation de la tangente au point A' se calcul donc comme ceci:

<center> <em> Notre fonction a pour équation: </em> </center>
$$f(x) = x^3 + 3$$
<center> <em> Sa derivé est donc: </em> </center>
$$f'(x) = 3x^2$$
<center> <em> La tagente au point A' (a=2.5) a donc pour equation: </em> </center>
$$
y=f'(A)(x-A) + f(A)\\
y=3A^2(x-A) + A^3 + 3\\
y=18,75x - 28,25\\
$$

#### Coordonnée du point B en fonction du point A
Connaissant l'équation de la tangente, les coordonnées du point B ou la tangente coupe l'axe des abscisses se calcul comment étant la résolution de l'équation linéaire $18,75x - 28,25=0$. Soit $x=28,25/18,75≈1,506$. Les coordonnées du point B sont donc (1.506,0).   
En reprenant nos formules vu plus haut, nous pouvons directement trouver une formule  pour calculer le point B(b,0) en fonction du point A(a,0). En effet, résoudre l'équation linéaire revient à faire:

$$f'(a)(b-a) + f(a) = 0\\$$
$$f'(a)(b-a) = -f(a)\\$$
$$(b-a) = \frac{-f(a)}{f'(a)}\\$$
$$b=a - \frac{f(a)}{f'(a)}$$

<center> <em> D'une manière générale, un point s'exprime en fonction du précédant par la formule suivante </em> </center>
$$x_{k+1} = x - \frac{f(x)}{f'(x)}\\$$


### En python 

En implémentant la méthode de Newton-Raphson en python, cela donne qqch comme ça:

```python
# Fonction cubique
def f(x):
    return x**3 + 3

# Derivé de la fonction cubique
def df(x):
    return 3*x**2

# Trouver la racine 
def racine(fct, derivate, iteration):
    a = 2.5 # On part d'un point aléatoire
    # On applique la formule sur plusieurs itérations
    for i in range(iteration):
        a = a - fct(a)/derivate(a)
        print(a)

# Sur 10 itérations 
racine(f,df,10)
# output
# 1.5066666666666668
# 0.5639244350466844
# -2.7685979807840897
# -1.9761928373643123
# -1.5735216658126505
# -1.4528964881677187
# -1.4423274010169043
# -1.4422495745072248
# -1.4422495703074085
# -1.4422495703074083

```

## Une régression linéaire 

Reprenons l'exemple d'une regression linéaire dont j'ai parlé dans le précédent billet. Nous avons le poid en fonction de la taille. L'objectif est de trouver la meilleur paramètre «a» de la droite d'équation y = ax pouvant expliquer la distribution de ces points.

<div class="figure">
    <img src="../images/gradient_descendant/observation.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div> 

Nous avions défini une fonction objective comme étant la somme des différente entre la points obsérvés et les points prédits par la droite de regression paramétré par «a». La meilleur valeur de «a» est celle ou la fonction objective est minimum. Plus exactement, c'est la valeur pour laquel la dérivé (ou la pente) de la fonction objective est nul. 

<div class="figure">
    <img src="../images/gradient_descendant/derivate.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>  

#### Méthode géométrique
En résumé, il faut chercher x tel que f'(x) = 0. Et c'est exactement ce que l'algorithme de Newton-Raphson sait faire. Tracons d'abord la fonction objective (bleue) et sa dérivé (orange) dont nous avions calculer les équations dans le précédent billet.

<center> <em> La fonction objective a pour équation </em> </center>
$$ f(a) = \frac{1}{n}\sum_{i=0}^{n}(-2y_{i}ax_{i} + a^{2}x_{i}^{2} ) $$ 

<center> <em> Sa dérivé a pour équation </em> </center>
$$ f'(a) = \frac{-2}{n}\sum_{i=0}^{n}(x_{i}(y_{i} - ax_{i})  $$ 

Appliquons alors l'algorithme de Newton-raphson. Prenons au hasard un point A, puis trouvons le point A' sur la dérivé pour tracer sa tangente. Etant donnée que la tangente d'une droite est cette même droite, vous constaterez qu'il suffira d'une seul itération pour trouver une approximation du point B ou la fonction objective est minimal.

<div class="figure">
    <img src="../images/newton_raphson/newton_gradient.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>  

#### Méthode algorithmique

D'une manière général, si vous voulez faire une régression avec la méthode de newton il vous faut: 

<center> <em> Une Fonction objective</em> </center>
$$f(a) = \frac{1}{n}\sum_{i=0}^{n}(-2y_{i}ax_{i} + a^{2}x_{i}^{2})$$

<center> <em> La dérivé de la fonction objective</em> </center>
$$ f'(a) = \frac{-2}{n}\sum_{i=0}^{n}(x_{i}(y_{i} - ax_{i})  $$ 

<center> <em> La Dérivé seconde de la fonction objective</em> </center>
$$ f''(a) = \frac{-2}{n}\sum_{i=0}^{n}x_{i}^2$$ 


En python, la régression linéaire revient donc à faire : 


```python
# Fonction objectif 
def error(a):
    yPred      = X * a 
    yObserved  = Y 
    size       = len(X)
    diff = sum((yPred - yObserved)**2)/size
    return diff

# Dérivé de la fonction objective
def derror(a):
    size = len(X)
    return -2/size * sum(X * (Y - a * X))

# Dérivé second de la fonction objective
def dderror(a):
    size = len(X)
    return 2/size * sum (X*X)

# Pas besoin de faire d'itération dans le cas d'une regression linéaire,
# on arrive direct au résultat en une itération.. Et ça, c'est magique ! 
# for i in range(iteration) 

a = 7.5   # point au hasard
a -= derror(a) / dderror(a)
print(a) # retourne 3.67955204188 le point ou la fonction objective est minimum 

```

# Conclusion

Si vous aviez lu le billet précedent, vous allez pouvoir comparer la méthode des gradients et celle de Newton. De manière général la methode est meilleur car elle s'approche beaucoup plus rapidement du résultat. Cependant, calculer la dérivé seconde peut parfois être complexe à calculer, surtout dans un espace multidimensionelle, et l'on préfère alors l'autre méthode. La dernière image vous montre la direction que prendrait les valeurs dans un espace à deux dimensions suivant la methode des gradients ou de Newton. 


<div class="figure">
    <img src="../images/newton_raphson/gradient_vs_newton.gif" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>  

