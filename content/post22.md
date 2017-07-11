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
Les séquenceurs de première générations de type [Sanger](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age_de_l%27ADN#M.C3.A9thode_de_Sanger) sont capable de lire des fragments assez long d'environ 800 paires de bases en 1 heures sur 1 capillaire. Si vous faites le calcul, vous verez rapidement que pour atteindre les 3 milliards de nucléotides, il vous faudra plus d'une vie pour reussir à séquencer votre génome (>400 ans). Pour allez plus vite, l'idée est de lire plusieurs fragments en même temps, c'est à dire paralléliser le séquençage. Les plus performant des séquenceurs Sanger, peuvent parallélisé jusqu'à [96 fois](https://www.thermofisher.com/order/catalog/product/3730XL) en utilisant 96 capillaires. On a donc 96 x 800 nucléotides lu en 1 heures. Les séquenceurs NGS de deuxièmes générations sont capable eux, de lire des fragments de 150 à 300 pb mais jusqu'à [20 milliard](https://www.illumina.com/systems/sequencing-platforms/novaseq.html) de fragments à la fois. 



# Librairie de séquençage
Ce qu'on appelle une **librarie**, est l'ensemble des fragments d'ADN que l'on veut séquencer. Pour créer une librarie, deux méthodes sont à retenir selon que l'on veuille séquencer l'ensemble du génome ou seulement des régions d'interets. 

### Méthode globale

Lancez le livre en l'air et tirez dessus au shotgun pour faire une pluie de fragment d'ADN aléatoire. C'est ce qu'on appelle *stricto sensu*, la [stratégie shotgun](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age_de_l%27ADN#M.C3.A9thode_globale_ou_Shotgun). Cette méthode est utilisé pour séquencer des génomes entiers.

<div class="figure">
    <img src="../images/post22/shotgun.png" /> 
    <div class="legend">La stratégie shotgun consiste à fragmenter l'ADN en séquence aléatoire puis à les séquencer.</div>
</div>   


#### Méthode de fragmentation
Plusieurs méthodes existe pour fragmenter l'ADN:

* **Fragmentation par sonication** : En envoyant des ultra-son à la bonne fréquence, on casse l'ADN en morceau de taille précise.
* **Fragmentation enzymatique** : L'utilisation d'[enzyme de restriction](https://fr.wikipedia.org/wiki/Enzyme_de_restriction) permet de couper l'ADN au niveau de certain motif. 


### Méthode ciblé 
On ne désirons pas forcément lire l'ensemble du génome. On peut vouloir par exemple sequencer uniquement la partie codante ([exome](https://fr.wikipedia.org/wiki/Exome)), qui je le rappel, represente [moins de 2%](http://dridk.me/genome_chiffre_1.html). Ou alors simplement séquencer une liste de gènes ([panel de gènes](https://www.gatc-biotech.com/fr/expertise/sequencage-cible/panel-de-genes.html)) associé à une maladie.   
Dans tous les cas, il faut enrichir la librairie en sélectionnant uniquement les fragments d'ADN désiré. Deux techniques sont à retenir:

* **L'enrichissement [par capture](https://www.ncbi.nlm.nih.gov/pubmed/18330355)** : Après fragmentation, les fragments d'ADN sont filtré en s'hybridant sur des séquences complementaire disposé sur une plaque ou en milieu liqude. Les fragments d'ADN qui ne s'hybride pas sont eliminé. 
  

<div class="figure">
    <img src="../images/post22/capture.png" /> 
    <div class="legend">Exemple d'enrichissement en phase liquide grâce à des billes magnétiques</div>
</div>   



* **Enrichissement par PCR** : Les fragments désirés sont amplifié par [PCR](https://fr.wikipedia.org/wiki/PCR). Nous pouvons amplifier une seul région avec un coupe d'amorces (simplex). Ou alors plusieurs régions avec plusieurs couples d'amorces (multiplex). Dans cette stratégie, toutes les séquences d'un même [amplicon](https://fr.wikipedia.org/wiki/Amplicon) seront identique. 


<div class="figure">
    <img src="../images/post22/amplicon.png" /> 
    <div class="legend">La stratégie par amplicon produit des séquences identiques</div>
</div>   



# Sequençage 
Ils existent différentes méthode de séquençage:

* Le séquençage par synthèse ([Illumina](https://www.illumina.com/)).
* Le pyroséquençage ([Roche 454](https://fr.wikipedia.org/wiki/Technique_de_s%C3%A9quen%C3%A7age_454)).
* La ligation ([SOLid](https://www.thermofisher.com/fr/fr/home/life-science/sequencing/next-generation-sequencing/solid-next-generation-sequencing.html) [Thermofisher](https://www.thermofisher.com/fr/fr/home.html)).
* La détéction des ion H+ ([Proton](https://www.thermofisher.com/fr/fr/home/life-science/sequencing/next-generation-sequencing/ion-torrent-next-generation-sequencing-workflow/ion-torrent-next-generation-sequencing-run-sequence/ion-proton-system-for-next-generation-sequencing.html) [Thermofisher](https://www.thermofisher.com/fr/fr/home.html)).

Dans l'ensemble, le principe général reste le même. Chaque fragment est d'abord cloné plusieurs fois afin d'amplifier le signal. Puis le brin complémentaire de chaque fragment cloné est synthétisé. A chaque incorporation d'un nucléotide un signal est détécté. De la lumière pour illumina ou une variation de pH sur du Proton. 
A la fin du séquençage, chaque fragment a été séquencé en parallèle. L'ensemble des données est enregistrer dans un fichier Fastq.


## Exemple de séquençage sur Proton

<div class="figure">
    <img src="../images/post22/ion.png" /> 
    <div class="legend">Schéma simplifié d'un séquençage type Proton</div>
</div>   


Pour plus de détail sur les techniques de séquençage, une vidéo commercial est toujours mieux qu'un grand discours : 

- [Ion Torrent™ next-gen sequencing technology](https://www.youtube.com/watch?v=WYBzbxIfuKs)
- [Illumina Sequencing by Synthesis](https://www.youtube.com/watch?v=fCd6B5HRaZ8&t=204s) 


# Alignement des séquences
A la fin du séquençage, la biologie fait place à la bioinformatique. Les séquences des fragments, qu'on appele maintenant des "reads", sont sauvegarder dans un fichier [fastq](https://fr.wikipedia.org/wiki/FASTQ) contenant les séquences et leurs qualités (score Phred). La qualité est une estimation de l'erreur de séquençage par nucléotide.    
Vous pouvez télécharger [ici](http://www.internationalgenome.org/data-portal/sample)un exemple pour voir à quoi ça ressemble. 

<div class="figure">
    <img src="../images/post22/fastq_fig.jpg" /> 
    <div class="legend">Aperçu d'un read dans un fichier fastq. Le score de qualité associe à chaque nucléotide un caractère <a href="https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange) correspondant à un score"> ASCII </a> </div>
</div>   

Mais le travail est loin d'être fini. Ce que nous avons, ce sont uniquement des courtes séquences de 150 pb en général. Ce que nous voulons c'est obtenir la séquence complète d'un gène ou d'un génome entier. Pour cela, il faut reconstruire un puzzle en réalisant un [alignement](https://fr.wikipedia.org/wiki/Alignement_de_s%C3%A9quences). Deux méthodes existent :

- **Alignement de novo** : Il s'agit de résoudre un puzzle sans son modèle. Les fragments d'ADN qui sont chevauchant permette petit à petit de reconstruire ce qu'on appelle un [contig](https://fr.wikipedia.org/wiki/Contig). L'assemblage des contigs entre eux permet d'obtenir un scaffold. Cette technique est très couteuse en terme de calcul. Des algorithmes bioinformatiques comme les[graphe de Bruijn](https://fr.wikipedia.org/wiki/Graphe_de_de_Bruijn), permettent de résoudre ce problème. Cette méthode est principalement employé pour reconstruire des génomes non connus.

<div class="figure">
    <img src="../images/post22/aligndenovo.png" /> 
    <div class="legend">L'alignement de novo ne s'aide pas d'un modèle</div>
</div>   


- **Alignement avec reference**: Il s'agit toujours de résoudre un puzzle. Mais cette fois, en s'aidant d'un modèle. Par exemple une version du génome humain ([hg19](https://en.wikipedia.org/wiki/Reference_genome#Human_reference_genome)) servira de référence. 
Chaque read est aligné sur cette référence. La complexité de calcul est plus simple qu'avec l'allignement de novo. On utilise en général l'algorithme de [Burrows Wheeler](http://dridk.me/bwt.html) permettant de rechercher de manière efficace une correspondance entre les reads et la référence. Après cette allignement, on obtient un fichier [BAM](https://en.wikipedia.org/wiki/SAM_(file_format)) associant à chaque reads ses coordonnées génomiques. En général le chromosome et la position génomique.    
On appelle la profondeur, le nombre moyen de reads qui se superpose et recouvrement, l'etalement des reads sur la zone d'interet.  

 

<div class="figure">
    <img src="../images/post22/alignref.png" /> 
    <div class="legend">L'alignement avec référence consiste à aligner les reads sur une référence</div>
</div>   


<div class="figure">
    <a href="../images/post22/samtools.png"><img src="../images/post22/samtools_thumb.png" /> </a>
    <div class="legend">Visualisation d'un alignement réel avec <a href="http://samtools.sourceforge.net/">Samtools</a></div>
</div>   


# Evaluation d'un séquenceur 

Avec tout ça, vous êtes capable d'évaluer la capacité d'un séquenceur comme vous le feriez avant l'achat d'un PC ou d'une voiture.   
Les capacités d'un séquenceurs sont défini par : 

- La longueur des reads produits (L)
- Le nombre de reads produits (n)
- Le nombre de nucléotides lu: (L x n)
- Le temps de séquençage 
- La qualité du séquençage
 
# Pour finir, les séquenceurs de 3 ème génération

A peine sortie, ces technologies sont déjà devancé par les séquenceurs de 3ème générations, qui feront surement l'objet d'un nouvel article. Ce sont des séquenceurs capable de générer de très long reads sans avoir besoin de cloner les fragments pour amplifier le signal. C'est pour cette raison qu'on les appelle aussi "Single molecule sequencing". En revanche, ces nouvelles techniques produisent encore beaucoup d'erreur de séquençage. Les deux leaders de ce Next Next generation sequencing sont [Nanopore](https://nanoporetech.com/) et [PacBio Science](https://www.google.fr/search?q=Pacific+bioscience&oq=Pacific+bioscience&aqs=chrome..69i57j0l5.4887j0j4&sourceid=chrome&ie=UTF-8) qui termine une [guerre de brevet](http://www.frontlinegenomics.com/news/10714/pacbio-lawsuit-oxford-nanopore/).  

- [Vidéo Pacific Biosciences Technologies](https://www.youtube.com/watch?v=v8p4ph2MAvI)
- [Vidéo Oxford Nanopore Technologies](https://www.youtube.com/watch?v=3UHw22hBpAk)

<div class="figure">
    <a href="../images/post22/samtools.png"><img src="../images/post22/smidgion.jpg" /> </a>
    <div class="legend">vous ne revez pas... C'est le <a href="https://nanoporetech.com/products/smidgion">SmidgIon</a> d'Ofxord nanopore qui se branche sur un IPhone</div>
</div>   

## Références
* [ABMGOOD: Tout comprendre sur le NGS](https://www.abmgood.com/marketing/knowledge_base/next_generation_sequencing_introduction.php#similarities)
* [Coursera : cours NGS](https://fr.coursera.org/learn/bioinformatics-pku/lecture/Wu9kW/from-sequencing-to-ngs)
* [Bioinformatics Algorithms: GENIAL ](http://bioinformaticsalgorithms.com/)

