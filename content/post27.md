Title: Quantifier les ARNm d'une cellules
Slug: sc-rna-seq
Date: 2017-08-28 16:23:49
Tags: puce,sonde,adn,exome,mas,dmd
Category: biologie
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

Toutes les cellules de votre corps sont constitués du même génome. Vous obtiendrez toujours le même texte en séquençant l'ADN provenant d'un morceau d'estomac, de cerveau ou de peau.  
Ce qui fait la difference, c'est l'expression des gènes ou "*transcriptome*". C'est à dire l'ensemble des ARNs messager transcript dans la cellule dont la traduction est responsable du phénotype cellulaire. Par exemple les cellules de votre rétine expriment différents gènes que celle de votre estomac. Leurs transcriptomes sont différents.  
Une des méthodes pour évaluer le transcriptome est le séquençage des ARNm ou RNAseq. A partir d'un tissue, toutes les cellules sont lysée puis les ARNs messagers sont capturé (en général par leurs queues polyadénylé), convertit  en ADNc par une rétrotranscriptase, amplifié, puis séquencer. L'étape de bioinformatique consiste à aligner les reads sur les exons d'un génome de référence pour évaluer quels gènes sont exprimé. Le nombre d'ARNm pour un gène correspond au niveau d'expression de ce gène ou *abondance*.    
Au final, en analysant différents tissues, on se retrouve avec une *matrice d'expression* ( voir figure ci-dessous).   
C'est un peu plus compliqué que ça. Et je vous invite à jeter un oeil sur l'article de bioinfo-fr à ce sujet.    

<div class="figure">
    <img src="../images/post27/rnaseq-overview.png" /> 
    <div class="legend">Schéma général de la technologie RNAseq. Le séquençage est réalisé sur deux échantillons (tumeur et normal). Les ARNs sont capturé grâce leurs queues polyA, sont converti en ADNc puis séquencer. Les reads sont alignés sur un génome de référence afin de mesurer l'expression de chaque gène. Cette expression est proportionnelle aux nombre d'ARN s'allignant sur un gène donné </br>Source: Wikipedia</div>
</div>

</br>
   
<div class="figure">
    <img src="../images/post27/expression-matrix.png" /> 
    <div class="legend">Exemple d'une matrice d'expression comparant deux tissues. L'expression des gènes dans le tissue normal est différent de celui du tissue cancereux</div>
</div>


## Résolution cellulaire

Le defaut de cette technique est qu'elle mesure l'expression d'un tissue et pas l'expression d'une cellule. En effet, dans un morceau de cerveau, il y aura différent type cellulaire (neurone, astrocytes, oligodentrocytes ...) avec des profils d'expression differente. La technique RNA-seq traditionnelle vous donnera seulement le niveau d'expression de cette ensemble.   
Aujourd'hui, une autre méthode permet de séquencer le transcriptome d'une seul cellule. C'est ce qu'on appelle du Single Cell RNA Seq (ScRNASeq). 
L'idée est de créer une librarie (Ensemble des fragments d'ADN déstiné au séquençage) ou chaque ARNm se voit greffer une séquence identifiant sa cellule d'origine (barcode). On peut alors après le séquençage, regrouper les reads entre eux grâce à leurs barcode et obtenir la matrice d'expression par cellules.   
Comment étiqueter chaque fragment d'ADN à sa cellule d'origine ? C'est ce qu'on va voir avec la méthode de microfluidique de 10xGenomics.

## Exemple avec 10xGenomics
La première étape consiste à isoler chaque cellule dans un goutelette d'huile contenant des réactifs de PCR ( polymérase, oligonucléotide...) et une bille ou GEM (Gel bead in EMulsion).

<div class="figure">
    <img src="../images/post27/GEM.png" /> 
    <div class="legend">Photo d'une GEM (Gel bead in EMulsion) </br> Source: <a href="https://www.10xgenomics.com/single-cell/">10xGenomics</a>
    </div>
</div>

Pour former cette goutelette, ils ont recourt à la microfluidique qui consiste à faire passer successivement dans des microcapillaires les cellules, les billes et l'huile. 

<div class="figure">
    <img src="../images/post27/gem-formation.gif" /> 
    <div class="legend">Photo d'une goutelette d'huile contenant la GEM et la cellule.</br> Source: <a href="https://www.10xgenomics.com/single-cell/">10xGenomics</a> </div>
</div>

<div class="figure">
    <img src="../images/post27/gem-formation2.gif" /> 
    <div class="legend">Photo d'une GEM. </br> Source: https://www.youtube.com/watch?v=zQoHc6PtIFk </div>
</div>


Chaque bille est recouverte de séquences adaptatrice unique contenant un barcode, un UMI et la séquence complémentaire à la queue PolyA (PolyT) des ARN messagers.    
- Le barcode est l'identifiant unique à la bille. 10xGenomics propose dans ses kits des billes avec 750 000 barcodes environ.       
- L'UMI (Unique Molecular Identifiers) est une courte séquence aléatoire unique  à chaque fragment entourant la bille. Il y a donc plusieurs UMI par bille. Cette identifiant est utilisé pour éviter les biais d'amplifications. Si une séquence est malencontreusement trop amplifier, Elle sera detecté car un même UMI sera trop representé.
- Une séquence de plusieurs nucléotide T ou va venir se fixer les ARNs par l'intermediaire de leurs queue polyA.

<div class="figure">
    <img src="../images/post27/gem-zoom.png" /> 
    <div class="legend">Photo d'une GEM </br> Source: <a href="https://www.10xgenomics.com/single-cell/">10xGenomics</a> </div>
</div>


## Résulats 
Au final, on obtient la matrice d'expression par gènes et par cellules.

<div class="figure">
    <img src="../images/post27/expression-matrix-cell.png" /> 
    <div class="legend">Photo d'une GEM </div>
</div>

On peut alors representer ce tableau dans un graphique en réalisant une analyse en composante principale. (10x genomics utilise une t-SNE). 
Chaque point correspond à une cellule. Plus les cellules sont proche sur le graphique, plus leurs expressions génétiques est similaires. 


<div class="figure">
    <img src="../images/post27/blood_example.png" /> 
    <div class="legend">Photo d'une GEM </div>
</div>

Plus jolie, cette vidéo montre le profil d'expression des cellule du cerveau dans une répresentation 3D. https://www.10xgenomics.com/single-cell/?wvideo=z54e2lemhd


## What next ? 
A l'heure ou j'écrivais cette article, Je suis tombé sur un article décrivant la technique DropNcSeq. Une méthode similaire à ce que je viens de décrire, mais concernant les noyaux des cellules et pas la cellule entière.    
C'est beau la technology :D 


https://www.youtube.com/watch?v=zQoHc6PtIFk

## Références
* [RNASeq sur bioinfo-fr](https://bioinfo-fr.net/lanalyse-de-donnees-rna-seq-mode-demploi)
* [10xGenomics](https://www.10xgenomics.com/single-cell/)

