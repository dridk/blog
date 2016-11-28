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
Commençons donc par définir ces deux termes à l'aide de wikipedia.     
Le **microbiote** est l'ensemble des micro-organismes ( bactéries, virus, champignons, levure) vivant dans un environnement spécifique appelé **microbiome**. L'exemple typique est le microbiote intestinale. Votre intestin est composé de millions d'espèces bactériennes différentes formant une communauté écologique en symbiose avec votre organisme. Ce microbiome est une partie intégrante de votre organisme nécessaire à son fonctionnement. Il joue par exemple un rôle de barrière vis à vis d'autre agent microbien pathogène. La destruction du microbiote intestinale par des antibiotiques,par exemple, est responsable des infections intestinales à Clostridium difficile.      
La **métagénomique** est la méthode d'étude du microbiote. C'est une technique de séquençage et d'analyse de l'ADN contenu dans un milieu. A l'instar de la génomique qui séquence le génome d'une espèce, la métagénomique séquence les génomes de plusieurs individus d'espèces différente dans un milieu donnée. Une analyse typique de métagénomique vous donnera la composition d'un microbiome. C'est à dire quels espèces sont présentes, leurs abondances et leurs diversités.    
C'est en partie grâce à l’evolution majeur des technologie de séquençage haut débit et à la bioinformatique, que la métagénomique est aujourd'hui d'actualité.    
Dans la suite de l'article, je parlerai uniquement de métagénomique bactérienne. Mais gardez bien en tête que la métagénomique virale et mycotique, bien que plus rare, existent aussi. 

# Stratégie en métagénomique 
Il existe deux grandes stratégies de séquençage en métagénomique. La stratégie globale et la stratégie ciblé.  
- **La métagénomique globale** consiste à fragmenter tous les ADNs présent dans un échantillons en court fragments de 100 à 300 paires de bases qui seront séquencer à l'aide d'un séquenceur haut débit. D'ou le nom de *Shotgun sequencing*. Les séquences obtenues sont ré-assembler bioinformatiquement afin de reconstruire les génomes bactériens d'origine.   
- **La métagénomique ciblé** n'est pas de la métagénomique à proprement parlé, mais de la métagénétique. En effet cette stratégie consiste à séquencer un unique gène au lieu d'un génome complet. Mais vu que le terme *métagénomique* est plus souvent employé pour décrire cette stratégie, je garde ce mot.  
Ce gène doit être commun à plusieurs espèces tout en présentant des régions suffisamment variable afin de discriminer une espèce. En bactériologie, le gène utilisé est celui de l'ARN 16S. Un gène présent uniquement chez les bactéries.    
Chaque stratégie a son avantage. La métagénomique globale est plus précise dans le sens ou elle séquence l'ensemble du génome d'une bactérie alors que la seconde ne s’intéresse qu'à un seul gène. De plus, cette stratégie permet de décrire le fonctionnement globale du microbiote en séquençant l'ensemble des gènes présents.   
La stratégie ciblé est quand à elle plus sélective. En effet l'ARN 16s est présent uniquement chez les bactéries qui seul seront séquencé. Tandis que la stratégie globale séquence tous les ADN présent dans le milieu sans discernement, que ce soit bactérien, virale ou encore humain.  
Enfin les algorithmes de traitements des données issue d'un séquençage ciblé, sont beaucoup plus simple que les assemblages de génomes nécessaire dans le séquençage globale. Pour comprendre cette complexité, essayer de mélanger toutes les pièces de 200 puzzles différents et tenter de retrouver les modèles originaux. C'est la problématique de la métagénomique globale.   
On ne s’intéressera ici qu'à la stratégie 16s, utilisé en bactériologie. C'est un bon point de départ pour commencer!


##Séquençage de l' ARN 16S 

Vous connaissez les ribosomes? Ces petits organelles formé de deux sous-unité permettant la traduction de l'ARN en protéine. Et bien chez la bactérie et uniquement chez elle, la petit sous unité est formé de l'ARN 16s.   
Il s'agit d'un ARN non codant composé d'environ 1500 nucléotides possédant des 
régions constante et variable. Il suffit d'aligner la séquence d'ARN 16s de différentes espèces bactérienne pour s'en rendre compte. En effet, comme vous pouvez le voir dans la figure suivante, certaine région sont identique ( constante ) entre les bactéries alors que d'autre région sont variable. 

<div class="figure">
    <img src="../images/post20/alignment.png" /> 
    <div class="legend">Graph du pipeline snakemake</div>
</div>

La figure suivante montre l'ARN 16s avec ses boucles et ces 9 régions variables. Ces régions n'ont pas de rôle fonctionnel important et peuvent divergé au cours de l'evolution sous l'effet des mutations neutres.  
Il s'agit d'un outil ideal pour discriminer les taxons bactériens au sein du microbiome. A chaque taxon correspondra une séquence particulière dans ces régions variable. Il s'agit de la signature du taxons. 
Les régions constantes vont permettre quand à elle de construire des amorces de PCR afin de sélectionner les ARN 16s de toutes les bactéries.     
Le séquençage haut débit ne permet pas de séquencer de longue séquence. Dans la plus part des cas, on ne séquence qu'une partie de l'ARN 16s. Le couple d'amorce V3-V5, que vous pouvez voir sur la figure 3, permet d'amplifier puis de séquencer une région de 500 nucléotides à l'aide de la technologie illumina MISeq. 

