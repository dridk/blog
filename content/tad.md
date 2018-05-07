Title: Les TADs et l'organisation spatiale du génome
Slug: tad
Date: 2018-03-27 21:51:09
Modified: 2018-05-07 19:32:01
Tags: tads,ngs,hi-c
Category: biologie
Author: Sacha schutz
Summary: 
Status: Draft

Lors de la [mitose](https://fr.wikipedia.org/wiki/Mitose), l'ADN des cellules [eucaryotes](https://fr.wikipedia.org/wiki/Eukaryota) s'organise en [chromosomes](https://fr.wikipedia.org/wiki/Chromosome) condensés et bien délimités. C'est l'image que nous avons tous d'un chromosome. Mais le reste du temps, pendant l'[interphase](https://fr.wikipedia.org/wiki/Interphase), ces chromosomes ressemblent davantage à une boule de spaghetti emmêlée dans tous les sens: Ce qu'on appelle la [chromatine](https://fr.wikipedia.org/wiki/Chromatine).   
Aujourd'hui, les technologies de [Capture de Conformation des Chromosomes](https://en.wikipedia.org/wiki/Chromosome_conformation_capture) nous révèlent l'organisation spatiale de cette chromatine, qui en réalité semble être loin de l'anarchie mais plutôt organisé de façon fonctionnelle. C'est ce que nous allons découvrir tout de suite avec les [TADs](https://en.wikipedia.org/wiki/Topologically_associating_domain) (Topology Assocation Domain).

## Analyser l'organisation spatiale de la chromatine
Il existe toute une famille de technologies permettant d'évaluer l'organisation spatiale des chromosomes au moment de l'interphase. C'est la [Capture de Conformation des chromosomes (Chromosom Conformation Capture)](https://en.wikipedia.org/wiki/Chromosome_conformation_capture). Cette méthode se décline sous plusieurs formes que vous trouverez sous le nom de [(3C,4C,5C,HiC,ChiA-PET)](https://en.wikipedia.org/wiki/Chromosome_conformation_capture#Original_methods). Elles reposent toutes sur le même principe qui est d'identifier sur la chromatine, des régions en contact physique. 
Imaginez la chromatine, comme un long ruban d'ADN, formant plein de boucles en se repliant sur elle même. Par ces technologies, vous allez pouvoir savoir qu'une région **x** de ce ruban est en contact physique avec une autre région **y**.   


<div class="figure">
    <img src="../images/tad/principe.png" />
    <div class="legend">Figure 1. Haut. Vision linéaire du génome. Bas. Vision spatiale du génome et identification d'une zone de contacte (orange)</div>
</div>


### Comment ça fonctionne ? 
L'idée générale consiste à capturer les deux régions d'ADN en contact (**x** et **y**) et construire un fragment d'ADN hybride contenant le fragment **x** à une extrémité et le fragment **y** de l'autre (Figure 2). Ce fragment hybride est alors identifié par différents techniques de biologie moléculaire.            
Tout d'abord, les régions de contact sont figées en créant des liaisons covalentes grâce à du [formaldéhyde](https://en.wikipedia.org/wiki/Formaldehyde). C'est l'étape du *cross-linking*. L'ADN est ensuite digéré avec des [enzymes de restriction](https://fr.wikipedia.org/wiki/Enzyme_de_restriction) pour ne garder que les régions de contact. On réalise alors une [ligation](https://fr.wikipedia.org/wiki/Ligase) des extrémités du cross-link pour obtenir des fragments d'ADN hybrides. 
Ces fragments peuvent alors être identifiés par les différentes méthodes de biologie moléculaire. Par exemple, la méthode 3C est une simple [PCR](https://fr.wikipedia.org/wiki/R%C3%A9action_en_cha%C3%AEne_par_polym%C3%A9rase) tandis que la méthode [Hi-C](https://en.wikipedia.org/wiki/Chromosome_conformation_capture#Hi-C_(all-vs-all)) est un [séquençage haut débit](ngs.html) de l' ensemble de fragments hybrides obtenus à partir d'un génome. C'est cette dernière que je vais détailler.

<div class="figure">
    <img src="../images/tad/methode.png" />
    <div class="legend">Figure 2. Fixation des régions de contact avec du formaldéhyde (crosslinking) puis digestion de l'ADN avec une enzyme de restriction. Grâce à une ligase, les deux extrémité du cross-link sont reliés. Après un reverse crosslinking, le fragment hybride est obtenue. Celui-ci va pouvoir être séquencé en paired-end sur de  <a href="https://www.illumina.com/science/technology/next-generation-sequencing/paired-end-vs-single-read-sequencing.html">l'Illumina</a>. Le read R1 correspondra à la région x et le read R2 à la région y.</div>
</div>


### Méthode Hi-C
À partir de la méthode décrite ci-dessous, on va pouvoir créer une [libraire](ngs.html) de séquençage. C'est-à-dire générer un ensemble de fragments hybrides correspondant à l'ensemble des zones de contact de la chromatine. Cette librairie peut alors être lu sur un séquenceur [Illumina](https://fr.wikipedia.org/wiki/Illumina) qui a la particularité de faire du [séquençage en paire](https://www.france-genomique.org/spip/spip.php?article235) *(paired-end)*. C'est-à-dire pouvoir lire un fragment d'ADN dans les deux sens. Pour chaque fragment d'ADN lu, nous obtenons une paire de read **R1** et **R2** qui correspondent aux deux régions de contact **x** et **y** (Figure 2). On aligne alors ces reads sur [le génome de référence](naviguer-dans-votre-adn.html) afin de leurs attribuer des coordonnées génomique. Et connaissant les pairs de reads, nous pouvons enfin savoir si une région **x** et un contact avec une région **y**.   
Par exemple, si dans nos données, il existe un read **R1** s'alignant sur le gène *A* et un read **R2** s'alignant sur le gène *B*, nous pouvons "conclure" qu'il y a interaction entre le gène *A* et le gène *B*. 


### Visualiser les données Hi-C
Pour représenter l'ensemble des régions de contact provenant d'une expérience Hi-C, on utilise une carte de chaleur ([heatmap](https://en.wikipedia.org/wiki/Heat_map)). Cette carte est une matrice n x n montrant le nombre d'interaction entre deux positions donnée du même chromosome. La technologie ne permettant pas d'avoir une résolution à la base exacte, les positions sont des intervalles de taille fixe. 
La valeur de chaque cellule est le nombre de paires de reads entre deux positions données. Plus la couleur d'une cellule est rouge, et plus il y a d'interaction entre les deux positions correspondant à cette cellule.   
La figure 3 gauche, montre comment construire une *heatmap* pour un chromosome. La figure 3 droite,  montre une *heatmap* sur des données réelles Hi-C pour le chromosome 14. La diagonale rouge vif signifie que les régions très proches dans la séquence, sont en contact physique, ce qui semble logique. Notons par ailleurs que la matrice est symétrique. En effet, "**x**" interagit avec "**y**", est équivalent à "**y**" interagit avec "**x**". Pour cette raison, on préfère représenter les données Hi-C par une demi *heatmap*, ce qui donne un triangle (figure 4).


<div class="figure">
    <img src="../images/tad/tad_correlation_matrix.png" />
    <div class="legend">Figure 3. Gauche: Le chromosome est découpé en intervalle de taille fixe. Après alignement, chaque read est associé à un intervalle. On comptabilise alors le nombre de paires existants pour deux intervalles données. Sur la figure de gauche, il y a 2 paires entre les deux extrémités "p" et une paire entre l'extrémité "p" et "q". Droite: Donnée réelle Hi-C sur le chromosome 14. Notez la symétrie de la matrice autour de la diagonale ainsi qu'une allure en damier. </div>
</div>

##  Les TADs

En regardant la matrice de plus près (Figure 4), des triangles d'allure fractale ressortent clairement. Ces triangles correspondent à un ensemble de régions qui interagissent tous ensemble mais qui sont isolées du reste. Ces domaines, ce sont nos fameux [TAD (Topologically associating domain)](https://en.wikipedia.org/wiki/Topologically_associating_domain). Imaginez-les comme des boules de noeud sur notre ruban D'ADN. Chaque noeud contient des régions qui interagissent avec les autres régions de ce même noeud. Deux TADs sont magnifiquement illustrés par mes soins en bas de la figure 4.

<div class="figure">
    <img src="../images/tad/tad_ex.png" />
    <div class="legend">Figure 4. Visualisation d'une région du chromosome 3. Les TADs sont des domaines qui interagissent et sont observés ici par des triangles rouges. Sur cette figure, la région x,y et z sont à egal distance l'un de l'autre. Cependant x et y appartiennent au même TAD tandis que z appartient à un autre différent. </div>
</div>


### Fonction des TADs 
Aujourd'hui, la fonction des [TAD](https://en.wikipedia.org/wiki/Topologically_associating_domain) n'est pas totalement élucidée. Mais il est clair qu'ils jouent un rôle important dans la [régulation de l'expression des gènes](https://fr.wikipedia.org/wiki/R%C3%A9gulation_de_l%27expression_des_g%C3%A8nes). Nous savons depuis longtemps que les gènes sont régulés par des séquences [promotrices](https://fr.wikipedia.org/wiki/Promoteur_(biologie)) situées en amont des gènes. Mais il existe aussi des régions très éloignées du gène qui peuvent moduler la transcription. Ce sont les [amplificateurs (enhancers)](https://fr.wikipedia.org/wiki/Amplificateur_(biologie)) et les [inactivateurs (silencers)](https://fr.wikipedia.org/wiki/Inactivateur) qui respectivement activent ou répriment la [transcription](https://fr.wikipedia.org/wiki/Transcription_(biologie)). Par exemple, en repliant l'ADN dans l'espace, l'enhancer et le promoteur vont pouvoir interagir et moduler la transcription (Figure 5).   

<div class="figure">
    <img src="../images/tad/regulation.png" />
    <div class="legend">Figure 5. Schéma de la régulation de la transcription via les amplificateurs. En se répliant, l'ADN met en contact l'amplificateur et le promoteur d'un gène</div>
</div>

Il est alors évident que pour agir, un amplificateur doit se situer dans le même TAD que ses gènes cibles. Plusieurs gènes au sein du même TAD peuvent ainsi être corrégulés par le même amplificateur.   

<div class="figure">
    <img src="../images/tad/regulation_tad.png" />
    <div class="legend">Figure 6. Un amplificateur peut interagir avec les gènes de son TAD mais pas avec un autre. </div>
</div>

Une autre région importante dans la régulation est [l'isolateur (insulator)](https://fr.wikipedia.org/wiki/Isolateur_(biologie)) qui se situe entre deux TAD en empêchant leurs fusions. Une [étude](https://www.ncbi.nlm.nih.gov/pubmed/25701871) a par exemple montré qu'une délétion dans un isolateur est responsable de la fusion de deux TADs en un seul. Les deux noeuds bien distincts ne forment plus qu'un seul gros noeuds. Les enhancers du premier TAD sont alors capable d'interagir avec un gènes du deuxième TAD. Ce qui entraîne sa surexpression qui est délétère pour l'organisme. 

### Formation des TADs
La formation des TADs a été récemment mise en évidence en validant le modèle de [Loop extrusion](https://www.sciencedirect.com/science/article/pii/S2211124716305307). Ce mécanisme fait intervenir la [cohésine](https://fr.wikipedia.org/wiki/Coh%C3%A9sine) et les protéines [CTCF](https://fr.wikipedia.org/wiki/CTCF) qui reconnaissent des motifs autour des TADs, et font glisser la chromatine au travers d'anneau. Les deux vidéos suivantes vous montrent clairement la formation de ces structures.

<div class="figure">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/Tn5qgEqWgW8?start=23" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    <div class="legend"> Simulation du modèle Loop extrusion </div>
</div>


<div class="figure">
<iframe width="560" height="315" src="https://www.youtube.com/embed/47v3RLfLXho" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    <div class="legend"> Visualisation de Loop extrusion temps-réel  </div>
</div>


## Conclusion 
La découverte d'une organisation spatiale de la chromatine a changé notre vision du génome. Les chromosomes étaient le support rigide de l'information génétique. Ils sont maintenant les acteurs d'une régulation fine contrôlé par l'épigénétique. L'exploration dans ce domaine nous permettra de mieux comprendre le fonctionnement du génome dans son intégralité, et justifiera certainement le séquençage complet des patients atteints de maladies génétiques.

epigéniétuqe
sequencage genome complet 
genome dynamique
organisation spatial du genome




## Références
* [La thèse d'un collègue ](https://dumas.ccsd.cnrs.fr/dumas-01628629/document)
* [Analysis methods for studying the 3D architecture of the genome](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4556012/)
* [Topological domains in mammalian genomes identified by analysis of chromatin interactions](https://www.nature.com/articles/nature11082)
* [bioinformaticsinstitute](http://bioinformaticsinstitute.ru/sites/default/files/tad_calling_methods_part_1_-_sidorov_16-dec-2016.pdf)
* [bioinfo-fr](https://bioinfo-fr.net/hi-c-explication-des-bases)
* [Outil: TAD disease](http://3dgb.cbi.pku.edu.cn/disease/)
* [Outil: Hi-C Browser](http://promoter.bx.psu.edu/hi-c/)
