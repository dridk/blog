Title: Single Cell RNA Seq
Slug: sc-rna-seq
Date: 2017-08-28 16:23:49
Tags: puce,sonde,adn,exome,mas,dmd
Category: biologie
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

Toutes les cellules de votre corps sont constitués du même génome. Vous obtiendrez toujours le même texte en séquençant l'ADN provenant d'un morceau d'estomac, de cerveau ou de peau.  
Ce qui fait la difference, c'est l'expression des gènes ou "*transcriptome*". C'est à dire l'ensemble des ARNs messager transcript dans la cellule dont la traduction est responsable du phénotype cellulaire. Par exemple les cellules de votre rétine expriment différents gènes que celle de votre estomac. Leurs transcriptomes sont différents.  
Une des méthodes pour évaluer le transcriptome est le séquençage des ARNm ou RNAseq. A partir d'un tissue, toutes les cellules sont lysée puis les ARNs messagers sont capturé (en général par leurs queues polyadénylé), convertit  en ADNc par une rétrotranscriptase, amplifié, puis séquencer pour être analyser par des méthode bioinformatique. Au final, on se retrouve avec une matrice d'expression contenant les proporitions de gènes exprimés par échantillons. 

[shema]    

## Résolution cellulaire

Le defaut de cette technique est qu'elle mesure l'expression d'un tissue et pas l'expression d'une cellule. En effet, dans un morceau de cerveau, il y aura différent type cellulaire (neurone, astrocytes, oligodentrocytes ...) avec des profils d'expression differente. La technique RNA-seq traditionnelle vous donnera seulement le niveau d'expression de cette ensemble.   
Aujourd'hui, une autre méthode permet de séquencer le transcriptome d'une seul cellule. C'est ce qu'on appelle du Single Cell RNA Seq (ScRNASeq). 
L'idée est de créer une librarie (Ensemble des fragments d'ADN déstiné au séquençage) ou chaque ARNm se voit greffer une séquence identifiant sa cellule d'origine (barcode). On peut alors après le séquençage, regrouper les reads entre eux grâce à leurs barcode et obtenir la matrice d'expression par cellules.   
Comment étiqueter chaque fragment d'ADN à sa cellule d'origine ? C'est ce qu'on va voir avec la méthode de microfluidique de 10xGenomics.

## La méthode 10x Genomics
La première étape consiste à isoler chaque cellule dans un goutelette d'huile contenant des réactifs de PCR ( polymérase, oligonucléotide...) et une bille. L'ensemble s'appelle une GEM (Gel bead in EMulsion).

[ photo reel ]

Chaque bille est recouverte de séquences adaptatrice unique contenant un barcode, un UMI et la séquence complémentaire à la queue PolyA (PolyT) des ARN messagers.
Pour chaque bille, et donc pour chaque cellule, il y a un barcode unique. 10xGenomics propose dans ses kits environ des billes avec 750 000 barcodes.
L'UMI (Unique Molecular Identifiers) est une courte séquence aléatoire unique  à chaque fragment. Il y a donc plusieurs UMI par bille. Cette identifiant est utilisé pour éviter les biais d'amplifications. Si une séquence est malencontreusement trop amplifier, on le detectera car un même UMI sera trop representé .

## Résulats 
On  analyse la matrice d'expression, apres normalisation etc .. et bioinfo 
PCA, clusterisation etc .. 
Ca donne ça :



1000 à 10 000 cell


[photo GEM]






## Références
* [Les methodes de fabrication des puces à ADN](http://bitesizebio.com/7463/how-dna-microarrays-are-built/)
* [Roche nimblegen](http://sequencing.roche.com/products/nimblegen-seqcap-target-enrichment.html)
* [Wikipedia: Fabrication des puces](https://fr.wikipedia.org/wiki/Puce_%C3%A0_ADN#Fabrication)
