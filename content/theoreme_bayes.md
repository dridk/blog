Title: Le théorème de Bayes en image
Slug: le-théorème-de-bayes-en-image
Date: 2018-06-26 23:18:50
Modified: 2018-06-26 23:18:50
Tags: 
Category: 
Author: 
Lang: 
Summary: 
Status: Draft

Je me rappel au lycée avoir beaucoup de mal avec les probabilités. C'était un concepte un peu abstrait et je preferai neterement l'aglèbre linéaire que je pouvais facilement visualisé. C'est plus tard lorsque j'ai compris que les probablités n'étaient qu'histoire de dénombrer tous les cas possibles d'un évenement que j'ai pu correctement visualisé et progressé. Par exemple, si vous voulez savoir la probabilité que la somme de deux dés lancé soit égal 6, il suffit de désinner une matrice avec tous les cas possibles et de compter les cases.    
J'étais assez content de cette vision de pensé qui est une conception des probablités qu'on appelle "fréquentiste". Sauf que voilà, il y a une autre conception des probabilités que je vois apparaitre partout. Que ce soit en biologie (calcul de risque suite à un test biologique) ou en bioinformatique ( intelligence artificiel, analyse du language naturel, reconstruction phylogénétique ). Cette conception c'est le Bayésianisme, un raisonement basé sur le théorème de Bayes. Et en croire certain youtubeur (Lee & truc), cette vision des probablités à l'effet d'un shoot de drogue passé en intraveineuse directement dans le le lobe raison! Donc forcément, j'ai voulu comprendre. Et vous savez quoi ? J'ai rien compris en lisant les différentes démonstrations de la formule de Bayes. Etonnement, c'est seulement en reprennant ma casquette de fréquentiste et en faisant un joli dessin que tout c'est éclairé! Voici donc la démonstration de la formule de Bayes façon biologiste ! 

## Des malades et un test biologique 
Dans le livre de Lee et la vidéo de truc, la démonstration de la formule  s'aide d'un exemple avec des patients et un test biologique. On va reprendre cette exemple en faisant un schéma et en utilisant les bon mots.
Voici 10 individus dont 4 sont malades. Sont entouré les individus dont le test grippal est positif. 

<div class="figure">
<img src="../images/bayes/intro.png" />
<div class="legend">Différentes lois normales d'espérance mu=0 et de variance sigma=2,3,4 et 5</div>
</div>


### Sensibilité et Spécificité d'un test 
Une petit apparté sur l'efficacité d'un test qui s'évalue à l'aide de deux grandeurs. La sensibilité et la spécificité. 
un test sensible nous assure que que tous les malades sont détécté quite à avoir des faux positif. Sa formule s'écrit : Sens = VP / VP + FN
Un test spécifique nous assure qu'aucun patient sain n'est détécté quite à avoir des faux négatif. Sa formule s'écrit : Spec = VN / VN + FP

<div class="figure">
<img src="../images/bayes/sens_spec.png" />
<div class="legend">Différentes lois normales d'espérance mu=0 et de variance sigma=2,3,4 et 5</div>
</div>

L'idéal serait d'avoir un test avec une sensibilité et une spécificité de 100% et dans la réalité c'est rarement le cas. 
En pratique, les test sensible sont utilisé pour faire du dépistage ( un test de grossesse sur les urines ) sur une population, pour ensuite faire un diagnostic avec un test spécifique (beta hCG sur une prise de sang ). 

## Il suffit de compter 
Revenons à nos 10 individus et mettons nous à compter.

#### Combien avons nous de malade ? 

<div class="figure">
<img src="../images/bayes/sick_count.gif" width="250px" />
<p>6 personnes sur 10 sont malades. Soit p(M) = 6/10</p>
</div>


#### Combien de personne ont un test positif? 
<div class="figure">
<img src="../images/bayes/test_count.gif" width="250px" />
<p>5 personnes sur 10 un un test postif. Soit p(T) = 5/10</p>
</div>


Maintenant passons au probabilité conditionnelle. Et pour cela, voici une subtilité du language que je vous conseil d'utiliser dans ces exemples.

<div class="figure">
<quote><b>Ne dite pas</b> 
<i>« La probablité de A sachant B »</i>
<b>Mais</b>  
<i>« La probabilité de A parmi B »</i>
</quote>
</div>

#### Combien avons nous de malade parmi les testé positifs ? 
<div class="figure">
<img src="../images/bayes/sick_in_test.gif" width="250px" />
<p>Parmi les 5 tests positifs il y a 4 malades. <br/>
Soit p(M|T) = p(M et T) / p(T) = 4 / 5</p>
</div>

#### Combien avons nous de testé positif parmi les malades? 
<div class="figure">
<img src="../images/bayes/test_in_sick.gif" width="250px" />
<p>Parmi les 6 malades, 4 ont un test positif. <br/>
Soit p(T|M) = p(M et T) / p(M) = 4 / 5</p>
</div>

## Et la formule de Bayes surgit 
Vous constaterez que dans les 2 formules précédante, p(T|M) et p(M|T), il y a un terme en commun: p(M et T+) qui correspond au nombre d'indiviu à la fois malade et testé positivement. 

<div class="figure">
<img src="../images/bayes/sick_and_test.png" />
<p>Les individus à la fois malade et avec un test positif.<br/>
Soit p(M et T) = 4/10 </p>
</div>

En remplacant ce terme, nous pouvons ainsi exprimer p(M|T) en fonction de p(T|M).

    p(T|M)    = p(M et T) / p(M)
    p(M et T) = p(M) * p(T|M)
    p(M|T)    = p(M) * p(T|M) / p(T)

Et nous voilà avec l'équation du théorème de Bayes qui se généralise comme suite

<div class="figure">
<img src="../images/bayes/bayes.jpg" />
<p></p>
</div>

On peut tester tout de suite sur nos 10 individus et voir que nous trouvons par le calcul ce que nous avions observé.

    p(M)    = 6/10
    p(T)    = 5/10
    p(T/M)  = 4/6 
    p(M/T)  = (p(T/M) * p(M)) / p(T) = 6/10 * 4/6 / 5/10 = 4/5
 

## Le théoreme de Bayes
Dans la mucovisidose, 


http://folk.uio.no/jonmic/Statkurs/03%20-%20Bayes%20law.%20Sensitivity,%20specificity.pdf