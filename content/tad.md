Title: Les T.A.D et l'organisation spatiale du génome
Slug: tad
Date: 2018-03-27 21:51:09
Modified: 2018-03-27 21:51:09
Tags: 
Category: 
Author: Sacha schutz
Summary: 
Status: Draft

Pendant la mitose, l'ADN des cellules eucaryotes est bien  organisé sous forme de chromosome. Alors que le reste du temps, pendant l'interphase, ce qu'on appelle la chromatine ressemble d'avantage à une boule de spagetti désorganisée et emmelée de façon aléatoire.    
Aujourd'hui, les technologies de "Chromatin Conformation Capture" nous révèle l'organisation spatiale de cette chromatine qui est en réalité loin d'etre aléatoire, mais plutot organiser de façon fonctionnelle. C'est ce que nous allons découvrir tout de suite avec les T.A.D (Topology Assocation Domain). 

#Chromatin Conformation Capture 
Il existe tout une serie de nouvelle technologie permettant d'évaluer l'organisation spatiale du génome pendant l'interphase. C'est la Capture de Conformation de la Chromatine (Chromatin Conformation Capture). Cette méthode se décline sous plusieurs formes que vous trouverez sous le nom de (3C,4C,5C,HiC,ChiA-PET). Elle repose toutes sur le même principe qui est d'identifier sur la chromatine, des régions en contact physique.   
Imaginez la chromatine, comme un long ruban d'ADN, formant plein de boucle en se repliant sur elle même. Grâce à ces technologies, vous allez pouvoir savoir qu'une région **x** de ce ruban est en contact physique avec une autre région **y**.  


<div class="figure">
    <img src="../images/tad/principe.png" />
    <div class="legend">A) Vision linéaire du génome. B) Vision spatiale du génome et identification d'une zone de contacte (orange)</div>
</div>


## Comment ça fonctionne ?
L'idée général consiste à capturer les deux régions d'ADN en contact (x et y) et construire un fragment d'ADN hybride contenant le fragment x à une extremité et le fragment y de l'autre. Ce fragment hybride est alors identifié par différents techniques de biologie moléculaire.            
Tout d'abord, les régions de contact sont figé en créant des liaisons covalence grâce à du formaldehyde. C'est l'étape du cross-linking. l'ADN est ensuite digéré avec des enzymes de restriction pour ne garder que les régions de contact. On réalise alors une ligation des extrémités du cross-link pour obtenir des fragments d'ADN hybrides.  
Ces fragments sont identifié par différents méthodes de biologie moléculaire. C'est ce qui fait la spécifité de la méthode. Par exemple, la méthode 3C est une simple PCR tandis que la methode Hi-C est un séquençage haut débit d'un ensemble de fragment obtenu à partir d'un génome. C'est cette dernière qui va nous interesser particulièrement.

<div class="figure">
    <img src="../images/tad/methode.png" />
    <div class="legend">A) Vision linéaire du génome. B) Vision spatiale du génome et identification d'une zone de contacte (orange)</div>
</div>


## Methode Hi-C
A partir de la méthode décrit ci-dessous, on va pouvoir créer une libraire de sequençage. C'est à dire générer un ensemble de fragments hybrides correspondant à l'ensemble des zones de contact de la chromatine. Cette librairie peut alors être séquencé sur Illumina qui a comme particularité de faire du pair-end. C'est à dire pouvoir lire un fragment d'ADN des deux cotés. Et là est tout l'interet. Car pour chaque fragment, nous obtenons une pair de read R1 et R2 correspondant aux deux régions de contact x et y.
Chaque read est aligné indépendement sur un génome de référence afin de leurs attribué des coordonnée génomique. Et connaissant les pairs, nous pouvons enfin savoir si une région x et un contact avec une region y.
Par exemple, si dans nos donnée, il existe un read R1 s'alignant sur le gène A et un read R2 s'alignant sur le gène B, nous pouvons "conclure" qu'il y a intéraction entre le gène A et le gène B. 

