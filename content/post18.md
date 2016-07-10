Title: Le diagnostic prénatal non-invasif de la trisomie 21
Slug: dpni
Date: 2016-06-29 21:27:53
Category: biologie
Tags: bioinformatique, génétique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

La trisomie 21 est un syndrome polymalformatif avec un retard mental plus ou moin sevère dont l'origine est la présence d'un chromosome 21 surnuméraire. On a tous en mémoire l'image de l'acteur Pascal Duquenne atteind de ce syndrome et loréat du prix d'interprétation au festival de cannes pour le film le *Huitème jour*.     
En France, le dépistage de la trisomie 21 est proposé à toutes les femmes enceintes au 1er trimestre de grossesse. Ce dépistage consiste à calculer un score en fonction de marqueurs sanguins (alpha foetaprotéine) associé à des signe d'appel échographique (clarté nuccal). Si ce score depasse un certain seuil, un diagnostic cytogénétique est proposé pour confirmer la trisomie. Il consiste à prélever des cellules foetales par des techniques invasives comme l'amniocentèse et de dénombrer le nombre de chromosome sur un caryotype comme illustré ci-dessous. 

<div class="figure">
    <img src="../images/post18/caryotype.jpg" />
    <div class="legend">Carytoype présentant 3 chromosomes 21 au lieu de 2</div>
</div>


Malheuresement ces gestes invasifs ne sont pas anodin. On estime entre 0.5% et 1% le risque de fausse couche lié à l'amniocentèse.  
Cela peu sembler faible, mais le dépistage actuel souffre d'une très mauvaise spécificité. C'est à dire que beaucoup de femme réponde positif au dépistage alors que leurs feotus est indemme. Par conséquence beaucoup trop d'amniocentèse sont réalisé innutilement avec le risque de fausse couche qui en découle.    
Mais depuis l'avenement récent du séquençage haut débit, un nouveau teste de dépistage beaucoup plus puissant en terme de sensibilité et de spécificité voit le jour. Il s'agit du DPNI pour Dépistage Prénatal Non Invasif. ( Vous lirez souvent diagnostic préntal non invasif, mais il s'agit pour l'heure de dépistage). Ce nouveau teste consiste à quantifier sur une simple prise de sang des fragments d'ADN foetal circulant. 

##Methode
### L'ADN foetal
Il y a des fragments d'ADN double brin qui circule librement dans votre sang. En général ce sont les votres sauf si vous faite des experiences tordus dans votre laboratoire ou si vous êtes enceintes. En effet chez la femme enceinte environs 10% de ces fragments proviennent du foetus. Plus précisement ces fragments proviennent de la lyse des cellule trophoblastiques, un composant du placenta ayant la même origine embryologique que le foetus.   
L'idée derrière le DPNI, c'est qu'à partir d'une simple prise de sang, on va pouvoir quantifier l'ADN circulant et dire si il y a trop de fragment d'ADN provenant du chromosome 21.     
La figure ci-dessous illustre la quantification d'ADN circulant chez une mère sans et avec foetus trisomique, en considérant que 90% de l'ADN circulant est maternel et 10% d'origine foetal. Cette quantification est permise grâce au nouvelle technologie de séquençage haut débit.

<div class="figure">
    <img src="../images/post18/chromosomes.png" />
    <div class="legend">Carytoype présentant 3 chromosomes 21 au lieu de 2</div>
</div>

### Le Séquençage de nouvelle génération 
Le NGS (Next Generation Sequencing) est une technologie récente permettant le séquençage de l'ADN de façon très rapide grâce à un haut niveau de parallelisation. Sans entrer dans les détails, les fragments d'ADN provenant du sang maternel,qu'on appelera read à présent, sont séquencé puis aligner sur le génome de référence par des algorithmes bioinformatiques. 
On obtiens alors un fichier BAM contenant la liste des reads associé à leurs positions sur le génome. C'est à dire qu'a chaque fragment séquencé son chromosome lui est associé.   
La figure ci-dessous résume les étapes du séquençage. 

<div class="figure">
    <img src="../images/post18/ngs.png" />
    <div class="legend">Les reads sont séquencé et sauvegardé dans un fichier fastQ. Les reads sont ensuite aligné sur le génome de référence hg19. En vert les reads provenant du foetus. En violet les reads maternelles</div>
</div>

## Quantification et teste statistique

Une trisomie 21 se caractèrise par un excès de reads s'allignant sur le chromosome 21. Pour mesurer cette excès ils nous faut des valeurs de réferences obtenues chez des femmes enceintes témoins dont le foetus est sains. 
Avec un nombre suffisant de témoin, le nombre de read moyen ainsi que l'écart-type sont calculé.      
Pour savoir si une patiente présente trop de reads, il suffit de recherche une différence significative à l'aide d'un Z-score en comparant les données de la patiente et les valeurs de référence.    
Le logiciel RapidR crée par le NHS utilise cette approche. Un exemple de résultats est présenté dans la figure suivante. 

<div class="figure">
    <img src="../images/post18/rapidR.png" />
    <div class="legend">En ordonnée le Z-score, en absisse les chromosomes. Sur ce graphique, la patiente présente un excès significatif en read s'allignant sur le chromosome 21</div>
</div>

Un autre logiciel, wisecondor approche différent le problème et propose d'utiliser les autres chromosomes comme références au sein du même échantillon. C'est une approche plus complexe, mais peut se résumer ainsi.   
Tout d'abord, le génome est segmenté en région de 10 kilobase appelé bin. Le nombre de reads est comptabilisé par bin au lieu d'être comptabilisé par chromosome comme précédement.       
A partir de mesure chez des témoins sains, les bins du chromosome 21 sont associé a d'autre bin du génome lorsqu'il contienne plus ou moin le même nombre de reads. La figure suivante est une représentation de ces associations.  
<div class="figure">
    <img src="../images/post18/wisecondor.png" />
    <div class="legend">En ordonnée le Z-score, en absisse les chromosomes. Sur ce graphique, la patiente présente un excès significatif en read s'allignant sur le chromosome 21</div>
</div>

Ce logiciel permet donc de mesurer l'excès de reads mappant le chromosome 21 en le comparant aux autres chromosomes. Cette technique à l'avantage de se passer des aléas du séquençage qui peuvent faire varier le nombre de reads. 


## Stratégie de dépistage 
En Novembre 2015, la Haute autorité de santé a évalué positivement ce nouveau teste de dépistage. La sensibilité et la spécificité avoisine les 100%. Le risque de faux négatif pouvant être lié l'absence d'ADN foetal si le prélevement est réalisé trop tôt. Un risque de faux positif est egalement possible dans les cas de mosaissime foetal.   
Aujourd'hui toutes les femmes enceintes, quel que soit leurs âge, sont informées de la possibilité de recourrir à ce teste.    
La stratégie actuel est de proposer le dépistage standard. Si celui ci revient positif, au lieu de proposer directement un geste invasif, le DPNI sera proposé. Si celui ci revient positif alors le geste invasif et le diagonstic cytogénétique est réalisé. 
A l'heure actuelle seul le laboratoire Cerba propose le DPNI. Mais depuis janvier 2016 certain centre hospitalier propose ce teste qui n'est pas malheuresement pas encore remboursé et avoisine les 800€.  

## Reference



## Remerciement 


