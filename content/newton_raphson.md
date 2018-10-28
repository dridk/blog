Title: L'algorithme de Newton-Raphson
Slug: newton-raphson
Date: 2018-10-28 12:00:35
Modified: 2018-10-28 12:00:35
Tags: algorithme, machine learning
Category: informatique
Author: Sacha Schutz 
SIDEBARIMAGE:../images/common/ia_banner.jpg
Summary: La méthode de [Newton-Raphson](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Newton) est une méthode algorithmique pour trouver la racine d'une fonction. C'est-à-dire trouver x tel que f(x) = 0. Cette méthode est d'une simplicité déconcertante que je vais détailler dans ce billet de façon géométrique puis algorithmique.

La méthode de [Newton-Raphson](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Newton) est une méthode algorithmique pour trouver la racine d'une fonction. C'est-à-dire trouver x tel que f(x) = 0. Cette méthode est d'une simplicité déconcertante que je vais détailler dans ce billet de façon géométrique puis algorithmique.

## Trouver la racine d'une fonction cubique

Prenons une [fonction cubique](https://fr.wikipedia.org/wiki/Fonction_cubique), par exemple $f(x) = x^3  +3$  et traçons la courbe sur un [repère cartésien](https://fr.wikipedia.org/wiki/Rep%C3%A8re_affine).

<div class="figure">
    <img src="../images/newton_raphson/cubic.png" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses au point rouge. Nous voulons trouver les coordonnées de ce point par une méthode algorithmique</div> </div>   

La méthode de Newton-Raphson nous permet de trouver le point x de la courbe tel que f(x) = 0. C'est-à-dire le point de la courbe qui coupe l'axe des abscisses. Bien sûr, nous pourrions simplement résoudre l'équation et trouver x. Mais parfois, les fonctions sont plus complexes et il n'existe aucune solution analytique. La méthode de Newton-Raphson nous permet d'y remédier par un [algorithme itératif](https://fr.wikipedia.org/wiki/M%C3%A9thode_it%C3%A9rative) décrit ci-dessous:

### Représentation géométrique 
Choisissons un point au hasard A sur l'axe des abscisses. 
Par exemple A=(2.5, 0).

<div class="figure">
    <img src="../images/newton_raphson/test0-1.png" />      
    <div class="legend">Prenons un point au hasard A</div> </div>   


Puis trouvons le point A' l'image de A par la fonction cubique. C'est-à-dire le point A'=(2.5, f(2.5)).

<div class="figure">
    <img src="../images/newton_raphson/test0-2.png" />      
    <div class="legend">Le point A' est l'image de A par f</div> </div>   


Enfin, traçons la [tangente](https://fr.wikipedia.org/wiki/Tangente_(g%C3%A9om%C3%A9trie)) de la courbe au point A'. Cette tangente est une droite qui couple l'axe des abscisses au point B.

<div class="figure">
    <img src="../images/newton_raphson/test0-3.png" />      
    <div class="legend">La tangente de la courbe au point A' coupe l'axe des abscisses au point B</div> </div>   

À partir du point B, il suffit de recommencer les mêmes étapes qu'avec le point A. Chercher B', tracer la tangente en B' puis trouver le point C et ainsi de suite... Vous verrez alors rapidement qu'en 7 itérations, les points convergent vers la racine (autour de -1.44) comme illustrée dans l'animation ci-dessous: 

<div class="figure">
    <img src="../images/newton_raphson/anim.gif" />      
    <div class="legend">La fonction cubique coupe l'axe des abscisses en point que nous cherchons à trouver par une méthode algorithmique</div> </div>  

### Représentation algébrique
Maintenant que vous visualisez comment trouver la racine d'une fonction en utilisant la méthode de Newton-Raphson, voyons comme la calculer. Quelques notions de math vues au lycée suffiront:

#### Équation de la tangente au point A'
[La tangente en un point](https://fr.wikipedia.org/wiki/Tangente_(g%C3%A9om%C3%A9trie)#Calculs_de_tangente) d'une fonction f(x) ayant pour dérivée f'(x) est une droite d'équation $y=f'(a)(x-a) + f(a)$ avec «a» les coordonnées de A sur l'axe des abscisses. Dans notre cas, l'équation de la tangente au point A' se calcule comme ceci:

<center> <em> Notre fonction cubique a pour équation: </em> </center>
$$f(x) = x^3 + 3$$
<center> <em> Sa derivé est donc: </em> </center>
$$f'(x) = 3x^2$$
<center> <em> La tagente au point A' (a=2.5) a donc pour equation: </em> </center>
$$
y=f'(a)(x-a) + f(a)\\
y=3a^2(x-a) + a^3 + 3\\
$$
<center> <em> En remplaçant «a» par 2.5:  </em> </center>
$$
y=18,75x - 28,25\\
$$

#### Coordonnée du point B en fonction du point A
connaissant l'équation, les coordonnées du point B ou la tangente coupe l'axe des abscisses se calcul en résolvant l'équation linéaire $18,75x - 28,25=0$. Soit $x=28,25/18,75≈1,506$. Les coordonnées du point B sont donc (1.506,0).  

D'une manière générale, nous pouvons calculer le point B(b,0) en fonction du point A(a,0). En effet, résoudre l'équation linéaire revient à faire:

$$f'(a)(b-a) + f(a) = 0\\$$
$$f'(a)(b-a) = -f(a)\\$$
$$(b-a) = \frac{-f(a)}{f'(a)}\\$$
$$b=a - \frac{f(a)}{f'(a)}$$

<center> <em> En résumé, le point $x_{k+1}$ en fonction du point $x_{k}$ s'exprime par la suite: </em> </center>
$$x_{k+1} = x - \frac{f(x)}{f'(x)}\\$$


### Représentation algorithmique en python


En implémentant la méthode de Newton-Raphson en python, cela donne :

```python
# Fonction cubique
def f(x):
    return x**3 + 3

# Dérivé de la fonction cubique
def df(x):
    return 3*x**2

a = 2.5 # On part d'un point aléatoire
# On applique la formule sur plusieurs itérations... Disons 10
for i in range(10):
    a = a - fct(a)/df(a)
    print(a)

# 1.5066666666666668
# 0.5639244350466844
# -2.7685979807840897
# -1.9761928373643123
# -1.5735216658126505
# -1.4528964881677187
# -1.4423274010169043
# -1.4422495745072248
# -1.4422495703074085
# -1.4422495703074083

```

### En résumé 

- La méthode de Newton-Raphson permet de trouver rapidement la racine d'une fonction et a beaucoup d'usage en informatique.

- La méthode de Newton permet de trouver les extrêmes (minimum et maximum) d'une fonction. En effet, trouver le minimum ou le maximum d'une fonction c'est trouver où la dérivée s'annule. Par exemple dans [le billet précédent sur la descente en gradient](http://dridk.me/gradient_descendant.html) vous pouvez calculer le minimum de la fonction objective en connaissant sa dérivée et sa dérivée seconde. Vous verrez que pour une régression linéaire il suffit d'une seule itération pour trouver le minimum.

- La méthode de Newton permet de trouver la solution à f(x)=c où «c» est une constante. Il suffit de trouver une fonction g(x)=f(x)-c de telle sorte que la racine de g résout l'équation qui nous intéresse.

- S’il y a plusieurs racines, on ne peut pas prédire vers quelle racine l'algorithme va converger.

- La méthode de Newton marche assez bien sûr des [fonctions monotones](https://fr.wikipedia.org/wiki/Fonction_monotone) mais 
peut ne pas converger avec d'autre fonction.

- On ne peut pas garantir la convergence si la fonction n'est pas deux 
fois dérivable à dérivée seconde continue.

- On doit bien partir d'un point. Même si, dans les bonnes conditions, 
le choix de ce point n'a pas grande importance, il peut en avoir avec 
les fonctions non monotones.

- Si les conditions sont respectées, cet algorithme est beaucoup plus performant que la [dichotomie](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_dichotomie).

- La méthode de Newton est utilisée dans [les modèles linéaires généralisés (MLG)](https://fr.wikipedia.org/wiki/Mod%C3%A8le_lin%C3%A9aire_g%C3%A9n%C3%A9ralis%C3%A9)

- La méthode de Newton a été utilisée pour calculer rapidement l'[inverse d'une racine carrée](https://fr.wikipedia.org/wiki/Racine_carr%C3%A9e_inverse_rapide) dans Quake3. 

# Référence 

- [Wikipedia](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Newton) 
- [An intuitive and physical approach to Newton’s method](ttps://medium.com/@ruhayel/an-intuitive-and-physical-approach-to-newtons-method-86a0bd812ec3)
- [Retrouver mon notebook sur github](https://github.com/dridk/notebook/blob/master/newton-raphson/)

# Remerciements

- Metaentropy
- O.Dameron
