Title: gradient descendant
Slug: gradient_descendant
Date: 2018-10-16 22:13:42
Modified: 2018-10-16 22:13:42
Tags: algorithme, machine learning
Category: informatique
Author: Sacha Schutz
Status: Draft


Si vous commencez à faire de l'intelligence artificielle, vous avez surement du entendre parler de la méthode du gradient descendant. Il s'agit d'un algorithme permettant de trouver rapidement le minimum d'une fonction mathématique. Pour faire simple, trouver x tel que f(x) = 0. 
Cette méthode est utilisé entre autre avec les réseaux de neurones. Mais avant d'en arriver là, nous allons tenter de comprendre cette algorithme en estimant les paramètres d'une droite dans un modèle de regression linéaire. 

## Une régression linéaire simple

J'ai ici généré 100 points aléatoires. Disons la taille en fonction du poids. Nous allons faire une regression linéaire et trouver l'équation de la droite passant au mieux par tous les points. Simple vous me dirait ? Effectivement, il existe une méthode analytique, c'est à dire une formule magique, permettant de trouver directement le param_tre a de l'équation y = ax. Il s'agit de la méthode des moindres carrée détaillé ici pour les plus curieux.  
Sauf que cette fois et parce que la majorité des modèles statistiques ne disposent pas de solution analytque, nous allons estimer ces paramètres par une méthode algorithmique: La descente en gradient. 

<div class="figure">
    <img src="../images/gradient_descendant/observation.png" />      
    <div class="legend">Taille en fonction du poids pour 100 observations</div> </div>   

## Une erreur à minimiser 

La première étape consiste à définir une fonction "objectif" que l'on cherchera à minimiser. Dans notre cas, nous voulons minimiser l'écart entre les points et la droite de regression paramètré par "a". 

<div class="figure">
    <img src="../images/gradient_descendant/less_square.png" />      
    <div class="legend">Nous voulons trouver le paramètre "a" qui minimise les distances ( en rouge ) entre les observations et la prédiction du modèle de regression liniéaire. Pour pouvons chercher "a" de façon que la sommes des écarts au carré soit minimum </div> </div>   

Pour cela, nous pouvons définir une fonction comme étant la somme des écarts au carré entre les valeurs observés (yi) et les valeurs calculés par la droite d'équation y=ax. 
Cette fonction peut s'écrire de la façon suivante. 

- "a" le paramètre à estimer.
- yi la valeur observé du point i 
- axi la valeur prédite par la droite au point i
- n le nombre de points

$$
f(a) = \frac{1}{n}\sum_{i=0}^{n}(y_{i}-ax_{i})^{2} \\
$$



En python cela s'écrit de la façon suivante : 

```python

def error(a):
    yPred      = X * a 
    yObserved  = Y 
    size       = len(X)
    
    diff = sum((yPred - yObserved)**2)/size
    return diff

```

De façon naîve, nous pourions tester toutes les valeurs du paramètre "et voir sur un graphique pour quel valeur l'erreur est minimum. A vu de nez ça tourne entre 3 et 5. 

<div class="figure">
    <img src="../images/gradient_descendant/naif.png" />      
    <div class="legend">Taille en fonction du poids pour 100 observations</div> </div>   

Dans la vrai vie, on ne peut pas s'amuser à tester toutes les valeurs possible. Si vous êtes par exemple avec un modèle à 20 paramètres, il y aurait beaucoup trop de combinaison à tester. C'est là qu'intervient la méthode de descente en gradient. 

## A petit pas jusqu'à l'arrivé

 La méthode de descente en gradient, consiste à prendre une valeur de "a" au hasard et la faire varier plus ou moin fortement par rapport à la pente de la fonction objective. Au lieu de tester toutes les valeurs de "a" avec des pas de 1, (-10, -9, -8, -7) on fait varier "a" avec des pas variable qui deviennent de plus en plus petit à mesure que l'on se rapproche de la bonne valeur de a. 

En cherchant dans vos souvenirs de lycée, cette pente c'est la dérivé encore appelé la dérivé partielle si vous travailler dans un espace multidimensionnel. Elle se calcul comme suite . ( rappelez vous que la dérivé de x^n c' nx^(n-1))

$$f(a) = \frac{1}{n}\sum_{i=0}^{n}(y_{i}-ax_{i})^{2} $$ 

<center> <em> Se développe en : </em> </center>

$$ f(a) = \frac{1}{n}\sum_{i=0}^{n}(y_{i}^{2}-2y_{i}ax_{i} + (ax_{i})^{2} ) $$ 

<center> <em> En dérivant par rapport à "a" nous obtenons : </em> </center>

$$ f'(a) = \frac{1}{n}\sum_{i=0}^{n}(-2y_{i}ax_{i} + a^{2}x_{i}^{2} ) $$ 

<center> <em> Soit </em> </center>

$$ f'(a) = \frac{-2}{n}\sum_{i=0}^{n}(x_{i}(y_{i} - ax_{i})  $$ 


En reprenant cette equation, nous pouvons écrire en python la fonction suivante calculant la dérivé au point a de la fonction objective: 

```python
def derror(a):
size = len(X)
return -2/size * sum(X * (Y - a * X))
```

La figure ci-dessous, vous montre les valeurs des pentes pour différentes valeurs de "a" allant de -10 à 10. Comme vous pouvez le constater, plus nous nous rapprochons du minimum et plus la pente diminue. Elle est négatif à gauche et positif à droite. Pour trouver la bonne valeur de a, il suffit de faire varier a en suivant gradient. Si le gradient diminue, on augmente a, si il augmente on diminue a.



<div class="figure">
    <img src="../images/gradient_descendant/derivate.png" />      
    <div class="legend">Taille en fonction du poids pour 100 observations</div> </div>   

La fonction suivante fait varier a en partant de -20 et en suivant le gradient jusqu'à ce que la pente soit quasi nul.( entre -0.5 et 0.5). Le paramètre taux, appelé taux d'apprentissage, permet d'ajuster la taille du pas. Si le taux d'apprentissage est grand, alors les pas seront plus petit, la précision du résultat sera bonne mais prendra plus de temps à atteindre. A l'inverse, un taux d'apprentissage petit sera moins précis mais plus rapide. 

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

L'animation ci-dessous illustre la descente en gradient calculé précédement qui trouve 3.8 comme valeur de a. En peut conclure que la Taille = Poid * 3.8.

<center>
<video controls>
  <source src="../images/gradient_descendant/gradient.mp4" type="video/mp4">

Your browser does not support the video tag.
</video>
</center>



## Conclusion 
Nous avons vu un exemple de descente en gradient pour évaluer un seul paramètre dans un modèle de regression linéaire. Dans un modèle avec deux paramètre comme a et b de l'equation y = ax + b, la fonction d'erreur est une equation multiparamètrique de la forme f(a,b). Visuellement, il s'agit d'un surface en 3D ou vous allez faire varier les paramètres a et b à l'aide des dérivées partielle. 

<div class="figure">
    <img src="../images/gradient_descendant/gradientDescent.jpg" />      
    <div class="legend">Descent en gradient pour 2 paramètres et une fonction objective</div> </div>   


Dans les réseaux neuronaux, les modèles sont constitués d'autant de paramètres qu'il y a de neurones. Et pour faire ces descente de gradient, des libraries comment TensorFlow ou Pytorch ont vu le jour pour optimiser les calculs de façon parallèles.



Le notebook contenant l'ensemble du code est disponnible ici

