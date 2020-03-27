Title: Inférence bayésienne et python
Slug: inference_bayesienne
Date: 2020-03-18 11:44:42
Modified: 2020-03-25 19:43:23
Tags: statistique, machine learning, python
Category: informatique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/stat_banner.jpg


Cela fait un moment que j'avais envie de publier sur l'*inférence bayésienne*. Mon intérêt pour ce sujet a été éveillé par la lecture du livre [La formule du savoir](https://laboutique.edpsciences.fr/produit/1035/9782759822614/La%20formule%20du%20savoir) par [Nguyên Hoang Lê](https://fr.wikipedia.org/wiki/L%C3%AA_Nguy%C3%AAn_Hoang).     
En deux mots, l'inférence bayésienne est une méthode permettant d'ajuster vos croyances par des observations.
Dans ce billet je définirai l'inférence bayésienne ainsi que son vocabulaire, à partir d'exemples intuitifs. Puis, j'appliquerai la méthode à l'aide d'un programme informatique rédigé en langage *python*, d'abord sous forme d'un programme autonome et, ensuite, en m'appuyant sur la librairie de programmation probabiliste [PyMC3](https://docs.pymc.io/). 

## La probabilité des causes
Selon le principe de causalité, la connaissance exhaustive d'un phénomène, appelé *cause*, permet de **prédire** le phénomène résultant, appelé *effet*. La mécanique newtonienne permet, par exemple, de prédire la trajectoire d'un javelot lancé par un athlète. Un modèle statistique permet de prédire la taille d'une population. Une fonction mathématique permet de calculer une valeur.       
Mais l'inverse est également possible. En observant les effets, nous pouvons **inférer** sur la probabilité des causes. Par exemple, en observant des traces de pas, nous pouvons supposer la présence du tueur sur la scène de crime. En observant les effets gravitationnels, les astrophysiciens peuvent supposer la présence d'une planète.        
En général, l'effet observable peut être parfaitement décrite alors que la description exhaustive de la cause est la plupart du temps hors de portée. L'inférence bayésienne permet de calculer un poids pour l'ensemble des paramètres de la cause à partir de l'effet observé. Le processus qui fait évoluer un système de la cause (par exemple la gravitation) vers l'effet (par exemple chute de la pomme) est décrit par une théorie (par exemple théorie de la gravitation) formalisée par les mathématiques (par exemple mécanique newtonienne).         

<center>
<img src="../images/inference_bayesienne/predire_inferer.png" />      
</center>


## Qui est dans la boite ? 

Imaginez une boite dans laquelle se cache une personne inconnue. Selon vous, quelle probabilité accordez-vous aux **hypothèses** suivantes:

- *la personne est un homme*
- *la personne est une femme*

<center>
<img src="../images/inference_bayesienne/box.jpg" />      
</center>

A priori, sans aucune autre information, on serait tenter de répondre que la probabilité est 50-50. Appelons cette probabilité, probabilité **a priori** notée **p(hypothèse)**, soit dans notre exemple **p(homme) = p(femme) = 0.5**.
Notons que la somme des probabilités doit être égale à 1. 
Si maintenant, nous disposons d'une **donnée** supplémentaire, à savoir que la personne inconnue a les cheveux longs, la probabilité que l'inconnu soit un homme ou une femme change en augmentant **p(femme)** et en diminuant d'autant **p(homme)**. Nous avons supposé que statistiquement les femmes ont plus tendance à porter les cheveux longs que les hommes.  
Cette nouvelle probabilité est appelée, en analyse statistique, **vraisemblance des données** : c'est la probabilité qu'une hypothèse est vraie en prenant une information donnée. Elle est notée **p(donnée|Hypothèse)**. Admettons, par l'exemple, que parmi toutes les personnes existantes, 70% des femmes et 10% des hommes ont les cheveux longs. Dans ce cas **p(cheveux_longs|femme) = 70%** et **p(cheveux_longs|Homme) = 10%**.     
Mais ce qui nous intéresse ici, ce n'est pas la vraisemblance des données. Nous voulons plutôt connaître la probabilité de la théorie sachant les données, appelée probabilité **a posteriori** et que l'on note **p(Théorie|Donnée)**. (Attention, ne confondez pas les deux. La probabilité d'être argentin sachant qu'on est le pape n'est pas la même chose que la probabilité d'être le pape sachant qu'on est argentin.)        
La probabilité a posteriori se calcule grâce à la [formule de Bayes](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Bayes):    

$$posteriori \sim priori \times  vraisemblance $$ 
<center>Soit</center>
$$p(T|D) \sim  p(T) * p(D|T) $$
<center>Avec T: Théorie et D: Données</center>

Ici le symbole ~ signifie proportionnel. Si nous voulions une égalité, il faudrait normaliser par une constante correspondant à la somme de toutes les autres théories. On retrouverait alors la formule classique de Bayes vu dans les livres d'école:

$$p(T|D) = \frac{p(T) \times p(D|T)}{\sum^{i} p(T_i) \times p(D|T_i) } $$

<br>
<center>Ce qui équivaut à: </center>
<br>
$$p(T|D)= \frac{p(T) \times p(D|T)}{ p(D)}$$

Essayons pour voir, dans notre exemple, de calculer les probabilités a posteriori de chaque théorie :

$$p(Homme) \times p(Cheveux|Homme) = 0.5 \times 0.1 = 0.05  $$
$$p(Femme) \times p(Cheveux|Femme) = 0.5 \times 0.7 = 0.35   $$

<center>Et donc: </center>

$$p(Homme|Cheveux) = \frac{0.05} {(0.35 + 0.05)} = 12,5\%$$
$$p(Femme|Cheveux) = \frac{0.35} {(0.35 + 0.05)} =  87,5\%$$


Dans cette boite, il y a donc 87,5% de chance que ce soit une femme et 12.5% de chance que ce soit un homme.      

Cependant le bayésiens préfèrent raisonner avec des paris plutôt qu'avec des probabilités. En effet, le dénominateur de la formule de Bayes est parfois très compliqué à calculer. Il s'annule lorsque l'on fait le rapport entre les deux théories. 
Dans notre cas :
$$ \frac{p(Femme|Cheveux)}{p(Homme|Cheveux)} = \frac{0.35}{0.05} = 7$$

Je peux alors vous faire un pari 7 contre 1 qu'il s'agit d'une femme dans la boîte. Retenez de cela que le bayésien évalue toujours une théorie par rapport aux autres théories. Les probabilités perdent leurs caractères absolus pour devenir relatif. 

En résumé, l'inférence bayésienne consiste à ajuster une croyance a priori par la vraisemblance des données observées pour obtenir une nouvelle croyance a posteriori. Cette croyance peut à son tour être considéré comme un priori et s'ajuster au regard de nouvelles données. En les accumulants, nos croyances convergent alors vers la "vérité".          
Un exercice, dans le contexte du [Covid-19](https://fr.wikipedia.org/wiki/Maladie_%C3%A0_coronavirus_2019) pendant votre confinement. Si je tousse là,  maintenant, quelle pari faite vous sur le fait que je sois contaminé ou pas ? C'est marrant, mais vous auriez certainement pas dit la même chose un an plutôt. Pourquoi à votre avis ? A cause de vos a priori !

## Bayes pour les distributions continues

Dans l'exemple précédent, les croyances pour les deux théories hommes et femmes pouvaient être représentées par une [distribution](https://fr.wikipedia.org/wiki/Liste_de_lois_de_probabilit%C3%A9#Distributions_discr%C3%A8tes) discrète à deux événements. Mais nous pourrions très bien imaginer ce problème avec plus d'événements. Par exemple, chercher la probabilité que la personne dans la boite soit blond(e), brun(e), roux, châtain. Nous pourrions allez encore plus loin en pariant par exemple sur la taille de la personne dans la boite. Dans ce cas, il y a une infinité d'événements et la distribution discrète devient une [densité de probabilité ](https://fr.wikipedia.org/wiki/Variable_al%C3%A9atoire_%C3%A0_densit%C3%A9) d'une variable aléatoire continue.

<center>
<img src="../images/inference_bayesienne/distr_continue.png" />      
</center>

Pour calculer la probabilité de cette variable aléatoire x sachant des données, la formule de Bayes s'applique de la même façon. Sauf que la somme au dénominateur devient une intégrale:

$$p(x|Donnee) = \frac{p(x) \times p(Donnee|x) }{\int p(x)p(Donnee|x) dx}$$ 


## Parier sur les paramètres d'une loi de probabilité

Une loi de probabilité est une fonction mathématique décrivant la distribution d'une variable aléatoire. Elle est définie par ses paramètres. Par exemple la moyenne (µ) et l'écart type (σ) pour une [loi normale](https://fr.wikipedia.org/wiki/Loi_normale), le paramètre lambda (λ) pour une [loi de poisson](https://fr.wikipedia.org/wiki/Loi_de_poisson) ou encore les paramètres (n,p) pour une [loi binomiale](https://fr.wikipedia.org/wiki/Loi_binomiale). 
En statistique bayésienne, on va être amené faire des paris sur les paramètres d'une loi après avoir observer des données. Supposons par exemple que la taille des individus dans la population suit une loi normale de moyenne µ. En observant les tailles de plusieurs individus dans un échantillon, nous pouvons essayer de deviner la valeur de µ. Plus exactement, nous allons chercher la distribution de probabilité des valeurs possible de µ.       
Dits autrement, le paramètre θ d'une loi de probabilité A décrivant une variable aléatoire X peut lui même être décrits comme une variable aléatoire suivant une autre loi de probabilité B. C'est très «*[meta](https://fr.wikipedia.org/wiki/M%C3%A9ta_(pr%C3%A9fixe))*» je sais.. Allez, un exemple concrêt pour mieux comprendre. 


## Comment savoir si une pièce est truquée ?  

Imaginez une pièce de monnaie que vous lancez et appelons thêta (θ) la probabilité de tomber sur face. Si la pièce n'est pas truquée alors la probabilité θ est de 1 chance sur 2. Dans le cas contraire, θ peut prendre n'importe quelle valeur comprise entre 0 et 1. 
Statistiquement parlant nous dirons que la variable aléatoire x (face ou pile) suit une [loi discrète de Bernouilli](https://fr.wikipedia.org/wiki/Loi_de_Bernoulli) paramétré par θ. 

$$x \sim Bern(p=\theta)$$

Malheureusement je n'ai aucune idée de la valeur de θ. Pour l'estimer, il faut expérimenter en lançant plusieurs fois la pièce et comptabiliser les faces (1) et les piles (0).
Voici par exemple ce que j'obtiens après 10 lancés : 

	Observation = [1,0,0,1,1,0,1,1,0,1]

À partir de ces données, comment faites-vous pour estimer θ ?       
Et bien grâce à l'inférence bayésienne, nous allons pouvoir calculer la distribution des valeurs possible de θ au regard de ces observations:   

$$p(θ|observations) \sim p(θ) * p(observations|θ)$$

Il nous faut donc un **a priori** et une **vraisemblance**.


### Calcul de l'a priori
θ est une probabilité. Sa valeur est comprise entre 0 et 1. Ils nous faut donc une loi définie sur cet intervalle.
Nous pourrions par exemple choisir la [loi uniforme](https://fr.wikipedia.org/wiki/Loi_uniforme_continue) sur [0-1]. C'est à dire associer à chaque valeur possible de θ la même probabilité. Ça marcherait, mais dans ce cas, l'a priori ne nous apporterait aucune information. 
Personnellement, j'aurais tendance à dire qu'une pièce truquée est peu probable, car après tout.... je n’en ai jamais vu !  
Nous allons donc choisir une [loi bêta](https://fr.wikipedia.org/wiki/Loi_b%C3%AAta), très souvent utilisé en inférence bayésienne pour définir l'a priori:

$$\theta \sim Beta(a, b)$$

La forme de cette loi bêta dépend de deux paramètres a et b illustrés dans la figure suivante. 

<div class="figure">
    <img src="../images/inference_bayesienne/beta.png" />      
    <div class="legend">différentes formes de la loi bêta selon les paramètres a et b 
    </div>
</div>   

Je vous propose d'utiliser la loi symétrique de paramètres a = 5, et b = 5, dont la probabilité est forte sur θ=0.5 et devient plus faible au fur et à mesure que l'on se rapproche des deux extrémités.           
A l'aide du module stats de la librarie [scipy](https://www.scipy.org/), nous pouvons écrire en python: 

```python
def prior(theta):
	prior = stats.beta(5,5).pdf(theta)
	return prior 
```

### Calcul de la vraisemblance 

La vraisemblance est la probabilité d'observer des données en supposant vrai la loi de Bernoulli sous une valeur spécifique de θ.
Etant donné qu'il y a plusieurs observations indépendantes (x1,x2,x3..) nous pouvons écrire : 

$$p(x_1,x_2,...x_n | \theta ) = p(x_1|\theta) \times p(x_2|\theta) \times ... \times p(x_n|\theta) $$

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

> *En réalité, nous aurions pu utiliser la loi binomiale... Mais nous n'allons pas nous encombrer d'une autre loi*.


### Calcul de l' a posteriori 
Il suffit maintenant d'appliquer la formule de Bayes pour avoir la forme de la distribution des probabilités a posteriori de θ et l'afficher avec [matplotlib](https://matplotlib.org/):

```python

def posteriori(theta, observations):
    prior = prior(theta)
	likelihood = vraissemblance(observations, theta)
    return  likelihood * prior

# 100 observations  
#observations = [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, .... ] 

# Calculer les probabilités pour plusieurs valeurs de θ 
x = np.linspace(0.1,1, 100)
y = [posteriori(theta, data[:100]) for theta in x]
plt.plot(x,y)

```

<div class="figure">
    <img src="../images/inference_bayesienne/posteriori.png" />      
    <div class="legend">Distribution a posteriori de θ montrant une forte probabilité autour de 0.8 </div>  
</div>

Pour bien comprendre ce graphique, j'ai calculé l' a posteriori avec un nombre d'observations croissant : 

<div class="figure">
    <img src="../images/inference_bayesienne/plot.svg" />      
    <div class="legend"> Distribution des probabilités θ en ajoutant successivement des observations. Plus les données s'accumulent, plus notre croyance pour θ = 0.8 augmente </div>   
</div>

Sans observation, la distribution des probabilités de θ est centré sur 0.5. Il s'agit là de notre a priori. Ensuite, avec l'accumulation progressive des observations, la distribution se rapproche de 0.8 et la variance s'amincit.    
Ainsi nous pouvons conclure, grâce à l'inférence bayésienne, que les observations sont en faveur d'une pièce truquée avec un θ probablement de 0.8. 
Effectivement.. J'avais généré automatiquement les observations avec une loi de Bernouilli paramétré par 0.8 et je vous ai caché volontairement le code pour éviter les confusions! 

## Utilisation de PyMC3 
Pour finir, voici le même algorithme, mais écris cette fois en utilisant la librairie [PyMC3](https://docs.pymc.io/). Il s'agit d'une librairie puissante et très simple permettant de faire de la programmation probabiliste. La librarie fonctionne à l'aide d'[echantillonneur MCMC](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Monte-Carlo_par_cha%C3%AEnes_de_Markov). Pour faire simple, les échantillonneurs vont générer aléatoirement des valeurs de θ suivant la distribution a posteriori recherchée. 
Cela permet d'éviter le calcul fastidieux de l'intégrale vu plus haut, et construire des modèles bien plus complexes avec de nombreux paramètres. 

```python	
import pymc3 as pm
import arviz as az

#observations = [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, .... ] 

with pm.Model() as model:
	# Definition d'un a priori suivant une loi bêta paramétrée par alpha et bêta 
    theta = pm.Beta("theta", alpha=5, beta=5) 

    # Définition de la vraisemblance des données sous l'hypothèse thêta 
    y = pm.Bernoulli("y", p=theta, observed = data)
    
    # Échantillonnage de 1000 valeurs de thêta
    trace = pm.sample(1000, random_seed=123)


# Visualisation des résultats avec la librarie arviz
az.plot_trace(trace)


```

<div class="figure">
    <img src="../images/inference_bayesienne/arviz.png" />      
    <div class="legend">Distribution des probabilités de θ avec <a href="https://en.wikipedia.org/wiki/Credible_interval)(Highest Posterior Density interval"> l'interval de crédibilité appelé HPD </a>  </div>  
</div>

Voilà pour ce billet qui est déjà assez long ! Je vous invite fortement à regarder les références plus bas. L'ensemble du code ayant servi à écrire ce billet est disponible et éditable sur [google colab](https://colab.research.google.com/drive/14RWMzPAfN6u-n0WrurPzjIbliv6ecHu9).    
Il y a également [ce billet](https://github.com/dridk/blog/blob/master/content/inference_bayesienne.md) pour anglophone dans le contexte du Covid-19 qui fait des prédictions bayésienne sur la cinétique de l'épidémie.



## Référence 
- [Blog de Sciencetonnante](https://sciencetonnante.wordpress.com/2012/10/15/linference-bayesienne-bayes-level-2/)
- [chaine YouTube de Lee](https://www.youtube.com/channel/UC0NCbj8CxzeCGIF6sODJ-7A) 
- [Introduction aux statistiques bayésiennes](https://dun.unistra.fr/ipm/unit/bayesien/co/1a_1_1.html)
- [Livre: Bayesian Analysis with Python](https://www.fnac.com/livre-numerique/a12861451/Osvaldo-Martin-Bayesian-Analysis-with-Python?Origin=fnac_google#FORMAT=ePub)


