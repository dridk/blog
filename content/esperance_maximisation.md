Title: Algorithme d'Espérance-Maximisation
Slug: expectation-maximisation
Date: 2018-08-06 18:13:58
Modified: 2018-08-06 18:13:58
Tags: algorithme,mixture model, expectation-maximisation
Category: informatique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/ia_banner.jpg

Nous allons voir dans ce billet l'algorithme d'[espérance-maximisation](https://fr.wikipedia.org/wiki/Algorithme_esp%C3%A9rance-maximisation) ou algorithme EM (Expectation-maximisation) qui va nous permettre d'identifier les paramètres de deux [lois normales](https://fr.wikipedia.org/wiki/Loi_normale) depuis une seule distribution mixte ou [mélange gaussien](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_m%C3%A9lange_gaussien) ou GMM (Gaussian Mixture model). 
Comme d'habitude, je vais faire au plus simple. Ce billet fait directement suite à celui sur [le maximum de vraisemblance](maximum-de-vraissemblance.html) mais vous n'êtes pas obligé de le lire.

## Mélange de Gaussienne
Nous allons étudier la distribution des tailles chez 1000 hommes et 1000 femmes. La taille des hommes suit une loi normale de moyenne **μ=190 cm** et d'écart-type **σ=10**. Celle des femmes, une moyenne **μ=160cm** et d'écart type **σ=5**.
Nous pouvons générer et representer visuellement ces données en [python](https://www.python.org/) avec [numpy](http://www.numpy.org/) et [seaborn](https://seaborn.pydata.org/): 

```python    
import numpy as np
import seaborn as sns

hommes = np.random.normal(190, 10, 1000)
# hommes = [171,171,173,180,190,159 ...]
femmes = np.random.normal(160,5, 1000)
# femmes = [145,170,145,161,139,150 ...]

sns.distplot(femmes, label="Femmes")
sns.distplot(hommes, label="Hommes")
```

<div class="figure">
<img src="../images/mixture_model/hommes_femmes.png" />
<div class="legend"> Distribution des tailles chez les femmes (roses) et les hommes (bleus) </div>
</div>

Imaginez maintenant que vous avez seulement une liste . Cette nouvelle distribution est la [concaténation](https://fr.wikipedia.org/wiki/Concat%C3%A9nation) des deux distributions précédentes : 

```python   
X  = np.concatenate((femmes,hommes))
sns.distplot(X, label="mixture", color="green")
plt.legend()
```

<div class="figure">
<img src="../images/mixture_model/mixture.png" />
<div class="legend"> Distribution des Tailles sans connaissance du sexe. </div>
</div>

**Le but du jeu à présent**, est de retrouver les paramètres des deux gaussiennes paramétrées par **(μA,σA) ** et **(μB,σB)** uniquement à partir de cette distribution que nous appellerons **X**.

## Algorithme EM 
L'[Algorithme EM](https://fr.wikipedia.org/wiki/Algorithme_esp%C3%A9rance-maximisation) ( Expectation-Maximisation ) va nous permettre de trouver les paramètres de ces deux gaussiennes en partant de valeurs aléatoires et en les ajustant au fur et mesure jusqu'à ce que la vraisemblance de ces modèles soient maximales. Les étapes sont les suivantes :    

1. Initialiser deux lois normales A et B en choisissant des valeurs aléatoires pour (μA /σA et μB / σB)  
2. Pour chaque valeur de **X**, calculer sa probabilité sous l'hypothèse A (pA) puis B (pB)
3. Pour chaque valeur de **X**, calculer le poids **wA** = pA/(pA+pB) et **wB**=pB/(pA+pB) 
4. Calculer des nouveaux paramètres (μA,σA) et (μB,σB) en ajustant **X** à partir des poids **wA** et **wB**.
5. Recommencer ...

En Python cela donne : 

```python   
    # Distribution des tailles X.. (voir plus haut )
    # X      = [159,158, 159, 179, 189 ....]

    # Générer un modèle aléatoire A 
    A_mean = np.random.randint(100,300)
    A_sd   = np.random.randint(10,30)

    # Générer un modèle aléatoire B   
    B_mean = np.random.randint(100,300)
    B_sd   = np.random.randint(10,30)

    # Faite 50 itérations... ( ca suffira)
    for i in range(50):

        # Pour chaque valeur de X, calculer la probabilité 
        # sous l'hypothèse A et B
        p_A = scipy.stats.norm(loc=A_mean, scale=A_sd).pdf(X)
        p_B = scipy.stats.norm(loc=B_mean, scale=B_sd).pdf(X)

        # Calculer pour chaque valeur de X, un poids correspondant 
        # à son degrès d'appartenance à la loi A ou B.

        p_total  = p_A + p_B 
        weight_A = p_A / p_total
        weight_B = p_B / p_total

        # Exemple : Si la taille de 189cm appartient à la lois B 
        # alors weight_B(189) sera grand et weight_A(189) sera petit.

        #Ajustement des paramètres (μA,σA) et (μB,σB) en fonction du poids.

        A_mean = np.sum(X * weight_A )/ np.sum(weight_A)
        B_mean = np.sum(X * weight_B )/ np.sum(weight_B)
        
        A_sd   = np.sqrt(np.sum(weight_A * (X - A_mean)**2) / np.sum(weight_A))
        B_sd   = np.sqrt(np.sum(weight_B * (X - B_mean)**2) / np.sum(weight_B))
    
        # On recommence jusqu'à convergence. Non testé ici, je m'arrête à 50 iterations.

```

Et voilà ce que l'on obtient en animant le tout à chaque itération:    
    
<div class="figure">
<img src="../images/mixture_model/em_algo.gif" />
<div class="legend"> Ajustement de deux lois normales (orange et bleu) à la distribution X (vert) selon l'algorithme EM </div>
</div>


# Loi normale multivariée
Dans cet exemple, nous avons étudié la distribution d'une seule variable (*la taille*) en utilisant une loi normale paramétrée par μ et σ. 
Mais nous pouvons faire encore mieux en étudier la distribution de plusieurs variables simultanément (Par exemple la taille et le poids). On utilise pour cela une généralisation de la loi normale que l'on appelle [loi normale multidimensionnelle](https://fr.wikipedia.org/wiki/Loi_normale_multidimensionnelle) paramètré par un vecteur μ et une matrice de covariance σ.     
En prenant 2 variables comme la Taille et le Poid, μ correspond à la liste des moyennes [μTaille, μPoid] et σ correspond à une matrice symétrique 2x2 contenant les [covariances](https://fr.wikipedia.org/wiki/Covariance) et [variances](https://fr.wikipedia.org/wiki/Variance_(statistiques_et_probabilit%C3%A9s)) de la taille et du poids. Exemple ci-dessous:


<center>

|               | Taille       | Poid        |
|------------   |:------------:|:-----------:|
| **Taille**    | vT           | cov(P,T)    |
| **Poid**      | cov(P,T)     | vP          |

<div class="legend"> Matrice de covariance d'une loi normale à deux dimensions. vT et vP sont les variances pour la Taille et le Poid. cov(P,T) est la covariance entre le poids et la taille</div>
</center>

Vous pouvez vous représenter une loi normale à deux variables comme un [Sombrero](https://fr.wikipedia.org/wiki/Sombrero) aplati et vu de haut ou chaque point est representé dans le plan par ses coordonnées (x=Taille et y=Poids).

<div class="figure">
<img src="../images/mixture_model/bivariate.png" />
<div class="legend"> Exemple d'une distribution normale bivariée. Imaginez que la courbe rouge représente la taille et la bleu le poid </div>
</div>

Comme nous l'avons fait précédement avec **une variable**, nous pouvons identifier plusieurs gaussiennes multivariées dans un espace à **plusieurs variables** (figure ci-dessous).     
En d'autres termes, identifier à quelle distribution appartient un point, c'est faire de la [clusterisation](https://fr.wikipedia.org/wiki/Partitionnement_de_donn%C3%A9es).


<div class="figure">
<img src="../images/mixture_model/bivariate2.png" />
<div class="legend"> Exemple: Gauche: Distribution de deux variables et identification de 2 clusters. Droite: Modèle normal bivarié montrant la densité sur son 3ème axe.  source: <br/><a href="https://www.sciencedirect.com/science/article/pii/S0167947315000171">Source</a>  </div>
</div>

# Hard et Soft clustering
Il existe d'autres algorithmes pour détecter des clusters, notamment l'algorithme [k-means](https://fr.wikipedia.org/wiki/K-moyennes) ou encore les [k-plus proches voisins](https://fr.wikipedia.org/wiki/M%C3%A9thode_des_k_plus_proches_voisins). Ces méthodes de clustering sont dites "[Hard clustering](https://www.youtube.com/watch?v=xtDMHPVDDKk)". C'est-à-dire qu'il catégorise de façon précise un point (Homme ou Femme). Au contraire, l'algorithme EM basé sur les mixtures gaussiennes permet de faire du [soft clustering](https://www.youtube.com/watch?v=xtDMHPVDDKk). Au lieu d'attribué un groupe à un point, on lui attribue une probabilité d'appartenance à chacun de ces groupes (80% Hommes, 10% Femmes). 

<div class="figure">
<img src="../images/mixture_model/clustering.png" />
<div class="legend"> Différence entre le soft et du hard clustering en utilisant un gradient de couleur. En rouge les femmes, en bleu les hommes </div>
</div>

# Conclusion 
L'algorithme EM fait partie de la grande famille du [machine learning](https://fr.wikipedia.org/wiki/Apprentissage_automatique) et de [l'apprentissage non supervisé](https://fr.wikipedia.org/wiki/Apprentissage_non_supervis%C3%A9). C'est un avant goût des méthodes bayesiennes utilisées en intelligence artificielle. Si vous voulez approfondir le sujet (c'est à dire sans se faire chier à écrire du code), allez voir du côté de la libraire [scikit-learn](http://scikit-learn.org/stable/modules/mixture.html). 

## Références

- [J'ai compris sur StackOverflow](https://stackoverflow.com/questions/11808074/what-is-an-intuitive-explanation-of-the-expectation-maximization-technique)
- [Coursera: Bayesian Methods for Machine Learning](https://www.coursera.org/learn/bayesian-methods-in-machine-learning)