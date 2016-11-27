Title: Introduction à la metagénomique
Slug: metagenomique
Date: 2016-09-20 18:51:48
Category: biologie
Tags: bioinformatique, génétique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/metagenomics.jpg
Status: draft

# Introduction
Le microbiote et la métagénomique son les deux mots tendances de ces dernières années dans les laboratoires de microbiologies. Derrière eux se cacherait les réponses à différentes maladies comme les maladies auto-immune ou encore l'autisme et la schizophrénie.    
Commençons donc par définir ces deux termes:     
Le **microbiote** est l'ensemble des micro-organismes ( bactéries, virus, champignons, levure) vivant dans un environnement spécifique appelé **microbiome**. L'exemple typique est le microbiote intestinale. Votre intestin est composé de millions d'espèces bactériennes différentes formant une communauté écologique en symbiose avec votre organisme. Ce microbiome est une partie intégrante de votre organisme nécessaire à son fonctionnement. Il joue par exemple un rôle de barrière vis à vis d'autre agent microbien pathogène. La prise d'antibiotique par exemple, favorise les infections intestinales à Clostridium difficile en détruisant les bactéries du microbiote intestinale.   
La **métagénomique** est la méthode d'étude du microbiote. C'est une technique de séquençage et d'analyse de l'ADN contenu dans un milieu. A l'instar de la génomique qui séquence le génome d'une espèce, la métagénomique séquence les génomes de plusieurs individus d'espèces différente dans un milieu donnée. Une analyse typique de métagénomique vous donnera la composition d'un microbiome. C'est à dire quels espèces sont présentes, leurs abondances et leurs diversités.    
C'est en partie grâce à l’evolution majeur des technologie de séquençage haut débit et à la bioinformatique, que la métagénomique est aujourd'hui d'actualité.

# Stratégie en métagénomique 
Il existe deux grandes stratégies de séquençage en métagénomique. La stratégie globale et la stratégie ciblé.  
- **La métagénomique globale** ou encore appelé *séquençage shotgun*,  consiste à séquencer tous les ADNs d'un prélèvement puis assembler les génomes à l'aide d'outil bioinformatique.  
- **La métagénomique ciblé** n'est pas de la métagénomique à proprement parlé, mais de la métagénétique. En effet cette stratégie consiste à séquencer un unique gène au lieu d'un génome complet. Mais vu que le terme *métagénomique* est plus souvent employé pour décrire cette stratégie, je garde ce mot.  
Ce gène cible doit être commun à plusieurs espèces tout en présentant des régions suffisamment variable pour pouvoir discriminer une espèce. En bactériologie, le gène utilisé est celui de l'ARN 16S. Un gène présent uniquement chez les bactéries.    
Chaque stratégie a son avantage. La métagénomique globale est plus précise dans le sens ou elle séquence l'ensemble du génome d'une bactérie alors que la seconde ne s’intéresse qu'à un seul gène. De plus, cette stratégie permet de décrire le fonctionnement globale du microbiote en séquençant l'ensemble des gènes présents.   
La stratégie ciblé est quand à elle plus sélective. En effet l'ARN 16s est présent uniquement chez les bactéries et seul celle ci seront séquencé. La stratégie globale séquence tous les ADN présent dans le milieu sans discernement, que ce soit bactérien, virale ou encore humain.  
Enfin les algorithmes de traitements des données issue d'un séquençage ciblé, sont beaucoup plus simple que les assemblages de génomes nécessaire dans le séquençage globale. Pour comprendre cette complexité, essayer de mélanger toutes les pièces de 200 puzzles différents et tenter de retrouver les modèles originaux.   
Dans cette article, on ne s’intéressera donc qu'à la stratégie 16s, utilisé en bactériologie. C'est un bon point de départ pour commencer!


##Séquençage de l' ARN 16S 

Vous connaissez les ribosomes? Ces petits organelles formé de deux sous-unité permettant la traduction de l'ARN en protéine. Et bien chez la bactérie et uniquement chez elle, la petit sous unité est formé de l'ARN 16s.   
Il s'agit d'un ARN non codant composé d'environ 1500 nucléotides possédant des 
régions constante et variable. Il suffit d'aligner la séquence d'ARN 16s de différentes espèces bactérienne pour s'en rendre compte. En effet, comme vous pouvez le voir dans la figure suivante, certaine région sont identique ( constante ) entre les bactéries alors que d'autre sont variable. 

<div class="figure">
    <img src="../images/post20/alignment.png" /> 
    <div class="legend">Graph du pipeline snakemake</div>
</div>

La figure suivante montre l'ARN 16s avec ses boucles et ces 9 régions variables. Ces régions peuvent être altéré au cours de l'Evolution sans impacter le fonctionnement du ribosome contrairement aux régions constantes. 
Il s'agit donc d'un outil ideal pour discriminer des espèces au sein du microbiome. Plus les espèces divergent, plus ces régions variables seront différentes.   
Les régions constantes vont permettre quand à elle de designer des amorces de PCR afin de sélectionner les ARN 16s de toutes les bactéries.    
Le séquençage haut débit ne permet pas de séquencer de longue séquence. Dans la plus part des cas, on ne séquence qu'une partie de l'ARN 16S. Le couple d'amorce V3-V5, que j'utilise pour ma thèse permet d'amplifier une région de 500 nucléotides à l'aide de la technologie Illumuna MiSeq et du Kit V3. Cette procédure nous donne une résolution assez grande pour discriminer le genre de bactérie présent. 

## Assignement taxonomique 
Une fois le séquençage réalisé, c'est au tour des bioinformaticiens de prendre le relais. Après plusieurs étapes de filtrage et de nettoyage des données, il faut assigner à chaque séquences le nom de la bactérie. Pour cela, deux stratégies existent.   
- La stratégie "close-reference" consiste à comparer chaque séquence aux séquences présente dans une base de donnée avec un seuil en général de 97% de similarité. Greengene, Silva et RDP sont les bases de données d'ARN 16s les plus connus. Cette stratégie à le mérite d'être rapide. Mais son principal problème et d'ignorer les séquences absent des bases de donnée. Pour palier à ce problème, la deuxième stratégie peut être utilisé.   
- La stratégie appelé"de novo", n'utilise pas de base donnée mais consiste à comparer les séquences entre elle et les regrouper par similarité. Les "clusters" ainsi formé élisent une séquence consensus qui peut à son tour être annoté par une base de donnée ou rester comme tel définissant une espèce inconnu. 

## La table des OTUs 
Le point de départ de toute analyse en métagénomique est d'obtenir à partir des données de séquençage la table des OTU. (Operationnal taxonomic unit). La notion d'espèce chez les bactéries n'existe pas, et on parle plutôt d'OTU pour définir un ensemble de bactéries similaire à plus de 97%.   
Il s'agit d'un tableau à deux entrées contenant l'abondance (Le nombre de séquence) par OTU et par échantillons. Dans le schéma suivant, 3 échantillons provenant de 3 patients ont été analysé permettant de construire la table des OTU. 
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




