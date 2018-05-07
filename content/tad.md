Title: Les T.A.D et l'organisation spatiale du génome
Slug: tad
Date: 2018-03-27 21:51:09
Modified: 2018-03-27 21:51:09
Tags: 
Category: 
Author: Sacha schutz
Summary: 
Status: Draft

Pendant la [mitose](https://fr.wikipedia.org/wiki/Mitose), l'ADN des cellules [eucaryotes](https://fr.wikipedia.org/wiki/Eukaryota) est bien  organisé sous la forme de chromosomes. Alors que le reste du temps, pendant l'[interphase](https://fr.wikipedia.org/wiki/Interphase), ce qu'on appelle la [chromatine](https://fr.wikipedia.org/wiki/Chromatine) ressemble davantage à une boule de spaghetti désorganisée et emmêlée de façon aléatoire.    
Aujourd'hui, les technologies de [Chromatin Conformation Capture](https://en.wikipedia.org/wiki/Chromosome_conformation_capture) nous révèlent l'organisation spatiale de cette chromatine qui est en réalité loin d'être aléatoire, mais plutôt organiser de façon fonctionnelle. C'est ce que nous allons découvrir tout de suite avec les [T.A.D](https://en.wikipedia.org/wiki/Topologically_associating_domain) (Topology Assocation Domain).

## Capturer la conformation de la chromatine
Il existe toute une série de nouvelle technologie permettant d'évaluer l'organisation spatiale du génome pendant l'interphase. C'est la [Capture de Conformation de la Chromatine (Chromatin Conformation Capture)](https://en.wikipedia.org/wiki/Chromosome_conformation_capture) . Cette méthode se décline sous plusieurs formes que vous trouverez sous le nom de [(3C,4C,5C,HiC,ChiA-PET)](https://en.wikipedia.org/wiki/Chromosome_conformation_capture#Original_methods). Elle repose toutes sur le même principe qui est d'identifier sur la chromatine, des régions en contact physique.   
Imaginez la chromatine, comme un long ruban d'ADN, formant plein de boucles en se repliant sur elle même. Par ces technologies, vous allez pouvoir savoir qu'une région **x** de ce ruban est en contact physique avec une autre région **y**.   


<div class="figure">
    <img src="../images/tad/principe.png" />
    <div class="legend">Figure 1. Haut. Vision linéaire du génome. Bas. Vision spatiale du génome et identification d'une zone de contacte (orange)</div>
</div>


### Comment ça fonctionne ? 
L'idée générale consiste à capturer les deux régions d'ADN en contact (**x** et **y**) et construire un fragment d'ADN hybride contenant le fragment **x** à une extrémité et le fragment **y** de l'autre (Figure 2). Ce fragment hybride est alors identifié par différents techniques de biologie moléculaire.            
Tout d'abord, les régions de contact sont figées en créant des liaisons covalentes grâce à du [formaldéhyde](https://en.wikipedia.org/wiki/Formaldehyde). C'est l'étape du *cross-linking*. L'ADN est ensuite digéré avec des [enzymes de restriction](https://fr.wikipedia.org/wiki/Enzyme_de_restriction) pour ne garder que les régions de contact. On réalise alors une [ligation](https://fr.wikipedia.org/wiki/Ligase) des extrémités du cross-link pour obtenir des fragments d'ADN hybrides.  
Ces fragments sont identifiés par différentes méthodes de biologie moléculaire. C'est ce qui fait la spécifiée de la méthode. Par exemple, la méthode 3C est une simple [PCR](https://fr.wikipedia.org/wiki/R%C3%A9action_en_cha%C3%AEne_par_polym%C3%A9rase) tandis que la méthode [Hi-C](https://en.wikipedia.org/wiki/Chromosome_conformation_capture#Hi-C_(all-vs-all)) est un [séquençage haut débit (voir mon billet)](ngs.html) d'un ensemble de fragments obtenus à partir d'un génome. C'est cette dernière que je vais détailler.

<div class="figure">
    <img src="../images/tad/methode.png" />
    <div class="legend">Figure 2. D'abord fixation des régions de contact avec du formaldéhyde puis digestion de l'ADN. Grâce à une ligase, un fragment hybride est construit qui pourra être séquencer en <a href="ngs.html">NGS</a>. Lors d'un séquençage <a href="https://www.illumina.com/science/technology/next-generation-sequencing/paired-end-vs-single-read-sequencing.html">illumina paired-end</a>, le read R1 correspondra à la région x et le read R2 à la région y.</div>
</div>


### Methode Hi-C
À partir de la méthode décrite ci-dessous, on va pouvoir créer une [libraire](ngs.html) de séquençage. C'est-à-dire générer un ensemble de fragments hybrides correspondant à l'ensemble des zones de contact de la chromatine. Cette librairie peut alors être séquencée sur [Illumina](https://fr.wikipedia.org/wiki/Illumina) qui a comme particularité de faire du [séquençage en paire](https://www.france-genomique.org/spip/spip.php?article235) *(paired-end)*. C'est-à-dire pouvoir lire un fragment d'ADN des deux côtés. Et c'est là tout l'intérêt. Pour chaque fragment d'ADN lu, nous obtenons une paire de read **R1** et **R2** correspondant aux deux régions de contact **x** et **y** (Figure 2). chaque read est aligné indépendamment sur un génome de référence afin de leurs attribué des [coordonnées génomiques](naviguer-dans-votre-adn.html). Et connaissant les pairs, nous pouvons enfin savoir si une région **x** et un contact avec une région **y**.
Par exemple, si dans nos données, il existe un read **R1** s'alignant sur le gène *A* et un read **R2** s'alignant sur le gène *B*, nous pouvons "conclure" qu'il y a interaction entre le gène *A* et le gène *B*. 


### Visualiser les données Hi-C
Pour représenter l'ensemble des régions de contact provenant d'une expérience Hi-C, on utilise une carte de chaleur ([heatmap](https://en.wikipedia.org/wiki/Heat_map)). Cette matrice a comme dimensions des régions chromosomiques de taille fixe et comme valeur le nombre de paires de reads observées entre deux régions. Plus la couleur d'une cellule est rouge, et plus il y a d'interaction entre les deux régions correspondant à cette cellule.   
La figure 3 gauche, montre comment construire une *heatmap* pour un chromosome. La figure 3 droite,  montre une *heatmap* sur des données réelles Hi-C pour le chromosome 14. La diagonale rouge vif signifie que les régions très proches dans la séquence, sont en contact physique, ce qui semble logique. Notons par ailleurs que la matrice est symétrique. En effet, "**x**" interagit avec "**y**", c'est la même chose qu’"**y**" interagit avec "**x**". Pour cette raison, on préfère représenter la moitié de la matrice sous forme d'un triangle (figure 4).


<div class="figure">
    <img src="../images/tad/tad_correlation_matrix.png" />
    <div class="legend">Figure 3. Gauche: Le chromosome est découpé en région de taille fixe. Après alignement, chaque read est associé à une région. On comptabilise alors le nombre de paires existants pour deux régions données. Droite: Donnée réelle Hi-C sur le chromosome 14. Notez la symétrie de la matrice autour de la diagonale ainsi qu'une allure en damier. </div>
</div>

##  Mise en évidence des TADs

En regardant la matrice de plus près (Figure 4), des triangles d'allure fractale ressortent clairement. Ces triangles correspondent à un ensemble de régions qui interagissent tous ensemble mais qui sont isolées du reste. Ces domaines, ce sont nos fameux [TAD (Topologically associating domain)](https://en.wikipedia.org/wiki/Topologically_associating_domain). Imaginez-les comme des boules de noeud sur notre ruban D'ADN. Chaque noeud contient des régions qui interagissent avec les autres régions de ce même noeud.

<div class="figure">
    <img src="../images/tad/tad_ex.png" />
    <div class="legend">Figure 4. La région x,y et z sont à egal distance l'un de l'autre. Cependant x et y appartiennent au même TAD tandis que z appartient à un autre différent. </div>
</div>


### La fonction des TADs 
Aujourd'hui, la fonction des [TAD](https://en.wikipedia.org/wiki/Topologically_associating_domain) n'est pas totalement élucidée. Mais il est clair qu'ils jouent un rôle important dans la [régulation de l'expression des gènes](https://fr.wikipedia.org/wiki/R%C3%A9gulation_de_l%27expression_des_g%C3%A8nes). Nous savons depuis longtemps que les gènes sont régulés par des séquences [promotrices](https://fr.wikipedia.org/wiki/Promoteur_(biologie)) situées amont des gènes. Mais il existe aussi des régions très éloignées du gène qui peuvent moduler la transcription. Ce sont les [amplificateurs (enhancers)](https://fr.wikipedia.org/wiki/Amplificateur_(biologie)) et les [inactivateurs (silencers)](https://fr.wikipedia.org/wiki/Inactivateur) qui respectivement activent ou répriment la [transcription](https://fr.wikipedia.org/wiki/Transcription_(biologie)). Par exemple, en repliant l'ADN dans l'espace, l'enhancer et le promoteur vont pouvoir interagir et moduler la transcription.   

<div class="figure">
    <img src="../images/tad/regulation.png" />
    <div class="legend">Figure 5. Schéma de la régulation de la transcription via les amplificateurs. En se répliant, l'ADN met en contact l'amplificateur et le promoteur d'un gène</div>
</div>

Il est alors évident que pour agir, un amplificateur doit se situer dans le même TAD que ses gènes cibles. Plusieurs gènes au sein du même T.A.D peuvent ainsi être corrégulés par le même amplificateur.   

<div class="figure">
    <img src="../images/tad/regulation_tad.png" />
    <div class="legend">Figure 6. Un amplificateur peut interagir avec les gènes de son TAD mais pas avec un autre. </div>
</div>

Une autre région importante dans la régulation est l'[isolateur (insulator)](https://fr.wikipedia.org/wiki/Isolateur_(biologie)) qui se situe entre deux TAD en empéchant leurs fusions. Une étude a par exemple montré qu'une délétion dans un insulator est responsable de la fusion de deux TAD en un seul. Les enhancers du premier TAD sont ainsi capable d'interagir avec un gènes du deuxième TAD. Ce qui entraine sa surexpression et une maladie chez le porteur.

### La formation des TADs
La formation des TADs a été récemment mise en évidence en validant le modèle de [Loop extrusion](https://www.sciencedirect.com/science/article/pii/S2211124716305307). Ce mécanisme fait intervenir la [cohésine](https://fr.wikipedia.org/wiki/Coh%C3%A9sine) et les protéines [CTCF](https://fr.wikipedia.org/wiki/CTCF) qui reconnaissent des motifs autour des TADs, et font glisser la chromatine au travers d'anneau. Les deux vidéos suivantes vous montrent clairement la formation de ces structures.

<div class="figure">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/Tn5qgEqWgW8?start=23" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    <div class="legend">Dans la figure ci-dessous la région x,y et z sont à egal distance l'un de l'autre. Cependant x et y appartiennent au même TAD tandis que z appartient à un autre. </div>
</div>


<div class="figure">
<iframe width="560" height="315" src="https://www.youtube.com/embed/47v3RLfLXho" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    <div class="legend">Dans la figure ci-dessous la région x,y et z sont à egal distance l'un de l'autre. Cependant x et y appartiennent au même TAD tandis que z appartient à un autre. </div>
</div>


https://bioinfo-fr.net/hi-c-explication-des-bases
http://atlasgeneticsoncology.org/Educ/ArchitectChromatinID30016FS.html
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3874846/figure/F1/
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3874846/