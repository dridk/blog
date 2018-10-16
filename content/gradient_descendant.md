Title: L'algorithme de descente en gradient
Slug: gradient_descendant
Date: 2018-10-16 22:13:42
Modified: 2018-10-16 22:13:42
Tags: algorithme, machine learning
Category: informatique
Author: Sacha Schutz
Status: Draft


Si vous déjà commencer à étudier l'intelligence artificielle, vous avez certainement du entendre parler de la méthode de descente en gradient. Il s'agit d'un algorithme permettant de trouver rapidement le minimum d'une fonction mathématique. Pour faire simple, trouver x tel que f(x) = 0. 
Cette méthode est très utilisée avec les réseaux de neurones. Mais avant d'en arriver là, nous allons tenter de comprendre cet algorithme en estimant le paramètre **a** d'une simple régression linéaire d'équation **y=ax**.

## Une modèle linéaire 

J'ai généré pour ce billet 100 points aléatoires (figure ci-dessous). Disons que ces points représentent la taille en fonction du poids. Nous voulons trouver l'équation de la droite passant au mieux par tous les points. Simple vous me direz ? Effectivement, il existe une méthode analytique, c'est-à-dire une formule magique, permettant de trouver directement le paramètre *a* de l'équation *y = ax*. Il s'agit de la méthode des moindres carrée détaillé ici pour les plus curieux.  
Sauf que cette fois pour l'exemple et parce que la majorité des modèles statistiques ne disposent pas de solution analytique, nous allons estimer ces paramètres par une méthode algorithmique: La descente en gradient. 

<div class="figure">
    <img src="../images/gradient_descendant/observation.png" />      
    <div class="legend">Taille en fonction du poids pour 100 observations</div> </div>   

## Une erreur à minimiser 

