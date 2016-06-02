Title: Le génome en chiffre - part 1 
Slug: genome_chiffre_1
Date: 2016-04-29 12:55:48
Tags: génétique, bash , bedtools
Category: génétique
Author: Sacha Schutz
Status: draft
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

Ça faisait longtemps que j'avais envie de faire une description numérique du génome. Vous savez ces chiffres repères qui nous permette de faire des comparaisons et de répondre à des questions du genre : "*Est ce que cette montagne est grande ?*" Si vous n'avez pas de référence, comme la taille du mont blanc, ça va être difficile de vous faire une idée...     
Nous allons faire pareil sur le génome humain! Et pour être sur qu'une organisation maçonnique n'a pas volontairement mis des faux chiffres sur  internet, nous allons tout calculer par nous  même! Ça sera l'occasion de faire un peu de [bash](https://fr.wikipedia.org/wiki/Bourne-Again_shell) et d'apprendre quelques commandes ! 

## Télécharger le génome humain  
Tout d'abord si vous n'avez pas le génome de référence, télécharger le depuis le [goldenpath d'ucsc](http://hgdownload.cse.ucsc.edu/goldenpath/hg19/bigZips/). C'est le fichier  *hg19.2bit* qui fait 778M.

    $ wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.2bit

Ce fichier est compressé. En faite chaque base est codé sur 2 octets au lieu de 8. On peut le convertir en fichier texte standard avec la commande **twoBitToFa** disponible également sur ucsc. 

    $ wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa
    $ chmod +x twoBitToFa 
    $ ./twoBitToFa hg19.2bit hg19.fa 

Vous voilà avec un fichier [fasta](https://fr.wikipedia.org/wiki/FASTA_%28format_de_fichier%29), contenant les séquences de chaque chromosome humain... Chaque.. En faite, non! Ce fichier contient des chromosomes en double avec des séquences alternatives ainsi que le chromosome mitochondriale. 
Tapez cette commande pour voir tous les noms des chromosomes du fichier *hg19.fa*.

    $ cat hg19.fa|grep ">chr"
  
Nous allons plutôt créer un fichier avec uniquement les chromosomes nucléaires de 1 à 22 et les deux chromosomes sexuels X et Y. Il y a un outil **faSomeRecords** sur ucsc qui fait très bien le travail. Il prend en argument notre génome *hg19.fa* et un fichier avec la liste des chromosomes souhaités. 

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
    $ 3095677412

**3'095'677'412** c'est le nombre de nucléotide qu'il y a dans le génome humain nucléaire selon l'assemblage hg19! Bref, gravez vous ce premier chiffre en tête : **3 millards** de base dans le génome humain !

## Pourcentage en GC du génome humain ? 
Pour ça, je vous propose d'utiliser un de mes outils préféré : [bedtools](http://bedtools.readthedocs.io/en/latest/) ! Le couteau suisse du bioinformaticien. Il est en principe dans les dépôts d'ubuntu mais je vous conseil la dernière version depuis le site officiel :  

    $ wget https://github.com/arq5x/bedtools2/releases/download/v2.25.0/bedtools-2.25.0.tar.gz
    $ tar -zxvf bedtools-2.25.0.tar.gz
    $ cd bedtools2
    $ make 
    $ sudo make install 

Pour connaître le pourcentage en base on utilise **bedtools nuc**. Cette commande permet de compter les pourcentages en base A,C,G,T dans un fichier fasta à partir des régions chromosomiques définies dans un fichier bed. On va calculer ces pourcentages pour chaque chromosome.   
Pour allez plus vite, on peut télécharger le fichier *hg19.chrom.sizes*. Celui ci contient sur chaque ligne, le nom du chromosome et sa taille en base. On va s'en servir pour créer le fichier nécessaire à bedtools. 

    $ wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.chrom.sizes
    $ cat hg19.chrom.sizes|grep -we "chr[0-9XY]*"|awk 'BEGIN{OFS="\t"}{print $1,0,$2}' > hg19_clean.sizes.bed 

Assurez vous que la somme des tailles des chromosomes tombe bien sur les 3 milliards précédents.

    $ cat hg19_clean.sizes.bed|cut -f3|paste -sd "+"|bc 

Lancer alors la commande  :

    $ bedtools nuc -fi hg19_clean.fa -bed hg19_clean.sizes.bed > hg19.stat 

Vous obtenez un fichier contenant pour chaque chromosome, le nombre de nucléotide A,T,C,G,N avec le pourcentage en AT et CG. N’hésiter pas à regarder l'aide de la commande.   
Le pourcentage en GC du génome humain tourne autour de **37%**. Avec comme extrême le chromosome 19 (**48%**) et le chromosome Y (**25%**). 

## Pourcentage en base A,C,G,T 
Dans le fichier *hg19.stat* précédemment généré, on observe aussi le nombre de base A,C,G,T. On faisant la somme, on obtient sur tous le génome :

- 846093191 base T soit 27.2%
- 844862932 base A soit 27.3% 
- 585012752 base C soit 18.8% 
- 585358256 base G soit 18.9% 

???WTF???? Il y a quasiment autant de base A que de T, et autant de base C que de G. Détrompez vous, si vous pensez que c'est [la loi de Chargaff](https://fr.wikipedia.org/wiki/R%C3%A8gles_de_Chargaff) expliquant la complémentarité des brins.. Car cette répartition est sur un seul brin d'ADN! Pas de double brin dans l'histoire! C'est comme si dans un livre de 3 milliards de lettre, il y avait autant de "s" que de "a".     
Bien sur j'ai recherché, j'ai demandé, j'ai eu toutes les réponses inimaginables. En faite c'est ce qu'on appelle la second loi de Chargaff, beaucoup moins connu! Et je vous assure, je n'ai pas encore trouvé d'explication, si ce n'est [celle-ci](http://www.basic.northwestern.edu/g-buehler/genomes/g_chargaff.htm)

## Combien de gène dans le génome humain  ?
Dans le génome il y a des gènes constitués d'intron et d'exon. Et chaque gène définit plusieurs transcrits.   
On peut télécharge [refseq](https://en.wikipedia.org/wiki/RefSeq), une base de donnée contenant tous les gènes officiels! Dans le fichier, ces colonnes vont nous intéressé par la suite. 

* colonne 3 : le chromosome 
* colonne 5 : le début du transcrit
* colonne 6 : La fin du transcrit
* colonne 7 : début du CDS 
* colonne 8 : fin du CDS 
* colonne 9 : le nombre d'exons
* colonne 10: liste des débuts d'exons
* colonne 11: liste des fins d'exons  
* colonne 13 : le nom du gène

Pour télécharger  : 

    $ wget wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz

Compter le nombre de gène unique : 

    $ zcat refGene.txt.gz|cut -f13|sort -u | wc -l
    $ 27048 

Votre Deuxième chiffre à retenir ! Environ **27000** gène constitue le génome humain !

### Quel est le pourcentage d'exons ?  
Dans le fichier refseq, colonne 10 et 11, nous avons tous les débuts et les fins des exons. J'ai juste fait la sommes des différences entre fin d'exon et début d'exon sur tous les gènes uniques. Avec awk, ça se fait tout seul : 

    $ zcat refGene.txt.gz|sort -u -k 13,13|awk '{SUM=0;split($10,s,","); split($11,e,",");for(i=1;i<length(s);i++){SUM+=e[i] - s[i]};print SUM}'|paste -sd "+"|bc 
    $ 72090466

On obtient **72090466**, le nombre de base dans les exons. En le divisant par la taille du génome, on se retrouve avec : **2.32 %** du génome est constitué d'exon.

### Quel est le pourcentage de base codante ? 
Pour cela, j'ai crée un fichier bed qui contient la position de tous les exons. Et un second fichier contenant la position de toutes les [cds](https://fr.wikipedia.org/wiki/S%C3%A9quence_codante). J'ai ensuite fait l'intersection avec bedtools. 

    $ zcat refGene.txt.gz|sort -u -k 13,13|awk 'BEGIN{OFS="\t"}{SUM=0;split($10,s,","); split($11,e,",");for(i=1;i<length(s);i++){print $3,s[i],e[i]} }' > exons.bed 

    $ zcat refGene.txt.gz|sort -u -k 13,13|awk 'BEGIN{OFS="\t"}{print $3,$7,$8 }' > cds.bed 

    $ bedtools intersect -a exons.bed -b cds.bed | awk '{print $3-$2}'|paste -sd "+" | bc  

On obtient **35269084**, le nombre de base codante. Ce qui fait **1.13 %** du génome . 1% du génome est codant. C'est vraiment pas beaucoup n'est ce pas ?

### Quel est le pourcentage d'intron ? 
Même logique, j'ai fait les zones transcrites soustraient des exons. Ce qui nous donne les introns avec les UTR. 

    $ zcat refGene.txt.gz|sort -u -k 13,13|awk 'BEGIN{OFS="\t"}{print $3,$5,$6 }' > transcrits.bed

    $ bedtools substract -a transcrits.bed -b exons.bed | awk '{print $3-$2}'|paste -sd "+" | bc  

On obtient **1184956505** bases dans les introns/UTRs soit **38.2 %** du génome! 
Il reste tout de même plus de 60% d'inconnu! Dans un prochaine article, on s'y attaque ! 


### Combien de mutation me distingue du génome de référence ? 
On ne va pas prendre mon génome.. Mais celui de [James Watson](https://fr.wikipedia.org/wiki/James_Dewey_Watson) co-découvreur de l'ADN avec [Francis Crick](https://fr.wikipedia.org/wiki/Francis_Crick) et [Rosalind Franklin](https://fr.wikipedia.org/wiki/Rosalind_Franklin). Son génome a été séquencé et distribué librement. Nous allons télécharger un fichier contenant uniquement les différences entre le génome de Watson et le génome de référence. C'est à dire un fichier contenant sur chaque ligne, la position et la base alternative.

    $ wget http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/pgWatson.txt.gz

En comptant le nombre de ligne : 

    $ cat pgWatson.txt.gz | wc -l 

On obtient **2059384** variants. Environs **2 millions** de base distingue James Watson du génome de référence. En  pourcentage, ça nous fait : **0.06 %**

### Combien de mutation je partage avec autre individu ? 
On va regarder les variants que partage [Craig Venter](https://fr.wikipedia.org/wiki/Craig_Venter) et James Watson. 
Même chose que précédemment, on récupère les données de Venter. 

    $ wget http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/pgVenter.txt.gz

Puis on transforme le fichier de Watson et Craig en fichier bed. 

    $ zcat pgVenter.txt.gz |cut -f2,3,4|sort > venter.bed
    $ zcat pgWatson.txt.gz |cut -f2,3,4|sort > watson.bed

Puis on fait l'intersection : 

    $ bedtools intersect -a venter.bed -b watson.bed|wc -l

On trouve alors **1'192'314** de variant en commun entre Venter et Watson! 

#Conclusion 
Nous allons nous arrêter la pour le moment, sinon on ne finira jamais! J'ai commencé par des questions simples. Mais dans le prochain article, nous allons poser d'autre question beaucoup plus précise. Ou se trouve les variations ? Qu'y a-t-il dans les 60% de l'ADN ? Quel sont les mutations les plus fréquente ?    
Pour cette fois retenez ceci : Votre ADN est composé de **3 millards** de base. **1%** constitue le génome codant pour **25 000** gènes. Et **1 millions** de variants vous distingue d'un autre individu. 