## Assignent taxonomique 
Une fois le séquençage réalisé, c'est au tour des bioinformaticiens de prendre le relais. Un fichier contenant l'ensemble des reads(sequences) et obtenus après séquençage. Après plusieurs étapes de filtrage et de nettoyage de ces données, il faut assigner à chaque séquences le nom de la bactérie. Pour cela, deux stratégies existent.   
- La stratégie "close-reference" consiste à comparer chaque séquence aux séquences présente dans une base de donnée avec un seuil en général de 97% de similarité. Greengene, Silva et RDP sont les bases de données d'ARN 16s les plus connus. Cette stratégie à le mérite d'être rapide. Mais son principal problème et d'ignorer les séquences absentes des bases de donnée. Pour palier à ce problème, la deuxième stratégie peut être utilisé.   
- La stratégie appelé"de novo", n'utilise pas de base donnée mais consiste à comparer les séquences entre elle et les regrouper par similarité. Les "clusters" ainsi formé élisent une séquence consensus qui peut à son tour être annoté par une base de donnée ou rester comme tel définissant alors une espèce inconnu. 

## La table des OTUs 
Le point de départ de toute analyse en métagénomique est d'obtenir à partir des données de séquençage la table des OTU. (Operationnal taxonomic unit). La notion d'espèce chez les bactéries n'existe pas, et on parle plutôt d'OTU pour définir un ensemble de bactéries similaire à plus de 97%.   
Il s'agit d'un tableau à deux entrées contenant l'abondance (Le nombre de séquence) par OTU et par échantillons. Dans le schéma suivant, 3 échantillons provenant de 3 patients ont été analysé permettant de construire la table des OTU. 
Cette table contient des valeurs absolus. Il faut les normaliser en pourcentage afin de rendre comparable les échantillons entre eux. D'autres méthodes de normalisation existe, mais ne sont pas detaillé ici.  

<div class="figure">
    <img src="../images/post20/otu_table.png" /> 
    <div class="legend">Strategie close reference et de novo</div>
</div>


## Analyse des données 

### Diversité Alpha
L'alpha diversité est un indicateur de la diversité d'un unique échantillon. Le nombre d'espèce contenu dans un échantillon est par un exemple un indicateur d'alpha diversité. Mais d'autre indicateurs existent. 
En effet, gardez à l'esprit que ce qui est séquencé n'est qu'un échantillon plus ou moins représentative de la réalité. 
Les bactéries abondantes d'un milieu seront certainement séquencé, mais les bactéries de faibles abondances le seront très peu voir pas du-tout. 
L'indicateur Chao1 estime ce nombre d'espèces non séquencé à partir de celles observées en comptant le nombre de singletons et de doubletons. (Une espèces observé 1 seul fois est un singleton, 2 fois est un doubletons).
D'autre indice existe comme l'indice de Shannon, de Simpson ou encore celui de Fisher.    
Le graphique ci-dessous est un exemple de diversité alpha montrant des différences de microbiotes intestinale en fonction du régime alimentaire.  

<div class="figure">
    <img src="../images/post20/alpha_diversity.jpg" /> 
    <div class="legend">Diversité alpha du microbiote intestinale en fonction du régime alimentaire</div>
</div>


### Diversité Beta
La beta diversité consiste à mesurer la diversité des espèces avec différents échantillons. On procède le plus souvent à l'analyse multivarié de la matrice des OTUs en ayant recourt aux méthodes d'ordinations comme l'analyse en composante principale. Pour faire simple, si nous avions 2 échantillons et 40 espèces dans notre matrice des OTUs, la représentation sur un graphique serait facile en utilisant 2 axes ( 1 par échantillons) et 40 points (les espèces) répartis sur les axes selon leurs abondances. On pourrait alors retrouver des groupes de points distincts. 

Mais le plus souvent, il y a plusieurs échantillons dans la table des OTU ce qui nécessite un nombre d'axe impossible à représenter graphiquement. Les méthodes d'ordination répondent à ce problème en projetant la variabilité de tous ces axes sur 2 axes pouvant être visualisé. 
L'Analyse en composante principale est un exemple d'ordination. Il en existe d'autre, et la plus couramment utilisé en métagenomique, jumelle de l'ACP, et l'analyse en coordonnée principale ( PCoA) que je ne détaillerai pas.    
Une fois la représentation réalisé, on cherche alors des groupes de points et la variable explicative que l'on visualise à l'aide d'une couleur. Sur le schéma ci dessous, l'analyse de plusieurs échantillons provenant de différent site anatomique, revèle des compositions propre à chaque site.

<div class="figure">
    <img src="../images/post20/beta_diversity.png" /> 
    <div class="legend">Analyse en composante principale de différent échantillons microbien provenant de différents sites anatomiques</div>
</div>

# Conclusion 
La métagénomique est un sujet complexe en plein essor qui necessite une connaissance précise des différentes techniques pour éviter toutes ecceuils. En effet de nombreux biais peuvent intervenir à toutes les étapes que ce soit coté biologie que bioinformatique. D'ailleurs, l'assignation taxonomique que je décris dans cette article est une méthode peu recommandé par les statisticien. La methode dite de "Minimum Entropy Decomposition" est préférable en s'abstenant d'utiliser le seuil théorique des 97%. 