## Matrice de correlation 
Pour representer l'ensemble des regions de contact provenant d'une experience Hi-C, on utilise une matrice de correlation. Celle-ci a comme dimensions les régions chromosomique et comme valeur le nombre de pairs entre deux régions.
La figure A, montre comment construire une matrice de correlation entre deux chromosome. La figure B montre une vrai matrice de corrélation sur donnée Hi-C entre le chromosome 14 et lui même. Plus la couleur est rouge, plus il existe de contact physique. La diagonal rouge vif montre que les régions très proches en terme de coordonnées génomiques sont en contact physique, ce qui parait logique. Notons par ailleur, que la matrice est symétrique. En effet, "x" interagit avec "y", c'est la même chose que "y" interagit avec "x". Pour cette raison, on préfère representer la moitié de la matrice sous forme d'un triangle. (figure)

<div class="figure">
    <img src="../images/tad/tad_correlation_matrix.png" />
    <div class="legend">Matrice de correlation</div>
</div>

# Mise en évidence des Tads 

En regardant la matrice de plus près, on peut observer des triangles rouge vifs, d'allure fractal. Ces triangles correspondent à un ensemble de région qui interagissent ensemble et qui sont isolé du reste. Ces domaines, ce sont nos fameux T.A.D (Topologically associating domain). Imaginez les comme des boules de noeud sur notre ruban D'ADN. Chaque noeud contient des régions qui interagissent avec les autres régions de ce même noeuds.     


<div class="figure">
    <img src="../images/tad/tad_ex.png" />
    <div class="legend">Dans la figure ci-dessous la région x,y et z sont à egal distance l'un de l'autre. Cependant x et y appartiennent au même TAD tandis que z appartient à un autre. </div>
</div>


# La fonction des Tads 
Aujourd'hui, la fonction des TAD n'est pas totallement élucidé. Mais il est clair qu'ils jouent un rôle important dans la régulation de l'expression des gènes. Nous savons depuis longtemps que les gènes sont régulé par des sequences promotrice situé amont des gènes. Mais il existe aussi des régions très éloignés du gène qui peuvent moduler la transcription. Ce sont les enhancers et les silencers qui respectivement activent ou répriment la transcription. Par exemple, en repliant l'ADN dans l'espace, l'enhancer et le promoteur vont pouvoir interagir et moduler la transcription.

<div class="figure">
    <img src="../images/tad/regulation.png" />
    <div class="legend">Dans la figure ci-dessous la région x,y et z sont à egal distance l'un de l'autre. Cependant x et y appartiennent au même TAD tandis que z appartient à un autre. </div>
</div>

Il est alors évident qu'un enhancer pour agir, doit se situer dans le même T.A.D que son gène cible. Plusieurs gènes au sein du même T.A.D peuvent ainsi  être corrégulé par le même enhancer.   

<div class="figure">
    <img src="../images/tad/regulation_tad.png" />
    <div class="legend">Dans la figure ci-dessous la région x,y et z sont à egal distance l'un de l'autre. Cependant x et y appartiennent au même TAD tandis que z appartient à un autre. </div>
</div>

Une autre région importante dans la regulation est l'"insulator" qui se situe entre deux T.A.D et empechent leurs fusions. Une étude a par example montré qu'une deletion dans un insulator est responsable de la fusion de deux T.A.D en un seul. Les enhancers du premier T.A.D vont alors intéragir avec un gène du deuxième TAD, ce qui entrainera sa surexpression et une maladie chez le porteur.

# La formation des TADs
La formation des T.A.D a été récemment mise en évidence en validant le modèle de "Loop extrusion". Ce mécanisme fait intervenir la cohésine et les protéines CTCF qui reconnaissent des motifs autour des T.A.Ds, et font glisser la chromatine au travers d'anneau. Les deux vidéos suivantes vous montre clairement la formation de ces structures.

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