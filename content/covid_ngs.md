Title: Analyse de génomes de SARS-CoV-2
Slug: covid_ngs
Date: 2021-01-25 23:51:29
Modified: 2021-01-25 23:51:29
Tags: virus,pipeline,sars-cov-2,covid
Category: bioinformatique
Author: Sacha SCHUTZ
SIDEBARIMAGE:../images/common/virus_banner.jpeg


La [pandémie mondiale de Covid-19](https://fr.wikipedia.org/wiki/Pand%C3%A9mie_de_Covid-19) a créé un élan sans précédent dans la production scientifique de données. Notamment, les données sur les génomes du virus produites par [séquençage haut débit](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age_de_l%27ADN#S%C3%A9quen%C3%A7age_haut_d%C3%A9bit_(HTS)) qui permettent aujourd'hui d'identifier de nouvelles mutations comme la [N501Y](https://fr.wikipedia.org/wiki/Variant_501.V2#Mutations) du variant anglais [B.1.1.7](https://fr.wikipedia.org/wiki/VOC-202012/01) où une [Asparagine](https://fr.wikipedia.org/wiki/Asparagine) (N) est remplacée par une [Tyrosine](https://fr.wikipedia.org/wiki/Tyrosine) (Y) à la position 501 de la [protéine S](https://fr.wikipedia.org/wiki/P%C3%A9plom%C3%A8re).     
Le génome du [SARS-CoV-2](https://fr.wikipedia.org/wiki/SARS-CoV-2) étant tout  petit (30 kbases) par rapport au génome humain (3 Gbases), l'analyse bioinformatique peut se faire avec un ordinateur personnel. Cette analyse est donc l'occasion d'un très bon exercice pour se familiariser avec les outils d'alignement et de détection de variants.  
Dans ce billet, je vous propose de suivre pas-à-pas l'analyse d'un génome de SARS-CoV-2 à partir des données brutes générées par un séquenceur [Illumina](https://fr.wikipedia.org/wiki/Illumina). Pour cela, j'ai récupéré les données de séquençage de 245 échantillons provenant d'un laboratoire de l'état du [Delaware](https://fr.wikipedia.org/wiki/Delaware) aux États-Unis. Plus précisément une paire de fichiers [Fastq](https://fr.wikipedia.org/wiki/FASTQ) par échantillon contenant les courtes séquences, appelées *reads*, lus par le séquenceur. Je les ai ensuite toutes alignées sur [le génome de référence de Wuhan](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512) pour en extraire les mutations que j'ai annotées. Enfin, j'ai reconstruit les génomes de chaque échantillon afin de pouvoir attribuer le nom de leurs lignées.                   
Pour réaliser cette analyse, il vous faudra de préférence un terminal [Linux](https://fr.wikipedia.org/wiki/Linux) avec différents outils que vous pouvez installer avec [conda](https://docs.conda.io/en/latest/miniconda.html). Sinon un [notebook](https://colab.research.google.com/) est à votre disposition à [cette adresse](https://colab.research.google.com/drive/1V8EsdFyCmr7fmVkVf09JQhraatTWcd3f).

## Analyse de l'échantillon SRR13182925
### Source des données 

Je connais 2 sources principales pour récupérer des données de séquençage. [SRA du NCBI](https://www.ncbi.nlm.nih.gov/sra) et la base européenne [ENA](https://www.ebi.ac.uk/ena/browser/home). J'ai choisi cette dernière par convenance.
En fouillant, j'ai d'abord découvert le projet [ICOG UK](https://www.cogconsortium.uk) constamment mis à jour et disposant de pas moins de 206 000 génomes à l'heure où j'écris ce billet.   
Mais pour mon petit PC de bureau, c'est trop de données. Nous nous contenterons pour le moment des 245 génomes  du projet [PRJNA673096](https://www.ebi.ac.uk/ena/browser/view/PRJNA673096) produit par le [Delaware Public Health Lab](https://www.dhss.delaware.gov/dhss/dph/lab/labs.html) aux États-Unis. Il s'agit de données produites sur un [Illumina MiSeq](https://emea.illumina.com/systems/sequencing-platforms/miseq.html) en [Amplicon](https://dridk.me/ngs.html).

### Téléchargement des données avec EnaBrowserTools

Nous pouvons télécharger les fichiers Fastq directement depuis le site de l'ENA. Mais il existe un outil [python](https://fr.wikipedia.org/wiki/Python_(langage)) en ligne de commande, [enaBrowserTools](https://github.com/enasequence/enaBrowserTools),  qui va nous faciliter la tâche. Pour l'installer, il suffit de suivre la [documentation](https://github.com/enasequence/enaBrowserTools/blob/master/README.md):    

- **enaDataGet** nous permet de télécharger les données associées à un échantillon. 

- **enaGroupGet** nous permet de télécharger l'ensemble des données d'un projet. 

Pour la suite de ce billet, nous nous contenterons d'analyser uniquement l'échantillon [SRR13182925](https://www.ebi.ac.uk/ena/browser/view/SRR13182925). Pour télécharger ses fichiers Fastq associés, taper la commande suivante:

```bash
enaDataGet -f fastq SRR13182925    
```

Cette commande crée un dossier **SRR13182925** contenant 2 fichiers Fastq : 

- *SRR13182925_1.fastq.gz* 
- *SRR13182925_2.fastq.gz*

Ces 2 fichiers contiennent les courtes séquences lues, appelées **reads**, d'environ 150 bases provenant du génome viral trouvé dans l'échantillon. Ces reads sont lus dans les deux sens par le séquenceur. Pour cette raison, il y a 2 fichiers, un par sens de lecture.    
Vous pourrez en avoir un aperçu à l'aide la commande suivante : 

```bash
zcat SRR13182925_1.fastq.gz|awk 'NR % 4 == 2 {print $0}'
```

```
AGATAATACAGTTGAATTGGCAGGCACTTCTGTTGCATTACCAGCTTGTAGACGTACTGTGGCAGCTAAACTACCAAGTAC
ATATTGGCTTCCGGTGTAACTGTTATTGCCTGACCAGTACCAGTGTGTGTAC
TCGTAACAATCAAAGTACTTATCAACAACTTCAACTACAAATAGTAGTTGTCTGATATCACACATTGTTGGTAGATTATAACGATAGTAGTCATAATCGCTGATAGCAGCATTACCATCCTGAGCAAAGAAGAAGTGTTTTAATTCAACAGAACTTCCTTCCTTAAAGAAACCCTTAGACACAGCAAAGTCATAGAAGTCTTTGTTAAAATTACCGGGTTTGACAGTTTGAAAAGCAACATTGTTAGTAAGTGCAGCTACTGAAAAGCACGTAGTGCGT
ACATTACACATAAACGAACTTATGGATTTGTTTATGAGAATCTTCACAATTGGAACTGTAACTTTGAAGCAAGGTGAAATCAAGGATGCTACTCCTTCAGATTTTGTTCGCGCTACTGCAACGATACCGATACAAGCC
GTTAGATAGCACTCTAGTGTCAAATCTACAAACAATGGAATTAGCAGGATATCTATCGACATTGCAATTCCAAAATAGGCATACACCATCTGTGAATTTGTCAGAATGTGTGGCATAAGAATAGAAT
GTTTATTACCCTGACAAAGTTTTCAGATCCTCAGTTTTACATTCAACTCAGGACTTGTTCTTACCTTTCTTTTCCAATGTTACTTGGTTCCATGCTATACATG
etc ...
```

Pour plus de précision sur le format Fastq, lisez [la spécification du format](https://fr.wikipedia.org/wiki/FASTQ).
    

### Alignement des reads sur le génome de Wuhan

L'alignement consiste à aligner les reads présents dans les fichiers Fastq (150 bases) sur un génome de référence du Sars-CoV-2 qui fait lui environ 30 000 bases.   
Nous devons d'abord télécharger ce génome de référence au doux nom de [NC_045512.2](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512). Il s'agit d'un fichier [Fasta](https://fr.wikipedia.org/wiki/FASTA_(format_de_fichier)) que vous pouvez récupérer depuis [le site](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512) ou via la commande suivante :

    wget -O wuhan.fasta https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&log$=seqview&db=nuccore&report=fasta&id=1798174254&extrafeat=null&conwithfeat=on&hide-cdd=on

Avant de procéder à l'alignement avec l'outil [bwa](http://bio-bwa.sourceforge.net/), il est nécessaire d'indexer ce génome. On fera de même avec l'outil [samtools](http://www.htslib.org/) qui nous servira par la suite :

    bwa index wuhan.fasta
    samtools faidx wuhan.fasta

L'alignement est réalisé à l'aide de la commande ci-dessous qui nous créera un nouveau fichier *SRR13182925.sam* contenant les reads associés à leur position d'alignement sur le génome.

    bwa mem wuhan.fasta SRR13182925_1.fastq.gz  SRR13182925_2.fastq.gz > SRR13182925.sam 

Ce fichier [SAM](https://samtools.github.io/hts-specs/SAMv1.pdf) est un fichier texte. On lui préfère sa version binaire, le [BAM](https://samtools.github.io/hts-specs/SAMv1.pdf) plus légère et indexable.
Faisant d'une pierre deux coups, je trie le fichier par position, le convertit au format BAM et l'indexe avec les commandes ci-dessous:

    samtools sort -O bam SRR13182925.sam > SRR13182925.bam
    samtools index SRR13182925.bam 


### Visualisation de l'alignement

Pour visualiser cet alignement, vous pouvez utiliser le logiciel **IGV** disponible à [cette adresse](http://software.broadinstitute.org/software/igv/). Une fois lancé, chargez d'abord le génome de Wuhan depuis le menu *Genomes > Load Genome From Server* en cherchant SARS-Cov-2. Puis chargez le fichier *SRR13182925.bam* précédemment créé via *File > Load From File*. 
Vous obtiendrez ainsi la vue suivante où j'ai zoomé sur le gène S pour visualiser une mutation.  

<div class="figure">     <img src="../images/covid_ngs/IGV.png" />      <div class="legend"> Visualisation des reads alignés sur le génome de référence avec le logiciel IGV. La flèche montre une mutation située sur le gène S visible sur l'ensemble des reads </div> </div>

### Appel des variants et annotation 
Vous pourriez parcourir l'alignement visuellement et chercher toutes les mutations. Mais il est préférable de procéder de façon automatique grâce à un [variant caller](https://www.researchgate.net/figure/Commonly-used-NGS-variant-calling-software-Download-information-for-these-software-is_tbl1_232077026). Pour cela j'utilise [freebayes](https://github.com/freebayes/freebayes), qui à partir du fichier BAM, crée un [fichier VCF](https://en.wikipedia.org/wiki/Variant_Call_Format) contenant l'ensemble des variants détectés. Avec [SnpSift](https://pcingola.github.io/SnpEff/), on garde uniquement les variants de bonne qualité avec un score superieur à 30 et on compresse avec [bgzip](http://www.htslib.org/doc/bgzip.html) le fichier pour pouvoir l'indexer avec [tabix](http://www.htslib.org/doc/tabix.html).

```bash
freebayes -f wuhan.fasta -p1 -C10 SRR13182925.bam|SnpSift filter "QUAL > 30" - > SRR13182925.vcf 
bgzip SRR13182925.vcf
tabix -p vcf SRR13182925.vcf.gz
```
    
Le fichier VCF obtenu contient uniquement les positions et les bases mutées. Pour avoir plus d'information, j'annote ce fichier avec [SnpEff](https://pcingola.github.io/SnpEff/) qui me donnera entre autres le nom de la mutation en [nomenclature HGVS](https://varnomen.hgvs.org/) ainsi que le gène où il se situe.

    snpEff -Xmx10G -v NC_045512.2 SRR13182925.vcf.gz > SRR13182925.ann.vcf

Il me suffit maintenant d'extraire de ce fichier les informations pertinantes. Pour cela, j'utilise [SnpSift filter](https://pcingola.github.io/SnpEff/ss_filter/) associé à [SnpSift extracFields](https://pcingola.github.io/SnpEff/ss_extractfields/) pour afficher les mutations dans un tableau à deux colonnes avec le nom de la mutation et le nom du gène ou elle se situe.

    SnpSift filter "(exists ANN[0].HGVS_P)" > SRR13182925.ann.vcf
    |SnpSift extractFields - "ANN[0].HGVS_P" "ANN[0].GENE"

    ANN[0].HGVS_P   ANN[0].GENE
    p.Phe924Phe     ORF1ab
    p.Thr1665Thr    ORF1ab
    p.Pro4715Leu    ORF1ab
    p.Thr95Asn      S
    p.Asp614Gly     S
    p.Ser68Phe      E
    p.Asp72Asp      E
 
Vous pouvez également ouvrir le fichier *SRR13182925.ann.vcf* via l'interface graphique de [Cutevariant](https://github.com/labsquare/cutevariant). C'est un logiciel de mon cru en version bêta! Donc, soyez indulgent. 

### Création du génome consensus 

Pour reconstruire la séquence du génome de l'échantillon à partir du fichier VCF, nous pouvons utiliser [bcftools](http://samtools.github.io/bcftools/bcftools.html) qui nous génère un fichier Fasta: 

```bash
bcftools consensus SRR13182910.vcf.gz  -f genome/whuan.fasta --sample unknown > SRR13182910.fa
```
Nous pouvons alors utiliser l'outil [pangolin](https://github.com/cov-lineages/pangolin) pour asigner le nom de la ligné à ce génome. La nomenclature est défini [dans ce papier](https://www.nature.com/articles/s41564-020-0770-5).

```
pangolin SRR13182910.fa 
```

Nous obtenons alors l'identifiant [B.1.1.119](https://cov-lineages.org/lineages/lineage_B.1.1.119.html) dont vous pouvez trouver la déscription [sur cette page](https://cov-lineages.org/lineages/lineage_B.1.1.119.html). Et comme nous pouvions s'y attendre, elle est trouvé en grande partie chez des nord-américains.


## Analyse des 245 génomes 
### Distribution des variants
J'ai d'abord téléchargés tous les fichiers Fastq du projet via la commande suivante :

```bash
enaGroupGet -f fastq PRJNA673096
```

Puis j'ai réalisé un pipeline avec [Snakemake](https://snakemake.readthedocs.io/en/stable/) [disponible ici](https://gist.github.com/dridk/c2a7c9c8a6232407bf0c45f4442e6fb6). Il reprend les mêmes étapes vues plus haut à la seule différence que l'ensemble des variants détectés est colligé dans un même fichier VCF.    
Après quelques heures de calcul, j'ai finalement obtenu ce fichier VCF qui m'a permis d'analyser la fréquence des variants le long du génome que j'ai reporté dans le graphique suivant.       
Au total, j'ai trouvé environ 630 variants répartis le long du génome dont 4 mutations particulièrement fréquentes.

<div class="figure">     <img src="../images/covid_ngs/lollipop.png" />      <div class="legend"> Repartition des variants trouvés parmi les 245 génomes avec leurs fréquences </div> </div>

Ces 4 mutations sont probablement la conséquence d'un processus de sélection.  
En googlant, je trouve [ce papier](https://www.biorxiv.org/content/10.1101/2020.05.12.092056v1) présentant les mutations Thr265Ile and Gln57His comme exclusif à la population Nord-Américaines. Ce qui colle bien avec l'origine de nos données.   
Le variant Pro4715Leu est également dominant et affecte [la polymérase RNA-dependent (RdRp)](https://fr.wikipedia.org/wiki/ARN_polym%C3%A9rase_ARN-d%C3%A9pendante) catalysant la réplication de l'ARN. Peut-être que cette mutation modifie la fidélité de la réplication impactant ainsi son taux de mutation et donc son [evolvabilité](https://fr.wikipedia.org/wiki/%C3%89volvabilit%C3%A9), c'est-à-dire sa capacité à évoluer.    
Plus intéressant, est le variant Asp614Gly situé sur le gène (S) de la [protéine Spike](https://fr.wikipedia.org/wiki/Glycoprot%C3%A9ine), là même ou se situe le variant anglais en permettant au virus de pénétrer plus facilement les cellules humaines. Cette mutation Asp614Gly serait apparue en Europe début 2020 et serait maintenant la forme majoritaire ([source](https://www.news-medical.net/news/20200925/22705/French.aspx)). 

### Distribution des lignées

J'ai également reconstruit chaque génome que j'ai assigné à sa ligné avec l'outil [pangolin](https://github.com/cov-lineages/pangolin). J'obtient la distribution suivant: 

<div class="figure">     <img src="../images/covid_ngs/lineage.png" />      <div class="legend"> Distribution des lignées de virus </div> </div>

Nous pouvons voir ici la présence de ligné [B.1.2](https://cov-lineages.org/lineages/lineage_B.1.2.html) en grand nombre. D'après [le site cov-lineages](https://cov-lineages.org/), elle est exclusivement Nord-américaine est descend de la ligné [B.1](https://cov-lineages.org/lineages/lineage_B.1.html) apparu précocement et que l'on trouve partout dans le monde.
Quand à la ligné [B.1.369](https://cov-lineages.org/lineages/lineage_B.1.369.html), elle a d'abord été vu en Océanie puis aux Etats-Unis à partir de Juin 2020.       
Bref, tout qui colle avec l'origine nord-américaine de mes données!  


## Conclusion 
Un très bon exercice rapide qui en intéressera certainement plus d'un. En tout cas, je me suis bien amusé ce week-end à apprendre un tas de chose interessante sur ce maudit virus.     
N'hésitez donc pas à reprendre mon pipeline si vous en avez besoin.
J'aimerai maintenant apprendre à reconstruire un arbre [phylogénétique](https://fr.wikipedia.org/wiki/Phylog%C3%A9nie) à la fois dans le temps et dans l'espace. Ce qu'ils ont fait sur le [site nextrain](https://nextstrain.org/ncov/europe?f_region=Europe), est vraiment trop stylé! Cela permet de tracer l'évolution de ce virus qui, on ne le rappellera jamais assez, est expliquée par la [théorie de l'évolution de Darwin](https://fr.wikipedia.org/wiki/Charles_Darwin).













