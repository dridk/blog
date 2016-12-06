Title: Introduction à la métagénomique
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
- Le **microbiote** est l'ensemble des micro-organismes (bactéries, virus, champignons, levures) vivants dans un environnement spécifique appelé **[microbiome](https://fr.wikipedia.org/wiki/Microbiome)**. L'exemple typique est le microbiote intestinal. Votre intestin est composé de millions d'espèces bactériennes différentes formant une communauté écologique en symbiose avec votre organisme et nécessaire à son bon fonctionnement. Il joue entre autre un rôle de barrière vis-à-vis d'autres agents microbiens pathogènes. La destruction du microbiote intestinal par des antibiotiques est par exemple responsable des infections intestinales par *[Clostridium difficile](https://fr.wikipedia.org/wiki/Clostridium_difficile)*.    
Pour vous prouver l'importante du microbiome, retenez que le génome humain est composé d'environ 23 000 gènes. Le nombre de gènes retrouvés dans l'ensemble des micro-organismes du microbiome intestinal se compte en millions.        
- La **métagénomique** est la méthode d'étude du microbiote. C'est une technique de [séquençage](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age) et d'analyse de l'ADN contenu dans un milieu. A l'inverse de la [génomique](https://fr.wikipedia.org/wiki/G%C3%A9nomique) qui consiste à séquencer un unique génome, la métagénomique séquence les génomes de plusieurs individus d'espèces différentes dans un milieu donné. Une analyse typique de métagénomique vous donnera la composition d'un microbiome. C'est à dire quelles espèces sont présentes, leurs abondances et leurs diversités.    
C'est en partie grâce à l’évolution majeure des technologies de séquençage haut débit et à la bioinformatique, que la métagénomique est aujourd'hui à notre portée.    
Dans la suite de cet article, nous verrons uniquement la métagénomique bactérienne, plus particulièrement la métagénomique ciblé sur l'[ARN 16S](https://fr.wikipedia.org/wiki/ARN_ribosomique_16S). Mais gardez bien en tête que les métagénomiques virales et mycotiques, bien que plus rares, existent aussi. 

# Stratégie en métagénomique 
Il existe deux grandes stratégies de séquençage en métagénomique : la stratégie globale et la stratégie ciblée.  

- **La métagénomique globale** consiste à fragmenter **tous** les ADNs présents dans un échantillon en courts fragments et les séquencer à l'aide d'un [séquenceur haut débit](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age_de_l'ADN). D’où le nom de *[Shotgun sequencing](https://en.wikipedia.org/wiki/Shotgun_sequencing)*. Les séquences (ou *reads*) obtenues sont ré-assemblées bioinformatiquement afin de reconstruire les génomes bactériens d'origine.   

<div class="figure">
    <img src="../images/post20/shotgun_sequencing.png" /> 
    <div class="legend">Stratégie globale : L'ensemble des ADNs présents dans un échantillon de microbiote sont séquencés.</div>
</div>

- **La métagénomique ciblée** n'est pas de la métagénomique à proprement parler, mais de la *métagénétique*. Cette stratégie consiste à séquencer un unique gène au lieu d'un génome complet. Cependant le terme de *métagénomique* étant plus régulièrement employé pour décrire cette stratégie, je continuerai ainsi. Ce gène doit être commun à plusieurs espèces tout en présentant des régions suffisamment variables afin de discriminer une espèce. En bactériologie, le gène utilisé est celui de l'ARN 16S. Il s'agit d'un gène présent uniquement chez les bactéries.    

<div class="figure">
    <img src="../images/post20/target_sequencing.png" /> 
    <div class="legend">Stratégie ciblé : Seuls les ADNs du gène cible sont séquencés. En bactériologie, le gène cible est l'ARN 16S. </div>
</div>

Chaque stratégie a son avantage. La métagénomique globale est plus précise dans le sens où elle séquence l'ensemble du génome d'une bactérie alors que la seconde ne s’intéresse qu'à un seul gène. Cette première stratégie permet par exemple de décrire le fonctionnement global du microbiote en séquençant l'ensemble des gènes présents.   
La stratégie ciblée est quant à elle plus sélective. En effet, le gène de l'ARN 16S est présent uniquement chez les bactéries qui seules seront séquencées. La stratégie globale va séquencer tous les ADN présents dans le milieu sans discernement, qu'ils soient bactériens, viraux ou encore humains.
Enfin, les algorithmes de traitements des données issues d'un séquençage ciblé sont beaucoup plus simples que les assemblages de génomes nécessaires dans le séquençage global. Pour comprendre cette complexité, essayez de mélanger toutes les pièces de 200 puzzles différents et tentez de retrouver les modèles originaux. C'est la problématique de la métagénomique globale.   
On ne s’intéressera ici qu'à la stratégie 16S, utilisée en bactériologie. C'est un bon point de départ pour commencer !


##L' ARN 16S 

Vous connaissez les [ribosomes](https://fr.wikipedia.org/wiki/Ribosome) ? Ces petits organelles dans la cellule formés de deux sous-unités permettant la traduction de l'ARN en protéine. Et bien chez la bactérie, et uniquement chez elle, la petite sous unité est formée de l'ARN 16S. 

<div class="figure">
    <a href="../images/post20/ARN16s.jpg"><img src="../images/post20/ARN16s_thumb.jpg" /> </a>
    <div class="legend">Structure secondaire de l'ARN 16S avec ses différentes boucles.</div>
</div>

Il s'agit d'un [ARN non codant](https://fr.wikipedia.org/wiki/ARN_non_codant) composé d'environ 1500 nucléotides possédant des régions constantes et variables. Il suffit d'aligner la séquence d'ARN 16S de différentes espèces bactériennes pour s'en rendre compte. Comme vous pouvez le voir sur la figure ci-dessous, certaines régions sont constantes entre les bactéries alors que d'autres régions sont variables. 


<div class="figure">
    <img src="../images/post20/alignment.png" /> 
    <div class="legend">Similarités des séquences d'ARN 16S entre plusieurs bactéries. Sous le graphique figurent les différents couples d'amorces utilisables.</div>
</div>



Les régions variables n'ont pas de rôle fonctionnel important et peuvent diverger au cours de l’évolution sous l'effet des [mutations neutres](https://fr.wikipedia.org/wiki/%C3%89volution_des_taux_de_mutation).  
C'est ce qui va nous permettre de discriminer les [taxons](https://fr.wikipedia.org/wiki/Taxon) bactériens au sein du microbiome. A chaque taxon correspondra une séquence particulière au niveau des régions variables. Il s'agit de la signature du taxon. 
Les régions constantes vont permettre quant à elles de capturer l'ensemble des ARN 16S. Ces régions étant identiques chez toutes les bactéries, il est possible de construire des [amorces](https://fr.wikipedia.org/wiki/Amorce_(g%C3%A9n%C3%A9tique)) comme pour une [PCR](https://fr.wikipedia.org/wiki/PCR) afin de sélectionner la région d’intérêt.    
En réalité, seule une partie de l'ARN 16S est séquencée car les séquenceurs haut débit ne peuvent pas séquencer d'un coup les 1500 nucléotides de l'ARN 16S (enfin... sauf le [Pacbio](http://www.pacb.com/)). Le couple d'amorce V3-V5, que vous pouvez voir sur la figure 3, permet par exemple de séquencer une région de 500 nucléotides contenant 3 régions variables. 

## Assignent taxonomique 
Une fois le séquençage réalisé, c'est au tour des bioinformaticiens de prendre le relais. Un fichier contenant l'ensemble des reads (séquences) est obtenu après séquençage. Après plusieurs étapes de filtrage et de nettoyage de ces données, il faut assigner à chaque séquence le nom de la bactérie. Pour cela, deux stratégies existent.

- La stratégie *[close-reference](http://qiime.org/tutorials/otu_picking.html#closed-reference-otu-picking)* consiste à comparer chaque séquence aux séquences présentes dans une base de donnéees avec un seuil en général de 97% de similarité. [Greengene](http://greengenes.lbl.gov/cgi-bin/nph-index.cgi), [Silva](https://www.arb-silva.de/) et [RDP](https://rdp.cme.msu.edu/) sont les bases de données d'ARN 16S les plus connues. Cette stratégie a le mérite d'être rapide mais son principal problème est d'ignorer les séquences absentes des bases de données. Pour palier à ce problème, la deuxième stratégie peut être utilisée.   


<div class="figure">
    <img src="../images/post20/close_reference.png" /> 
    <div class="legend">Stratégie 1. Chaque séquence est recherchée dans une base de données et assignée à son taxon.</div>
</div>

- La stratégie appelée *[de novo](http://qiime.org/tutorials/otu_picking.html#open-reference-otu-picking)*, n'utilise pas de base données mais consiste à comparer les séquences entre elles puis les regrouper par similarité. Les [clusters](https://fr.wikipedia.org/wiki/Partitionnement_de_donn%C3%A9es) ainsi formés élisent une [séquence consensus](https://fr.wikipedia.org/wiki/S%C3%A9quence_consensus) qui peut à son tour être annotée par une base de données ou rester comme telle définissant alors une espèce inconnue.   

<div class="figure">
    <img src="../images/post20/de_novo.png" /> 
    <div class="legend">Stratégie 2. Les séquences sont comparées entre elles pour former des groupes similaires ou clusters.</div>
</div>

Une fois l’assignation taxonomique réalisée, il suffit de compter le nombre d'espèces présentes dans chaque échantillon et de construire la table des [OTUs](https://fr.wikipedia.org/wiki/OTU).

## La table des OTUs 
Le point de départ de toutes analyses en métagénomique est la construction de la table des OTUs (operationnal taxonomic unit). La notion d'espèce est difficile avec les bactéries, on parle plutôt d'OTU pour définir un ensemble de bactéries similaires à plus de 97 %.   
La table des OTUs est un tableau à double entrées contenant le nombre de séquences par OTU et par échantillon. On parle d'*abondance*. Ces abondances absolues sont normalisées afin de rendre les échantillons comparables. Plusieurs méthodes de normalisation existent, mais la plus courante est d'utiliser les pourcentages. Sur la figure ci-dessous, les échantillons 1 et 3 ont tous les deux une abondance absolue de 3 en bactéries rouges. En pourcentage, leurs abondances relatives deviennent 42,8 % et 75 % respectivement. 

<div class="figure">
    <img src="../images/post20/otu_table2.png" /> 
    <div class="legend">Tables des OTUs obtenues à partir de plusieurs échantillons</div>
</div>

## Analyse des données 

### Diversité Alpha
La [diversité alpha](https://fr.wikipedia.org/wiki/Richesse_sp%C3%A9cifique) est une mesure indiquant la diversité d'un échantillon unique.
Le nombre d'espèce est par exemple un indicateur d'alpha diversité.

<div class="figure">
    <img src="../images/post20/alpha1.png" /> 
    <div class="legend">B est plus diversifié que A car il contient deux fois plus d'espèces</div>
</div>

 Mais comme vous pouvez le voir dans la figure ci-dessous, Le nombre d'espèce n'est pas toujours adapté. C'est pour cette raison que d'autres indicateurs existent.

<div class="figure">
    <img src="../images/post20/alpha2.png" /> 
    <div class="legend">B contient plus d'espèce mais semble moins diversifié</div>
</div>

L'indice de Shannon ou entropie de Shannon est un exemple d'alpha diversité répondant à ce problème.  Cette indice reflète aussi bien le nombre d'espèce que leurs abondances. Sa formule est la suivante : 

<div class="figure">
    <img src="../images/post20/shannon.svg" /> 
    <div class="legend">Indice de Shannon. Pour chaque espèce faire la somme des fréquences multiplié par le log des fréquences </div>
</div>

La figure A précédente contient 13 espèces, dont 4 vertes, 5 rouges et 4 bleues. La diversité de shannon pour A est donc : 

<div class="figure">
    <img src="../images/post20/eq1.gif" /> 
</div>

En faisant de même pour B, on retrouve alors une diversité plus faible de 0.72.

<div class="figure">
    <img src="../images/post20/alpha3.png" /> 
    <div class="legend">L'entropie de A est supérieur à celle de B</div>
</div>

Les autres indicateurs répondent chacun à des problèmes différents. L'indice [Chao1](http://www.evolution.unibas.ch/walser/bacteria_community_analysis/2015-02-10_MBM_tutorial_combined.pdf) estime le nombre d'espèce réel dans l'environnement à partir du nombre d'espèce dans l'échantillon. Il y a aussi l'indice de [Simpson](http://www.countrysideinfo.co.uk/simpsons.htm), de [Fisher](http://groundvegetationdb-web.com/ground_veg/home/diversity_index) et l'[indice ACE](http://www.evolution.unibas.ch/walser/bacteria_community_analysis/2015-02-10_MBM_tutorial_combined.pdf). Faite un tour sur [ce site](http://www.evolution.unibas.ch/walser/bacteria_community_analysis/2015-02-10_MBM_tutorial_combined.pdf) pour avoir plus des informations plus détaillées.      
Le graphique ci-dessous montre les différences de diversité alpha du microbiote intestinal en fonction du régime alimentaire.  

<div class="figure">
    <img src="../images/post20/alpha_diversity.jpg" /> 
    <div class="legend">Diversité alpha du microbiote intestinal en fonction du régime alimentaire. <br/><i> <a href="https://peerj.com/articles/659/">Source </a></i></div>
</div>


### Diversité Beta
La [diversité bêta](https://fr.wikipedia.org/wiki/Diversit%C3%A9_b%C3%AAta) consiste à mesurer la diversité des espèces entre les échantillons. On procède le plus souvent à l'[analyse multivariée](https://fr.wikipedia.org/wiki/Statistique_multivari%C3%A9e) de la matrice des OTUs en ayant recours aux méthodes d'[ordinations](https://en.wikipedia.org/wiki/Ordinate) comme l'[analyse en composantes principales](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales). Pour faire simple, imaginons que notre table des OTUs soit composée de 2 bactéries et 6 échantillons. La représentation sur un graphique serait facile en utilisant 2 axes (1 par bactérie). Chaque point de ce graphique serait un échantillon dont les coordonnées représentent l'abondance pour chaque bactérie. La figure de gauche ci-dessous illustre cet exemple. En colorant ces points sur une variable attachée aux échantillons, comme le site de prélèvement, on pourrait découvrir des groupes distincts, comme l'illustre la figure de droite.

<div class="figure">
    <img src="../images/post20/2dplot.png" /> 
    <div class="legend">Chaque point représente un échantillon réparti sur les deux axes en fonction de leurs abondances. Certains échantillons semblent associées entre eux. </div>
</div>

Bien entendu, il y a plus de deux bactéries différentes dans un microbiome. Ce qui nécessite un nombre d'axe impossible à représenter graphiquement. Les méthodes d'ordination répondent à ce problème en projetant la variabilité de tous ces axes sur 2 axes pouvant être visualisés. 
L'analyse en composantes principales (ACP) est un exemple d'ordination. Il en existe bien évidemment d'autres. La plus couramment utilisée en métagénomique est une jumelle de l'ACP, [l'analyse en coordonnées principales](https://en.wikipedia.org/wiki/Multidimensional_scaling#Types) (PCoA) que je ne détaillerai pas.    
Une fois la représentation réalisée, on cherche alors des groupes de points et la variable explicative que l'on visualise à l'aide d'une couleur. Sur la figure ci-dessous, l'analyse de plusieurs échantillons provenant de différents sites anatomiques révèle les compositions propres à chaque site.

<div class="figure">
    <img src="../images/post20/beta_diversity.png" /> 
    <div class="legend">Analyse en composantes principales de différents échantillons microbiens provenant de différents sites anatomiques. <br/><i><a href="http://www.nature.com/nature/journal/v486/n7402/full/nature11234.html"> Source </a> </i></div>
</div>

# Conclusion 
La métagénomique est un sujet complexe en plein essor qui nécessite une connaissance précise des différentes techniques pour éviter tout écueil. De nombreux biais peuvent intervenir à toutes les étapes, tant du coté biologique que bioinformatique. D'ailleurs, l'assignation taxonomique que je décris dans cet article reste simple et naïve. D'autres méthodes plus complexes mais valables statistiquement sont préférables. Par exemple la méthode dite de « [Minimum Entropy Decomposition](http://www.nature.com/ismej/journal/v9/n4/full/ismej2014195a.html) » permet de classer les OTU en s'abstenant du seuil théorique des 97 %.    
Enfin, si vous voulez approfondir la métagénomique, je vous invite très fortement à regarder [les vidéos de Dan Knights](https://www.youtube.com/watch?v=htbeJhtFAXw&list=PLOPiWVjg6aTzsA53N19YqJQeZpSCH9QPc) (un dieu en métagénomique) disponibles sur YouTube! 


## Références
* [Cours en vidéo de Dan Knights](https://www.youtube.com/watch?v=htbeJhtFAXw&list=PLOPiWVjg6aTzsA53N19YqJQeZpSCH9QPc)
* [Génomique et métagénomique bactérienne: applications cliniques et importance médicale](https://www.revmed.ch/RMS/2014/RMS-N-450/Genomique-et-metagenomique-bacteriennes-applications-cliniques-et-importance-medicale)
* [Enterotype of the human gut microbiome](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3728647/)
* [Structure, function and diversity of the healthy human microbiome](http://www.nature.com/nature/journal/v486/n7402/full/nature11234.html)
* [Outil : QIIME](http://qiime.org/)
* [Outil : Vsearch ](https://github.com/torognes/vsearch)
* [Outil :Philoseq](https://joey711.github.io/phyloseq/)

## Remerciements 
[@Thibaud_GS ](https://twitter.com/Thibaud_GS)    
[@Piplopp  ](https://github.com/Piplopp)    
[@pausrrls ](https://github.com/pausrrls)   
[@Oodnadatta](https://github.com/Oodnadatta)   



