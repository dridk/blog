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

On peut alors programmer cette algorithme et l'executer sur des très longues séquences voir des génomes entiers. Et ça donne de très jolies images:

<div class="figure">
    <img src="../images/fractal_dna/CGR_exemple.png" /> 
    <div class="legend">réparation par recombinaison homologue</div>
</div>

pour comprendre ce graphique, garder à l'esprit qu'à chaque point correspond une partie de la séquence donnée. Par exemple il y a un point correspond au 4 premiers nucléotides et un autre point correspondant au 20 premiers nucléotides. Si vous reflechissez un peu, vous devinerez que toutes les sous séquences commençant par un A se trouve dans le quart inférieur gauche, celles commençant par un G dans le quart supérieur droite ainsi de suite ...  Mais nous pouvons aller encore plus loin. Toutes les séquences commençant par CG, se trouve dans le quart supérieur gauche du quart droit. Toutes les séquences commençant par TAG, dans le quart inférieur droit, du quart inférieur gauche, du quart supérieur droit. Cette dichotomie illustré sur la figure ci-dessous, permet d'associé à chaque séquence une coordonnée unique !

<div class="figure">
    <img src="../images/fractal_dna/CGR_zoom.png" /> 
    <div class="legend">réparation par recombinaison homologue</div>
</div>



## Une méthode pour compresser l'ADN
A part être joli, à quoi ça sert ? Et bien plusieurs chose. Cette representation apporte une information globale (sur toutes la séquence) et une information locale (sur le contenu de la séquence). Par exemple, sur la figure suivante, vous pouvez voir un "trou" dans le quart G (supérieur droite). Ce motif se répète à plusieurs échelles ( dans les sous-quarts) et correspond à une dispersion des répétitions CG. (A vrai dire, j'ai encore du mal à intérpréter ce phénomène).  

<div class="figure">
    <img src="../images/fractal_dna/game7.png" /> 
    <div class="legend">réparation par recombinaison homologue</div>
</div>

On peut s'en servir aussi comme une signature. Ou encore pour visualiser des réarangement, des répétitions de séquence etc ...     
Mais le meilleur, je vous le garde pour la fin. Plus haut je vous ai dit que pour chaque séquence il y avait un unique point. On peut donc representer n'importe quel séquence par un couple de coordonnée x,y !!   
Bon, ça c'est le concepte. D'un point de vu informatique, on va vite être limité par la limite du nombre de chiffre après la virgule. Avec l'algorithme que nous venons de voir, nous pouvons compresser 32 nucléotides en un couple de nombre floatant x,y. C'est pas mal, mais il y a mieux. Un article récent montre qu'il est possible de compresser 1024 nucléotides dans un couple d'entier (x,y) en modifiant la méthode de calcul du graphique. Au lieu de calculer le milieu d'un segment, il calcul une somme somme entre les deux point avec une puissance de 2 dans l'équation.   
N'importe quel séquence de moins de 1024 nucléotides peut ainsi être écrit en utilisant 3 nombres : la longeur de la séquence, et les coordonnées x, y.    
On pourrait alors très bien imaginer un algorithme, qui découpe une très longues séquences d'ADN en bloc de 1024 nucléotides. 

    # Exemple d'une séquence de 3072 (1024*3) nucléotdes écrit sur une ligne
    (2334,12345)(49993,23322)(49993,23322)
    # Ohaaoooo!!!!!!!!!!!!!!

<div class="figure">
    <img src="../images/fractal_dna/amazing.gif" /> 
    <div class="legend">réparation par recombinaison homologue</div>
</div>


# Source  

 http://www.lifenscience.com/bioinformatics/chaos-game-representation

 Jeffrey in 1990 (Jeffrey, H. J. 1990). In his method of representing gene structure using Chaos gam

