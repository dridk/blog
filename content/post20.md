Title: Introduction à la metagénomique
Slug: metagenomique
Date: 2016-09-20 18:51:48
Category: biologie
Tags: bioinformatique, génétique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/metagenomics.jpg
Status: draft

# Intro 
La métagénomique est le mot tendance de ces dernières années dans les laboratoires de microbiologies. Avec ce mot, il semblera que les mystères qui se cachent derrière des maladies comme l’auto-immunité, l'autisme ou même la schizophrénie soient enfin résolu. 
Mais alors à part un mot qui en jette, c'est quoi la métagénomique ?  
La métagénomique est une technique de séquençage et d'analyse de l'ADN contenu dans un milieu. A l'instar de la génomique qui séquence le génome d'une espèce, la métagénomique séquence les génomes de plusieurs individus d'espèces différente dans un milieu donnée.      
Par exemple le sol, les océans ou votre intestin sont composé de millions de bactérie d'espèce différente. On appelle ça un Microbiome. Une analyse typique de métagénomique cherche à connaître la composition de ce microbiome. C'est à dire les espèces présentes, leurs abondances et leurs diversités.
En gros, vous récupéré un prélevement multimicrobien, vous séquencez l'ensemble des ADN, et le but du jeux est de trouver a quelles espèces appartiennent chaque fragment d'ADN. Un vrai casse-tête de bioinformatique! 

# Stratégie en métagénomique 
Il existe deux grandes stratégies de séquençage en métagénomique. La stratégie shotgun consiste à séquencer tous les ADNs d'un prélèvement puis ré-assembler les génomes à l'aide d'outil bioinformatique.  
La seconde stratégie n'est pas de la métagénomique à proprement parlé, mais de la métagénétique. Cette stratégie consiste à séquencer un unique gène au lieu d'un génome complet. Ce gène doit être commun à plusieurs espèces et présenter des régions suffisamment variable pour pouvoir discriminer une espèce.    
En bactériologie, cette stratégie utilise le gène de l'ARN 16s. Un gène présent uniquement chez les bactéries.   
Chaque méthode a son avantage. La stratégie shotgun est plus précise car elle séquence l'ensemble du génome d'une bactérie alors que la seconde ne s’intéresse qu'à un seul gène. En revanche la deuxième stratégie est plus sélective. En effet la méthode Shotgun séquence tous les ADN présent dans le milieu sans discernement, que ce soit bactérien, virale ou encore humain.   Tandis que la stratégie par l'ARN 16s, ne produit que des séquences bactériennes.
Dans cette article, on ne s’intéressera qu'à la stratégie utilisant l'ARN 16s. C'est un bon point de départ avant de se lancer dans la vrai métagénomique.


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

L'ARN 16s est un outil ideal pour discriminer des populations dans le microbiome. Les régions constantes vont permettre de designer des amorces de PCR afin de sélectionner les gènes de toutes les bacteries. Tandis que les régions variables vont permettre d'identifier les différentes espèces.      
Il n'est pas nécessaire de séquencer tous le gène. Certaine régions du gène sont suffisamment informative tout en diminuant les côuts technique d'un séquençage complet. Le couple d'amorce V3-V5 et souvent utilisé permettant d'amplifier une région de 500 nucléotides. Taille idéal pour un séquençage en Sanger ou en NGS.

## Séquençage
C'est grâce à l'évolution rapide des technologies de séquençage haut débit que la métagénomique est devenu tendance. Ces machines sont capable de séquencer des milliards de nucléotides en un temps records là ou les anciens séquenceurs comme le Sanger prenait 10 ans.    
Par exemple, le séquençage Illumina sur la plateforme MiSeq est souvent utilisé en métagénomique 16s. Il permet de séquencer jusqu'à 25 millions de fragments d'ADN contenant la région V3-V5.   
Détailler le séquençage haut débit nécessiterai un article entier. Mais en résumé vous mettez dans cette machine les ADN de votre prélèvement et il en resort un fichier FastQ contenant les séquences d'ARN 16s de toutes les bactéries présentent. 

## Assignement taxonomique 
Après avoir nettoyer le fichier fastq des artefacts de séquençage, il faut assigner le nom de la bactérie à chaque reads puis les dénombrer afin d'estimer l'abondance des bactéries.   

<div class="figure">
    <img src="../images/post20/otu_picking.png" /> 
    <div class="legend">Strategie close reference et de novo</div>
</div>

Pour cela il existe deux stratégies. La première stratégie appelé "close-reference" consiste à comparer chaque séquence aux séquences d'une base de donnée de bactéries connus. Si une séquence n'est pas présente dans cette base de donnée, alors elle est ignoré. Greengene, Silva et RDP sont les bases de données d'ARN 16s les plus connus.     
La deuxième stratégie appelé "de novo", n'utilise pas de base donnée. Cette stratégie consiste à comparer les reads entre eux et les regrouper par similarité. On appelle ça de la clusterisation et différent algorithme existe. 
Par exemple la clusterisation par k-means est bien expliqué dans cette vidéos.
Enfin, les deux stratégies peuvent être couplé. Les reads absent des bases de données peuvent être secondairement clusterisé.  

## La table des OTUs 
L'étape ultime de toute analyse en métagénomique est d'obtenir à partir des données de séquençage la table des OTU. (Operationnal taxonomic unit). La notion d'espèce chez les bactéries n'existe pas, on parle plutôt d'OTU qui se défini chez les bactéries par une similarité supérieur à 97%.    
Il s'agit d'un tableau à deux entrées contenant le nombre de reads ou abondance par OTU  et par échantillons. Dans le schéma suivant, 3 échantillons provenant de 3 patients ont été analysé permettant de construire la table des OTU. 
Il est important de normaliser cette table. En effet si l'on considère les valeurs brutes, il y a le même nombre de séquence verte chez le patient 1 et 3. On peut donc raisonner en pourcentage ce qui nous donne 30% et 55% respectivement. D'autre méthode de normalisation existe . 
Cette table est souvent sauvegarder dans un fichier *.biom qui peut alors être analyser avec des outils statistiques.    

<div class="figure">
    <img src="../images/post20/otu_table.png" /> 
    <div class="legend">Strategie close reference et de novo</div>
</div>




## Analyse des données 
A partir de notre table des OTU, il est possible de générer un tas de graphique trop cool. Vous pouvez tester le site phinch avec un jeux d'exemple .

<div class="figure">
    <img src="http://microbe.net/wp-content/uploads/2014/06/Screen-Shot-2014-06-06-at-10.54.56-AM.png" /> 
    <div class="legend">Strategie close reference et de novo</div>
</div>

2 indicateurs sont interessant a calculer . L'alpha et la beta diversité 
## Alpha diversité 
## Beta diversité 




