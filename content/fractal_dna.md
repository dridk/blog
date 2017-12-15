Title: Fractal et ADN
Slug: des-fractales-dans-ladn
Date: 2017-12-15 10:25:26
Tags: algorithme
Category: biologie, informatique
Author: Sacha schutz
Status: Draft


Vous connaissez le jeux du chaos? Il s'agit d'une construction géométrique très simple permettant de faire apparaitre des fractales. La construction la plus connu est le triangle de Sierpinski que vous pouvez dessiner vous même avec un papier et un crayon:   

- Dessiner un triangle en numérotant les trois sommets A,B,C. 
- Puis dessiner dedans un point P choisi au hasard . 
- Tirer alors un nombre aléatoire correspondant à A,B ou C. 
- Si par exemple vous tirez le A, dessiner le point correspondant au milieu du segment [PA].
- Ce nouveau point appelez le P, puis répéter la procédure de façon itérative en partant du nouveau point. 

Si tout se passe bien, vous devrez voir apparaitre le triangle de Sierpinski. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/IGlGvSXkRGI" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>

## Le jeux du chaos appliqué à l'ADN  
Au lieu d'utiliser un dé, nous pouvons utiliser une séquence d'ADN pour choisir les sommets. Et au lieu d'un triangle, ce sera un carré ou chaque sommet correspond aux nucléotide A,C,G,T. Pour chaque base lu dans la séquence, dessiner le point correspodant au centre du segment [P-base] puis continuer jusqu'à la dernière base. 

<div class="figure">
    <img src="../images/fractal_dna/CGR_DNA.png" /> 
    <div class="legend">réparation par recombinaison homologue</div>
</div>

On peut alors programmer cette algorithme et l'executer sur des très longues séquences voir des génomes entiers. Et ça donne de très jolies images.  

<div class="figure">
    <img src="../images/fractal_dna/CGR_exemple.png" /> 
    <div class="legend">réparation par recombinaison homologue</div>
</div>

## Quelles informations en dégager ? 
Plusieurs, mais la plus plus importante 

 Jeffrey in 1990 (Jeffrey, H. J. 1990). In his method of representing gene structure using Chaos gam

 http://www.lifenscience.com/bioinformatics/chaos-game-representation

## Un algorithme de compression de l'ADN 
Compression 