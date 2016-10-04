Title: Introduction à la metagénomique
Slug: metagenomique
Date: 2016-09-20 18:51:48
Category: biologie
Tags: bioinformatique, génétique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/metagenomics.jpg
Status: draft

# Intro 
La métagénomique est le mot tendance de ces dernières années dans les laboratoires de microbiologies. Avec ce mot, il semblera que le mystère d'un tas de maladie soit enfin resolu comme l'autisme, la schyzophrénie ou encore les maladies autoimmune. 
Mais alors à part un mot qui en jete, c'est quoi la métagénomique ?  
La métagénomique est une technique de séquençage et d'analyse de l'ADN contenu dans un milieu. A l'instar de la génomique qui séquence l'ADN d'une espèce, la métagénomique séquence les ADN de plusieurs individus d'espèces différente dans un milieu donnée.      
Par exemple le sol, les océans ou votre intestin sont composé de millions de bactérie d'espèce différente. On appelle ça un Microbiome. Une analyse typique de métagénomique cherche à connaitre dans ce microbiome le contenu en espèces, l'abondance des espèces ou encore leurs diversités.   
En gros vous mettez un prélevement multimicrobien dans un mixeur, et le but du jeux c'est de trouver le type et le pourcentage de bactéries présents rien qu'à partir des ADN! Un vrai puzzle génomique!

# Stratégie de séquençage
Il existe deux grandes stratégies de séquençage en métagénomique. On peut soit séquencer tous les ADNs d'un prélevement. C'est la stratégie "shotgun".   
Ou alors séquencer un unique gène commun à toutes les espèces et suffisament variable pour pouvoir discriminer les espèces entre elle. 
En bactériologie, cette stratégie utilise le gène de l'ARN 16s. Un gène présent uniquement chez les bactéries.   
Chaque stratégie a son avantage. La stratégie shotgun est plus précise car elle séquence l'ensemble de l'ADN d'une bactérie alors que la seconde ne s'interesse qu'à une fraction du génome bactérien. En revanche les données générés avec l'ARN 16s sont moin volumineuse et plus facile à manipuler. Mais surtout elles sont selectif. En effet la première strategie séquence tous les ADN présent dans le milieu sans discernement, que ce soit bactérien, virale ou encore humain alors que la seconde produit uniquement des séquences provenant de bactéries.   
Je bosse en ce moment sur la métagenomique 16s, donc on ne parlera que de cette stratégie. 

## ARN 16S 

Vous connaissez les ribosomes? Ces petits organelles formé de deux sous-unité permettant la traduction de l'ARN en protéine. Et bien chez la bactérie et uniquement chez elle, la petit sous unité est formé de l'ARN 16s.   
Il s'agit d'un ARN non codant composé d'environ 1500 nucléotides possédant des régions constante et variable. Il suffit d'aligner la séquence d'ARN 16s de différentes espèces bactérienne pour s'en rendre compte. En effet, comme vous pouvez le voir dans la figure suivante, certaine région sont identique ( constante ) entre les bactéries alors que d'autre sont variable. 

<div class="figure">
    <img src="../images/post20/alignment.png" /> 
    <div class="legend">Graph du pipeline snakemake</div>
</div>

La figure suivante montre l'ARN 16s avec ses boucles et ces 9 régions variables. Ce sont des régions pouvant être altéré au cours de l'Evolution sans impacter grandement le fonctionnement du ribosome contrairement aux régions constantes. 

<div class="figure">
    <a href="../images/post20/ARN16s.jpg">
    <img src="../images/post20/ARN16s_thumb.jpg" /> </a>
    <div class="legend">Graph du pipeline snakemake</div>
</div>

L'ARN 16s est donc l'outil ideal pour faire de la métagenomique. Car d'une part il possède des régions constante permettant de selectionner le même gène chez toutes les espèces, et d'autre part il possède des régions variable permettant d'identifier l'espèces.      
En général on ne s'interesse qu'à une sous partie de l'ARN 16s séquencé à grâce à un couple d'amorce. Pour ma part, j'utilise le couple d'amorce englobant V3-V5. ( Figure 1)

## Séquençage
## Assignement taxonomique 
## fichier biom 

## Indicateur de biodiversité ! 
## Alpha diversité 
## Beta diversité 




