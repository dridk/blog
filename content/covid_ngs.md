Title: Analyse de genomes de SARS-CoV-2
Slug: covid_ngs
Date: 2020-09-20 18:34:56
Modified: 2020-09-20 18:34:56
Tags: statistique,machine learning,python
Category: informatique
Author: Sacha SCHUTZ
Status: Draft
SIDEBARIMAGE:../images/common/stat_banner.jpg


La [pandémie mondiale de Covid-19](https://fr.wikipedia.org/wiki/Pand%C3%A9mie_de_Covid-19) a créé un elan sans précédent dans la production scientifique de données. Avec notamment des séquences complète de génomes viraux produient par [séquençage haut débit](https://fr.wikipedia.org/wiki/S%C3%A9quen%C3%A7age_de_l%27ADN#S%C3%A9quen%C3%A7age_haut_d%C3%A9bit_(HTS)) qui permet aujourd'hui d'identifier des nouvelles mutations comme la N501Y dy variant anglais [VOC-202012/01](https://fr.wikipedia.org/wiki/VOC-202012/01) ou une Asparagine (N) est remplacé par une Tyrosine (Y) au niveau du codon 501 du gène S.     
Le génome du SARS-CoV-2 étant tout  petit ( 30kb ) par rapport à celui d'un humain ( 3Gb ), l'analyse bioinformatique est tout à fait réalisable sur un ordinateur personel. C'est donc un très bon exercice pour se familiariser avec les outils d'alignment et de detection de variants.  
Dans ce billet, je vous propose de voir pas à pas, comment réaliser l'analyse d'un génome de SARS-CoV-2 à partir des données brutes généré par un séquenceur [Illumina](https://fr.wikipedia.org/wiki/Illumina). Pour cela j'ai récupéré les données de séquençage de 245 échantillons provenant d'un laboratoire de l'état de [Delaware](https://fr.wikipedia.org/wiki/Delaware) aux États-Unis. . Plus précisement une paire de fichier [Fastq](https://fr.wikipedia.org/wiki/FASTQ) par échantillon contenant les courtes séquences, appelé *reads*, lu par le séquenceur. je les ai ensuite tous aligné sur [le génome de réference de Whuan](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512) pour en extraire les mutations que j'ai annoté.      
Pour réaliser cette analyse, il faut faudra de préférence un terminal [Linux](https://fr.wikipedia.org/wiki/Linux) avec différents outils que vous pouvez installer par exemple avec [conda](https://docs.conda.io/en/latest/miniconda.html). Sinon, j'ai mis à disposition un [notebook sur google-collab](https://colab.research.google.com/drive/1V8EsdFyCmr7fmVkVf09JQhraatTWcd3f).

## Source des données 

Je connais 2 sources principales pour récupérer des données de séquençage. [SRA du NCBI](https://www.ncbi.nlm.nih.gov/sra) et la base européenne [ENA](https://www.ebi.ac.uk/ena/browser/home). J'ai choisi ce dernier par convenance.
En fouillant, j'ai d'abord découvert le projet [ICOG UK](https://www.cogconsortium.uk), constamment mis à jour et disposant de pas moins de 206 000 génome viraux à l'heure ou j'écris ce billet.   
Mais pour mon petit PC de bureau, c'est un peu trop. On se contentera pour l'exemple, des 245 génomes viraux du project [PRJNA673096](https://www.ebi.ac.uk/ena/browser/view/PRJNA673096) produit par le [Delaware Public Health Lab](https://www.dhss.delaware.gov/dhss/dph/lab/labs.html) aux Etats-Unis. Il s'agit de données produites sur un [Illumina MiSeq](https://emea.illumina.com/systems/sequencing-platforms/miseq.html) en Amplicon WGS.

### Téléchargement des données avec EnaBrowserTools

Nous pouvons télécharger les fichiers Fastq directement depuis le site de l'ENA. Mais il existe un outil en ligne de commande, [enaBrowserTools](https://github.com/enasequence/enaBrowserTools), fonctionnant avec python qui va nous faciliter la tâche.    

- **enaDataGet** nous permet de télécharger les données associes à un échantillon. 

- **enaGroupGet** nous permet de télécharger l'ensemble des échantillons d'un projet. 

Pour l'installer, on suit la [documentation](https://github.com/enasequence/enaBrowserTools/blob/master/README.md): 

```bash
git clone git@github.com:enasequence/enaBrowserTools.git
alias enaDataGet=$(pwd)/enaBrowserTools/python3/enaDataGet
alias enaGroupGet=$(pwd)/enaBrowserTools/python3/enaGroupGet
```

Pour la suite de ce billet, nous nous contenterons d'analyser uniquement l'échantillon [SRR13182925](https://www.ebi.ac.uk/ena/browser/view/SRR13182925). Pour télécharger les fichiers Fastq associés, tapper la commande suivante:

```bash
enaDataGet -f fastq SRR13182925    
```

Vous devriez alors obtenir un dossier **SRR13182925** contenant 2 fichiers fastq : 

- *SRR13182925_1.fastq.gz* 
- *SRR13182925_2.fastq.gz*

Ces fichiers contiennent des courtes séquences lus, appelé **reads**, d'environ 150 bases provenant du génome virale trouvé dans l'échantillon. Ces reads sont lu dans les deux sens par le séquenceur. Pour cette raison, il y a 2 fichiers, un pour chaque sens de lecture.    
Vous pouvez jeter un oeil à ces reads l'aide la commande suivante: 

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

Pour plus de précision sur le format Fastq, allez lire de [la documentation](https://fr.wikipedia.org/wiki/FASTQ).
    

### Alignement des reads sur le génome de Wuhan

L'alignement consiste à aligner les reads présents dans les fichiers fastq (150 bases) sur un génome de référence du Sars-CoV-2 qui fait lui environ 30 000 bases.   
Nous devons d'abord télécharger ce génome de réference au doux nom de [NC_045512.2](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512). Il s'agit d'un fichier [Fasta](https://fr.wikipedia.org/wiki/FASTA_(format_de_fichier)) que vous pouvez récupérer depuis le site ou via la commande suivate:

    wget -O wuhan.fasta https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&log$=seqview&db=nuccore&report=fasta&id=1798174254&extrafeat=null&conwithfeat=on&hide-cdd=on

Avant de procédér à l'alignement avec l'outil [bwa](http://bio-bwa.sourceforge.net/), il est nécessaire d'indexer ce génome. On fera de même avec samtools qui nous servira par la suite:

    bwa index wuhan.fasta
    samtools faidx wuhan.fasta

L'allignement est réalisé à l'aide de la commande suivante. Celle-ci nous produit un nouveau fichier *align.sam* contenant les reads associés à leurs position d'alignement sur le génome.

    bwa mem wuhan.fasta SRR13182925_1.fastq.gz  SRR13182925_2.fastq.gz > align.sam 

Ce fichier [SAM](https://samtools.github.io/hts-specs/SAMv1.pdf) est un fichier texte. On lui préfère sa version binaire, le [BAM](https://samtools.github.io/hts-specs/SAMv1.pdf) plus légère et indexable.
D'une pierre deux coups, je trie le fichier par position et le converti en BAM avec la commande suivante. Je l'index par la même occasion:

    samtools sort -O bam align.sam > align.bam
    samtools index align.bam 


## Visualisation de l'alignement

Pour visualiser cette alignement, vous pouvez utiliser le logiciel **IGV** disponnible à [cette adresse](http://software.broadinstitute.org/software/igv/). Une fois lancé, charger d'abord le génome de whuan depuis le menu *Genomes > Load Genome From Server* en cherchant SARS-Cov-2. Puis charger le fichier *align.bam* précement produit via *File > Load From File*. 
Vous devriez pouvoir obtenir la vue suivante ou j'ai zoomé sur le gène S pour visualiser une mutation.  

<div class="figure">     <img src="../images/covid_ngs/IGV.png" />      <div class="legend"> Vous ne pouvez recevoir qu'une réponse par oui ou par non. Utiliser votre carnet pour poser le minimum de question </div> </div>

## Appel des variants et annotation 
Vous pouvez très bien parcourir l'alignement visuellement et chercher toutes les mutations. Mais il est préférable de faire ça automatique grâce à un "variant caller". Pour cela j'utilise [freebayes](https://github.com/freebayes/freebayes), qui à partir du fichier BAM, mee produit un fichier VCF contenant l'ensemble des variants détéctés.

    freebayes -f wuhan.fasta -p1 -C10 align.bam > variant.vcf 

L'argument "p" signifie que l'on est sur un génome haploïde et l'argument "C" fixe le nombre de read minimum nécessaire pour détécter une mutation.    

Le fichier VCF obtenu contient uniquement les positions et les bases mutés. Pour avoir plus d'information, j'annote ce fichier avec [SnpEff](https://pcingola.github.io/SnpEff/) qui me donnera entre autre le nom de la mutation en [nomenclature HGVS](https://varnomen.hgvs.org/) ainsi que le gène ou il se situe.

    snpEff -Xmx10G -v NC_045512.2 variant.vcf > variant.ann.vcf

Il me suffit maintenant de filtrer dans ce fichier, tous les variants ayant une bonne qualité de séquençage affectant un des gènes du virus. Pour cela, j'utilise [SnpSift filter](https://pcingola.github.io/SnpEff/ss_filter/) associé à [SnpSift extracFields](https://pcingola.github.io/SnpEff/ss_extractfields/) pour afficher les mutations dans un tableau à deux colonnes avec le nom de la mutation et le nom du gène ou elle se situe.

    SnpSift filter "(QUAL > 100) & (exists ANN[0].HGVS_P)" SRR13182925.ann.vcf|SnpSift extractFields - "ANN[0].HGVS_P" "ANN[0].GENE"

    ANN[0].HGVS_P   ANN[0].GENE
    p.Phe924Phe     ORF1ab
    p.Thr1665Thr    ORF1ab
    p.Pro4715Leu    ORF1ab
    p.Thr95Asn      S
    p.Asp614Gly     S
    p.Ser68Phe      E
    p.Asp72Asp      E
 
Vous pouvez egallement ouvrir le fichier *variant.ann.vcf* via l'interface graphique de [Cutevariant](https://github.com/labsquare/cutevariant). C'est un logiciel de mon cru en version bêta! Donc soyez indulgent. 

## Analyse des 245 génomes 

Pour analyser l'ensemble des 245 génomes je les ai d'abord télécharger via la commande suivante:

```bash
enaGroupGet -f fastq PRJNA673096
```

Puis j'ai réalisé un pipeline avec [Snakemake](https://snakemake.readthedocs.io/en/stable/) [disponible ici](https://gist.github.com/dridk/c2a7c9c8a6232407bf0c45f4442e6fb6). Il reprant les même étapes vu plus haut à la seul difference que l'ensemble des variants détéctés est colligé dans un même fichier VCF.    
Après qque heure de calcul, j'ai finalement obtenu ce fichier VCF qui m'a permis d'analyser le nombre d'occurence des variants le long du génome que j'ai reporté dans le graphique suivant.       
Au total, j'ai trouvé environ 630 variants répartis le long du génome dont 4 mutations ayant une forte occurence parmi les 245 génomes.

<div class="figure">     <img src="../images/covid_ngs/lollipop.png" />      <div class="legend"> Repartition des variants trouvés parmis les 245 génomes avec leurs fréquences </div> </div>

## Résultats
On trouve ainsi 4 mutations qui sortent du lot, probablement la conséquence d'un processus de selection.      
En googlant, je trouve [ce papier](https://www.biorxiv.org/content/10.1101/2020.05.12.092056v1) présentant les mutations Thr265Ile and Gln57His comme exclusive à la population Nord américaine. Ce qui correspond bien à l'origine américaine de nos données.   
Le variant Pro4715Leu est égallement dominant et affecte [la polymérase RNA-dependent (RdRp)](https://fr.wikipedia.org/wiki/ARN_polym%C3%A9rase_ARN-d%C3%A9pendante) catalysant la réplication de l'ARN.
Plus interessant, est le variant Asp614Gly dans le gène (S) de la protéine Spike qui permet au virus de pénétrer plus facillement les cellules humaines. Ce dernier serait apparu en europe en Février 2020 et serait maintenant la forme majoritaire ([source](https://www.news-medical.net/news/20200925/22705/French.aspx)). 

## Conclusion 
Un très bon exercice rapide qui en interessera plus d'un! N'hesitez donc pas à reprendre mon pipeline si vous en avez besoin.
J'aimerai maintenant pour le fun, analyser l'ensemble des mutations décrites afin de construire un arbre philogénétique à la fois dans le temps et dans l'espace. Ca permettrait de voir l'évolution de ce virus, qu'on ne rappelera jamais assez, s'explique au regard de la théorie de Darwin.
















