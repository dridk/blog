Title: Séquençage des ARNs messagers à partir de cellules uniques 
Slug: sc-rna-seq
Date: 2017-08-28 16:23:49
Tags: rna-seq,single-cell,microfluidique
Category: biologie
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

Toutes les cellules de votre corps sont constituées du même génome. Vous obtiendrez toujours le même texte en séquençant l'ADN provenant d'un morceau d'estomac, de cerveau ou de peau (sauf cas très particuliers: [mosaïques](https://fr.wikipedia.org/wiki/Mosa%C3%AFque_(g%C3%A9n%C3%A9tique))).  
Ce qui fait la différence, c'est l'expression des gènes ou « *[transcriptome](https://fr.wikipedia.org/wiki/Transcriptome)* ». C'est-à-dire l'ensemble des [ARNs messagers (ARNm)](https://fr.wikipedia.org/wiki/Acide_ribonucl%C3%A9ique_messager) transcrits dans la cellule dont la traduction est responsable du [phénotype cellulaire](https://fr.wikipedia.org/wiki/Ph%C3%A9notype_cellulaire). Par exemple, les cellules de votre rétine expriment d'autres gènes que votre estomac. Leurs transcriptomes sont différents.  
Une des méthodes pour évaluer le transcriptome est le séquençage des [ARN messager](https://fr.wikipedia.org/wiki/Acide_ribonucl%C3%A9ique_messager) ou [RNA-seq](https://fr.wikipedia.org/wiki/RNA-Seq).    
En résumant rapidement (figure ci-dessous) : 
À partir d'un tissu, toutes les cellules sont lysées puis les ARNs messagers sont capturés (en général par leurs [queues polyadénylées](https://fr.wikipedia.org/wiki/Polyad%C3%A9nylation)). Ils sont ensuite convertis  en [ADN complémentaire](https://fr.wikipedia.org/wiki/ADN_compl%C3%A9mentaire) (ADNc) par une [rétrotranscriptase](https://fr.wikipedia.org/wiki/Transcriptase_inverse), amplifiés, puis séquencés. L'étape bio-informatique consiste à aligner les [reads](http://dridk.me/ngs.html) sur un génome de référence et faire des normalisations pour évaluer quels gènes sont exprimés. Le nombre d'ARNm séquencés d'un gène correspond à son niveau d'expression ou « *abondance »*.    
Finalement, en analysant différents tissus, on obtient  une *matrice d'expression* (voir tableau ci-dessous).   
Pour plus de détails sur l'analyse bio-informatique,  je vous invite à jeter un oeil sur l'[article de bioinfo-fr](https://bioinfo-fr.net/lanalyse-de-donnees-rna-seq-mode-demploi) traitant de ce sujet.    

<div class="figure">     <img src="../images/post27/rnaseq-overview.png" />      <div class="legend">Schéma général de la technologie RNAseq. Dans cet exemple, le séquençage est réalisé sur deux échantillons (tumeur et normal). Les ARNs sont capturés grâce leurs queues polyA, sont convertis en ADNc puis séquencés. Les reads sont alignés sur un génome de référence afin de mesurer l'expression de chaque gène. Cette expression est proportionnelle aux nombres d'ARN s'alignant sur un gène donné </br>Source : <a href="https://fr.wikipedia.org/wiki/RNA-Seq">Wikipedia</a></div> </div>

<div class="figure">     <img src="../images/post27/expression-matrix.png" />      <div class="legend">Exemple d'une matrice d'expression comparant deux tissus. Les valeurs du tableau correspondent aux quantités d'ARNm retrouvées par gène et par tissu. L'expression des gènes dans le tissu 1 est différente de celle dans le tissu 2</div> </div>

## ScRNA-seq : Nouvelle approche plus résolutive

Le défaut avec la technologie RNA-seq est qu'elle mesure l'expression d'un tissu et pas l'expression d'une cellule. En effet, dans un morceau de cerveau par exemple, il y aura différents types cellulaires (neurone, [astrocytes](https://fr.wikipedia.org/wiki/Astrocyte), [oligodendrocytes](https://fr.wikipedia.org/wiki/Oligodendrocyte) ...) avec des profils d'expression différents. Le  RNA-seq vous informe seulement du niveau d'expression de cet ensemble de cellules.   
Aujourd'hui, une autre méthode permet de séquencer le transcriptome d'**une seule** cellule. C'est ce qu'on appelle du [Single Cell RNA Seq  (ScRNA-Seq)](https://en.wikipedia.org/wiki/Single-cell_transcriptomics). 
L'idée est de créer une [librairie](ngs.html) (Ensemble des fragments d'ADN destinés au séquençage) où chaque ARNm se voit greffer une séquence identifiant sa cellule d'origine ([barcode](https://fr.wikipedia.org/wiki/Barcoding_mol%C3%A9culaire)). On peut alors, après séquençage, regrouper les [reads](http://dridk.me/ngs.html) entre eux grâce à leurs barcodes et obtenir une matrice d'expression par cellules et par gènes.   
Comment étiqueter chaque fragment d'ADN avec sa cellule d'origine ? C'est ce qu'on va voir tout de suite avec la méthode de [microfluidique](https://fr.wikipedia.org/wiki/Microfluidique) de [10xGenomics](https://www.10xgenomics.com/).

## Isoler les cellules en microfluidique
La microfluidique est une technologie manipulant des fluides dans des microcanaux. Grâce à cette technique, on va pouvoir isoler chaque cellule dans une gouttelette d'huile contenant des réactifs (polymérase, oligonucléotide, retrotranscriptase...) et une bille particulière appelée **GEM** (Gel bead in EMulsion). 

<div class="figure">     <img src="../images/post27/GEM.png" />      <div class="legend">Microgoutelette avec une cellule et une GEM (Gel bead in EMulsion) </br> Source : <a href="https://www.10xgenomics.com/single-cell/">10xGenomics</a>     </div> </div>

<div class="figure">     <img src="../images/post27/gem-formation.gif" />      <div class="legend">Animation montrant la formation des microgoutelettes en microfluidique. Les GEMs sont définies par un barcode unique représenté ici par une couleur</br> Source : <a href="https://www.10xgenomics.com/single-cell/">10xGenomics</a> </div> </div>

<div class="figure">     <img src="../images/post27/gem-formation2.gif" />      <div class="legend">Vidéo de microfluidique </br> Source : <a href="https://www.youtube.com/watch?v=zQoHc6PtIFk">Dolomite Microfluidics</a> </div> </div>

## Chaque cellule a son barcode unique
Chaque GEM est recouverte  (figure ci-dessous) de séquences adaptatrices uniques contenant un **barcode**, un **[UMI](https://en.wikipedia.org/wiki/Unique_molecular_identifier)** et la **séquence PolyT** .          
- Le **barcode** est l'identifiant unique à la bille, et donc unique à la cellule. 10xGenomics propose 750 000 barcodes environ.       
- L'**UMI** (Unique Molecular Identifiers)  est une courte séquence aléatoire unique  à chaque fragment entourant la bille. Il y a donc plusieurs UMI par bille. Cet identifiant est utilisé pour éviter les biais d'amplifications. Si une séquence est malencontreusement trop amplifiée dans une goutte, elle sera détectée, car le même UMI sera représenté plusieurs fois.    
- **La séquence polyT** va permettre la fixation des ARNs messagers par complémentarité avec leurs queues polyA.

<div class="figure">     <img src="../images/post27/gem-zoom.png" />      <div class="legend">Zoom sur une GEM et les séquences la recouvrant</br> Source : <a href="https://www.10xgenomics.com/single-cell/">10xGenomics</a> </div> </div>

La réaction de RNA-seq peut alors se faire dans ce microréacteur. Après lyse de la cellule, les ARNs messagers sont capturés à la surface de la GEM par leurs queues polyA. Et les nouvelles séquences Barcode+UMI+ARNm sont converties en ADNc.

## Création d'une librairie et séquençage 
Il ne reste plus alors qu'à créer la librairie pour le séquençage. Tous les fragments d'ADNs identifiés par leurs barcodes sont poolés ensemble après avoir enlevé l'huile. Les adaptateurs de séquençage ([Illumina](https://www.youtube.com/watch?v=fCd6B5HRaZ8&t=3s)) sont ajoutés afin d'obtenir la librairie.   
Après le séquençage et l'alignement, il suffira de regrouper les reads provenant d'une même cellule en comparant leurs barcodes pour obtenir une matrice d'expression (tableau ci-dessous).

<div class="figure">     <img src="../images/post27/expression-matrix-cell.png" />      <div class="legend">Exemple d'une matrice d'expression en Single Cell RNA Seq. En réalité, il y a des milliers de cellules (autant que de barcode) et au moins 23 000 gènes (pour l'homme). Les valeurs du tableau correspondent à la quantité d'ARNm retrouvé par gène et par cellule</div> </div>

## Représentation graphique 

On peut alors représenter la matrice d'expression dans un graphique en réalisant une [analyse en composantes principales](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales) (10x genomics utilise une [t-SNE](https://fr.wikipedia.org/wiki/Algorithme_t-SNE)). 
Chaque point correspond à une cellule. Plus les cellules sont proches sur le graphique, plus leurs expressions génétiques sont similaires. 

<div class="figure">     <img src="../images/post27/blood_example.png" />      <div class="legend">Profil d'expression obtenu à partir des cellules du sang (2,700 cellules mononuclées du sang périphérique <a href="https://fr.wikipedia.org/wiki/Cellule_mononucl%C3%A9%C3%A9e_sanguine_p%C3%A9riph%C3%A9rique)))">PBMC</a>. On visualise après clusterisation les différentes familles.</br> Source : <a href="http://satijalab.org/seurat/get_started_v1_4.html">http://satijalab.org/seurat/get_started_v1_4.html</a></div> </div>

Encore plus parlant, [cette vidéo ](https://www.10xgenomics.com/single-cell/?wvideo=z54e2lemhd) qui montre le profil d'expression des cellules du tissu cérébral dans un repère à 3 axes animé.

## What next ? 
À l'heure où j'écrivais ce post, je suis tombé sur un article décrivant la technique [DropNc-Seq](http://www.genengnews.com/gen-news-highlights/single-nucleus-rna-seq-merges-with-microfluidics/81254868). Une méthode similaire à ce qui vient d'être décrit. Mais au lieu des cellules, ce sont les noyaux qui sont isolés pour le séquençage. On obtient alors le transcriptome nucléaire... Cool hein ?     

## Références
* [RNASeq sur bioinfo-fr](https://bioinfo-fr.net/lanalyse-de-donnees-rna-seq-mode-demploi)
* [10xGenomics](https://www.10xgenomics.com/single-cell/)
* [Dolomite Microfluids](https://www.youtube.com/watch?v=zQoHc6PtIFk)
* [Massively parallel digital transcriptional profiling of single cells](https://www.ncbi.nlm.nih.gov/pubmed/28091601)
* [Vidéo commerciale](https://www.youtube.com/watch?v=kIGwv0Kpgro)
