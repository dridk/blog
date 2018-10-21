Title: L'algorithme de Newton-Raphson
Slug: newton-raphson
Date: 2018-10-21 12:32:39
Modified: 2018-10-21 12:32:39
Tags: algorithme, machine learning
Category: informatique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/ia_banner.jpg

Je vais dans ce billet vous parler d'une autre méthode qui fait directement suite au billet précédent sur le gradient descendant. Il s'agit de la méthode de Newton-Raphson qui est d'une redoutable efficacité pour trouver la racine d'une fonction. C'est à dire trouver x tel que f(x) = 0.    
Cette methode est d'une simplicité déconcernante et n'importe qui à l'aide d'un crayon et une règle pourrait reproduire l'algorithme sur une feuille de papier. Commençons donc avec un exemple simple, trouver la racine d'une fonction cubique.

## Trouver la racine d'une fonction cubique

Prenons une fonction cubique, par exemple $f(x) = x^3  +3$  et traçon la courbe sur un repère cartésien.

<div class="figure">
    <img src="../images/newton_raphson/cubic.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>   

La méthode de Newton-Raphson nous permet de trouver le point x de la courbe tel que f(x) = 0. C'est à dire le point de la courbe qui coupe l'axe des abcisses.

## Representation géométrique 
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

A partir du point B, il suffit de recommencer les même étape qu'avec le point A. Chercher B', tracer la tangente en B' puis trouver le point C et ainsi de suite... Vous verez alors rapidement, qu'en 7 itéartions, les points convergent vers la racine autour de la valeur -1.44 illustré dans l'animation ci-dessous: 

<div class="figure">
    <img src="../images/newton_raphson/anim.gif" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>  

## Representation algébrique 
Maintenant que vous visualisez comment trouver la racine d'une fonction, nous allons voir comment la calculer.

### Equation de la tangente au point A'
La tangente en un point est une droite d'équation $y=f'(a)(x-a) + f(a)$. Dans notre cas, l'équation de la tangente au point A' se calcul comme ceci:

<center> <em> Notre fonction a pour équation: </em> </center>
$$f(x) = x^3 + 3$$
<center> <em> Sa derivé est donc: </em> </center>
$$f'(x) = 3x^2$$
<center> <em> La tagente au point A=2.5 a donc pour equation </em> </center>
$$
y=f'(A)(x-A) + f(A)\\
y=3A^2(x-A) + A^3 + 3\\
y=18,75x - 28,25\\
$$

### Coordonnée du point B en fonction du point A
Connaissant l'équation de la tangente, les coordonnées du point B ou la tangente coupe l'axe des abscisses se calcul comment étant la résolution de l'équation $18,75x - 28,25=0$ , soit $B=28,25/18,75≈1,506$.    
Le point B peut en faite se calculer directement en fonction du point A par la formule suivante: 

$$f'(a)(b-a) + f(a) = 0\\$$
$$f'(a)(b-a) = -f(a)\\$$
$$(b-a) = \frac{-f(a)}{f'(a)}\\$$
$$b=a - \frac{f(a)}{f'(a)}$$

<center> <em> D'une manière générale, un point s'exprime en fonction du précédant par la formule suivante </em> </center>
$$x_{k+1} = x - \frac{f(x)}{f'(x)}\\$$


### En python 
Appliquons maintenant notre formule avec python : 

```python
# Fonction cubique
def f(x):
    return x**3 + 3

# Derivé de la fonction cubique
def df(x):
    return 3*x**2

# Trouver la racine 
def racine(fct, derivate, iteration):
    a = 2.5
    for i in range(iteration):
        a = a - fct(a)/derivate(a)
        print(a)

# On cherche sur 10 itérations 
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

## Trouver le minimum d'une fonction objectif 

Dans le billet précédant, nous avons chercher à estimer le paramètre a de l'équation y=ax dans une simple régression linéaire. Nous avions utiliser la méthode de descente en gradient pour trouver le minimum d'une fonction objective. 

<div class="figure">
    <img src="../images/gradient_descendant/derivate.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>  

Dans notre cas, la dérivé de la fonction objective (bleu) est une droite (orange) qui coupe l'axe des abscisses à son minimum. C'est à dire que chercher x tel que f'(x) = 0 revient à chercher le minimum de f(x). On peut donc appliquer l'algorithme de Newton-raphson pour trouver la racine de cette droite. 
Prenons au hasard A=-7.5, cherchons A' et traçons la tagente en ce point pour trouver le point B. Etant donnée que la tangente d'une droite est une droite, vous n'avez rien à faire. Et vous constaterez qu'il vous auras suffit d'une seul itération pour trouver une approximation de racine qui est donc le minimum de notre fonction objective.

<div class="figure">
    <img src="../images/newton_raphson/newton_gradient.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>  

D'une manière général, nous avons calculer le minimum d'une fonction objective en cherchant la racine de sa dérivé. Pour cela, il faut calculer la dérivé $f'(x)$ de la fonction objective ainsi que la dérivé de la dérivé ou encore dérivé seconde $f''(x)$. On peut alors appliquer la formule de l'algorithme de Newton-raphson et trouver le minimum de la fonction objectif . 

<center> <em> Fonction objective</em> </center>
$$f(a) = \frac{1}{n}\sum_{i=0}^{n}(-2y_{i}ax_{i} + a^{2}x_{i}^{2})$$

<center> <em> Dérivé de la fonction objective</em> </center>
$$ f'(a) = \frac{-2}{n}\sum_{i=0}^{n}(x_{i}(y_{i} - ax_{i})  $$ 

<center> <em> Dérivé seconde de la fonction objective</em> </center>
$$ f''(a) = \frac{-2}{n}\sum_{i=0}^{n}x_{i}^2$$ 

<center> <em> En partant de x = -7.5 et nos données observées </em> </center>
$$
x_{k+1} = x - \frac{f'(x)}{f''(x)}\\
x_{k+1} = -7.5 - \frac{f'(-7.5)}{f''(-7.5)}\\
x_{k+1} = -7.5 - \frac{f'(-7.5)}{f''(-7.5)}\\
x_{k+1} = 3.73195362149 \\
$$





