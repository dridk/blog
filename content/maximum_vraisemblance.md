Title: Le maximum de vraisemblance
Slug: maximum-de-vraissemblance
Date: 2018-06-05 22:48:39
Modified: 2018-06-05 22:48:39
Tags: statistique
Category: informatique
Author: Sacha schutz
Status: Draft

Je continue ma lancée avec ce billet traitant d'un sujet important aussi bien en statistique qu'en intelligence artificielle: **[Le maximum de vraisemblance](https://fr.wikipedia.org/wiki/Maximum_de_vraisemblance)**. Je rappelle que je ne suis ni statisticien ni mathématicien et que j'essaie d'expliquer ces concepts avec un simple regard naïf de programmeur.     
Le maximum de vraisemblance est une méthode statistique permettant de trouver les paramètres d'un modèle les plus "*vraisemblables*" pour expliquer des données observées. On peut comparer cela avec une [régression linéaire](https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire) où l'objectif est d'identifier les paramètres a et b de l'équation y = ax+b. Dans la suite de ce billet, ce ne sera pas les paramètres d'une droite, mais les paramètres d'une [loi normale](https://fr.wikipedia.org/wiki/Loi_normale) que nous essayerons de déterminer.

### Nos données observées

Imaginons une série de valeur, disons l'âge de 1000 étudiants pris au hasard dans une fac. En traçant l'histogramme de ces données, nous obtenons : 

    data  = np.random.normal(24, MYSTERE ,1000)

<div class="figure">
<img src="../images/maximum_vraisemblance/normal_dist.png" />
<div class="legend">distribution des âges suivant une loi normale. Les données ont été générées avec np.random.normal. Le paramètre MYSTERE a volontairement été caché</div>
</div>

On peut voir ici que la distribution des valeurs suit approximativement une loi normale avec une moyenne aux alentours de 24 et un écart type difficile à évaluer au premier coup d'oeil. Ce dernier est le paramètre MYSTERE que nous allons découvrir en cherchant l'équation de la loi normale qui s'ajuste au mieux aux données.

### La fonction de la loi normale

 La loi normale est une fonction de x à deux paramètres **mu** et **sigma** définissant respectivement le centre de la courbe ([l'espérance](https://fr.wikipedia.org/wiki/Esp%C3%A9rance_math%C3%A9matique)) et sa largeur ([la variance](https://fr.wikipedia.org/wiki/Variance_(statistiques_et_probabilit%C3%A9s))). 

<div class="figure">
<img src="../images/maximum_vraisemblance/equation.png" />
<div class="legend">fonction définissant une la loi normale</div>
</div>

En python cette fonction est implémentée dans la librairie [scipy](https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.stats.norm.html). Pour tracer cette fonction, il suffit de faire: 

```python
import scipy 
import numpy as np
import matplotlib.pyplot as plt

def loi_normale(x,mu = 0 ,sigma = 1):
    return scipy.stats.norm.pdf(x,loc = mu, scale=sigma)

x = np.arange(-10,10,0.1)
y = loi_normale(x)
plt.plot(x,y)
```

<div class="figure">
<img src="../images/maximum_vraisemblance/loi_normale.png" />
<div class="legend">Exemple d'une loi normale d'espérance 0 et de variance 1</div>
</div>

En faisant varier *mu* et *sigma*, vous verrez différentes formes de cloche. Le but est donc de trouver quelles sont les meilleures valeurs de ces deux paramètres pouvant expliquer la distribution de nos données.

### Calcul de la vraisemblance 
Pour faire simple, nous allons uniquement évaluer le paramètre *sigma* et fixer *mu* à 24. Il faut d'abord attribuer à chaque valeur possible de *sigma* un indicateur appelé vraisemblance que l'on note *L(sigma)*. Il s'agit du produit de *f(x)* pour toute valeur *x* provenant de nos données observées.

    L(sigma) = f(x1) * f(x2) * f(x3) * .... 

Son implémentation en python est la suivante : 

```python    
def vraisemblance(data, sigma):
    L = []
    for x in data:
        y =  loi_normale(x,mu = 24, sigma = sigma)
        L.append(y)
    return np.prod(L)  
```

On préfère cependant utiliser le *log* pour remplacer les multiplications par des additions.

```python    
def log_vraissemblance(data, sigma):
    L = []
    for x in data:
        y =  loi_normale(x,mu = 24, sigma = sigma)
        L.append(np.log(y))
    return np.sum(L)  
```

### Le maximum de vraisemblance
En réfléchissant 2 minutes, vous comprendrez tout de suite que la valeur idéale de *sigma* est celle qui va maximiser la vraisemblance.    
On peut tout de suite confirmer cette intuition en testant différentes valeurs de sigma et identifier celle dont la vraisemblance est maximale. 

```python
x = np.arange(1,5,0.1)
y = []
for sigma in x:
    y.append(vraisemblance(data,sigma))

plt.plot(x,y)
```

<div class="figure">
<img src="../images/maximum_vraisemblance/vraisemblance_test.png" />
<div class="legend">Vraisemblance en fonction de sigma</div>
</div>

En recherchant la valeur de sigma qui donne la plus grande vraisemblance, on trouve sigma ~ 2.1

    import pandas as pd
    df=  pd.DataFrame({"x":x,"y":y})
    # Liste des valeur x et y
    # 1.0 -3110.531663
    # 1.1 -2825.482705
    # 1.2 -2623.199764
    # 1.3 -2478.103466
    # 1.4 -2373.570530
    # 1.5 -2298.445032
    # 1.6 -2245.033229
    # 1.7 -2207.903507
    # 1.8 -2183.142831
    # 1.9 -2167.881929
    # 2.0 -2159.983996
    # 2.1 -2157.835771  <=
    # 2.2 -2160.204391
    # 2.3 -2166.137473
    # 2.4 -2174.892189
    # 2.5 -2185.884166
    
    # Ou plus simplement avec idxmax
    df.iloc[df["y"].idxmax()]
    #x       2.1
    #y   -2157.835771

En traçant la fonction normale avec les paramètres mu=24 et sigma=2.1, on peut alors dessiner une courbe en cloche qui s'ajuste parfaitement. 

<div class="figure">
<img src="../images/maximum_vraisemblance/adjusted.png" />
<div class="legend">Modèle ajusté à nos données</div>
</div>


### Conclusion
Le maximum de vraisemblance permet de faire beaucoup plus de choses bien plus stylées. Il est par exemple impliqué dans [l'algorithme d'espérance-maximisation](https://fr.wikipedia.org/wiki/Algorithme_esp%C3%A9rance-maximisation) permettant par exemple d'extraire deux lois normales à partir d'un jeu de données mélangées. J'y reviendrai.. Quand j'aurais bien compris ! 
