Title: Euler et l'assemblage des génomes
Slug: assemblage
Date: 2018-07-04 18:45:20
Modified: 2018-07-19 02:19:30
Tags: algorithme
Category: biologie
Author: Sacha Schutz
Status: Draft

Imaginez une pile de journaux identiques que vous faites sauté avec des pétards pour en faire une pluie de fragments de texte aléatoire. Comment feriez-vous, à partir de ces milliers de morceaux de papier, pour reconstruire un exemplaire complet du journal ? 
La même question se pose lorsque l'on désire reconstruire le génome d'un organisme à partir des milliards de courtes séquences générés par un [séquenceur haut débit](http://dridk.me/ngs.html). Si vous pensez qu'il suffit de tester toutes les combinaisons en comparant les fragments deux à deux, sachez qu'avec l'ordinateur le plus puissant au monde, il vous faudra plusieurs années pour reconstruire les 3 milliards de bases que constitue le génome humain.    
Nous allons donc voir dans ce billet, comment les programmes d'assemblage fonctionnent et comment un type du nom d'Euler, en s'amusant à compter les ponts de la ville de Königsberg, nous a permis aujourd'hui d'assembler efficacement un génome.

# Les *k*-mers 
Les [*k*-mers](https://en.wikipedia.org/wiki/K-mer) sont l'ensemble des mots de k lettres que l'on peut lire dans une séquence. Par exemple, la séquence suivante **TAATGCCATGGGATGT** peut se décomposer (avec des pétards ou non) en 14 mots de 3 lettres appelés 3-mers:

    TAATGCCATGGGATGT
    TAA
     AAT
      ATG
       TGC
        GCC
         CCA
          CAT
           ATG
            TGG
             GGG
              GGA
               GAT
                ATG
                 TGT
                  

Ce que nous allons tenter dans la suite de ce billet, c'est de reconstruire la séquence d'origine à partir de l'ensemble de ces 3-mers.    
Notez dans cette liste, que le mot **ATG** est présent 3 fois. Il s'agit de l'abondance du k-mer.    
Pour reconstruire notre séquence, nous aurons donc besoin d'une liste de k-mers associés à leurs abondances respectives. 

    AAT     1 fois
    ATG     3 fois
    CAT     1 fois
    CCA     1 fois
    GAT     1 fois 
    GCC     1 fois 
    GGA     1 fois 
    GGG     1 fois 
    TAA     1 fois
    TGC     1 fois
    TGG     1 fois
    TGT     1 fois 

# Construction d'un graphe
À partir de cette liste de 3-mers, nous allons construire un [graphe](https://www.youtube.com/watch?v=YYv2R1cCTa0) dirigé. C'est-à-dire un ensemble de nœuds reliés par des flèches. Pour cela deux méthodes s'offrent à nous.

## Les k-mers sont des nœuds 
Si nous représentons chaque k-mer par un nœud, alors deux nœuds consécutifs dans la séquence partagent le même suffixe et préfixe.
Par exemple le k-mer T**GC** précède le k-mer **GC**C car le suffixe du premier (xGC) correspond au préfixe du second (GCx). Cette relation se représente avec deux nœuds et une flèche:

<div class="figure">
<img src="../images/assemblage/hamilton_node.png" />
<div class="legend"> Lien entre deux k-mers dans un graphe. Le suffixe (k-1) du premier correspond au préfixe (k-1) du second</div>
</div>

En reprenant tous nos k-mers, nous pouvons alors construire un graphe en reliant tous les nœuds via leurs suffixes et leurs préfixes. On obtient alors ce graphe:

 <div class="figure">
<img src="../images/assemblage/hamilton_graphe.png" />
<div class="legend"> Graphe représentant chaque k-mer par un noeud.</div>
</div>

Pour reconstruire la séquence d'origine, il faut trouver un chemin passant par tous les nœuds une fois et une seul. C'est ce qu'on appelle un [parcours Hamiltonien](https://fr.wikipedia.org/wiki/Graphe_hamiltonien). Vous pouvez vous amuser à le chercher vous-même ou en regarder l'animation ci-dessous:

 <div class="figure">
<img src="../images/assemblage/hamilton_graphe_path.gif" />
<div class="legend"> Chemin dans un graphe </div>
</div>

Cette méthode est simple à comprendre. Mais il y a un hic. La recherche du parcours Hamiltonien est un problème mathématique dit [NP-complet](https://fr.wikipedia.org/wiki/Probl%C3%A8me_NP-complet). Pour faire simple, il n'existe pas d'algorithme rapide pour trouver ce chemin. Pour un graphe plus complexe, tel que celui utilisé pour reconstruire la séquence d'un génome, il faudrait énormément de temps de calcul, même avec les plus super des super calculateurs.    
Il nous faut une autre méthode ...

## Les k-mers sont des flèches  
Nous allons cette fois construire un graphe en représentant les k-mers par des flèches. Les nœuds contiendront le préfixe et le suffixe du k-mer. Par exemple si une flèches représente le k-mer TGC alors les deux nœuds de autour de la flèche sont TG et GC.

<div class="figure">
<img src="../images/assemblage/euler_node.png" />
<div class="legend"> Représentation d'un k-mer par une flèches. Les nœuds contiennent les suffixe et préfixe des k-mers</div>
</div>

En utilisant tous nos k-mers vu précédemment, on peut alors construire le graphe suivant:

<div class="figure">
<img src="../images/assemblage/not_fusion_graphe.png" />
<div class="legend">  Graphe représentant chaque k-mer par une flèches.</div>
</div>

Cette fois au lieu de chercher un chemin passant par tous les nœuds une seule fois, nous allons chercher un chemin passant par toutes les flèches une fois et une seul. Si vous essayer sur le graphe ci-dessus, vous verrez tout de suite qu'il y a un problème et qu'un tel chemin n'existe pas. Nous allons donc devoir modifier ce graphe.     
Vu que rien ne nous empêche de passer plusieurs fois par le même nœud, nous pouvons fusionner les nœuds identiques. 
Sur le graphe, ce sont les 3 nœuds violets AT, les 3 nœuds rouges TG et les 2 noeuds vert GG que nous pouvons fusionné. 
En faisant cette transformation, vous obtenez ce qu'on appelle [Graphe de de Bruijn](https://fr.wikipedia.org/wiki/Graphe_de_de_Bruijn).

 <div class="figure">
<img src="../images/assemblage/debruijn_graphe.png" />
<div class="legend"> Graphe de de Bruijn </div>
</div>

Cette fois, vous pouvez vous amuser à chercher le chemin passant par toutes les flèches une fois et une seul. C'est ce qu'on appelle un parcours [Eulérien](https://fr.wikipedia.org/wiki/Graphe_eul%C3%A9rien) que vous pouvez visualiser sur l'animation suivante:

 <div class="figure">
<img src="../images/assemblage/euler_path.gif" />
<div class="legend"> Chemin dans un graphe </div>
</div>

Cette méthode est plus complexe à mettre en place. Mais contrairement au parcours Hamiltonien, le parcours Eulérien, si il existe, peut être trouvé rapidement par un algorithme informatique. Et on le doit à [Leonhard Euler](https://fr.wikipedia.org/wiki/Leonhard_Euler) et la ville de [Königsberg](https://fr.wikipedia.org/wiki/K%C3%B6nigsberg).

# Les  ponts de Konigsberg 
En 1873, un mathématicien du nom de Leonhard Euler s'est posé la question de savoir si il existait une promenade dans la ville de Königsberg passant par tous les ponts une seule fois et une seul.

 <div class="figure">
<img src="../images/assemblage/Konigsberg_bridges.png" />
<div class="legend"> Gauche: Pont de Königsberg Droite: représentation des ponts par un graphe. Existe-t-il un chemin passant par tous les ponts ? </div>
</div>

En résumé, Euler démontre qu'un parcours Eulerien existe dans un graphe si et seulement chaque nœud est relié à un nombre pair d'arêtes. En effet, si l'on veut entrer dans un nœud par 1 arête, il faut forcément ressortir par 1 autre arêtes. Dans le cas des ponts de Königsberg, un tel chemin n'existe pas, car le nombre d'arrêtés par nœud est respectivement de 5,3,3,3 (voir graphique). 
Dans un graphe dirigé, lorsque les arrêtes sont des flèches, un chemin Eulerien existe si le nombre de flèches à l'entrée d'un nœud et le même qu'à la sortie.   
Voyons si cela s'applique à notre graphe de de Bruijn en faisant une petite modification:

 <div class="figure">
<img src="../images/assemblage/euler_cycle.png"/>
<div class="legend"> Graphe de de Bruijn modifié pour pouvoir avoir un cycle de Euler. En rouge le nombre de flèches à l'entré d'un nœud, en vert le nombre de flèches à la sortie d'un nœud. Le [degré](https://fr.wikipedia.org/wiki/Degr%C3%A9_(th%C3%A9orie_des_graphes)) d'entré et de sortie pour chaque nœud sont identique. D'après le théorème, il existe donc un chemin Eulérien passant par toutes les flèches une fois et une seul </div>
</div>

# L'algorithme de Euler
Euler propose une algorithme pour pouvoir trouver le chemin Eulérien de façon rapide. 

-  Prendre un noeud V1 au hasard
-  Parcourir le graphe au hasard jusqu'à retomber sur V1
-  Si vous n'avez pas visité tous les nœuds et que vous êtes bloqué
    +  Choisissez un nouveau nœud V2 voisin de V1
    +  Parcourir le même chemin que précédemment jusqu'à retomber sur V2
    +  Et ainsi de suite ....

Plus sérieusement, si vous voulez comprendre cet algorithme, je vous conseille très très fortement de voir cette courte vidéo sur la chaîne YouTube "[ À la découverte des graphes](https://www.youtube.com/channel/UCHtJVeNLyR1yuJ1_xCK1WRg)". Personnellement, c'est la meilleure chaîne de vulgarisations sur ce sujet. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/DH0Hxes2nOo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


En résumé, pour reconstruire une séquence à partir de ses k-mers, nous pouvons chercher un parcours Hamiltonien dans un graphe.  Celui-ci est simple à comprendre, mais n'a pas d'algorithme efficace. En revanche, le parcours Eulérien dans un graphe de de Bruijn a une solution algorithmique efficace, et c'est cette méthode qui est utilisée par la majorité des assembleurs. 


# Conclusion 
Dans ce billet, j'ai voulu être le plus pédagogique possible en simplifiant à l'extrême. Pour cela, je me suis inspiré grandement du livre [Bioinformatics algoritmics](https://www.amazon.fr/Bioinformatics-Algorithms-Active-Learning-Approach/dp/0990374602) que je vous conseille.    
Dans la réalité, la reconstruction d'un génome est plus complexe. En effet il existe plusieurs chemins eulérien dans un graphe, on ne sais pas lequel choisir. 
Il y a ensuite une second étape d'assemblage en utilisant les notions des [contigs](https://fr.wikipedia.org/wiki/Contig)et des [scaffolds](https://en.wikipedia.org/wiki/Scaffolding_(bioinformatics)) ou encore le [gap filling](https://www.ncbi.nlm.nih.gov/pubmed/23095524).
Mais tout cela change déjà avec [les séquenceurs de 3e génération](http://www.biorigami.com/?tag=sequenceurs-3eme-generation) permettant le séquençage de long fragments avec un tas de nouveaux problèmes algorithmiques rendant ce billet déjà obsolète.  


## References 
- [BioinformaticsAlgorithms](http://bioinformaticsalgorithms.com/)
- [A la découverte des graphes](https://www.youtube.com/channel/UCHtJVeNLyR1yuJ1_xCK1WRg)
- [cours: Assemblage de nobo](http://www.iro.umontreal.ca/~csuros/IFT6299/H2014/content/prez13-assembly.pdf)
- Reference assembleur ==> Demander à NATIR 

## Remerciements
Merci à [@Natir](https://twitter.com/natir_chan?lang=fr) pour la relecture
