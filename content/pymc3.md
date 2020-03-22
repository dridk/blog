Title: Inférence bayesienne en Python
Slug: inference-bayesienne
Date: 2020-03-18 11:44:42
Modified: 2020-03-18 11:44:42
Tags: 
Category: 
Author: 
Lang: 
Summary: 
Status: Draft
SIDEBARIMAGE:../images/common/stat_banner.jpg


L'inférence bayesienne est partout. Sans même le savoir, vous en faîtes quotidiennenement. Que ce soit pour deviner qui sonne à la porte ou pour prédire les pensée d'une personne rien qu'en la regardant.
Je vais essayer dans ce billet de vous définir l'inférence bayesienne et son vocabulaire de la façon la plus clair qu'il soit avec plusieurs exemples. Et nous finirons par implémenter cette méthode en python grâce à la librarie PyMC3.




# L'inférence bayesienne selon Laplace

Imaginez une boite ou se cache à l'interieur une personne. Selon vous, quelle est la probabilité que cette personne soit une femme ? Soit un homme ? 

<center>
<img src="../images/inference_bayesienne/box.jpg" />      
</center>

**A priori** sans aucune autre information, vous allez me repondre 1 chance sur 2, soit une probabilité 0.5 pour les deux évenements noté *p(Homme) = 0.5* et *p(Femme) = 0.5*.
Si maintenant, je vous apporte comme **donnée** supplémentaire que cette personne a des cheveux longs. Alors votre **croyance** devrait changer en attribuant une plus grande probabilité à la **théorie**: "Il y a une femme dans la boite". 
En effet, le nombre de personne aux cheveux long est plus fréquent (vraisemblable) chez les femmes que chez les hommes. 
En statistique, cette quantité est appelé la vraisemblance. C'est à la probabilité d'observé des données en supposant une théorie vrai que l'on note p(Donnée|Théorie). Dans notre cas, nous pourrions dire par exemple que parmi les femmes 70% ont les cheveux long p(Donnée|Femme) = 70% et parmi les hommes 10% seulement ont les cheveux long p(Donnée|Homme) = 10%. 
A partir de votre a priori et de la vraisemblance des données apporté, vous allez pouvoir calculer une nouvelle croyance a posteriori noté p(Théorie|Donnée). Par exemple p(Femme|Donnée) est la probabilité qu'il y est une femme dans la boite sachant qu'elle a des cheveux longs. Attention, ne confondez pas p(Théorie|Donnée) et p(Donnée|Théorie). La probabilité d'être argentin sachant qu'on est le pape n'est pas la même chose que la probabilité d'être argentin sachant qu'on est le pape. 

Faire de l'inférence bayesienne c'est ajuster une croyance a priori grâce à **la vraisemblance de données observés** pour obtenir une nouvelle croyance a posteriori. 

Distribution a priori => Distribution a posteriori 

La relation de ces 3 élements est donnée par la relation de proportionnalité suivante : 

Posteriori ~ Priori * Vraisemblance

$$p(T|D) % p(T) * p(D|T)$$

Dans notre cas :

$$
p(F|Donnée) % p(F) * p(Donnée|F) \\
p(H|Donnée) % p(H) * p(Donnée|F) \\
$$

Ici le symbole ~ veut dire proportionnel. Si nous voulions une égalité, il faudrait normalisé la posteriori pour que la valeur soit toujours comprise entre 0 et 1. On retrouverait alors la formule de Bayes comme je l'avais déjà défini dans un billet précédent.

p(T|D) = p(T) * p(D|T) / Sum (pT) * p(D|T)
" legend "

Dans notre exemple : 

p(F|Donnée) = p(F) | p(Donnee|F) / truc ... = Vrai résultat. 

Dans la plus part des cas, nous pouvons nous contenter de la relation entre les deux théories au lieu de calculer une probabilité. Par exemple, ici nous avons x fois plus de chance d'être une femme qu'en homme. Dit autrement, je fais le pari x contre y. Dans ce cas, le dénominateur complexe, n'a pas besoin d'être calculé et la relation de proportionnalité suffit.



## Bayes pour les distribution continues

Dans l'exemple précédent, les croyances pour la théorie de l'homme et de la femme pouvait être representé par un distribution discrète à deux évenements. Nous pourrions très bien imaginer un problème avec plus d'évenements. Par exemple, chercher la probabilité que la personne dans la boite soit blond(e), brun(e), roux, chatain. Mais nous pourrions allez encore plus loin en pariant par exemple sur la taille de la personne dans la boite. Il y a dans ce cas une infinité de valeurs possible. Les théories discrètes deviennent une variable aléatoire et la distribution discrète devient une densité de probabilité continue.

