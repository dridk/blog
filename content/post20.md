Title: Introduction à la metagénomique
Slug: metagenomique
Date: 2016-09-20 18:51:48
Category: biologie
Tags: bioinformatique, génétique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/metagenomics.jpg
Status: draft

# Introduction
Le [microbiote](https://fr.wikipedia.org/wiki/Microbiote) et la [métagénomique](https://fr.wikipedia.org/wiki/M%C3%A9tag%C3%A9nomique) sont les deux mots tendances de ces dernières années dans les laboratoires de microbiologies. Derrière eux se cacherait les réponses à de nombreuses maladies maladies comme le [diabète](https://fr.wikipedia.org/wiki/Diab%C3%A8te), la [maladie de Crohn](https://fr.wikipedia.org/wiki/Maladie_de_Crohn) et même l'[autisme](https://fr.wikipedia.org/wiki/Autisme) ou la [schizophrénie](https://fr.wikipedia.org/wiki/Schizophr%C3%A9nie).       
Commençons donc par définir ces deux termes:    
- Le **microbiote** est l'ensemble des micro-organismes ( bactéries, virus, champignons, levure) vivants dans un environnement spécifique appelé **[microbiome](https://fr.wikipedia.org/wiki/Microbiome)**. L'exemple typique est le microbiote intestinal. Votre intestin est composé de millions d'espèces bactériennes différentes formant une communauté écologique en symbiose avec votre organisme nécessaire à son bon fonctionnement. Il joue par exemple un rôle de barrière vis-à-vis d'autres agents microbiens pathogènes. La destruction du microbiote intestinal par des antibiotiques est par exemple responsable des infections intestinales à [Clostridium difficile](https://fr.wikipedia.org/wiki/Clostridium_difficile).    
Pour vous prouvez l'importante du microbiome, retenez que le génome humain est composé d'environ 23 000 gènes. Le nombre de gène retrouvé dans l'ensemble des micro-organismes du microbiome intestinale se compte en millions.        
- La **métagénomique** est la méthode d'étude du microbiote. C'est une technique de [séquençage](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age) et d'analyse de l'ADN contenu dans un milieu. A l'instar de la [génomique](https://fr.wikipedia.org/wiki/G%C3%A9nomique) qui consiste à séquencer un unique génome, la métagénomique séquence les génomes de plusieurs individus d'espèces différente dans un milieu donnée. Une analyse typique de métagénomique vous donnera la composition d'un microbiome. C'est à dire quels espèces sont présentes, leurs abondances et leurs diversités.    
C'est en partie grâce à l’évolution majeur des technologies de séquençage haut débit et à la bioinformatique, que la métagénomique est aujourd'hui d'actualité.    
Dans la suite de cette article, je parlerai uniquement de la métagénomique bactérienne, plus particulièrement la métagénomique ciblé sur l'[ARN 16S](https://fr.wikipedia.org/wiki/ARN_ribosomique_16S). Mais gardez bien en tête que la métagénomique virale et mycotique, bien que plus rare, existent aussi. 

# Stratégie en métagénomique 
Il existe deux grandes stratégies de séquençage en métagénomique. La stratégie globale et la stratégie ciblé.  
- **La métagénomique globale** consiste à fragmenter **tous** les ADNs présent dans un échantillons en courts fragments et les séquencer à l'aide d'un [séquenceur haut débit](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age_de_l'ADN). D’où le nom de *[Shotgun sequencing](https://en.wikipedia.org/wiki/Shotgun_sequencing)*. Les séquences (ou *reads*) obtenues sont ré-assembler bioinformatiquement afin de reconstruire les génomes bactériens d'origine.   

<div class="figure">
    <img src="../images/post20/shotgun_sequencing.png" /> 
    <div class="legend">Stratégie globale. L'ensemble des ARNs présents dans un échantillon de microbiote sont séquencés</div>
</div>

- **La métagénomique ciblé** n'est pas de la métagénomique à proprement parlé, mais de la métagénétique. En effet cette stratégie consiste à séquencer un unique gène au lieu d'un génome complet. Mais vu que le terme *métagénomique* est employé partout pour décrire cette stratégie, je continuerai ainsi. Ce gène doit être commun à plusieurs espèces tout en présentant des régions suffisamment variable afin de discriminer une espèce. En bactériologie, le gène utilisé est celui de l'ARN 16S. Un gène présent uniquement chez les bactéries.    

<div class="figure">
    <img src="../images/post20/target_sequencing.png" /> 
    <div class="legend">Stratégie ciblé. Seul les ADNs du gène cible sont séquencés. En bactériologie, le gène cible est l'ARN 16S </div>
</div>

Chaque stratégie a son avantage. La métagénomique globale est plus précise dans le sens ou elle séquence l'ensemble du génome d'une bactérie alors que la seconde ne s’intéresse qu'à un seul gène. De plus, la première stratégie permet de décrire le fonctionnement globale du microbiote en séquençant l'ensemble des gènes présents.   
La stratégie ciblé est quand à elle plus sélective. En effet le gène de l'ARN 16S est présent uniquement chez les bactéries qui seul seront séquencé. La stratégie globale séquence tous les ADN présent dans le milieu sans discernement, que ce soit bactérien, virale ou encore humain.  
Enfin les algorithmes de traitements des données issue d'un séquençage ciblé, sont beaucoup plus simple que les assemblages de génomes nécessaire dans le séquençage globale. Pour comprendre cette complexité, essayer de mélanger toutes les pièces de 200 puzzles différents et tenter de retrouver les modèles originaux. C'est la problématique de la métagénomique globale.   
On ne s’intéressera ici qu'à la stratégie 16S, utilisé en bactériologie. C'est un bon point de départ pour commencer!


##L' ARN 16S 

Vous connaissez les [ribosomes](https://fr.wikipedia.org/wiki/Ribosome)? Ces petits organelles dans la cellule formés de deux sous-unité permettant la traduction de l'ARN en protéine. Et bien chez la bactérie et uniquement chez elle, la petit sous unité est formé de l'ARN 16S. 

<div class="figure">
    <a href="../images/post20/ARN16s.jpg"><img src="../images/post20/ARN16s_thumb.jpg" /> </a>
    <div class="legend">Structure secondaire de l'ARN 16S avec ces différentes boucles.</div>
</div>

Il s'agit d'un [ARN non codant](https://fr.wikipedia.org/wiki/ARN_non_codant) composé d'environ 1500 nucléotides possédant des 
régions constante et variable. Il suffit d'aligner la séquence d'ARN 16S de différentes espèces bactériennes pour s'en rendre compte. En effet, comme vous pouvez le voir sur la figure ci-dessous, certaine région sont constante entre les bactéries alors que d'autres régions sont variables. 


<div class="figure">
    <img src="../images/post20/alignment.png" /> 
    <div class="legend">Similarité des séquences d'ARN 16S entre plusieurs bactérie. Sous le graphique figure les différents couples d'amorces utilisable</div>
</div>



Les régions variables n'ont pas de rôle fonctionnel important et peuvent divergé au cours de l’évolution sous l'effet des [mutations neutres](https://fr.wikipedia.org/wiki/%C3%89volution_des_taux_de_mutation).  
C'est ce qui va nous permettre de discriminer les [taxons](https://fr.wikipedia.org/wiki/Taxon) bactériens au sein du microbiome. A chaque taxon correspondra une séquence particulière au niveaux de ces régions variables. Il s'agit de la signature du taxons. 
Les régions constantes vont permettre quand à elle de capturer l'ensemble des ARN 16S. En effet ces régions étant identique chez toutes les bactéries, il est possible de  construire des [amorces](https://fr.wikipedia.org/wiki/Amorce_(g%C3%A9n%C3%A9tique)) comme en [PCR](https://fr.wikipedia.org/wiki/PCR) afin de sélectionner la région d’intérêt.    
En réalité, seul une partie de l'ARN 16S est séquencé car Les séquenceurs haut débit ne peuvent peuvent pas séquencer d'une traite les 1500 nucléotides de l'ARN 16S. (enfin..sauf le [Pacbio](http://www.pacb.com/)). Le couple d'amorce V3-V5, que vous pouvez voir sur la figure 3, permet par exemple de séquencer une région de 500 nucléotides contenant 3 régions variables. 

## Assignent taxonomique 
Une fois le séquençage réalisé, c'est au tour des bioinformaticiens de prendre le relais. Un fichier contenant l'ensemble des reads (séquences) et obtenus après séquençage. Après plusieurs étapes de filtrage et de nettoyage de ces données, il faut assigner à chaque séquences le nom de la bactérie. Pour cela, deux stratégies existent.   
- La stratégie *[close-reference](http://qiime.org/tutorials/otu_picking.html#closed-reference-otu-picking)* consiste à comparer chaque séquence aux séquences présente dans une base de donnée avec un seuil en général de 97% de similarité. [Greengene](http://greengenes.lbl.gov/cgi-bin/nph-index.cgi), [Silva](https://www.arb-silva.de/) et [RDP](https://rdp.cme.msu.edu/) sont les bases de données d'ARN 16S les plus connues. Cette stratégie à le mérite d'être rapide. Mais son principal problème et d'ignorer les séquences absentes des bases de donnée. Pour palier à ce problème, la deuxième stratégie peut être utilisé.   


<div class="figure">
    <img src="../images/post20/close_reference.png" /> 
    <div class="legend">Stratégie 1. Chaque séquence est rechercher dans une base de donnée et assigné à son taxon</div>
</div>

- La stratégie appelé *[de novo](http://qiime.org/tutorials/otu_picking.html#open-reference-otu-picking)*, n'utilise pas de base donnée mais consiste à comparer les séquences entre elles et les regrouper par similarité. Les [clusters](https://fr.wikipedia.org/wiki/Partitionnement_de_donn%C3%A9es) ainsi formés élisent une [séquence consensus](https://fr.wikipedia.org/wiki/S%C3%A9quence_consensus) qui peut à son tour être annoté par une base de donnée ou rester comme tel définissant alors une espèce inconnu.   

<div class="figure">
    <img src="../images/post20/de_novo.png" /> 
    <div class="legend">Stratégie 2. Les séquences sont comparé être elle pour former des groupes similaires ou cluster</div>
</div>

Une fois l’assignation taxonomique réalisée, il suffit de compter le nombre d'espèces présent pour chaque échantillon et de construire la table des [OTUs](https://fr.wikipedia.org/wiki/OTU).

## La table des OTUs 
Le point de départ de toutes analyses en métagénomique commence par la construction de la table des OTUs (Operationnal taxonomic unit). La notion d'espèce est difficile avec les bactéries, on parle plutôt d'OTU pour définir un ensemble de bactéries similaire à plus de 97%.   
La table des OTUs est un tableau à doubles entrées contenant le nombre de séquence par OTU et par échantillons. On parle d'*abondance*. Ces abondances absolues sont normalisées afin de rendre les échantillons comparable. Plusieurs méthode de normalisation existe, mais la plus courante et d'utiliser les pourcentages. Sur la figure ci-dessous L'echantillons 1 et 3 ont tous les deux une abondances absolues de 3 en bactéries rouges. En pourcentage, leurs abondances relatives changent en 42.8% et 75%. 

<div class="figure">
    <img src="../images/post20/otu_table2.png" /> 
    <div class="legend">Strategie close reference et de novo</div>
</div>

## Analyse des données 

### Diversité Alpha
La [diversité alpha](https://fr.wikipedia.org/wiki/Richesse_sp%C3%A9cifique) est un indicateur de diversité dans un échantillon unique. Le nombre d'espèce dans un échantillon est par un exemple un indicateur d'alpha diversité. Mais d'[autres indicateurs existent](http://drive5.com/usearch/manual/alpha_diversity.html). 
En effet, gardez à l'esprit que ce qui est séquencé n'est qu'un échantillon plus ou moins représentative de la réalité. 
Les bactéries abondantes d'un milieu seront certainement séquencé, mais les bactéries de faibles abondances le seront très peu voir pas du-tout. 
L'indicateur *Chao1* estime le nombre d'espèces non-séquencés à partir de celles observées en comptant le nombre de singletons et de doubletons. (Une espèces observé 1 seul fois est un singleton, 2 fois est un doubletons).
D'autre indice existe comme l'[indice de Shannon](https://en.wikipedia.org/wiki/Diversity_index), de [Simpson](http://www.countrysideinfo.co.uk/simpsons.htm) ou encore celui de [Fisher](http://groundvegetationdb-web.com/ground_veg/home/diversity_index).    
Le graphique ci-dessous est un exemple de diversité alpha montrant les différences de microbiote intestinal en fonction du régime alimentaire.  

<div class="figure">
    <img src="../images/post20/alpha_diversity.jpg" /> 
    <div class="legend">Diversité alpha du microbiote intestinal en fonction du régime alimentaire. <br/><i> <a href="https://peerj.com/articles/659/">Source </a></i></div>
</div>


### Diversité Beta
La [diversité bêta](https://fr.wikipedia.org/wiki/Diversit%C3%A9_b%C3%AAta) consiste à mesurer la diversité des espèces entre les échantillons. On procède le plus souvent à l'[analyse multivarié](https://fr.wikipedia.org/wiki/Statistique_multivari%C3%A9e) de la matrice des OTUs en ayant recourt aux méthodes d'[ordinations](https://en.wikipedia.org/wiki/Ordinate) comme l'[analyse en composante principale](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales). Pour faire simple, si nous avions 2 échantillons et 40 espèces dans notre matrice des OTUs, la représentation sur un graphique serait facile en utilisant 2 axes ( 1 par échantillons) et 40 points (les espèces) répartis sur les axes selon leurs abondances. On pourrait alors retrouver des groupes de points distincts. 

<div class="figure">
    <img src="../images/post20/2dplot.png" /> 
    <div class="legend">Chaque point représente une espèces repartis sur les deux échantillons en fonction de leurs abondances. Certaines espèces semble associées entre elles. </div>
</div>

Mais le plus souvent, il y a plusieurs échantillons dans la table des OTU ce qui nécessite un nombre d'axe impossible à représenter graphiquement. Les méthodes d'ordination répondent à ce problème en projetant la variabilité de tous ces axes sur 2 axes pouvant être visualisé. 
L'Analyse en composante principale (ACP) est un exemple d'ordination. Il en existe d'autre, et la plus couramment utilisé en métagénomique, jumelle de l'ACP, et [l'analyse en coordonnée principale](https://en.wikipedia.org/wiki/Multidimensional_scaling#Types) ( PCoA) que je ne détaillerai pas.    
Une fois la représentation réalisé, on cherche alors des groupes de points et la variable explicative que l'on visualise à l'aide d'une couleur. Sur le figure ci-dessous, l'analyse de plusieurs échantillons provenant de différent site anatomique, révèle les compositions propre à chaque site.

<div class="figure">
    <img src="../images/post20/beta_diversity.png" /> 
    <div class="legend">Analyse en composante principale de différent échantillons microbien provenant de différents sites anatomiques. <br/><i><a href="http://www.nature.com/nature/journal/v486/n7402/full/nature11234.html"> Source </a> </i></div>
</div>

# Conclusion 
La métagénomique est un sujet complexe en plein essor qui nécessite une connaissance précise des différentes techniques pour éviter toutes écueil. En effet de nombreux biais peuvent intervenir à toutes les étapes que ce soit coté biologie que bioinformatique. D'ailleurs, l'assignation taxonomique que je décris dans cette article reste simple et naïve. D'autre méthode plus complexe mais valable statistiquement sont préférable. Par exemple la méthode dite de ["Minimum Entropy Decomposition"](http://www.nature.com/ismej/journal/v9/n4/full/ismej2014195a.html) permet de classer les OTU en s'abstenant du seuil théorique des 97%.    
Enfin, si vous voulez approfondir la métagénomique, je vous invite très fortement à regarder [les vidéos de Dan Knights](https://www.youtube.com/watch?v=htbeJhtFAXw&list=PLOPiWVjg6aTzsA53N19YqJQeZpSCH9QPc) ( un dieu en métagénomique) disponible sur youtube! 


## Référence
* [Cours en vidéo de Dan Knights](https://www.youtube.com/watch?v=htbeJhtFAXw&list=PLOPiWVjg6aTzsA53N19YqJQeZpSCH9QPc)
* [Génomique et métagénomique bactérienne: applications cliniques et importance médicale](https://www.revmed.ch/RMS/2014/RMS-N-450/Genomique-et-metagenomique-bacteriennes-applications-cliniques-et-importance-medicale)
* [Enterotype of the human gut microbiome](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3728647/)
* [Structure, function and diversity of the healthy human microbiome](http://www.nature.com/nature/journal/v486/n7402/full/nature11234.html)
* [Outil : QIIME](http://qiime.org/)
* [Outil : Vsearch ](https://github.com/torognes/vsearch)
* [Outil :Philoseq](https://joey711.github.io/phyloseq/)

## Remerciement 
[@Thibaud_GS ](https://twitter.com/Thibaud_GS)



