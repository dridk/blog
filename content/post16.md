Title: Le génome en chiffre
Slug: genome_chiffre
Date: 2016-04-29 12:55:48
Tags: génétique
Category: génétique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/plasmodium_banner.jpg

Ça faisait longtemps que j'avais envie de faire une description numérique du génome. Vous savez ces chiffres repères qui nous permet de faire des comparaisons et de répondre à des questions du genre : "Est ce que cette montagne est grande ?" Si vous n'avez pas de référence, comme la taille du mont blanc, ça va être difficile de répondre...  
Bref, nous allons faire pareil sur le génome humain! Et pour être sur qu'une organisation maçonnique n'a pas volontairement mis des faux chiffres sur  internet, nous allons tout calculer par nous nous même! Ça sera l'occasion de faire un peu de bash et d'apprendre quelque commande ! 

## Télécharger le génome humain  
Tout d'abord si vous n'avez pas le génome de référence hg19, télécharger le depuis le goldenpath d'ucsc. Ca fait 778M, ça risque de prendre du temps pour certain. 

    $ wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.2bit

Ce fichier est compressé. En faite chaque base est codé sur 2 octets au lieu de 8. On peut le convertir en fichier texte standard avec la commande **twoBitToFa** disponible également sur ucsc. 

    $ wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa
    $ chmod +x twoBitToFa 
    $ ./twoBitToFa hg19.2bit hg19.fa 

Vous voilà avec un fichier fasta, contenant les séquences de chaque chromosome humain... Chaque.. En faite, non! Ce fichier contient aussi des chromosomes avec des séquences alternative ainsi que le chromosome mitochondriale. 
Tapez cette commande pour voir tous les noms des chromosomes du fichier hg19.

    $ cat hg19.fa|grep ">chr"
  
Nous allons plutôt créer un fasta avec uniquement les chromosomes nucléaire de 1 à 22 et les deux chromosomes sexuels X et Y. Il y a un outil faSomeRecords sur ucsc qui fait très bien le travail. Il prend en argument notre génome hg19.fa et un fichier contenant la liste des chromosomes souhaité. 

    $ wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/faSomeRecords
    $ chmod +x faSomeRecords
    #Création d'une liste de chromosomes 
    $ for i in {1..22}; do echo chr$i; done > chromosomes.list
    $ echo chrX >> chromosomes.list 
    $ echo chrY >> chromosomes.list 
    $ ./faSomeRecords hg19.fa chromosomes.list hg19_clean.fa 

Voilà, un fichier tout propre contenant uniquement les 24 chromosomes du génome humain. 

## Quel est la taille du génome humain ? 
Il suffit de compter le nombre de base! On supprime tous les retours à la ligne du fichier fasta et on compte avec la commande wc -c ! 

    $ cat hg19_clean.fa|grep -v "chr." | tr --delete "\n" | wc -c
    3095677412

3'095'677'412 c'est le nombre de nucléotide qu'il y a dans le génome humain nucléaire selon l'assemblage hg19! Bref, gravez vous ce premier chiffre en tête : 3 millards de base dans le génome humain !

## Pourcentage de base dans le génome humain ? 
Pour ça, je vous propose d'utiliser un de mes outils préféré : [bedtools](http://bedtools.readthedocs.io/en/latest/) ! Le couteau suisse du bioinformaticien. Il est en principe dans les dépôts d'ubuntu mais je vous conseil la dernière version :  

    $ wget https://github.com/arq5x/bedtools2/releases/download/v2.25.0/bedtools-2.25.0.tar.gz
    $ tar -zxvf bedtools-2.25.0.tar.gz
    $ cd bedtools2
    $ make 
    $ sudo make install 

Pour connaître le pourcentage en base on utilise "bedtools nuc". Cette commande permet de compter les pourcentages en base A,C,G,T dans un fichier fasta à partir des régions chromosomiques défini dans un fichier bed. On va calculer ces pourcentages par chromosomes.   
Pour allez plus vite, on peut télécharger le fichier hg19.chrom.sizes. Ce fichier contient sur chaque ligne, le nom du chromosome et sa taille en base. On va s'en servir pour créer le fichier bed nécessaire à bedtools. 

    $ wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.chrom.sizes
    $ cat hg19.chrom.sizes|grep -we "chr[0-9XY]*"|awk 'BEGIN{OFS="\t"}{print $1,0,$2}' > hg19_clean.sizes.bed 

Assurez vous que la somme des tailles des chromosomes tombe bien sur les 3 milliards précédents.

    $ cat hg19_clean.sizes.bed|cut -f3|paste -sd "+"|bc 

Lancer alors la commande  :

    $ bedtools nuc -fi hg19_clean.fa -bed hg19_clean.sizes.bed > hg19.stat 

Vous obtenez un fichier contenant pour chaque chromosome, le nombre de nucléotide A,T,C,G et le pourcentage en AT et CG. N’hésiter pas à regarder l'aide de la commande.   
Le pourcentage en GC du génome humain tourne autour de 37%. Avec comme extrême le chromosome 19 (48%) et le chromosome Y (25%). 

## Nombre de base A,C,G,T dans le génome ... WTF ?? 
Dans le fichier hg19.stat précédemment généré, on observe aussi le nombre de base A,C,G,T. On faisant la somme, on obtient sur tous le génome :

- 846093191 base T soit 27.2%
- 844862932 base A soit 27.3% 
- 585012752 base C soit 18.8% 
- 585358256 base G soit 18.9% 

???What???? Il y a quasiment autant de base A que de T, et autant de base C que de G. Détrompez vous, si vous pensez que c'est la loi de Chargaff expliquant la complémentarité des brins.. Car cette répartition c'est sur un seul brin d'ADN!! C'est comme si dans un livre de 3 milliards de lettre, il y avait autant de "s" que de "a".   
Bien sur j'ai récherché, j'ai demandé, j'ai eu toutes les réponses inimaginable. En faite c'est ce qu'on appelle la second loi de Chargaff! Et je vous assure... Je n'ai pas encore trouvé d'explication, si ce n'est celle ci..

## Le contenu du génome  
Les exons, introns ... 

## La variabilité 

## Les mutations les plus frequentes


## Références
* [Diagnostic microscopique du paludisme](http://www.cdc.gov/dpdx/resources/pdf/benchAids/malaria/Congo_Bench_Aid_vF.pdf)
* [Kraemer, S. M. & Smith, J. D. A family affair: var genes, PfEMP1 binding, and malaria disease. Curr. Opin. Microbiol. 9, 374–380 (2006).](http://biologie.univ-mrs.fr/upload/p87/kraemer_2006.pdf)
* [OMS](http://www.who.int/mediacentre/factsheets/fs094/fr/)
* [Ferreira, A. et al. Sickle hemoglobin confers tolerance to Plasmodium infection. Cell 145, 398–409 (2011).](http://www.ncbi.nlm.nih.gov/pubmed/21529713)
* [Langhi, D. M. & Bordin, J. O. Duffy blood group and malaria. Hematol. Amst. Neth. 11, 389–398 (2006).](http://www.ncbi.nlm.nih.gov/pubmed/17607593)
* [Parasitoses et mycoses des régions tempérées et tropicales, Auteur : Association Française des Enseignants de Parasitologie médicales ANOFEL, Editeur : ELSEVIER / MASSON paru le : 09/2014 (3ème édition)](http://www.remede.org/documents/parasitoses-et-mycoses-des-regions.html)
