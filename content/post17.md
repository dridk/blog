Title: Transition et transversion dans le génome
Slug: transition_transversion
Date: 2016-06-29 21:27:53
Category: biologie
Tags: bioinformatique, génétique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

Le génome humain et une longue séquence de 3 milliards de nucléotides, qui au cours de l'histoire de vivant a subit de nombreuse mutations. Elles ont pour rôle essentiel d'être le moteur de l'Evolution des espèces. 
Les mutations les plus abondantes sont les substitutions. C'est à dire le remplacement dans l'ADN d'un base azotés (Adénine,Cytosine,Guanine ou Tymine) par un autre.  
Les bases azotées sont classé en 2 familles: les purines et les pyrimidines. 
l'Adénine et la Guanine sont des purines, composé de deux cycles aromatiques. Tandis que la Tymine et la Cytosine sont des pyrimidines composées d'un seul cycle. Gravez vous en tête que cYtosine et tYmine sont des pYrimidines car ils contiennent tous un Y ! 

## Transition et Tranversion 
Une transition est une substitution entre deux bases sans changement de famille. C'est à dire une purine qui devient une autre purine, ou alors une pyrimidine qui devient une autre pyrimidine.    
Alors qu'une transversion est associé à un changement de famille. C'est une purine qui se transforme en pyrimidine ou l'inverse. 
L'image ci-dessous résume tous les cas possibles. 

<p align="center">
    <img src="../images/post17/transition_transversion.png">
</p>

## Notation consensus
Si nous résumons, il y a au total : 

* 4 transitions   : A>G, G>A, C>T, T>C
* 8 transversions : A>C,C>A,G>T,T>G,G>C,C>G,A>T,T>A 

Mais rappelons nous que l'ADN est double brin avec une complémentarité des bases. L'Adénine est toujours en face d'une Tymine et la Guanine toujours en face d'une Cytosine. Si il y a une mutation sur un brin, disons un A>G , alors il y aura sur le brin complémentaire un T>C. Ces deux notations sont donc equivalente. En général, on utilise la notation consensus dont la base de référence est une Tymine ou une Cytosine. Dans notre exemple T>C.  
En reprenant notre combinatoire précédente, on se retrouve donc avec : 

* 2 transition   : C>T, T>C 
* 4 transversion : C>A, T>G, C>G, T>A 

Si les mutations sont aléatoires alors nous devrions avoir 2 fois plus de transversion que de transion.   
Verifions cela en regardant quels sont les mutations substitutives qui différencie James Watson au génome de référence hg19. 

## Téléchargement des données nécessaires
### Génome de référence hg19.fa 
Le génome humain dans sa version hg19 est disponnible sur ucsc. 

    $ wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/hg19.2bit

Il faut utiliser l'outil twoBitToFa pour convertir le génome au format fasta. 

    $ wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa
    $ chmod +x twoBitToFa
    $ ./twoBitTo hg19.2bit hg19.2bit hg19.fa 

### Variant de James Watson pgWatson.txt.gz
Ce fichier contient l'ensemble des variations de James Watson par rapport au génome de référence. 

    $ wget http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/pgWatson.txt.gz


### Téléchargement de bedtools 
bedtools est un outil permettant de manipuler des fichiers bed. C'est à dire des fichiers contenant des régions génomiques de la forme : 

    chromosome  debut  fin 

C'est un peu le couteau suisse du bioinformaticien. Si vous ne l'avez toujours pas, Veuillez suivre les instructions pour l'installer ou tapper les commandes suivante. 

    $ wget https://github.com/arq5x/bedtools2/releases/download/v2.25.0/bedtools-2.25.0.tar.gz
    $ tar -zxvf bedtools-2.25.0.tar.gz
    $ cd bedtools2
    $ make


## Bash pour Nidja 
### Récupérer les régions des variants de James Watson 
Les trois première colonne du fichier pgWatson.txt.gz correspond à la région génomique avec le chromosome , la position de début et de fin. Dans notre cas, la taille est de 1 base. 

    zcat pgWatson.txt.gz|cut -f1,2,3 > region.bed

### Récupération des bases depuis hg19.fa 
On récupère les bases réference depuis hg19.fa aux coordonnées défini dans region.bed. 

    bedtools getfasta  -fi hg19.fa -bed region.bed -fo /dev/stdout | awk 'NR%2 == 0 {print $0}' > ref_bases.txt

### Récupération des bases depuis pgWatson.txt.gz
On parse le fichier afin de récupérer la base alternative selon que le variant est homozygote ou hétérozygote. 

    zcat pgWatson.txt.gz|cut -f5|awk -F "/" 'NF==2{print $2} NF==1{print $1}' > alt_bases.txt 

### Concatenation des deux fichiers 
On fusionne ref_bases.txt et alt_bases.txt dans un fichier à deux colonnes. Les bases sont toutes mise en majuscules. 

    paste -d '' ref_bases.txt alt_bases.txt|tr '[:lower:]' '[:upper:]' > substitution.txt  

### Notation consensus 
Toutes les substitions sont écris en respectant la notation consensus. 

    cat substitution.txt |sed -e 's/AG/TC/' -e 's/GA/CT/' -e 's/AC/TG/' -e 's/GT/CA/' -e 's/GC/CG/' -e 's/AT/TA/'|sort |uniq -c > consensus.txt


### Compatage des substitutions 

    cat consensus.txt|sort|uniq -c 

Nous obtenons alors : 

     697641 CT
     683841 TC
     183890 CA
     173279 TG
     172228 CG
     146872 TA
        466 GG
        403 AA
        395 CC
        369 TT


Il reste plus qu'a faire un jolie graphique avec ça!

## Resultats

<p align="center">
    <img src="../images/post17/chart.jpg">
</p>

Ce graphique represente les différente substitutions retrouvé chez James Watson par rapport au génome de référence. Et comme vous pouvez le constater, cela ne colle absolument pas avec notre hypothèse des mutations aléatoire. Les 2 transitions possible represente 2/3 des substitution, la ou les 4 transversions ne represente qu' 1 quart. 

## Explication 
Evolution, origine des mutations , selection ... 
Je sais pas en faite .. :D 

A finir...




## Remerciement 


