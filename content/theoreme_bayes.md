Title: Le théorème de Bayes en image
Slug: le-theoreme-de-bayes
Date: 2018-06-26 23:18:50
Modified: 2018-06-29 02:38:02
Tags: statistique, épidémiologie
Category: biologie
Author: Sacha schutz
SIDEBARIMAGE:../images/common/stat_banner.jpg


J'ai longtemps galéré avec les probabilités...     
C'est assez tard que j'ai compris qu'il s'agissait juste d'un problème de dénombrement. Par exemple, si vous cherchez à savoir la probabilité pour que la somme de deux dés lancés soit égale 8, il [suffit de dessiner une matrice 6x6](https://bestcase.files.wordpress.com/2011/01/dicediagram.jpg) contenant toutes les combinaisons possibles et  compter les cases contenant un 8. J'étais assez satisfait de cette conception des probabilités qu'on appelle "[fréquentiste](https://fr.wikipedia.org/wiki/Interpr%C3%A9tations_de_la_probabilit%C3%A9#Fr%C3%A9quentisme)". Sauf que voilà, q'il y a une autre vision des probabilités très tendance en informatique. En [intelligence artificielle](https://fr.wikipedia.org/wiki/Classification_na%C3%AFve_bay%C3%A9sienne), dans la [reconstruction des arbres phylogénétique](https://hal.archives-ouvertes.fr/halsde-00193036/document), dans [l'analyse naturelle du langage](https://fr.wikipedia.org/wiki/Analyse_syntaxique_de_la_langue_naturelle) ou même dans [la détection des mutations génétique](https://software.broadinstitute.org/gatk/documentation/tooldocs/3.8-0/org_broadinstitute_gatk_tools_walkers_haplotypecaller_HaplotypeCaller.php) sur des données de séquençage haut débit. Cette conception c'est le Bayésianisme, un raisonnement basé sur le [théorème de Bayes](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Bayes). Et en croire certain youtubeur ([Monsieur Phi](https://www.youtube.com/watch?v=3FOrWMDL8CY) & [Science4All](https://www.youtube.com/watch?v=DgrRlP_GRRY)) , cette vision des probabilités à l'effet pour le cerveau, d'un shoot de cocaïne accompagné d'un massage thaïlandais! Donc forcément, j'ai voulu comprendre. Et vous savez quoi ? Je n’ai rien compris en lisant les différentes démonstrations de la formule de Bayes. Étonnement, c'est seulement en reprenant ma casquette de fréquentiste et en faisant de jolis dessins que tout c'est éclairé. Et c'est ce que nous allons voir maintenant. 

## Des malades et un test biologique 
Sur internet, les démonstrations de la formule s'aident souvent d'un exemple avec des patients et un test biologique. On va reprendre cet exemple en s'aidant d'un schéma et en utilisant les bons mots.
Voici 10 patients dont 6 sont malades. Sont entourés les individus dont le test biologique est positif (par exemple un test grippal) . 

<div class="figure">
<img src="../images/bayes/intro.png" />
<div class="legend"> En vert les patients sains, en rouge les patients malades. </div>
</div>


## Sensibilité et Spécificité
Commençons par un petit aparté sur l'efficacité d'un test qui s'évalue à l'aide de deux grandeurs. [La sensibilité et la spécificité](https://fr.wikipedia.org/wiki/Sensibilit%C3%A9_et_sp%C3%A9cificit%C3%A9). 

<div class="figure">
<img src="../images/bayes/sens_spec.png" />
<div class="legend">Sensibilité et spécificité d'un test biologique. Un test sensibilité détecte tous les malades. Un test spécifique ne se positive jamais chez des patients sains</div>
</div>

Un test très sensible (droite de la figure) nous assure que tous les malades sont détectés quitte à avoir des faux positifs. Sa formule s'écrit:

    Sensibilité = Vrai positif / Tous les malades 
    Ou encore 
    Sensibilité = Vrai positif / (Vrai positif + Faux négatif)

Un test très spécifique (gauche de la figure) nous assure qu'aucun patient sain n'est détecté quitte à avoir des faux négatifs. Sa formule s'écrit: 

    Specificité = Vrai négatif / Tous les sains 
    Ou encore 
    Spécificité = Vrai négatif / ( Vrai négatif + Faux positif)


L'idéal est d'avoir un test avec une sensibilité et une spécificité de 100%. Mais en pratique, c'est rarement le cas et le test est choisi en fonction de l'utilisation. Un test sensible est utilisé pour faire du dépistage sur une population (un [test de grossesse](https://fr.wikipedia.org/wiki/Test_de_grossesse) sur les urines), tandis qu'un test spécifique est utilisé pour faire du diagnostic sur des patients ciblés ([bêta-hCG](https://fr.wikipedia.org/wiki/Hormone_chorionique_gonadotrope_humaine) sur une prise de sang ).    
Gardons tout cela en tête, car cela servira pour la suite.

## Savez-vous compter ?  
Revenons à nos 10 individus et posons-nous les questions suivantes.

#### Combien avons-nous de malades ? 

<div class="figure">
<img src="../images/bayes/sick_count.gif" width="250px" />
<p>6 personnes sur 10 sont malades. Soit p(M) = 6/10</p>
</div>


#### Combien de personnes ont un test positif? 
<div class="figure">
<img src="../images/bayes/test_count.gif" width="250px" />
<p>5 personnes sur 10 ont un test postif. Soit p(T) = 5/10</p>
</div>

#### Combien de personnes sont malades ET avec un test positif? 
<div class="figure">
<img src="../images/bayes/inter_count.gif" width="250px" />
<p>4 personnes sur 10 sont malade avec un test postif. Soit p(M et T) = 4/10</p>
</div>

Maintenant, passons aux probabilités conditionnelles. Et pour cela, voici une subtilité du langage que je vous conseille d'utiliser.
Ne dites pas « *La probabilité de A **sachant** B *» mais « *La probabilité de A **parmi** B* »

#### Combien avons-nous de malades parmi les patients testés positifs ? 
<div class="figure">
<img src="../images/bayes/sick_in_test.gif" width="250px" />
<p>Parmi les 5 tests positifs il y a 4 malades. <br/>
Soit p(M|T) = p(M et T) / p(T) = 4 / 5</p>
</div>

#### Combien avons-nous de personnes testées positive parmi les malades? 
<div class="figure">
<img src="../images/bayes/test_in_sick.gif" width="250px" />
<p>Parmi les 6 malades, 4 ont un test positif. <br/>
Soit p(T|M) = p(M et T) / p(M) = 4 / 6.    
Cette dernière formule correspond à la sensibilité du test </p>
</div>

## Et la formule de Bayes surgit 
Vous constaterez que dans les 2 formules précédentes, **p(T|M)** et **p(M|T)**, il y a un terme en commun: **p(M et T)** qui correspond au nombre d'individus à la fois malades et testés positivement.    
En remplaçant ce terme, nous pouvons alors exprimer **p(M|T)** en fonction de **p(T|M)**. 

    On a :
    p(T|M)    = p(M et T) / p(M)

    et donc:
    p(M et T) = p(M) * p(T|M)

    en remplaçant :
    p(M|T)    =  p(T|M) * p(M)  / p(T)

Et nous voilà alors, avec la fameuse formule de Bayes : 

<center>
<img src="../images/bayes/bayes.gif" />
<p></p>
</center>

On peut tout de suite vérifier sur nos 10 individus que nous trouvons par le calcul la même chose que ce que nous observons.      
Calculons p(M/T) et vérifions que c'est égal à 4/5:

    p(M)    = 6/10
    p(T)    = 5/10
    p(T/M)  = 4/6 
    p(M/T)  = ( p(M) * p(T/M) ) / p(T) = 6/10 * 4/6 / 5/10 = 4/5
 

## La loi total de Bayes
En pratique, on utilise le théorème de Bayes en médecine pour estimer le risque qu'un individu soit malade sachant que son test est positif.
Malheureusement nous n'avons pas toutes les informations nécessaires pour appliquer la formule de Bayes aussi facilement que dans notre exemple.   
Les seuls éléments que nous ayons à disposition sont la [prévalence](https://fr.wikipedia.org/wiki/Pr%C3%A9valence) de la maladie dans la population p(M) et la sensibilité/spécificité du test correspondant respectivement à p(T|M) et p(nonT|nonM).    
Il faut alors réussir à calculer p(T).

<div class="figure">
<img src="../images/bayes/final.png" />
<p>p(T) est la somme de A=p(M et T) et B=p(non M et T) sur les 10 individus</p>
</div>

p(T) se calcul en sommant <mark style="background-color:#F84AA9">le nombre de patients malades ET testés positifs p(M et T)</mark> avec <mark style="background-color:#92D050">le nombre de patients sains ET testés positifs p(non M et T)</mark>. Et comme vu précédemment, nous pouvons exprimer chacun de ces termes par : 

    p(M et T)     = p(M) * (T|M)
    p(non M et T) = p(non M) * (T|non M)

On peut alors écrire la loi totale de Bayes :

<center>
<img src="../images/bayes/total_bayes.gif" />
<p>Loi totale de Bayes</p>
</center>

## Un exemple avec la mucoviscidose
On s'intéresse ici au patient porteur d'une mutation dans le gène [CFTR](https://fr.wikipedia.org/wiki/G%C3%A8ne_et_prot%C3%A9ine_CFTR) qui est impliqué dans la [mucoviscidose](https://fr.wikipedia.org/wiki/Mucoviscidose). 
En France, [1 personne sur 34](http://www.anpgm.fr/index.php/arbres-decisionels?download=181:anpgm-074-v3-cftr&start=60) [p(M)=**1/34**] est porteuse de la mutation , la plus fréquente étant la [ΔF508](https://fr.wikipedia.org/wiki/%CE%94F508). ( cela n'implique pas d'être malade, car il s'agit d'une [maladie autosomique récessive](https://fr.wikipedia.org/wiki/Transmission_autosomique_r%C3%A9cessive)). Il existe un [test](http://www.medicalexpo.fr/prod/fujirebio-europe-nv/product-95077-831367.html) pouvant détecter ces mutations avec une sensibilité de 85% [p(T|M)=**1/85**] et une spécificité avoisinant les 100% [p(Tneg|non M)=**1**].    
Après vous avoir fait le test qui s'est négativé, quelle est la probabilité que vous soyez tout de même porteur ?    


<center>
<img src="../images/bayes/muco.gif" />
<p>Attention subtilité: Ici p(Tneg|M) est égal à 1-sensibilité.<br/>La probabilité d'être porteur malgré la négativité du test est d'environ 1 chance sur 220 </p>
</center>


## Conclusion 
J'espère à présent que vous visualisez aussi bien que moi la formule de Bayes. Personnellement, en faisant les dessins sur papiers, je retrouve très facilement les formules. Donc inutile de les apprendre par coeur.
J'espère maintenant pouvoir bientôt devenir un vrai Bayesien pour pouvoir frimer en soirée et même changer ma façon de penser. En effet, je ne sais pas si vous connaissez le [problème de Monty Hall](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_Monty_Hall). C'est une experience complétement contre intuitif et parait que seul des r̶e̶p̶t̶i̶l̶i̶e̶n̶s bayésiens ont le pouvoir de trouver ça logique.

### Réferences

- [Monsieur Phi](https://www.youtube.com/watch?v=3FOrWMDL8CY)
- [Livre: La formule du savoir](https://laboutique.edpsciences.fr/produit/1035/9782759822614/La%20formule%20du%20savoir)
- [Bayes Law. Sensitivity, specificity](http://folk.uio.no/jonmic/Statkurs/03%20-%20Bayes%20law.%20Sensitivity,%20specificity.pdf)
- [bonnes pratiques des etudes du gene cftr - anpgm](http://www.anpgm.fr/index.php/arbres-decisionels?download=181:anpgm-074-v3-cftr&start=60)
