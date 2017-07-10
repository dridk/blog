Title: Le séquençage de nouvelle génération
Slug: ngs
Date: 2017-05-16 15:58:18
Tags: biologie
Category: génétique
Author: Sacha Schutz
Status: Draft

[Le séquençage de nouvelle génération ](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age_de_l%27ADN#S.C3.A9quen.C3.A7age_haut_d.C3.A9bit_.28HTS.29)(NGS: Next Generation Sequencing) est la révolution biotechnologique de ces dernières années, en permettant de séquencer de grande quantité d'ADN en des temps records.
A titre d'exemple, entre 1990 et 2003 lors du projet *[human genome](https://en.wikipedia.org/wiki/Human_genome)*, il a fallu 3 milliards de dollars pour séquencer le génome humain en utilisant des séquenceurs de type [Sanger](https://en.wikipedia.org/wiki/Sanger_sequencing) répartis dans plusieurs laboratoire à travers le monde. Aujourd'hui, Avec un séquenceur NGS [Illumina HiSeq X](https://www.illumina.com/systems/sequencing-platforms/hiseq-x.html), en trois jours, on peut séquencer trois génomes humains pour [$1000](http://www.nature.com/news/is-the-1-000-genome-for-real-1.14530) chacun. Le graphique ci-dessous, que vous verez regulièrement, montre l'évolution du coût de séquençage par million de nucléotide au cours du temps. Et encore, ce graphique s'arrête en 2013. La société illumina à déjà promis le génome à [$100](https://www.illumina.com/company/news-center/press-releases/press-release-details.html?newsid=2236383) d'ici deux ans avec le nouveau séquenceur [Illumina NovaSeq](https://www.illumina.com/systems/sequencing-platforms/novaseq.html).  
Cet article est un avant-gout très vulgarisé pour découvrir les bases du séquençage haut débit.  

<div class="figure">
    <img src="../images/post22/moore.png" /> 
    <div class="legend">Diminutions du coût du séquençage par nucléotides au cours des dernières années</div>
</div>   


# Un séquençage à haut-débit

Imaginons que votre génome s'assimile à un gros livre de plus de 3 milliards de caractères écrit avec les lettres A,C,G et T. Séquencer, c'est lire le contenu de ce livre. Vous pouvez soit le lire entièrement, c'est à dire séquencer l'ensemble de votre génome, soit lire certaine page, c'est à dire faire du séquençage ciblé.      
Les séquenceurs de première générations de type [Sanger](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age_de_l%27ADN#M.C3.A9thode_de_Sanger) sont capable, sur un capillaire, de lire des fragments assez long d'environ 800 paires de bases en 1 heures. Si vous faites le calcul, vous verez rapidement que pour atteindre les 3 milliards de nucléotides, il vous faudra plus d'une vie pour reussir à séquencer votre génome (>400 ans). Pour allez plus vite, l'idée est de lire plusieurs fragments en même temps, c'est à dire paralléliser le séquençage. Les plus performant des séquenceurs Sanger, peuvent parallélisé jusqu'à [96 fois](https://www.thermofisher.com/order/catalog/product/3730XL) en utilisant 96 capillaires. On a donc 96 x 800 nucléotides lu en 1 heures. Les séquenceurs NGS de deuxièmes générations sont capable eux de lire jusqu'à [20 milliard](https://www.illumina.com/systems/sequencing-platforms/novaseq.html) de fragments à la fois. 



# Librairie de séquençage
Ce qu'on appelle une librarie, est l'ensemble des fragments d'ADN que nous désirons séquencer. Pour créer une librarie, deux méthodes sont à retenir selon que l'on veuille séquencer l'ensemble du génome ou seulement des régions d'interets. 

### Méthode globale

Lancez le livre en l'air et tirez dessus au shotgun pour faire une pluie de fragment d'ADN aléatoire. C'est ce qu'on appelle *stricto sensu*, la [stratégie shotgun](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age_de_l%27ADN#M.C3.A9thode_globale_ou_Shotgun). Cette méthode est utilisé pour séquencer des génomes entiers.

<div class="figure">
    <img src="../images/post22/shotgun.png" /> 
    <div class="legend">La stratégie shotgun consiste à fragmenter l'ADN en séquence aléatoire puis à les séquencer.</div>
</div>   


#### Méthode de fragmentation
Plusieurs méthodes existe pour fragmenter l'ADN:

* **Fragmentation par [sonication](https://www.ncbi.nlm.nih.gov/pubmed/22485919)** : En envoyant des ultra-son à la bonne fréquence, on arrive à créer des fragments d'ADN de la taille désiré. 

* **Fragmentation enzymatique** : L'utilisation d'enzyme de restriction permet de couper l'ADN au niveau de certain mot précis.   


### Méthode ciblé 
Nous ne désirons pas forcément connaître l'ensemble du livre. Nous voulons peut être séquencer uniquement le paragraphe contenant la séquence d'un seul gène, ou tout les paragraphes du livres contenant les gènes associés au retard mentaux. Pour cela nous pouvons enrichir notre librairie en sélectionnant uniquement les fragments d'ADN désiré. Deux techniques sont à retenir:

* **L'enrichissement [par capture](https://www.ncbi.nlm.nih.gov/pubmed/18330355)** : Après fragmentation, les fragments d'ADN sont filtré en s'hybridant sur des séquences complementaire disposé sur une plaque ou en milieu liqude. Les fragments d'ADN qui ne s'hybride pas sont eliminé. 
  

<div class="figure">
    <img src="../images/post22/capture.png" /> 
    <div class="legend">Exemple d'enrichissement en phase liquide grâce à des billes magnétiques</div>
</div>   



* **Enrichissement par PCR** : Les fragments désiré sont amplifié par PCR. Nous pouvons amplifier une seul région avec un coupe d'amorces (simplexe). Ou alors plusieurs régions avec plusieurs couples d'amorces (multiplexe). Dans cette stratégie, toutes les séquences d'un même amplicon seront identique. 


<div class="figure">
    <img src="../images/post22/amplicon.png" /> 
    <div class="legend">La stratégie par amplicon produit des séquences identiques</div>
</div>   



# Sequençage 
Ils existent différentes méthode de séquençage

* Le séquençage par synthèse ( Illumina).
* Le pyroséquençage (Roche 454).
* La ligation (SOLid Thermofisher).
* La détéction des ion H+ (Proton Thermofisher).

Dans l'ensemble, le principe général reste le même. Chaque fragment est d'abord cloné plusieurs fois afin d'amplifier le signal. Puis le brin complémentaire de chaque fragment est synthétisé. A chaque incorporation d'un nucléotide un signal est détécté. De la lumière pour illumina ou une variation de pH sur du Proton. 
A la fin du séquençage, chaque fragment a été séquencé en parallèle. L'ensemble des données est enregistrer dans un fichier Fastq.


## Exemple de séquençage sur Proton

<div class="figure">
    <img src="../images/post22/ion.png" /> 
    <div class="legend">Schéma simplifié d'un séquençage type Proton</div>
</div>   


# Alignement des séquences
A la fin du séquençage, la biologie fait place à la bioinformatique. Les séquences des fragments, que nous appelerons maintenant des "reads", sont sauvegarder dans un fichier fastq contenant les séquences et leurs qualité. Cette qualité est un score (Phred) évaluant à chaque nucléotide sa fidélité de séquençage.
Vous pouvez télécharger ici un exemple pour voir à quoi cela ressemble.   
Mais le travail est loin d'être fini. Ce que nous avons, ce sont uniquement des courtes séquences de 150 pb. Ce que nous voulons c'est obtenir la séquence complète d'un gène ou d'un génome entier. Pour cela, il faut reconstruire un puzzle en réalisant un alignement:
Deux méthodes existent :

- **Alignement de novo** : Il s'agit de résoudre un puzzle sans modèle. Les fragments d'ADN qui sont chevauchant permette petit à petit de reconstruire un contig. Puis l'assemblage des contigs entre eux permet d'obtenir un scaffold. Cette technique est très couteuse en terme de calcul. Des algorithmes bioinformatiques comme les graphe de Debruijn, permettent de résoudre ce problème. Cette méthode est principalement employé pour reconstruire des génomes non connus.

<div class="figure">
    <img src="../images/post22/aligndenovo.png" /> 
    <div class="legend">L'alignement de novo ne s'aide pas d'un modèle</div>
</div>   



- **Alignement avec reference**: Il s'agit toujours de résoudre un puzzle. Mais cette fois, en s'aidant d'un modèle. Par exemple une version du génome humain (hg19) servira de référence. 
Chaque read est aligné sur cette référence. La complexité de calcul est netement plus simple qu'avec l'allignement de novo. On utilise en général l'algorithme de Burrows Wheeler permettant de rechercher de manière efficace une correspondance entre les reads et la référence. Après cette allignement, on obtient un fichier BAM associant à chaque reads des coordonnées génomique ( chromosome + position). La representation visuel d'un fichier bam ressemble à la figure ci dessous. On appelle la profondeur, le nombre moyen de reads qui se superpose et couverture, l'etalement des reads sur la zone d'interet.  

<div class="figure">
    <img src="../images/post22/alignref.png" /> 
    <div class="legend">L'alignement par référence s'aide d'un modèle</div>
</div>   

<div class="figure">
    <a href="../images/post22/samtools.png"><img src="../images/post22/samtools_thumb.png" /> </a>
    <div class="legend">L'alignement par référence s'aide d'un modèle</div>
</div>   




# Evaluation d'un séquenceur 

Les capacités d'un séquenceur haut débit sont défini par : 

- La longueur des reads produits(L)
- Le nombre de reads produits (n)
- Le nombre de nucléotides lu: (L x n)
- Le temps de séquençage 
- La qualité du séquençage
 
# Vers les séquenceurs de 3 ème génération

Mais à peine sortie, ces technologies deviennent rapidement obsolète. En effet, je ne vous ai pas parlé des séquenceurs de 3ème générations, qui feront surement l'objet d'un nouvel article. Ce sont des séquenceurs capable de générer de très long reads (jusqu'a x) sans avoir besoin de cloner les reads qui peut être source une source de biais. En revanche, ces nouvelles techniques produisent encore beaucoup d'erreur de séquençage. Les deux leaders de ce Next Next generation sequencing sont Nanopore et PacBio Science qui termine le guerre de brevet. Et rien que voir la miniaturisation de leurs séquenceur, ça me plonge dans un monde futuriste

photo nanopore 