La première étape consiste à définir une [fonction objectif](https://fr.wikipedia.org/wiki/Fonction_objectif) que l'on cherchera à minimiser. C'est à dire une fonction qui prendra en paramètre **a** et qui retournera une erreur. Dans notre cas, nous voulons minimiser l'écart entre les points et la droite de régression. 

<div class="figure">
    <img src="../images/gradient_descendant/less_square.png" />      
    <div class="legend">Nous voulons trouver le paramètre "a" qui minimise les distances ( en rouge ) entre les observations et la prédiction du modèle de régression linéaire. Nous pouvons trouver "a" de façon que la somme de ces écarts au carré soit minimum </div> </div>   

Cette fonction objective peut se définir comme étant la somme des écarts au carré entre les valeurs observés (yi) et les valeurs calculées par la droite d'équation y=ax. 
Cette fonction s'écrit de la façon suivante. 

- a, le paramètre à estimer de la droite de régression y=ax
- y<sub>i</sub> , la valeur observée au point i 
- ax<sub>i</sub> la valeur prédite par la droite au point i
- n le nombre de points

$$
f(a) = \frac{1}{n}\sum_{i=0}^{n}(y_{i}-ax_{i})^{2} \\
$$



En python cela peut s'écrire de la façon suivante : 

```python
X = np.array([....]) // poids
Y = np.array([....]) // taille

def error(a):
    y_pred      = X * a 
    y_observed  = Y 
    size        = len(X)
    
    diff = sum((y_pred - y_observed)**2)/size
    return diff

```

De façon naïve, nous pouvons tester toutes les valeurs du paramètre a, en faisant des pas de 1, et voir sur un graphique pour quelle valeur l'erreur est minimum. 

<div class="figure">
    <img src="../images/gradient_descendant/naif.png" />      
    <div class="legend">Fonction objective: L'erreur en fonction du paramètre a. L'erreur minimum se situe au alentour de 3</div> </div>   

Dans la vraie vie, on ne va  pas pouvoir s'amuser à tester toutes les valeurs des paramètres possibles. Si vous êtes par exemple avec un modèle à 20 paramètres, il y aurait beaucoup, beaucoup trop de combinaison à tester. Et C'est là qu'intervient la méthode de descente en gradient. 

## À petit pas jusqu'à l'arrivée

 La méthode de descente en gradient consiste à prendre une valeur de "a" au hasard et la faire varier plus ou moins fortement par rapport à la pente de la fonction objective. Au lieu de tester toutes les valeurs de "a" avec des pas de 1, vous faites varier "a" avec des pas variables qui deviennent de plus en plus petits au fur et à mesure que l'on se rapproche du minimum.

En cherchant dans vos souvenirs de lycée, cette pente c'est la dérivé encore appelé dérivé partiel si vous travaillez avec plusieurs paramètres. Elle se calcule comme suite: 

$$f(a) = \frac{1}{n}\sum_{i=0}^{n}(y_{i}-ax_{i})^{2} $$ 

<center> <em> Se développe en : </em> </center>

$$ f(a) = \frac{1}{n}\sum_{i=0}^{n}(y_{i}^{2}-2y_{i}ax_{i} + (ax_{i})^{2} ) $$ 

<center> <em> En dérivant par rapport à "a" nous obtenons : </em> </center>

$$ f'(a) = \frac{1}{n}\sum_{i=0}^{n}(-2y_{i}ax_{i} + a^{2}x_{i}^{2} ) $$ 

<center> <em> Soit </em> </center>

$$ f'(a) = \frac{-2}{n}\sum_{i=0}^{n}(x_{i}(y_{i} - ax_{i})  $$ 


En reprenant cette équation, nous pouvons écrire en python la fonction qui calcul la dérivé au point a: 

```python
def derror(a):
size = len(X)
return -2/size * sum(X * (Y - a * X))
```

La figure ci-dessous montre les valeurs des pentes pour différentes valeurs de "a" allant de -10 à 10. Comme vous pouvez le constater, plus nous nous rapprochons du minimum et plus la pente diminue. Elle est négative à gauche et positive à droite. Pour trouver la bonne valeur de a, il suffit de faire varier a en suivant gradient. Si le gradient diminue, on augmente a, s’il augmente on diminue a.

<div class="figure">
    <img src="../images/gradient_descendant/derivate.png" />      
    <div class="legend">différente pente pour différente valeur de a</div> </div>   

L'implémentation en python est alors triviale (ci-dessous). En partant de a=-20, on fait une boucle faisant varier a en fonction du gradient. Le paramètre taux, appelé taux d'apprentissage, permet d'ajuster la taille du pas. Si le taux d'apprentissage est grand, alors les pas seront plus petits, la précision du résultat sera bonne, mais mettra plus de temps à atteindre. À l'inverse, un taux d'apprentissage petit sera moins précis, mais plus rapide. 
Lorsque le minimum est atteint, c'est à dire lorsque le gradient est nul ( entre -0.5 et 0.5), on s'arrête et on récupère la valeur de a calculé.

```python
def gradient(a=-20, taux = 400000):
    
    e = 100.0 
    while True:
        
        e = derror(a) 
        g = e / taux
        
        if -0.5 <= e <= 0.5:
            return a
        
        a += -g
        
        print(a)
```

L'animation ci-dessous illustre cette descente en gradient qui s'équilibre autour de 3.8 comme valeur de a. Nous pouvons alors conclure que notre algorithme à estimer que la Taille = Poid * 3.8.

<center>
<video controls>
  <source src="../images/gradient_descendant/gradient.mp4" type="video/mp4">

Your browser does not support the video tag.
</video>
</center>



## Conclusion 
Nous avons vu un exemple de descente en gradient pour évaluer un seul paramètre dans un modèle de régression linéaire. Dans un modèle avec deux paramètres comme a et b de l'équation y = ax + b, la fonction d'erreur est une équation multiparamètrique de la forme f(a,b). Visuellement, il s'agit d'un surface en 3D ou vous allez faire varier les paramètres a et b à l'aide des dérivées partielles. 

<div class="figure">
    <img src="../images/gradient_descendant/gradientDescent.jpg" />      
    <div class="legend">Descent en gradient pour 2 paramètres et une fonction objective</div> </div>   


Dans les réseaux neuronaux, les modèles sont constitués d'autant de paramètres qu'il y a de neurones. Et pour faire ces descentes de gradient, des libraries comment TensorFlow ou Pytorch ont vu le jour pour optimiser les calculs de façon parallèles.



Le notebook contenant l'ensemble du code est disponible ici

