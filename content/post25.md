Title: Fabrication des sondes de captures par technologie MAS
Slug: puce-adn-mas
Date: 2017-07-23 11:26:45
Tags: puce,sonde,adn,
Category: biologie
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

Pour séquencer un [exome](https://fr.wikipedia.org/wiki/Exome), il faut d'abord capturer toutes les séquences exoniques. Une méthode est d'utiliser des sondes [oligonucléotidiques](https://fr.wikipedia.org/wiki/Oligonucl%C3%A9otide) qui s'hybrident spécifiquement sur les [exons](https://fr.wikipedia.org/wiki/Exon). Ce qui demande une connaissance préalable des séquences codantes, mais aussi une technologie capable de fabriquer des millions de sondes avec leurs séquences déterminées.  
Comment ces sondes sont produites ? 

# Technologie Maskless Array Synthesis (MAS)
[Roche/NimbleGen](http://sequencing.roche.com/products/nimblegen-seqcap-target-enrichment.html) utilise une technique de synthèse des sondes sur lame *in situ*. C'est-à-dire que les sondes sont directement synthétisées sur la lame et non déposées par un robot comme les techniques classiques ([Microarray spotting](https://fr.wikipedia.org/wiki/Puce_%C3%A0_ADN#Par_d.C3.A9p.C3.B4t_.28spotted.29)).  
Pour cela ils utilisent la [photolithographie](https://fr.wikipedia.org/wiki/Photolithographie) associée à une [matrice de micro-miroirs](https://fr.wikipedia.org/wiki/Matrice_de_micro-miroirs). Cette technologie consiste à utiliser des rayons lumineux dirigés par des miroirs pour guider la synthèse des sondes. 
Chaque nucléotide est protégé par une [groupement photolabile](https://en.wikipedia.org/wiki/Photolabile_protecting_group) qui empêche l'association avec un autre nucléotide. En présence de lumière, cette molécule est supprimé, un nouveau nucléotide peut alors se lier.  
Pour faire simple :

- Prener une lame et déposez-y des nucléotides protégés. 
- Éclairer certains nucléotides pour les déprotéger. 
- Inonder votre lame avec plein de nucléotides 'G' qui se fixe uniquement sur les nucléotides libérés. 

Recommencer la procédure, mais cette fois en inondant avec que du C, et ainsi de suite.  
La vidéo ci-dessous résume bien ce cycle de synthèse. 

<div class="figure">
    <img src="../images/post25/MAS1.png" /> 
    <div class="legend">Illustration de la technologie MAS</div>
</div>

<div class="figure">
<video controls src="../images/post25/media2.webm"> Synthèse des oligonucléotides</video>
</div>

## Digital Micromirror Device (DMD)
Maintenant, comment eclairer les milliers de sondes spécifiquement ?
Ils utilisent pour cela, des matrices de micro-miroirs de 16µm chacun. Il s'agit d'une grille composée de millions de petits miroirs qui peuvent s'incliner independement dans deux conformations ON ou OFF. En eclairant tout la grille, les rayons lumineux sont réfléchis vers la lame suivant l'orientation des miroirs. Anis, en programmant les états ON/OFF des micros-miroirs pendant le cycle de synthèse, on peut synthétiser des millions de sondes en spécifiant leurs séquences.  
Jetez un oeil sur cette dernière vidéo résumant mes propos.

<div class="figure">
<video controls src="../images/post25/media1.webm"> Matrices de micro-miroirs</video>
</div>

## Références
* [Les methodes de fabrication des puces à ADN](http://bitesizebio.com/7463/how-dna-microarrays-are-built/)
* [Roche nimblegen](http://sequencing.roche.com/products/nimblegen-seqcap-target-enrichment.html)
* [Wikipedia: Fabrication des puces](https://fr.wikipedia.org/wiki/Puce_%C3%A0_ADN#Fabrication)
