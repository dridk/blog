Title: Densité des variants entre J.Watson et C.Venter
Slug: localisation_snp
Date: 2016-08-02 21:42:51
Category: informatique
Tags: bioinformatique, génétique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

Nous avions vu dans un [précédent post](http://dridk.me/genome_chiffre_1.html) que le génome de [James Watson](https://fr.wikipedia.org/wiki/James_Dewey_Watson) comptait un peu plus de 2 millions de variants par rapport au génome de référence. Et qu'environs la moitié de ces variants étaient partagés avec [Craig Venter](https://fr.wikipedia.org/wiki/Craig_Venter).   
Aujourd'hui, j'ai cherché à savoir si la densité en mutation à travers leurs génomes étaient semblables. Pour cela, j'ai fragmenté le génome en intervals réguliers que j'appelle *bins*. Et pour chaque *bin*, j'ai compté le nombre de variants chez Watson puis chez Venter qui tombait dedans. J'ai alors calculé la différence entre Watson et Venter pour chaque bin à l'aide d'un z-score.  
Et voila les résultats! 

## Pipeline 
J'ai tous codé dans un pipeline disponible sur [github](https://github.com/dridk/snp_location).    
Vous aurez besoin de [Snakemake](https://bitbucket.org/johanneskoester/snakemake/wiki/Home), de [bedtools](http://bedtools.readthedocs.io/en/latest/) et du package R [IdeoViz](https://www.bioconductor.org/packages/release/bioc/html/IdeoViz.html) disponible depuis [bioconductor](https://www.bioconductor.org/).   
Aucunes données n'est nécessaire. Tout se téléchargent directement depuis le [golden path d'UCSC](http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/). Vous pouvez d’ailleurs, si vous le voulez, lancer le pipeline avec d'autre génome.  

## Exécution 
La commande que j'utilise est la suivante : 

    snakemake -F --core 4 --config bin_size=100000 first=pgVenter second=pgWatson

**bin_size** correspond à la taille des bins. **first** et **second** sont les noms des fichiers correspondant aux "*personal genom (pg)*" retrouvés dans [UCSC](http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/).   
L'option **F** sert à régénérer l'ensemble des fichiers dans le cas d'une deuxième exécution. Et l'option **core** spécifie le nombre de cœurs à utiliser.   
Le schéma suivant représente les différentes étapes du pipeline.    

<div class="figure">
    <img src="../images/post19/pipeline.png" />
    <div class="legend">Graph du pipeline snakemake</div>
</div>

## Résultats
Si tout se passe bien vous devez obtenir 2 images : *correlation.png* , *both.png* et *ideogram.png*  que vous pouvez voir ci-dessous . 

<div class="figure">
    <img src="../images/post19/correlation.png" />
    <div class="legend">corrélation du nombre de snp par bin entre Watson et Venter avec des bins de 1000000 pb </div>
</div>

Sur le graphique *correlation.png* est représenté le nombre de snp par bin entre Watson et Venter en utilisant des bins d' 1 millions de paire de bases.  
La corrélation est net. Les régions riches en snp chez Watson le sont aussi chez Venter. 

<div class="figure">
    <img src="../images/post19/both.png" />
    <div class="legend">Densité en variant par bin pour Watson (orange) et Venter (bleue)</div>
</div>

Le graphique *both.png* montre la densité des variants par bin pour Watson (orange) et Venter (bleue). 
Les courbes sont très similaire. 

<div class="figure">
    <img src="../images/post19/ideogram.png" />
    <div class="legend">Différence des snps par bin entre Watson et Venter sur tous le génome.</div>
</div>

Le graphique *ideogram.png* montre les différences du nombre de snp par bin entre Watson et Venter sur tous le génome. La différence est normalisé et il s'agit ici d'un z-score. En zoomant, vous pouvez voir que les différences sont rarement significative en restant inférieur à 2. Par contre certaines régions, notamment sur le bras long du chromosome X (avant dernier), montre de grandes différences. 


## Conclusion 
Les régions riches en mutation chez Watson le sont aussi chez Venter en utilisant des bins d'1 million. Ceci peut s'expliquer par le contenu de la séquence. Peut être que certaines régions sont plus susceptible à muter à cause de leurs teneurs en non-codant, en zones répétées ou en autres choses. Il faudrait que je regarde si il y a une corrélation avec la teneur en exon, en GC...    
Quand à la distribution sur le génome, elle fluctue de la même façon chez Watson et Venter. On retrouve cependant quelques différences dans des zones précises. Peut être des CNV...   
Bref, prochaine objectif, comparer ces courbes avec des données d'annotation style 1000génomes et SNP ! 


