Title: Inférence bayesienne et python
Slug: inference_bayesienne
Date: 2020-03-18 11:44:42
Modified: 2020-03-18 11:44:42
Tags: statistique
Category: informatique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/stat_banner.jpg


Dans mon entourage, qu'il soit médecin ou bioinformaticiens, peu de gens connaisse l'inférence bayesienne. Pourtant sans même le savoir, nous en faisons quotidiennenent. Que ce soit pour estimer la probabilité d'un infarctus devant une douleur thoracique ou pour déviner le menu à la cantine rien qu'à l'odeur. En deux mots, l'inférence bayesienne nous permet de quantifer nos incertitudes. 
Dans ce billet, nous allons définir l'inférence bayesienne et son vocabulaire à partir d'exemple intuitive. Puis, nous l'appliquerons à travers un exemple codé en python et la librairie PyMC3. 



# L'inférence bayesienne selon Laplace

Imaginez une boite ou se cache à l'interieur une personne inconnues. Selon vous, quelle probabilité accordez-vous aux **théories** suivantes:

- *« Il y a un homme dans la boite ? »*
- *« Il y a une femme dans la boite ? »*

<center>
<img src="../images/inference_bayesienne/box.jpg" />      
</center>

**A priori** sans aucune autre information, et dans ce **contexte**, vous allez me repondre 1 chance sur 2, soit une probabilité de 0.5 pour les deux théories notées *p(Homme) = 0.5* et *p(Femme) = 0.5*.      
Si maintenant, je vous apporte comme **donnée** supplémentaire que cette personne a des cheveux longs. Alors votre **croyance** ou **crédence** devrait changer en attribuant une plus grande probabilité à la théorie: « *Il y a une femme dans la boite* ». 
En effet, le nombre de personne aux cheveux long est plus fréquent, est plus **vraisemblable** chez les femmes que chez les hommes. 
En statistique, cette quantité est appelé la vraisemblance. C'est la probabilité d'observé des données en supposant une théorie vrai que l'on note *p(Donnée|Théorie)*. Dans notre cas, par exemple, nous pourrions dire que parmi toutes les femmes, 60% ont les cheveux long *p(Donnée|Femme) = 70%* alors chez les hommes 10% seulement ont les cheveux long *p(Donnée|Homme) = 10%*.        
Mais ce qui nous interesse ici, ce n'est pas la vraisemblance des données. Nous voulons plutôt connaître la probabilité de la théorie connaissant les données, appelé probabilité **a posteriori** et que l'on note *p(Théorie|Donnée)*. Attention, ne confondez pas les deux. La probabilité d'être argentin sachant qu'on est le pape (100%) n'est pas la même chose que la probabilité d'être le pape sachant qu'on est argentin ( 0.00001%).     
Cette probabilité a posteriori se calcule grâce à la formule de Bayes :    

$$posteriori \sim apriori \times  vraisemblance $$ 
<center>Soit</center>
$$p(Theory|Donnee) \sim  p(Theorie) * p(Donnee|Theorie) $$


Ici le symbole ~ veut dire proportionnel. Si nous voulions une égalité, il faudrait normalisé la probabilité par une constante correspondant à la sommes de toutes les autres théories. On retrouverait alors la formule classique de Bayes vu dans les livres:

$$p(Theorie|Donnee) = \frac{p(Theorie) \times p(Donnee|Theorie)}{\sum^{i} p(Theorie_i) \times p(Donnee|Theorie_i) } $$

<br>
<center>Ce qui equivaut à: </center>
<br>
$$p(Theorie|Donnee)= \frac{p(Theorie) \times p(Donnee|Theorie)}{ p(Donnee)}$$


Nous pouvons reprendre notre exemple précédent et calculer les probabilités a posteriori de chaque théories :


$$p(Homme) * p(Cheveux|Homme) = 0.5 \times 0.1 = 0.05  $$
$$p(Femme) * p(Cheveux|Femme) = 0.5 \times 0.7 = 0.35   $$

<center>Soit : </center>

