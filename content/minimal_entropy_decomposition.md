Title: Décomposition par minimisation de l’entropie
Slug: minimal_entropy_decomposition
Date: 2015-04-06 16:25:55
Tags: algorithme
Category: bioinformatique
Author: Sacha Schutz
SIDEBARIMAGE:../images/post8/cover.jpg
Status:draft

Derrière ce titre se cache un algorithme qui permet de grouper des séquences par similarité. On utilise cet algorithme, entre autre, pour grouper les séquence d'ARN 16S issu du séquençage d'un microbiote et déterminer sa composition. 
Par exemple vous serez peut 

<center>
<b style="color:blue">CGTGTTATG </b><br/>
<b style="color:green">CGCGAAATG </b><br/>
<b style="color:blue">CGTGTTATG </b><br/>
<b style="color:green">CGTGAAATG </b><br/>
    </center>

Avec des reads plus long et en plus grand nombre, ce sera plus difficile de faire de visu. Mais l'algorithme est là pour nous aider.

## L'entropie de Shannon
L'entropie de Shannon est un indice correspondant la quantité d'information d'une séquence. Plus la séquence est aléatoire (non informative), plus la distribution des bases est homogène et plus l'entropie est grande. 
Par exemple la séquence B contient plus d'information que la séquence A.

    > sequenceA 
    ACGTACGTACGTACGTACGT  # Entropy = H = 2
    > sequenceB
    AAAAAAAAAAAAAAAAACGT  # Entropy = H = 0.84758
    
La fomule de l'entropie consiste à sommer les fréquences de chaques nucléotides en utilisant un logarithme. 

Equation : 

Pour la séquence A les fréquences des nucléotides sont : 
A : 0.25
C : 0.25
G : 0.25
T : 0.25

    
## Decomposition 
L'idée est simple. On va regarder l'alignment de nos séquences et calculer l'entropie pour chaque colonne. Celle ayant l'entropie la plus élevé est choisi pour discriminer les groupes (Toutes les séquences portant un T à gauche, avec un G à droite ). On recommence ainsi pour chaque nouveau groupe crée de façon itérative jusqu'à obtenir une entropie minimum pour chaque groupe.
on se retrouve au final avec plusieurs groupes contenant des séquences identiques.
Voila, c'etait simple non ? 



# references
http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2722627/
http://mylinuxbook.com/hexdump/,      