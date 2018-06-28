Title: Le théorème de Bayes en image
Slug: le-théorème-de-bayes-en-image
Date: 2018-06-26 23:18:50
Modified: 2018-06-26 23:18:50
Tags: statistique, épidémiologie
Category: informatique
Author: Sacha schutz
Status: Draft

J'ai longtemps galéré avec les probabilités. C'est assez tard que j'ai compris qu'il s'agissait juste d'un problème de dénombrement. Par exemple, si vous chercher à savoir la probabilité pour que la somme de deux dés lancé soit égal 8, il suffit de désiner une matrice 6x6 contenant toutes les combinaison possible et de compter les cases contenant un 8. J'étais assez content de cette conception des probabilités qu'on appelle "fréquentiste". Sauf que voilà, il y a une autre vision des probabilités que l'on trouve partout en informatique. En intelligence artificiel, dans la reconstruction des arbres phylogénétique, dans l'analyse naturel du language ou même dans la détection des mutations génétique sur des données de séquençage haut débit. Cette conception c'est le Bayésianisme, un raisonement basé sur le théorème de Bayes. Et en croire certain youtubeur (Lee & truc), cette vision des probablités à l'effet d'un shoot de cocaïne accompagné d'un massage taillandais! Donc forcément, j'ai voulu la comprendre. Et vous savez quoi ? J'ai rien compris en lisant les différentes démonstrations de la formule de Bayes. Etonnement, c'est seulement en reprennant ma casquette de fréquentiste et en faisant de joli dessin que tout c'est éclairé! C'est ce que je vais vous partager maintenant. 

## Des malades et un test biologique 
Sur internet, les différentes démonstrations de la formule s'aide d'un exemple avec des patients et un test biologique. On va donc reprendre cette exemple en s'aidant d'un schéma et en utilisant les bons mots.
Voici donc 10 individus dont 4 sont malades. Sont entouré les individus dont le test biologique ( par exemple un test grippal) est positif. 

<div class="figure">
<img src="../images/bayes/intro.png" />
<div class="legend">Différentes lois normales d'espérance mu=0 et de variance sigma=2,3,4 et 5</div>
</div>


### Sensibilité et Spécificité d'un test 
Commencons par une petite apparté sur l'efficacité d'un test qui s'évalue à l'aide de deux grandeurs. La sensibilité et la spécificité. 
un test sensible nous assure que que tous les malades sont détécté quite à avoir des faux positif. Sa formule s'écrit:

    Sensibilité = Vrai positif / Tous les malades 
    Ou encore 
    Sensibilité = Vrai positif / (Vrai positif + Faux négatif)

Un test spécifique nous assure qu'aucun patient sain n'est détécté quite à avoir des faux négatif. Sa formule s'écrit: 

    Specificité = Vrai négatif / Tous les sains 
    Ou encore 
    Spécificité = Vrai négatif / ( Vrai négatif + Faux positif)

Une image vaut mieux que des formules ...

<div class="figure">
<img src="../images/bayes/sens_spec.png" />
<div class="legend">Sensibilité et spécificité d'un test biologique. Un test sensibilité détecte tous les malades. Un test spécifique ne se positive jamais chez des patients sains</div>
</div>

L'idéal est d'avoir un test avec une sensibilité et une spécificité de 100%. Mais en pratique, c'est rarement le cas et le test est choisi en fonction de l'utilisation. Un test sensibile est utilisé pour faire du dépistage sur une population( un test de grossesse sur les urines ), tandis qu'un test spécifique est utilisé pour faire du diagnostique sur des patients ciblés (beta hCG sur une prise de sang ).    
Gardons cela en tête, car çela servira pour la suite.

## Il suffit de savoir compter 
Revenons à nos 10 individus et posons nous les questions suivantes.

#### Combien avons nous de malade ? 

<div class="figure">
<img src="../images/bayes/sick_count.gif" width="250px" />
<p>6 personnes sur 10 sont malades. Soit p(M) = 6/10</p>
</div>


#### Combien de personne ont un test positif? 
<div class="figure">
<img src="../images/bayes/test_count.gif" width="250px" />
<p>5 personnes sur 10 ont un test postif. Soit p(T) = 5/10</p>
</div>

#### Combien de personne sont malade ET avec un test positif? 
<div class="figure">
<img src="../images/bayes/inter_count.gif" width="250px" />
<p>4 personnes sur 10 sont malade avec un test postif. Soit p(M et T) = 4/10</p>
</div>

Maintenant passons au probabilité conditionnelle. Et pour cela, voici une subtilité du language que je vous conseil d'utiliser dans notre exemple.
Ne dite pas « *La probablité de A **sachant** B *» mais « *La probabilité de A **parmi** B* »