Graph => 2 evenement VERS distribution

La formule de Bayes s'écrit alors de façon suivante avec la somme qui devient une intégrale : 

p(X|D) = p(X) * p(D|X) / integral ... 


## Parier sur les paramètres d'une loi de probabilité

Une loi de probabilité est une fonction mathématique décrivant la distribution d'une variable aléatoire. Par exemple, les tailles des individus dans une population peut être décrite par une loi normale donnant la fréquence de chaque taille observé. (En vrai, c'est faux pour une densité de probabilité, mais le but c'est de comprendre).
Une loi est défini par ses paramètres. Par exemple la moyenne et l'écart type pour une loi normale, le paramètre lambda pour une loi de poisson ou encore les paramètres (n,p) pour une loi binomiale.
En statistique bayesienne, on va être amener à parier sur les paramètres d'une loi inconnues à partir d'observation de donnée.
Autrement dit, les paramètres d'une loi de probabilité décrivant une variable aléatoire X peuvent eux même être décrite comme une variable aléatoire théta suivant une AUTRE loi de probabilité. 
Ces lois de probabilités sont disponnible en python depuis scipy.stats.

## Parier sur une pièce 

Imaginez une pièce de monnaie que vous lancez et appelons theta la probabilité de tombé sur face. Si la pièce n'est pas truqué alors la probabilité theta est de 1 chance sur 2, sinon n'importe quel valeurs possible entre 0 et 1. 
Cette distribution discrètes des évenements Face et Pile suit une loi de Bernouilli de paramètre theta. 

Image : Bernouilli 

Le problème est que je n'ai aucune idée de la valeur de theta. Comment faire pour l'estimer ? 
Et bien, il suffit d'experimenter en lancant plusieurs fois la pièce.
Voici ce qu'on obtient : 

	Data = [1,0,0,1,1,0,1,1,0,1]
	theta = ? 


A partir de ces données, nous allons pouvoir calculer la distribution de probabilité de theta en suivant la formule de Bayes : 

p(theta|Data) ~ p(theta) * p(Data|theta)


### Calcul de l'a priori
La valeur de theta est compris entre 0 et 1. Ils nous faut donc une loi defini sur cette intervalle.
Nous pourions par exemple choisir la loi uniforme sur [0-1]. C'est à dire associer à chaque valeur de theta la même probabilité. Ca marcherait, mais ça ne serait pas informatif et la posteriori dependrait uniquement de le vraisemblance. 
Nous allons donc plûtôt choisir la loi béta qui est très souvent utilisé en inférence bayesienne pour définir la prior.
La forme de cette loi beta depend de deux paramètres a et b illustré dans la figure suivante. 

[ i ]

Je propose d'utiliser la loi de parametres a = 5, et b = 5, dont la probabilité est forte sur theta=0.5. 
Après tout, les pièces de monnaies truqué, ça ne court pas les rues. 
En implementant mon a priori p(theta) en python: 

		def prior(theta):
	    	prior = stats.beta(5,5).pdf(theta)
	    	return 


### Calcul de la vraisemblance 

La vraisemblance est la probabilité d'observer les données D en supposant theta vrai avec une loi de bernouilli.
Etant donnée qu'il y a plusieurs observations indépendante (x1,x2,x3..) dans nos donnée D, nous pouvons écrire : 

p(x1,x2,x3...xn | theta ) = p(x1|theta) * p(x2|theta) * .... 

En implement la vraisemblance en python: 

	def vraissemblance(data, theta):
	    L = []
	    loi =  stats.bernoulli(theta)
	    for x in data:
	        y =  loi.pmf(x)
	        L.append(y)
	    return np.prod(L)  

NOTE: En realité, nous aurions pu utilisé la loi binomiale.. Mais bon.. 


### Calcul de la posteriori 
Pour calculer les probabilités de theta, il suffit mainteant d'appliquer la formule.
Dans le code suivant, le calcul iterativement les posteriori en utilisant de plus en plus de donnée.








## Utilisation de PyMC3 

Nous allons juste réécrire le code précédent avec la librarie PyCM3. 
En réalité, il y a souvent plusieurs paramètre à évaluer, et le calcul de l'intégralle devient très difficile. 
On estime alors la probabilité a posteriori en utilisant l'algorithme MCMC. 







# Exemple avec PyMC3

https://dun.unistra.fr/ipm/unit/bayesien/co/1a_1_1.html