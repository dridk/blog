Title: Euler et l'assemblage des génomes
Slug: assemblage_genome
Date: 2018-07-04 18:45:20
Modified: 2018-07-04 18:45:20
Tags: 
Category: 
Author: 
Lang: 
Summary: 
Status: Draft


Intro
Imaginez une pile de journaux identiques que vous faite sauté avec des pétards pour en faire une pluie de fragments contenant des portions de texte aléatoire. Comment feriez-vous, à partir de ces milliers de fragments, pour reconstruire un exemplaire complet du journal ? 
La même question se pose lorsque l'on désire reconstruire le génome d'un organisme à partir des milliards de courtes séquences générér par un séquenceur haut débit. Si vous pensez qu'il suffit de tester toutes les combinaisons en comparant les fragments deux à deux, sachez qu'avec l'ordinateur le plus puissant au monde, il faudrait plusieurs années pour reconstruire les 3 milliards de bases que constitue le génome humain.    
Nous allons donc voir dans ce billet, comment un mec du nom de Euler, en s'amusant à compter les ponts de sa ville, a décourt un algorithme permettant d'assembler efficacement des génomes.

# K-mer 
Les k-mers sont l'ensemble des mots de k lettres que l'on peut lire dans une séquence. Dans la suite de ce billet, nous chercherons à reconstruire la séquence S=**TAATGCCATGGGATGTT** à partir de l'ensemble des 3-mers qui la compose: 

    TAATGCCATGGGATGTT
    TAA
     AAT
      ATG
       TGC
        GCC
         CCA
          CAT
           ATG
            GGG
             GGA
              ATG
               TGT
                GTT

Imaginez donc n'avoir que cette liste de 3-mers:
TAA,AAT,ATG,TGC,GCC,CCA,CAT,GGG,GGA,TGT,GTT et essayons de trouver la séquence d'origine. Essayez tout seul déjà pour voir !  
Notez que le 3-mers ATG est lu 3 fois.     
Pour les chevronez de l'informatique, vous pouvez utiliser le programme jellyfish pour obtenir la liste des k-mers de n'importe quel séquence.


# Reconstruction à partir des k-mers
A partir de ces 3-mers, nous pouvons construire un graphe. C'est à dire un ensemble de noeuds relié par des arrêtes. 
2 façon de faire sont possible.

## Representer les k-mers par des noeuds 
Si nous representons chaque k-mer par un noeuds, alors deux noeuds consécutif dans la séquence partage le même suffix et prefix.
Par exemple le k-mer T**GC** précède le k-mer **GC**C car le suffix du premier correspond au prefix du second. Ce lien s'écrit comme cela:  

<div class="figure">
<img src="../images/assemblage/hamilton_node.png" />
<div class="legend"> Chemin dans un graphe </div>
</div>

En reprenant tous nos k-mers, nous pouvons alors construire un graphe en liant les noeuds par leurs suffix et leurs prefix. 

 <div class="figure">
<img src="../images/assemblage/hamilton_graphe.png" />
<div class="legend"> Chemin dans un graphe </div>
</div>

Dans ce graphe, il y a un chemin qui permet de retrouver votre séquence. Il s'agit de celui passant par tous les noeuds exactement une fois. C'est ce qu'on appelle un chemin Hamiltonien. 

## Representer les k-mers par des arrêtes 
Nous allons cette fois representer les k-mers par des arrêtes. Cette representation peut paraitre contre intuitive, mais elle va s'averer par la suite d'une extreme importance. 

<div class="figure">
<img src="../images/assemblage/euler_node.png" />
<div class="legend"> Chemin dans un graphe </div>
</div>

On obtient alors un nouveau graphe. Et cette fois, le chemin permettant de retrouver la séquence est celui passant par toutes les arretes exactement une fois. C'est ce qu'on appelle le chemin Eulerien.

## Euler ou Hamilton ? 
A vu de nez, vous pouvez penser que les deux méthodes se valle car dans les deux cas, le chemin est facile à trouver. Avec des vrai de données de séquençage, le graphe sera beaucoup plus complexe et il faudra alors un algorithme informatique pour pouvoir trouver les chemins.   
C'est ce qui fait toute la différence entre les deux méthodes.
- Le parcours Hamiltion n'a pas de solution algorithmique (NP-complet)
- Le parcours Eulerien a une solution algorithmique (temps linéaire)


### Le graphe de Debruijn

Reprenons notre graphe avec les arrêtes pour k-mers. Une méthode pour simplifier ce graphe est de fusionner les noeuds identiques. On obtient alors un multigraphe que l'on appelle le graphe de Debruijn. 
Essayons de retrouver notre séquence d'origine :  

# Les  ponts de Konigsberg 
Pour trouver un chemin passant une seul fois par toutes les arrêtes du graphe de Debruijn, nous allons faire un saut en 18... dans la ville de Konigsberg, ou un mathématicien Leonhard Euler a répondu à la question de savoir si il existait un chemin passant une seul fois par tout les ponts de sa ville. 
Il faut un cycle et des edge balanced.

Algo : 
- prendre une noeud au hasard
- parcourir 
- etc ... 


# Conclusion 
Vous savez maintenant reconstruire une séquence à partir de ces k-mers de manière optimale ! En essayant avec un du papier, y a ptetre moyen ! 


contigs, Scaffold, 
read pairé, 
logiciel exemples 



