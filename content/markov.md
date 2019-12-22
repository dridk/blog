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
Je me les represente comme des générateurs de séquences aléatoire (ou processus stochastique) dont la probabilité de chaque base depend de la précédente.
Dans ce billet, nous alons les définir et voir comment les utiliser avec application pratique en génétique.

## Un dé à 4 faces
Imaginez un dé à 4 face sur lesquelles sont representé chaque base de l'ADN : A,C,G,T. Lancez ce dé plusieurs fois en notant chaque résultat.
Par exemple, le premier lancé vous donne un A, le deuxième un T, le troisème un A etc ... jusqu'à générér une longue séquence.
Si le dé n'est pas truqué, à chaque lancé, vous avez exactement une chance sur 4 d'obtenir chaques bases.    
Une façon de representer ce tirage aléatoire est d'utiliser un graphe ou chaque noeuds represente les symboles ou état et les arrêtes les probabilités de transitions. Dans la figure ci-dessous, il y a 4 états (A,C,G,T) et 16 transitions avec leurs probabilité toutes égales à 1/4. 
Pour générger une séquence, choissiez un état au hasard, puis faite une marche dans ce graphe en suivant les probabilité de transition. Notez la valeur de chaque noeuds traversé. Bravo, vous venez de générer une séquence à l'aide une chaine de Markov. 

<div class="figure">     <img src="../images/markov/animation.gif" />      <div class="legend">Chaine de Markov. Il y a 4 états (A,C,G,T) et 4x4=16 transitions possible toutes avec une probabilité de 1/4</div> </div>   


## Définition d'une chaine de Markov
Une chaine de Markov se défini donc par une vecteur d'état E et une matrice de transition P.    
Dans notre cas, il y a 4 états possibles soit $$E = \{A,C,G,T\}$$ et 16 probabilités de transition que l'on peut representer par la matrice suivante avec A,C,G,T en ligne et en colonne:

$$
T = \begin{bmatrix}
1/4 &  1/4 & 1/4 & 1/4 \\ 
1/4 & 1/4  & 1/4 & 1/4\\ 
1/4 & 1/4 & 1/4 & 1/4\\ 
1/4 & 1/4 & 1/4 & 1/4 \\
\end{bmatrix}
$$

En changant les probabilité de transition, nous pouvons alors générer différente famille de séquence. Par exemple dans la figure suivante, j'ai modifié les transition G -> C et C -> G pour obtenir des séquences riche en GC.


<div class="figure">     <img src="../images/markov/animation2.gif" />      <div class="legend"> GCGAAGGCGTAAGGGCGCCGCGCGTTGCGCGTTTGCGCGCGCGCGCTAGCGCCGCTCTACGGGTAGCGCGGCGCGATGCTCATTATTGCGTCCACTAAAC.</div> </div>   



## Distribution stationnaire
En faisant tourner votre générateur assez longtemps et en comptant la fréquence d'apparition de chaque lettre, vous obtiendrez une distribution qui deviendra stationnaire au bout d'un certain temps. C'est à dire que peut importe la longueur de la séquence, la probabilité de voir apparaitre une certaine lettre dans la séquence sera toujours la même. 
Les histogrammes ci-dessous montre la fréquence des 10,50,100,500,1000 et 5000 nucléotides premier nucléotide généré par une chaine de markov utilisant la matrice de transition vu plus haut. Comme on peut s'y attendre, cette distribution tend à être uniforme.  

<div class="figure">     <img src="../images/markov/distribution1.png" />      <div class="legend"> Transition equiprobable</div> </div>   


Ces distributions se calculer en faisant un peu d'algèbre linéaire. 
On choisi de representer la distribution des 4 bases par un vecteur $\pi_{0} = [pA, pC, pG, pT]$ à un temps donnée t. Par exemple, si nous choissisons une séquence commençant par un A, alors la distribution au temps $t_0$ est $\pi_{t}$ = [1,0,0,0].
On calcule alors la distribution au temps t+1 en faisant le produit du vecteur par la matrix de transition T. 

$$
\pi_{t+1} = \pi_{t} T
$$

De façon général, on peut calculer la distribution au temps n par :

$$
\pi_{t} = \pi_{0}T^n
$$

Trouver la distribution stationnaire, c'est chercher la distribution qui ne change pas:

$$
\pi = \pi T
$$


## Un modèle d'apprentissage 
Si maintenant, au lieux de générer des séquences à partir d'une chaine de Markov nous faisions l'inverse. C'est à dire construire une chaine de Markov en observant des séquences. Pour cela il suffit de comptabiliser toutes les transitions existante dans une jeux de séquence pour en déduire les probabilité de la matrice de transition.

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

Il est alors possible de générer une nouvelle séquence semblable au séquences ayant été utilisé pour construire le modèle. C'est de cette façon par exemple que du texte aléatoire est généré. Voir ici.
On peut egalement tester si une nouvelle séquence fait partie de la même famille que les séquences du modèle. Par exemple quel est la probabilité que la séquence ATTCG soit générer par une chaine de Markov $\theta$  ?
Etant donnée que la probabilité d'apparition d'un symbole depend uniquement du précédement, la probabilité peut s'écrire comme le produit de chaque transition: 
$$
p(ATTCG|\theta) = p(A) * p(T|A) * p(T|A) * p(T|T) * p(C|T) * p(G|C)
$$

Ou plus généralement : 

$$
P(S|\theta) = \prod_{0}^{n} p(S_{n}|S_{n-1}) 
$$

Et comme les additions c'est mieux que les multiplications, on calcule la vraissemblance : 

$$
L_{\theta}(S) = \sum_{0}^{n} log(p(S_{n}|S_{n-1})) 
$$



## Vers les chaines de Markov cachées 
Une chaine de markov cachée est simplement une chaine de Markov ou certain des états sont caché. Plus préscisement ce sont des états qui ne font pas partie de la séquence générés. Reprenons notre dé, appelons X et ajoutons un deuxième dé truqué appelé Y contenant uniquement des G sur ces 4 faces. On lance toujours un seul dé pour générer une séquence. sauf que cette fois, à chaque lancé, il y a une chance sur 2 que nous changions de dé. La chaine de Markov peut être representé comme suite. 

<div class="figure">     <img src="../images/markov/hmm.png" />      <div class="legend">Chaine de Markov</div> </div>   

Comme vu plus haut, il est possible de construire une chaine de Markov en apprenant à partir d'une liste de séquence. Mais cette fois, les probabilités de transitionss cachés sont beaucoup plus difficile à calculé car non observé. 
On peut les estimer en cherchant les valeurs les plus vraissemblance avec par exemple l'algorithme de Baum-Welch permet de résoudre ce problème. Il s'agit d'un algorithme d'esperance maximisation que nous avons déjà vu dans un autre billet. Notez aussi l'algorthme de Viterbi très utilisé en bioinformatique car il permet de trouver des alignements prenant les insertions et délétion en considération.



### Référence 
- [Super vidéo d'Aurélien Géron (en)](https://www.youtube.com/watch?v=ErfnhcEV1O8)
- [Une autre super vidéo (en)](https://www.youtube.com/watch?v=R4OlXb9aTvQ)
- [La théorie de l'information: L'origine de l'entropie](http://www.yann-ollivier.org/entropie/entropie1)

### Merci 
[@andhena](https://github.com/andhena)