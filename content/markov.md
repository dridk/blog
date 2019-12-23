Title: Les chaines de Markov
Slug: chaine-de-markov
Date: 2019-03-17 18:53:39
Modified: 2019-06-07 12:18:36
Tags: statistique,maths,café
Category:informatique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/stat_banner.jpg


Les chaines de Markov sont très populaire en bioinformatique, en particulier lorsqu'on manipule des séquences d'ADN. 
Je me les represente comme des machines générant de séquences aléatoires, ou processus stochastique, dont la probabilité d'apparition de chaque nucléotide depend du précédent.    
Dans ce billet, nous alons les définir et voir comment les utiliser avec l'ADN.

## Un dé à 4 faces
Imaginez un dé à 4 face sur lesquelles sont representé les quatres bases A,C,G,T de l'ADN. Lancez ce dé plusieurs fois en notant chaque résultat.
Par exemple, le premier lancé vous donne un A, le deuxième un T, le troisème un A et ainsi de suite jusqu'à générér une longue séquence.
Si le dé n'est pas truqué, à chaque lancé, vous avez exactement une chance sur 4 d'obtenir chacune des bases.         
Une façon de representer ce tirage aléatoire est d'utiliser un graphe, appelé diagramme de transition, ou chaque noeuds represente les bases ou état et les arrêtes les probabilités de transitions. Dans la figure ci-dessous, il y a 4 états (A,C,G,T) et 16 transitions avec leurs probabilité toutes égales à 1/4. Par exemple, La probabilité d'obtenir un C après en A est de 1/4 et il en va de même pour toutes les autres transitions.     
Pour générger une séquence, choissiez un noeud au hasard, puis faite une marche dans ce graphe en suivant les probabilité de transition. Notez la valeur de chaque noeuds traversé. Bravo, vous venez de générer une séquence à l'aide une chaine de Markov. 

<div class="figure">     <img src="../images/markov/animation.gif" />      <div class="legend">Chaine de Markov. Il y a 4 états (A,C,G,T) et 4x4=16 transitions possible toutes avec une probabilité de 1/4</div> </div>   


## Définition d'une chaine de Markov
Une chaine de Markov se défini donc par une vecteur d'état E et une matrice de transition P.    
Dans notre cas, il y a 4 états possibles soit $$E = \{A,C,G,T\}$$ et 16 probabilités de transition que l'on peut representer par une matrice carré suivante avec A,C,G,T en ligne et en colonne. Par exemple la transition A vers A correspond se lis dans la matrice au coordonnée (0,0). La transition A vers C, au coordonnée (0,1) etc ...

$$
T = \begin{bmatrix}
0.25 &  0.25 & 0.25 & 0.25 \\ 
0.25 & 0.25  & 0.25 & 0.25 \\ 
0.25 & 0.25 & 0.25 & 0.25\\ 
0.25 & 0.25 & 0.25 & 0.25 \\
\end{bmatrix}
$$

En changant les probabilité de transition, nous pouvons alors générer des séquences avec des profils particulier. Dans la figure suivante, j'ai donnée une probabilité de 0.7 aux transitions G -> C et C -> G. Avec cette nouvelle table de transition, je peux alors générer des séquence riche en GC.


<div class="figure">     <img src="../images/markov/animation2.gif" />      <div class="legend"> Dans ce graphe, les probabilités de transitons G->C et C->G sont à 0.7. Pour respecter les proportions, d'autre transitions sont passé à 0.1 </div> </div>   



## Distribution stationnaire
En faisant tourner votre générateur assez longtemps et en comptant la fréquence d'apparition de chaque base, vous obtiendrez une distribution qui deviendra stationnaire au bout d'un certain temps. C'est à dire que peut importe la longueur de la séquence, la probabilité de voir apparaitre une certaine base dans la séquence sera toujours la même. 
Les histogrammes ci-dessous montre la fréquence des 10,50,100,500,1000 et 5000 premier nucléotide généré par une chaine de markov en utilisant la matrice de transition du dé à 4 faces. Comme on peut s'y attendre, cette distribution converge pour devenir uniforme.  

<div class="figure">     <img src="../images/markov/distribution1.png" />      <div class="legend"> Transition equiprobable</div> </div>   


Ces distributions se calculer en faisant un peu d'algèbre linéaire. 
On choisi de representer la distribution des 4 bases par un vecteur $\pi_{0} = [pA, pC, pG, pT]$ à un temps donnée t. Par exemple, si nous choissisons une séquence commençant par un A, alors la distribution au temps $t_0$ est $\pi_{t}$ = [1,0,0,0].
On peut alors calculer la distribution au temps t+1 en faisant le produit du vecteur par la matrix de transition T. 

$$
\pi_{t+1} = \pi_{t} T
$$

De façon général, on peut calculer la distribution au temps n par :

$$
\pi_{t} = \pi_{0}T^n
$$

Trouver la distribution stationnaire, c'est chercher celle qui ne change pas entre deux temps. C'est à dire résoudre l'équation suivante :

$$
\pi = \pi T
$$

Sachant cela, vous allez pouvoir construire des générateurs de séquences aléatoire avec une distribution désiré.   
De façon beaucoup plus général, utilisé les chaines de markov comme générateurs aléatoire d'une distribution particulière est à la base des algorithmes MCMC. Principalement en inférence bayesienne pour calculer une distribution a posteriori. Mais ça c'est une autre pair de manche ! 