$$p(Homme|Cheveux) = 0.05 / (0.35 + 0.05) = 0.125 = 12,5\%$$
$$p(Femme|Cheveux) = 0.35 / (0.35 + 0.05) = 0.875 =  87,5\%$$


Dans cette boite, il y a donc 87,5% de chance que ce soit une femme et 12.5% de chance que ce soit un homme.       
Le dénominateur de la formule de Bayes est parfois très compliqué à calculer. Il s'annule lorsqu'on calcule le rapport entre les deux théories. C'est pour cette raison que les bayesiens préfèrent raisonner en pari plûtot qu'en probabilité.

$$ p(Femme|Cheveux) / p(Homme|Cheveux) = 0.35 / 0.05 = 7$$

Je vous parie 7 contre 1, que la personne dans la boite est une femme ! 

En résumé, l'inférence bayesienne consiste à ajuster une croyance à priori par la vraisemblance des données observées pour obtenir une nouvelle croyance a posteriori . Cette  croyance peut à son tour devenir un a priori et s'ajuster au regard de nouvelles données. 
Tous les jours, votre cerveaux utilisent des a priori et les données qu'ils recoient pour quantifier ses incertitudes. 
Si je tousse là toute de suite, vous pensez quoi  ? 


## Bayes pour les distribution continues

Dans l'exemple précédent, les croyances pour la théorie de l'homme et de la femme pouvait être representé par un distribution discrète à deux évenements. Nous pourrions très bien imaginer un problème avec plus d'évenements. Par exemple, chercher la probabilité que la personne dans la boite soit blond(e), brun(e), roux, chatain. Mais nous pourrions allez encore plus loin en pariant par exemple sur la taille de la personne dans la boite. Il y a dans ce cas une infinité de valeurs possible. Les théories deviennent une variable aléatoire et la distribution discrète deviet une densité de probabilité continue.



<center>
<img src="../images/inference_bayesienne/distr_continue.png" />      
</center>

La formule de Bayes s'écrit alors de façon suivante avec la somme qui devient une intégrale : 

$$p(x|Donnee) = \frac{p(x) \times p(Donnee|x) }{\int p(x)p(Donnee|x) dx}$$ 


## Parier sur les paramètres d'une loi de probabilité

Une loi de probabilité est une fonction mathématique décrivant la distribution d'une variable aléatoire. Par exemple la taille dans une population. Elle est défini par ses paramètres. La moyenne (µ) et l'écart type (σ) pour une loi normale, le paramètre lambda (λ) pour une loi de poisson ou encore les paramètres (n,p) pour une loi binomiale. 
En statistique bayesienne, on va être amener faire des pari sur les paramètres d'une loi en observant des données. Supposons par exemple que la taille des individus dans la population suit une loi normale de moyenne µ. En observant les tailles de plusieurs individus dans un échantillon, on va chercher à deviner la valeur de µ. Plus exactement, on on va chercher la distribution de probabilité des valeurs possible de µ. 
Autrement dit, les paramètres θ d'une loi de probabilité A décrivant une variable aléatoire X peuvent eux même être décrite comme une variable aléatoire suivant une autre loi de probabilité B. C'est très «*meta*» non ? Allez, un exemple concrêt pour mieux comprendre. 


## Comment savoir si une pièce est truqué ?  

Imaginez une pièce de monnaie que vous lancez et appelons thêta (θ) la probabilité de tombé sur face. Si la pièce n'est pas truqué alors la probabilité θ est de 1 chance sur 2, sinon n'importe quel valeurs possible entre 0 et 1. 
Ici, la variable aléatoire x (face ou pile) suit une loi discrète de Bernouilli de paramètre θ. 

$$x \sim Bern(p=\theta)$$



Malheuresement je n'ai aucune idée de la valeur de theta. Pour l'estimer, il faut expermenter en lancant plusieurs fois la pièce.
Voici ce que j' obtiens : 

	Observation = [1,0,0,1,1,0,1,1,0,1]

A partir de ces données, nous allons calculer la distribution des valeurs possible de θ en utilisant la formule de Bayes.  