#### Combien avons nous de malade parmi les patients testé positifs ? 
<div class="figure">
<img src="../images/bayes/sick_in_test.gif" width="250px" />
<p>Parmi les 5 tests positifs il y a 4 malades. <br/>
Soit p(M|T) = p(M et T) / p(T) = 4 / 5</p>
</div>

#### Combien avons nous de personne testé positif parmi les malades? 
<div class="figure">
<img src="../images/bayes/test_in_sick.gif" width="250px" />
<p>Parmi les 6 malades, 4 ont un test positif. <br/>
Soit p(T|M) = p(M et T) / p(M) = 4 / 5.    
Très important à noter. Cette dernière question correspond à la sensibilité du test </p>
</div>

## Et la formule de Bayes surgit 
Vous constaterez que dans les 2 formules précédante, p(T|M) et p(M|T), il y a un terme en commun: p(M et T+) qui correspond au nombre d'indiviu à la fois malade et testé positivement.    
En remplacant ce terme, nous pouvons alors exprimer p(M|T) en fonction de p(T|M).

    On a :
    p(T|M)    = p(M et T) / p(M)

    et donc:
    p(M et T) = p(M) * p(T|M)

    en remplacant :
    p(M|T)    = p(M) * p(T|M) / p(T)

Et nous voilà alors, avec la fameuse formule de Bayes : 

<center>
<img src="../images/bayes/bayes.gif" />
<p></p>
</center>

On peut tout de suite verifier sur nos 10 individus que nous trouvons par le calcul la même chose que ce que nous avons observé.

    p(M)    = 6/10
    p(T)    = 5/10
    p(T/M)  = 4/6 
    p(M/T)  = (p(T/M) * p(M)) / p(T) = 6/10 * 4/6 / 5/10 = 4/5
 

## Application du théorème
En pratique, on utilise le théorème de Bayes en médecine pour estimer le risque qu'un individu soit malade sachant que son test est positif.
Malheuresement nous n'avons pas toutes les informations nécessaire pour appliquer la formule de Bayes aussi facilement que dans notre exemple.   
Les seuls que nous ayons à disposition sont la prévalence de la maladie dans la population p(M) et la sensibilité du test qui n'est autre que p(T|M). 
Il faut alors réussir à trouver p(T).

<div class="figure">
<img src="../images/bayes/final.png" />
<p>p(T) est la somme de A=p(M et T) et B=p(non M et T) sur les 10 individus</p>
</div>

p(T) se calcul en sommant <mark style="background-color:#F84AA9">le nombre de patient malade ET testé positif p(M et T)</mark> avec <mark style="background-color:#92D050">le nombre de patient sain ET testé positif p(non M et T)</mark>. Et comme vu précédement, nous pouvons expirmer chacun de ces termes par : 

    p(M et T)     = p(M) * (T|M)
    p(non M et T) = p(non M) * (T|non M)

On peut alors formuler la loi total de Bayes :

<center>
<img src="../images/bayes/total_bayes.gif" />
<p>Loi total de Bayes</p>
</center>

## Un exemple avec la mucoviscidose
On s'interesse ici au patient porteur d'une mutation dans le gène CFTR qui est impliqué dans la mucoviuscidose.   
En france, 1 personne sur 34 [p(M)=1/34] est porteur de la mutation , la plus fréquente étant la deltaF508. ( cela n'implique pas d'être malade car il s'agit d'une maladie récessive). Il existe un test pouvant détecter ces mutations avec une sensibilité de 85% [p(T|M)=1/85] et une spécificité avoisinant les 100% [p(Tneg|non M)=1].    
Après vous avoir fait le test qui s'est négativé, quel est la probabilité que vous soyez tout de même porteur ?    


<center>
<img src="../images/bayes/muco.gif" />
<p>Attention: Ici p(Tneg|M) est égal à 1-sensibilité </p>
</center>


## Conclusion 
J'espère à présent que vous visualiser aussi bien que moi la formule de Bayes. Personnellement, en faisant les dessins sur papiers, je retrouve très facilement les formules. Donc innutile de les apprendre par coeur.
La prochaine étape c'est de devenir un vrai Bayesien pour que d'un coup de baguette, je puisse résoudre un tas de problème bioinformatique, voir même changer ma façon de penser. En effet, je sais pas si vous connaissez le problème de Monty Hall, mais parait que seul des bayesiens peuvent trouver ça logique.


 
http://folk.uio.no/jonmic/Statkurs/03%20-%20Bayes%20law.%20Sensitivity,%20specificity.pdf