## Un modèle d'apprentissage 
Si maintenant, au lieux de générer des séquences à partir d'une chaine de Markov nous faisions l'inverse. C'est à dire construire une chaine de Markov en observant des séquences. Pour cela il suffit de comptabiliser toutes les transitions existante dans une jeux de séquence pour déduire les probabilité de la matrice de transition. Parmi les séquences suivante, il y a 5 transition TA sur 32 transitions possible. On notera alors dans notre matrice que la transition T->A est de 5/32. On fait de même pour les autres transitions pour obtenir une chaine de markov.

<div class="figure">
<code>
<b style="color:red">TA</b>CGC <br/>
CCT<b style="color:red">TA</b> <br/>
GCCGC <br/>
AG<b style="color:red">TA</b>G <br/>
AGCGC <br/>
C<b style="color:red">TA</b><b style="color:red">TA </b><br/>
GTGCA<br/>
CGCCA <br/>
</code>
<div class="legend">Chaine de Markov</div>
</div>

Il est alors possible de générer une nouvelle séquence semblable à celles utilisé dans la construction du modèle. C'est de cette façon que les générateur de texte aléatoire fonctionne. Par exemple, ce site qui gènere des tweet de Donald Trump https://filiph.github.io/markov/.
En génétique, on va plutôt tester si une nouvelle séquence a le même profil que les séquences d'un modèle $\theta$. Par exemple quel est la probabilité que la séquence ATTCG soit une séquence de régulation ? 
Etant donnée que la probabilité d'apparition d'une base depend uniquement du précédement, la probabilité de ATTCG peut s'écrire comme le produit de chaque transition: 
$$
p(ATTCG|\theta) = p(A) * p(T|A) * p(T|A) * p(T|T) * p(C|T) * p(G|C)
$$

Ou plus généralement : 

$$
P(S|\theta) = \prod_{0}^{n} p(S_{n}|S_{n-1}) 
$$

Et comme les additions c'est mieux que les multiplications, on calcule la vraissemblance via le logarithme: 

$$
L_{\theta}(S) = \sum_{0}^{n} log(p(S_{n}|S_{n-1})) 
$$

En lisant les probabilité de la table de transition, on peut alors calculer un score indiquant si une séquence fait parti d'une famille ou non. Ce genre d'algorithme s'utilise par exemple pour détécter des homologies de protéines. En réalité ce sont des chaines de Markov plus complexe, appelé chaine de markov caché que je vais décrire rapidement.

## Les chaines de Markov cachées 
Une chaine de markov cachée est simplement une chaine de Markov ou certain des états sont caché. Plus préscisement ce sont des états qui ne font pas partie de la séquence générés. Reprenons notre dé, appelons le X et ajoutons un deuxième dé truqué appelé Y contenant uniquement des G sur ces 4 faces. On lance toujours un seul dé pour générer une séquence. sauf que cette fois, à chaque lancé, il y a une chance sur 2 que nous changions de dé. La chaine de Markov peut être representé comme suite. On dit que X et Y sont les états cachés avec 4 probabilités d'emission chacun.

<div class="figure">     <img src="../images/markov/hmm.png" />      <div class="legend">Chaine de Markov</div> </div>   

Ces 2 états cachés peuvent representer par exemple les introns et les exons. Ils est peut être par exemple plus rare d'avoir du GC dans un exon que dans un intron. Les probabilités d'emissions seront différents selon l'état caché actuel.
On utilise egalement les chaine de markov caché pour modéliser les insertions et les délétions. C'est ce genre de modèle qui est utilisé dans les HMM:

<div class="figure">     <img src="../images/markov/hmm2.png" />      <div class="legend">Chaine de Markov</div> </div>   

Comme vu plus haut, il est possible de construire une chaine de Markov caché en apprenantde depuis un corpus de séquence. Mais cette fois, les probabilités de transitionss cachés sont beaucoup plus difficile à calculé car on ne les observe pas. 
On peut les estimer en cherchant les valeurs les plus vraissemblance avec par exemple l'algorithme de Baum-Welch. Il s'agit d'un algorithme d'esperance maximisation que nous avons déjà vu dans un autre billet. Notez aussi l'algorthme de Viterbi qui permet d'identifier le chemin le plus probable, lorsqu'on désire aligner une séquence sur un profil HMM. 

## En bref 
Les chaine de markov sont des processus stochastiques dont l'état futur dépend uniquement du présent. Elles peuvent être utilisé en génétique pour générer des séquences mais surtout comme modèle d'apprentissage comme les profil HMM.

http://nazejournal.free.fr/article.php?page=chaines-markov
https://mattiacinelli.com/hidden-markov-model-applied-to-biological-sequence-part-2/

### Référence 
- [Super vidéo d'Aurélien Géron (en)](https://www.youtube.com/watch?v=ErfnhcEV1O8)
- [Une autre super vidéo (en)](https://www.youtube.com/watch?v=R4OlXb9aTvQ)
- [La théorie de l'information: L'origine de l'entropie](http://www.yann-ollivier.org/entropie/entropie1)

### Merci 
[@andhena](https://github.com/andhena)