$$p(θ|observations) \sim p(θ) * p(observations|θ)$$

Nous avons donc besoin de calculer un a priori et une vraisemblance.


### Calcul de l'a priori
θ est une probabilité. Sa valeur est compris entre 0 et 1. Ils nous faut donc une loi defini sur cette intervalle.
Nous pourions par exemple choisir la loi uniforme sur [0-1]. C'est à dire associer à chaque valeur possible de θ la même probabilité. Ca marcherait, mais dans ce cas, l'a priori ne nous apporterait aucune information. 
Personnelement, j'aurais tendance à dire qu'une pièce truqué est peu probable, car j'en ai jamais vu après tout ... 
Nous allons donc choisir une loi beta, très souvent utilisé en inférence bayesienne pour définir l'a priori.

$$\theta \sim Beta(a=5, b=5)$$


La forme de cette loi beta depend de deux paramètres a et b illustré dans la figure suivante. 

<div class="figure">
    <img src="../images/inference_bayesienne/beta.png" />      
    <div class="legend">Différentes formes de la loi bêta selon les paramètres a et b 
    </div>
</div>   



Je propose d'utiliser la loi de parametres a = 5, et b = 5, dont la probabilité est forte sur θ=0.5. 
En python, la librairie scipy me permet d'écrire cette probabilité a priori sur theta: 

```python
def prior(theta):
	prior = stats.beta(5,5).pdf(theta)
	return prior 
```

### Calcul de la vraisemblance 

La vraisemblance est la probabilité d'observer des données en supposant une loi de bernouilli sous théta
Etant donnée qu'il y a plusieurs observations indépendante (x1,x2,x3..) nous pouvons écrire : 

$$p(x_1,x_2,x_3...x_n | \theta ) = p(x_1|\theta) \times p(x_2|\theta) \times ... \times p(x_n|\theta)  $$

La vraisemblance des données sous θ peut alors s'écrire de la façon suivante :  

```python
def vraissemblance(observations, theta):
    L = []
    loi =  stats.bernoulli(theta)
    for x in observations:
        y =  loi.pmf(x)
        L.append(y)
    return np.prod(L)  
```

<center> <quote>En realité, nous aurions pu utilisé la loi binomiale... Mais on va s'encombrer d'une autre loi</quote></center>


### Calcul de la posteriori 
Il suffit maintenant d'appliquer la formules de Bayes pour connaître la forme de la distrubtion des probabilités de theta.

```python

def posteriori(theta, observations):
    prior = stats.beta(5,5).pdf(theta)
    LD = vraissemblance(observations, theta)

    return  LD * prior
```

Pour bien comprendre comment les données influencent l'apriori, j'ai calculé iterativement la probabilité a posteriori en consommant les données petit à petit. 

```python

#observations = [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, ...]

# valeurs possible de theta entre 0 et 1
theta = np.linspace(0,1, 100)

# On injecte de 10 en 10, nos observations 
for n in range(0, 100, 10):
    
    # On récupère les n premieres observations
    subset = observations[:n]

    # On calcul la vraissemblance de chaque valeur de theta 
    p = [posteriori(i, subset) for i in theta]
    
    plt.plot(theta, p)

```

<div class="figure">
    <img src="../images/inference_bayesienne/plot.svg" />      
    <div class="legend"> Distribution des probabilités theta en ajoutant succivement des données. Plus les données s'accumulent, plus notre crédence pour theta = 0.8 augmente </div>   
</div>




## Utilisation de PyMC3 
PyMC3 est une librairie puissante permettant de faire de la programmation probabiliste. La librarie fonctionne à l'aide d'echantillonneur MCMC. Pour faire simple, les échantillonneurs vont générer aléatoirement des valeurs de théta suivant la distribution rechercher. 
Cela permet d'éviter le calcul fastidieux de l'intégrale vu plus haut, et construire des modèles bien plus complexes avec de nombreux paramètres. 
Voici le même algorithme vu plus haut mais écrit avec PyMC3 : 

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



https://dun.unistra.fr/ipm/unit/bayesien/co/1a_1_1.html