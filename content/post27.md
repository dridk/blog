Title: Quantifier les ARNm d'une cellule
Slug: sc-rna-seq
Date: 2017-08-28 16:23:49
Tags: puce,sonde,adn,exome,mas,dmd
Category: biologie
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

Toutes les cellules de votre corps sont constituées du même génome. Vous obtiendrez toujours le même texte en séquençant l'ADN provenant d'un morceau d'estomac, de cerveau ou de peau.  
Ce qui fait la différence, c'est l'expression des gènes ou « *[transcriptome](https://fr.wikipedia.org/wiki/Transcriptome)* » . C'est à dire l'ensemble des [ARNs messagers (ARNm)](https://fr.wikipedia.org/wiki/Acide_ribonucl%C3%A9ique_messager) transcrits dans la cellule dont la traduction est responsable du [phénotype cellulaire](https://fr.wikipedia.org/wiki/Ph%C3%A9notype_cellulaire). Par exemple, les cellules de votre rétine expriment différents gènes de votre estomac. Leurs transcriptomes sont différents.  
Une des méthodes pour évaluer le transcriptome est le séquençage des ARNm ou [RNA-seq](https://fr.wikipedia.org/wiki/RNA-Seq). À partir d'un tissu, toutes les cellules sont lysées puis les ARNs messagers sont capturés (en général par leurs [queues polyadénylées](https://fr.wikipedia.org/wiki/Polyad%C3%A9nylation)). Ils sont ensuite convertis  en [ADN complémentaire](https://fr.wikipedia.org/wiki/ADN_compl%C3%A9mentaire) (ADNc) par une [rétrotranscriptase](https://fr.wikipedia.org/wiki/Transcriptase_inverse), amplifiés, puis séquencés. L'étape bio-informatique consiste à aligner les [reads](http://dridk.me/ngs.html) sur les [exons](https://fr.wikipedia.org/wiki/Exon) d'un génome de référence pour évaluer quels gènes sont exprimés. Le nombre d'ARNm séquencé d'un gène correspond à son niveau d'expression ou « *abondance »*.    
Finalement, en analysant différents tissus, on obtient  une *matrice d'expression* ( voir tableau ci-dessous).   
Pour plus de détails sur l'analyse bio-informatique,  je vous invite à jeter un oeil sur l'[article de bioinfo-fr](https://bioinfo-fr.net/lanalyse-de-donnees-rna-seq-mode-demploi) traitant de ce sujet.    

<div class="figure">
    <img src="../images/post27/rnaseq-overview.png" /> 
    <div class="legend">Schéma général de la technologie RNAseq. Dans cet exemple, le séquençage est réalisé sur deux échantillons (tumeur et normal). Les ARNs sont capturés grâce leurs queues polyA, sont converti en ADNc puis séquencer. Les reads sont alignés sur un génome de référence afin de mesurer l'expression de chaque gène. Cette expression est proportionnelle aux nombres d'ARN s'alignant sur un gène donné </br>Source: Wikipedia</div>
</div>

</br>
   
<div class="figure">
    <img src="../images/post27/expression-matrix.png" /> 
    <div class="legend">Exemple d'une matrice d'expression comparant deux tissues. L'expression des gènes dans le tissue normal est différent de celui du tissue cancéreux</div>
</div>


## ScRNA-seq: Nouvelle approche plus résolutive

Le défaut du RNA-seq est qu'elle mesure l'expression d'un tissu et pas l'expression d'une cellule. En effet, dans un morceau de cerveau, il y aura différent type cellulaire (neurone, [astrocytes](https://fr.wikipedia.org/wiki/Astrocyte), [oligodendrocytes](https://fr.wikipedia.org/wiki/Oligodendrocyte) ...) avec des profils d'expression différente. La technique RNA-seq traditionnelle vous informera seulement du niveau d'expression de cet ensemble.   
Aujourd'hui, une autre méthode permet de séquencer le transcriptome d'une seule cellule. C'est ce qu'on appelle du [Single Cell RNA Seq  (ScRNA-Seq)](https://en.wikipedia.org/wiki/Single-cell_transcriptomics). 
L'idée est de créer une librarie (Ensemble des fragments d'ADN destiné au séquençage) ou chaque ARNm se voit greffer une séquence identifiant sa cellule d'origine ([barcode](https://fr.wikipedia.org/wiki/Barcoding_mol%C3%A9culaire)). On peut alors après séquençage, regrouper les reads entre eux grâce à leurs barcodes et obtenir une matrice d'expression par cellules et par gènes.   
Comment étiqueter chaque fragment d'ADN à sa cellule d'origine ? C'est ce qu'on va voir tout de suite avec la méthode de [microfluidique](https://fr.wikipedia.org/wiki/Microfluidique) de [10xGenomics](https://www.10xgenomics.com/).

## Isoler les cellules en microfluidique
La microfluidique est une technologie manipulant des fluides dans des mini-tuyaux de l'ordre du micromètre. 
Grâce à ça, on peut isoler chaque cellule dans une gouttelette d'huile contenant des réactifs ( polymérase, oligonucléotide, Retrotranscriptase...) ainsi qu'une bille particulière appellée GEM (Gel bead in EMulsion).

<div class="figure">
    <img src="../images/post27/GEM.png" /> 
    <div class="legend">microgoutelette avec une cellule et une GEM (Gel bead in EMulsion) </br> Source: <a href="https://www.10xgenomics.com/single-cell/">10xGenomics</a>
    </div>
</div>

Pour former cette gouttelette, ils font passer successivement les cellules, les billes et l'huile dans un circuit de microcapillaires: ( Voir ci-dessous).

<div class="figure">
    <img src="../images/post27/gem-formation.gif" /> 
    <div class="legend">Annimation montrant la formation des microgoutelettes</br> Source: <a href="https://www.10xgenomics.com/single-cell/">10xGenomics</a> </div>
</div>

<div class="figure">
    <img src="../images/post27/gem-formation2.gif" /> 
    <div class="legend">Formation des microgoutellettes en vidéo </br> Source: <a href="https://www.youtube.com/watch?v=zQoHc6PtIFk">Dolomite Microfluidics</a> </div>
</div>

## Chaque cellule a son barcode unique
Chaque bille est recouverte de séquences adaptatrice uniques contenant un barcode, un UMI et la séquence complémentaire à la queue PolyA (PolyT) des ARN messagers.    
- Le barcode est l'identifiant unique à la bille, et donc unique à la cellule. 10xGenomics propose dans ses kits des billes avec 750 000 barcodes environ.       
- [L'UMI (Unique Molecular Identifiers)](https://en.wikipedia.org/wiki/Unique_molecular_identifier)  est une courte séquence aléatoire unique  à chaque fragment entourant la bille. Il y a donc plusieurs UMI par bille. Cet identifiant est utilisé pour éviter les biais d'amplifications. Si une séquence est malencontreusement trop amplifiée dans une goutte, elle sera détectée, car le même UMI sera représenté plusieurs fois.    
- La séquence polyT est l'extremité ou va venir se fixer les ARNs par complémentarité par leurs queues polyA.

<div class="figure">
    <img src="../images/post27/gem-zoom.png" /> 
    <div class="legend">Zoom sur une GEM et les séquences la recouvrant</br> Source: <a href="https://www.10xgenomics.com/single-cell/">10xGenomics</a> </div>
</div>

## Création d'une librarie et séquençage 
Pour finir, il ne reste plus qu'à créer la librarie pour le séquençage. Tous les fragments d'ADNs identifié par leurs barcodes sont pooler ensemble après lyses des goutelettes d'huiles. Les adaptateurs de séquençages ([Illumina](https://www.youtube.com/watch?v=fCd6B5HRaZ8&t=3s)) sont ajouté afin d'obtenir la libraire.   
Après le séquençage et l'allignement, il suffira de regrouper les reads provenant d'une même cellule en comparant leurs barcodes.

## Des jolies graphiques comme résultat
On obtient alors la matrice d'expression par gènes et par cellules:

<div class="figure">
    <img src="../images/post27/expression-matrix-cell.png" /> 
    <div class="legend">Exemple d'une matrice d'expression en Single Cell RNA Seq. En réalité, il y a des milliers de cellules (autant que de barcode) et au moins 23 000 gènes (pour l'homme).</div>
</div>

On peut alors représenter ce tableau dans un graphique en réalisant une [analyse en composante principale](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales). (10x genomics utilise une [t-SNE](https://fr.wikipedia.org/wiki/Algorithme_t-SNE)). 
Chaque point correspond à une cellule. Plus les cellules sont proches sur le graphique, plus leurs expressions génétiques sont similaires. 


<div class="figure">
    <img src="../images/post27/blood_example.png" /> 
    <div class="legend">Profil d'expression obtenu à partir des cellules du sang (2,700 cellules mononuclées du sang périphérique <a href="https://fr.wikipedia.org/wiki/Cellule_mononucl%C3%A9%C3%A9e_sanguine_p%C3%A9riph%C3%A9rique)))">PBMC</a></br> Source: <a href="http://satijalab.org/seurat/get_started_v1_4.html">http://satijalab.org/seurat/get_started_v1_4.html</a></div>
</div>

Plus jolie, cette vidéo montre le profil d'expression des cellules du cerveau dans une repère à 3 axes.

<p align="center">
<a href="https://www.10xgenomics.com/single-cell/?wvideo=z54e2lemhd"><img src="../images/post27/brain10x.png"/></a>
</p>

## What next ? 
À l'heure ou j'écrivais cet article, je suis tombé sur un article décrivant la technique [DropNc-Seq](http://www.genengnews.com/gen-news-highlights/single-nucleus-rna-seq-merges-with-microfluidics/81254868). Une méthode similiaire à ce que je viens de décrire, mais ce sont les noyaux qu'on isole et pas les cellules. On obtient donc le transcriptome nucléaire.     
Bref, c'est chouette hein ? 


## Références
* [RNASeq sur bioinfo-fr](https://bioinfo-fr.net/lanalyse-de-donnees-rna-seq-mode-demploi)
* [10xGenomics](https://www.10xgenomics.com/single-cell/)
* [Dolomite Microfluids](https://www.youtube.com/watch?v=zQoHc6PtIFk)
* [Massively parallel digital transcriptional profiling of single cells](https://www.ncbi.nlm.nih.gov/pubmed/28091601)
