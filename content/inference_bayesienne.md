Title: Inférence bayesienne et python
Slug: inference_bayesienne
Date: 2020-03-18 11:44:42
Modified: 2020-03-18 11:44:42
Tags: statistique
Category: informatique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/stat_banner.jpg


Dans mon entourage, que ce soit en médecine ou en bioinformatique, peu de personne savent ce qu'est [l'inférence bayesienne](https://fr.wikipedia.org/wiki/Inf%C3%A9rence_bay%C3%A9sienne). Pourtant sans même le savoir, nous en faisons quotidiennenent. Que ce soit pour deviner le menu à la cantine rien qu'à l'odeur ou lorsque le médecin pense à l'infarctus du myocarde devant une douleur thoracique. 
En deux mots, l'inférence bayesienne est une méthode permettant de quantifer nos incertitudes à partir de nos a priori et de nos observations. Dans ce billet, nous allons définir l'inférence bayesienne et son vocabulaire à partir d'exemples intuitives. Puis, nous l'appliquerons à travers un exemple codé en python et avec la librairie [PyMC3](https://docs.pymc.io/). 



# L'inférence bayesienne selon Laplace

Imaginez une boite ou se cache à l'interieur une personne inconnues. Selon vous, quelle probabilité accordez-vous aux **théories** suivantes:

- *« Il y a un homme dans la boite ? »*
- *« Il y a une femme dans la boite ? »*

<center>
<img src="../images/inference_bayesienne/box.jpg" />      
</center>

**A priori** sans aucune autre information, vous allez me repondre 1 chance sur 2 pour les deux théories notées **p(Homme) = 0.5** et **p(Femme) = 0.5**.   
Si maintenant, je vous apporte une **donnée** supplémentaire en vous disant que cette personne a des cheveux longs. Alors votre **croyance** devrait changer en attribuant une plus grande probabilité à la théorie:      « *Il y a une femme dans la boite* ». En effet, le nombre de personne aux cheveux long est plus fréquent (est plus vraisemblable) chez les femmes que chez les hommes. 
En statistique, cette quantité est appelé la **vraisemblance**. C'est la probabilité d'observé des données en supposant une théorie vrai que l'on note **p(Donnée|Théorie)**. Dans notre cas, par exemple, nous pourrions dire que parmi toutes les femmes, 70% ont les cheveux longs **p(Donnée|Femme) = 70%** et chez les hommes 10% seulement ont les cheveux long **p(Donnée|Homme) = 10%**.     
Mais ce qui nous interesse ici, ce n'est pas la vraisemblance des données. Nous voulons plutôt connaître la probabilité de la théorie sachant les données, appelé probabilité **a posteriori** et que l'on note **p(Théorie|Donnée)**. Attention, ne confondez pas les deux. La probabilité d'être argentin sachant qu'on est le pape n'est pas la même chose que la probabilité d'être le pape sachant qu'on est argentin.     
Cette probabilité a posteriori se calcule grâce à la [formule de Bayes](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Bayes) :    

$$posteriori \sim apriori \times  vraisemblance $$ 
<center>Soit</center>
$$p(Theory|Donnee) \sim  p(Theorie) * p(Donnee|Theorie) $$


Ici le symbole ~ veut dire proportionnel. Si nous voulions une égalité, il faudrait normalisé la probabilité par une constante correspondant à la sommes de toutes les autres théories. On retrouverait alors la formule classique de Bayes vu dans les livres:

$$p(Theorie|Donnee) = \frac{p(Theorie) \times p(Donnee|Theorie)}{\sum^{i} p(Theorie_i) \times p(Donnee|Theorie_i) } $$

<br>
<center>Ce qui equivaut à: </center>
<br>
$$p(Theorie|Donnee)= \frac{p(Theorie) \times p(Donnee|Theorie)}{ p(Donnee)}$$


Essayons pour voir avec notre exemple et calculons les probabilités a posteriori de chaque théories :


$$p(Homme) \times p(Cheveux|Homme) = 0.5 \times 0.1 = 0.05  $$
$$p(Femme) \times p(Cheveux|Femme) = 0.5 \times 0.7 = 0.35   $$

<center>Soit : </center>

$$p(Homme|Cheveux) = 0.05 / (0.35 + 0.05) = 0.125 = 12,5\%$$
$$p(Femme|Cheveux) = 0.35 / (0.35 + 0.05) = 0.875 =  87,5\%$$


Dans cette boite, il y a donc 87,5% de chance que ce soit une femme et 12.5% de chance que ce soit un homme.       
Le dénominateur de la formule de Bayes est parfois très compliqué à calculer. Il s'annule lorsque l'on fait rapport entre les deux théories. C'est pour cette raison que les bayesiens préfèrent raisonner en pari plûtot qu'en probabilité. Je vous parie 7 contre 1, que la personne dans la boite est une femme :

$$ p(Femme|Cheveux) / p(Homme|Cheveux) = 0.35 / 0.05 = 7$$

En résumé, l'inférence bayesienne consiste à ajuster une croyance à priori par la vraisemblance des données observées pour obtenir une nouvelle croyance a posteriori. Cette  croyance peut à son tour devenir un a priori et s'ajuster au regard de nouvelles données. 
Contrairement aux «[statistiquex frequentistes](https://fr.wikipedia.org/wiki/Interpr%C3%A9tations_de_la_probabilit%C3%A9)», les bayesiens introduisent la notion d'apriori qui peut paraitre subjective aux yeux de certains. Mais c'est pourtant la toutes sa puissance. Car contrairement aux autres, les bayesiens vont pouvoir inférer des théories mêmes avec très peu de données. 


## Bayes pour les distribution continues

Dans l'exemple précédent, les croyances pour les deux théories homme et femme pouvait être representé par un [distribution](https://fr.wikipedia.org/wiki/Liste_de_lois_de_probabilit%C3%A9#Distributions_discr%C3%A8tes) discrète à deux évenements. Mais nous pourrions très bien imaginer ce problème avec plus d'évenements. Par exemple, chercher la probabilité que la personne dans la boite soit blond(e), brun(e), roux, chatain. Nous pourrions allez encore plus loin en pariant par exemple sur la taille de la personne dans la boite. Dans ce cas, il y a une infinité d'évenements et la distribution discrète devient alors une [densité de probabilité ](https://fr.wikipedia.org/wiki/Variable_al%C3%A9atoire_%C3%A0_densit%C3%A9) d'une variable aléatoire continue.

<center>
<img src="../images/inference_bayesienne/distr_continue.png" />      
</center>

Pour calculer la probabilité d'une variable aléatoire x sachant des données, la formule de Bayes s'applique de la même façon. Sauf que la somme au dénominateur devient une intégrale:

$$p(x|Donnee) = \frac{p(x) \times p(Donnee|x) }{\int p(x)p(Donnee|x) dx}$$ 


## Parier sur les paramètres d'une loi de probabilité

Une loi de probabilité est une fonction mathématique décrivant la distribution d'une variable aléatoire. Elle est définie par ses paramètres. Par exemple La moyenne (µ) et l'écart type (σ) pour une loi normale, le paramètre lambda (λ) pour une loi de poisson ou encore les paramètres (n,p) pour une loi binomiale. 
En statistique bayesienne, on va être amener faire des pari sur les paramètres d'une loi en observant des données. Supposons par exemple que la taille des individus dans la population suit une loi normale de moyenne µ. En observant les tailles de plusieurs individus dans un échantillon, on va chercher à deviner la valeur de µ. Plus exactement, on va chercher la distribution de probabilité des valeurs possible de µ.       
Dit autrement, les paramètres θ d'une loi de probabilité A décrivant une variable aléatoire X peuvent eux même être décrite comme une variable aléatoire suivant une autre loi de probabilité B. C'est très «*[meta](https://fr.wikipedia.org/wiki/M%C3%A9ta_(pr%C3%A9fixe))*» non ? Allez, un exemple concrêt pour mieux comprendre. 


## Comment savoir si une pièce est truqué ?  

Imaginez une pièce de monnaie que vous lancez et appelons thêta (θ) la probabilité de tombé sur face. Si la pièce n'est pas truqué alors la probabilité θ est de 1 chance sur 2. Mais si elle est truqué, θ peut prendre n'importe quelle valeur comprise entre 0 et 1. 
Statistiquement parlant nous dirons que la variable aléatoire x (face ou pile) suit une [loi discrète de Bernouilli](https://fr.wikipedia.org/wiki/Loi_de_Bernoulli) paramétré par θ. 

$$x \sim Bern(p=\theta)$$



Malheuresement je n'ai aucune idée de la valeur de θ. Pour l'estimer, il faut expermenter en lancant plusieurs fois la pièce et comptabilisé les faces (1) et les piles (0).
Voici par exemple ce que j'obtiens après 10 lancés : 

	Observation = [1,0,0,1,1,0,1,1,0,1]

A partir de ces données, comment faites-vous pour estimer θ ?       
Et bien grâce à l'inférence bayesienne, nous allons pouvoir calculer la distribution des valeurs possible de θ au regard de ces observations:   

$$p(θ|observations) \sim p(θ) * p(observations|θ)$$

Nous avons donc besoin de calculer un **a priori** et une **vraisemblance**.


### Calcul de l'a priori
θ est une probabilité. Sa valeur est compris entre 0 et 1. Ils nous faut donc une loi defini sur cette intervalle.
Nous pourions par exemple choisir la [loi uniforme](https://fr.wikipedia.org/wiki/Loi_uniforme_continue) sur [0-1]. C'est à dire associer à chaque valeur possible de θ la même probabilité. Ca marcherait, mais dans ce cas, l'a priori ne nous apporterait aucune information. 
Personnelement, j'aurais tendance à dire qu'une pièce truqué est peu probable, car après tout.... j'en ai jamais vu !  
Nous allons donc choisir une [loi beta](https://fr.wikipedia.org/wiki/Loi_b%C3%AAta), très souvent utilisé en inférence bayesienne pour définir l'a priori:

$$\theta \sim Beta(a=5, b=5)$$


La forme de cette loi beta depend de deux paramètres a et b illustré dans la figure suivante. 

<div class="figure">
    <img src="../images/inference_bayesienne/beta.png" />      
    <div class="legend">Différentes formes de la loi bêta selon les paramètres a et b 
    </div>
</div>   

Je propose d'utiliser la loi de parametres a = 5, et b = 5, dont la probabilité est forte sur θ=0.5 et devient plus faible au fur et à mesure que l'on se rapproche des extremités.           
En python avec le module stats de la librarie [scipy](https://www.scipy.org/):

```python
def prior(theta):
	prior = stats.beta(5,5).pdf(theta)
	return prior 
```

### Calcul de la vraisemblance 

La vraisemblance est la probabilité d'observer des données en supposant une loi de bernouilli sous une valeur spécifique de θ.
Etant donnée qu'il y a plusieurs observations indépendantes (x1,x2,x3..) nous pouvons écrire : 

$$p(x_1,x_2,x_3...x_n | \theta ) = p(x_1|\theta) \times p(x_2|\theta) \times ... \times p(x_n|\theta)  $$

En python :  

```python
def vraissemblance(observations, theta):
    L = []
    loi =  stats.bernoulli(theta)
    for x in observations:
        y =  loi.pmf(x)
        L.append(y)
    return np.prod(L)  
```

> *En realité, nous aurions pu utilisé la loi binomiale... Mais on va s'encombrer d'une autre loi


### Calcul de la posteriori 
Il suffit maintenant d'appliquer la formules de Bayes pour avoir la forme de la distrubtion des probabilités a posteriori de θ et l'afficher avec [matplotlib](https://matplotlib.org/):

```python

def posteriori(theta, observations):
    prior = stats.beta(5,5).pdf(theta)
    LD = vraissemblance(observations, theta)
    return  LD * prior

# 100 observations  
#observations = [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, .... ] 

#Afficher la distribution 
x = np.linspace(0.1,1, 100)
y = [posteriori(i, data[:100]) for i in x]
plt.plot(x,y)

```

<div class="figure">
    <img src="../images/inference_bayesienne/posteriori.png" />      
    <div class="legend">Distribution a posteriori de θ montrant une forte probabilité autour de 0.8 </div>  
</div>



Pour bien comprendre comment les données influencent l'apriori, j'ai calculé l' a posteriori avec un nombre d'observation croissant : 

<div class="figure">
    <img src="../images/inference_bayesienne/plot.svg" />      
    <div class="legend"> Distribution des probabilités theta en ajoutant succivement des données. Plus les données s'accumulent, plus notre croyance pour theta = 0.8 augmente </div>   
</div>

Sur cette figure, nous pouvons voir que sans observation la distribution des probabilité de θ est centré sur 0.5. Il s'agit là de notre a priori. Ensuite, avec l'accumulation des observations, la distribution se rapproche de 0.8 et la variance autour s'aminci.    
Ainsi nous pouvons conclure, grâce à l'inférence bayesienne, que les observations sont en faveur d'une pièce truqué.       

## Utilisation de PyMC3 
[PyMC3](https://docs.pymc.io/) est une librairie puissante permettant de faire de la programmation probabiliste. La librarie fonctionne à l'aide d'[echantillonneur MCMC](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Monte-Carlo_par_cha%C3%AEnes_de_Markov). Pour faire simple, les échantillonneurs vont générer aléatoirement des valeurs de θ suivant la distribution posteriori recherché. 
Cela permet d'éviter le calcul fastidieux de l'intégrale vu plus haut, et construire des modèles bien plus complexes avec de nombreux paramètres. 
Voici le même algorithme vu plus haut mais écrit cette fois avec PyMC3: 

```python	
import pymc3 as pm
import arviz as az

with pm.Model() as model:
	# Definition d'un a priori suivant une loi beta paramètré par alpha et beta 
    theta = pm.Beta("theta", alpha=5, beta=5) 

    # Définition de la vraisemblance des données sous l'hypothèse theta 
    y = pm.Bernoulli("y", p=theta, observed = data)
    
    # Echantillonnage de 1000 valeurs de theta
    trace = pm.sample(1000, random_seed=123)


# Visualisation des résultats avec la librarie arviz
az.plot_trace(trace)


```

<div class="figure">
    <img src="../images/inference_bayesienne/arviz.png" />      
    <div class="legend">A gauche: Distribution de probabilité de thetas. A droite: echantillonnage du paramètre theta</div>  
</div>

## Réference 
[Blog de Sciencetonnante](https://sciencetonnante.wordpress.com/2012/10/15/linference-bayesienne-bayes-level-2/)
[Chaine youtube de Lee](https://www.youtube.com/channel/UC0NCbj8CxzeCGIF6sODJ-7A) 
[Livre: Bayesian Analysis with Python](https://www.fnac.com/livre-numerique/a12861451/Osvaldo-Martin-Bayesian-Analysis-with-Python?Origin=fnac_google#FORMAT=ePub)



<img src="../images/inference_bayesienne/frequentists_vs_bayesians.png" />   

https://dun.unistra.fr/ipm/unit/bayesien/co/1a_1_1.html