Title: Répartition des variants entre J.Watson et C.Venter
Slug: localisation_snp
Date: 2016-08-02 21:42:51
Category: informatique
Tags: bioinformatique, génétique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

Nous avions vu dans un [précédent post](http://dridk.me/genome_chiffre_1.html) que le génome de [James Watson](https://fr.wikipedia.org/wiki/James_Dewey_Watson) comptait un peu plus de 2 millions de variants par rapport au génome de référence. Et qu'environ la moitié de ces variants étaient partagés avec [Craig Venter](https://fr.wikipedia.org/wiki/Craig_Venter).   
Aujourd'hui, j'ai cherché à savoir si la densité des mutations à travers leurs génomes étaient semblables. Pour cela, j'ai fragmenté le génome en intervalles réguliers que j'appelle *bins*. Et pour chaque *bin*, j'ai compté le nombre de variants chez Watson puis chez Venter qui tombaient dedans. J'ai alors calculé la différence entre Watson et Venter pour chaque *bin* à l'aide d'un z-score.  
Et voila les résultats! 

## Pipeline 
J'ai tout codé dans un pipeline disponible sur [github](https://github.com/dridk/snp_location).    
Vous aurez besoin de [Snakemake](https://bitbucket.org/johanneskoester/snakemake/wiki/Home), de [bedtools](http://bedtools.readthedocs.io/en/latest/) et du package R [IdeoViz](https://www.bioconductor.org/packages/release/bioc/html/IdeoViz.html) disponible depuis le site [bioconductor](https://www.bioconductor.org/).   
Aucune donnée n'est nécessaire. Tous se téléchargent directement depuis le [golden path d'UCSC](http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/). Vous pouvez d’ailleurs, si vous le voulez, lancer le pipeline sur d'autres génomes.

## Exécution 
La commande que j'utilise est la suivante : 

    snakemake -F --core 4 --config bin_size=100000 first=pgVenter second=pgWatson

**bin_size** correspond à la taille des *bins*. **first** et **second** sont les noms des fichiers correspondant aux "*personal genom (pg)*" retrouvés dans [UCSC](http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/).   
L'option **F** sert à régénérer l'ensemble des fichiers dans le cas d'une seconde exécution. Et l'option **core** spécifie le nombre de cœurs à utiliser.   
Le schéma suivant représente les différentes étapes du pipeline.    

<div class="figure">
    <img src="../images/post19/pipeline.png" />
    <div class="legend">Graph du pipeline snakemake</div>
</div>

## Résultats
Si tout se passe bien vous devriez obtenir 3 images : *correlation.png* , *both.png* et *ideogram.png*  que vous pouvez voir ci-dessous . 

<div class="figure">
    <img src="../images/post19/correlation.png" />
    <div class="legend">corrélation du nombre de SNP par bin entre Watson et Venter avec des bins de 1 Mpb </div>
</div>

Sur le graphique *correlation.png* est représenté le nombre de SNP par *bin* entre Watson et Venter en utilisant des *bins* d' 1 million de paires de bases.  
La corrélation est nette. Les régions riches en SNP chez Watson le sont également chez Venter. 

<div class="figure">
    <img src="../images/post19/both.png" />
    <div class="legend">Densité en variants par bin pour Watson (orange) et Venter (bleue)</div>
</div>

Le graphique *both.png* montre la densité des variants par *bin* pour Watson (orange) et Venter (bleue). 
Les tendances générales des courbes semblent similaire.  

<div class="figure">
    <img src="../images/post19/ideogram.png" />
    <div class="legend">Différence des SNPs par bin entre Watson et Venter sur tout le génome.</div>
</div>

Le graphique *ideogram.png* montre les différences du nombre de SNP par *bin* entre Watson et Venter sur tout le génome. La différence est ici normalisée  par un z-score. En zoomant, vous pouvez voir que les différences sont rarement significatives en restant inférieures à 2. En revanche, certaines régions notamment sur le bras long du chromosome X (avant dernier), montrent de grandes différences. 


## Conclusion 
Les régions riches en mutations chez Watson le sont aussi chez Venter en utilisant des *bins* d'1 Mpb. Ceci peut s'expliquer par le contenu de la séquence. Il est possible que certaines régions soient plus susceptibles de muter à cause de leurs teneurs en non-codants, en zones répétées ou en autres choses. Il faudrait d'ailleurs que je regarde si il y a une corrélation avec la teneur en exons, en GC...    
Quant à la distribution sur le génome, elle fluctue de la même façon chez Watson et Venter. On retrouve cependant quelques différences dans des zones précises. Peut être des CNV...   
Bref, prochain objectif, comparer ces courbes avec des données d'annotation style 1000génomes et SNP ! 


