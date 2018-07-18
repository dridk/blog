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

Imaginez une pile de journaux identiques que vous faite sauté avec des pétards pour en faire une pluie de fragments de texte aléatoire. Comment feriez-vous, à partir de ces milliers de morceaux de papier, pour reconstruire un exemplaire complet du journal ? 
La même question se pose lorsque l'on désire reconstruire le génome d'un organisme à partir des milliards de courtes séquences générér par un séquenceur haut débit qu'on appelle "reads". Si vous pensez qu'il suffit de tester toutes les combinaisons en comparant les fragments deux à deux, sachez qu'avec l'ordinateur le plus puissant au monde, il vous faudra plusieurs années pour reconstruire les 3 milliards de bases que constitue le génome humain.    
Nous allons donc voir dans ce billet, a travers un exemple, comment un mec du nom de Euler, en s'amusant à compter les ponts de sa ville, a décrit un algorithme très simple qui nous permet aujourd'hui d'assembler efficacement un génome.

# Les k-mers 
Les k-mers sont l'ensemble des mots de k lettres que l'on peut lire dans une séquence. Par exemple, la séquence suivante **TAATGCCATGGGATGT** peut se décomposé (avec des pétard ou non) en 14 mots de 3 lettres appelé 3-mers.

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
Notez par ailleur que le mot "ATG" est présent 3 fois dans cette liste. 
Pour reconstruire notre séquence, nous auront donc besoin d'une liste k-mer associé à leurs abondances. 

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

# Construction d'un graphe
A partir de ces 3-mers, nous allons construire un graphe. C'est à dire un ensemble de noeuds relié par des arrêtes. Pour cela deux méthodes s'offre à nous.

## Les k-mers sont des noeuds 
Si nous representons chaque k-mer par un noeuds, alors deux noeuds consécutif dans la séquence partage le même suffix et prefix.
Par exemple le k-mer T**GC** précède le k-mer **GC**C car le suffix du premier (xGC) correspond au prefix du second (GCx). Ce lien se represente comme cela dans un graphe:

<div class="figure">
<img src="../images/assemblage/hamilton_node.png" />
<div class="legend"> Lien entre deux k-mers dans un graphe. Le suffix (k-1) du premier correspond au prefix (k-1) du second</div>
</div>

En reprenant tous nos k-mers, nous pouvons alors construire un graphe en reliant tous les noeuds via leurs suffix et leurs prefix. On obtient alors ce graphe:

 <div class="figure">
<img src="../images/assemblage/hamilton_graphe.png" />
<div class="legend"> Graphe representant chaque k-mer par un noeuds.</div>
</div>

Pour reconstruire la séquence d'origine, il suffit de trouver un chemin passant par tous les noeuds une fois et une seul. C'est ce qu'on appelle un [parcours Hamiltonien](https://fr.wikipedia.org/wiki/Graphe_hamiltonien). Vous pouvez vous amuser à le chercher vous même ou en regarder l'animation ci-dessous:

 <div class="figure">
<img src="../images/assemblage/hamilton_graphe_path.gif" />
<div class="legend"> Chemin dans un graphe </div>
</div>

Cette méthode est simple à comprendre. Mais il y a un hic. La recherche du parcours hamiltonien est un problème mathématique dit NP-complet. Pour faire simple, il n'existe pas d'algorithme rapide pour trouver ce chemin. Pour un graphe plus complexe, tel que celui utilisé pour reconstruire la séquence d'un génome, il faudrait énormement de temps de calcul, même avec les plus super des super calculateurs.    
Il nous faut une autre méthode ...

## Les k-mers sont des arrêtes  
Nous allons cette fois construire un graphe en representant les k-mers par des arrêtes. Les noeuds contiendrons le prefix et le suffix du k-mer. Par exemple si une arrêtes represente le k-mer TGC alors les deux noeuds de cette arrêtes sont TG et GC.

<div class="figure">
<img src="../images/assemblage/euler_node.png" />
<div class="legend"> Representation d'un k-mer par une arrête. Les noeuds contiennent les suffix et prefix des k-mers</div>
</div>

En utilisant tous nos k-mers vu précedement, on peut alors construire le graphe suivant:

<div class="figure">
<img src="../images/assemblage/not_fusion_graphe.png" />
<div class="legend">  Graphe representant chaque k-mer par une arrête.</div>
</div>

Cette fois au lieu de chercher un chemin passant par tous les noeuds une seul fois, nous alons chercher un chemin passant par toutes les arrêtes une fois et une seul. Si vous essayer sur le graphe ci-dessus, vous verez tout de suite qu'il y a un problème et qu'un tel chemin n'existe pas. Nous allons donc devoir modifier ce graphe.     
Vu que rien ne nous empeche de passer plusieurs fois par le même noeuds, nous pouvons tout simplement fusionner les noeuds identiques. 
Sur le graphe, ce sont les 3 noeuds violets AT et les 3 noeuds rouge TG que nous pouvons fusionné pour former un noeud AT et un noeud TG. 
En faisant cette transformation de tête, vous devriez obtenir le graphe suivant que l'on appelle: Le graphe De Debruijn.

 <div class="figure">
<img src="../images/assemblage/debruijn_graphe.png" />
<div class="legend"> Chemin dans un graphe </div>
</div>

Et cette fois, vous pouvez vous amuser à chercher le chemin passant par toutes les arrêtes une fois et une seul. C'est ce qu'on appelle un parcours Eulerien que vous pouvez voir sur l'animation suivante. 

 <div class="figure">
<img src="../images/assemblage/euler_path.gif" />
<div class="legend"> Chemin dans un graphe </div>
</div>

Cette méthode est plus complexe à mettre en place. Mais elle a un avantage certain. Il existe un algorithme rapide pour trouver un tel chemin dans un graphe, si il existe. Et on le doit à Euler et sa ville de Konigberg.

# Les  ponts de Konigsberg 
En 1873 en pologne dans la ville de Konigsberg, un mathématicien du nom de Leonhard Euler s'est posé la question de savoir si il existait une promenade passant par tous les pont une seul fois et une seul.

 <div class="figure">
<img src="../images/assemblage/Konigsberg_bridges.png" />
<div class="legend"> Gauche: Pont de Konigsberg Droite: representation des ponts par un graphe. Existe il un chemin passant par tous les ponts </div>
</div>

En résumé, Euler démontre qu'un parcours eulerien existe dans un graphe si et seulement chaque noeuds est relié à un nombre pair d'arrête. En effet, si l'on veut entrer dans un noeud par 1 arrête il faut forcément resortir par 1 autre arrête. Dans le cas des ponts de Konigsberg, un tel chemin n'existe pas car le nombre d'arrete par noeud est respectivement de 5,3,3,3 ( voir graphique). 
Dans un graphe dirigé, lorsque les arrêtes ont des flèches, un chemin eulerien existe si le nombre d'arrête à l'entrée d'un noeud (degrée d'entrée) et le même qu'à la sortie (degrée de sortie).     
En modifiant notre graphe de Debruijn de façon à faire un cycle, vous verez qu'il repond à ces critères.

 <div class="figure">
<img src="../images/assemblage/euler_cycle.png"/>
<div class="legend"> Graphe de Debruijn modifié pour pouvoir avoir un cycle de euler. En rouge le nombre d'arrête d'entré, en vert le nombre d'arrête de sortie. Le dégrée d'entré et de sortie pour chaque noeuds sont identique. D'après le théorème, il existe donc un chemin eulerien passant par toutes les arrête une fois et une seul </div>
</div>

# L'algorithme de Euler
Euler propose une méthode simple pour pouvoir trouver le chemin eulerien de façon rapide. 

-  Prendre un noeud V1 au hasard
-  Parcourir le graphe au hasard jusqu'a retombé sur V1
-  Si vous n'avez pas visiter tous les noeuds et que vous êtes bloqué
    +  Choissisez un nouveau noeud V2 voisin de V1
    +  Parcourir le même chemin que précedement jusqu'à retombé sur V2
    +  Et ainsi de suite

Plus serieusement, si vous voulez comprendre cette algorithme, je vous conseille très très fortement de voir cette courte vidéo sur la chaine youtube "A la découverte des graphes". Personnellement, c'est la meilleurs chaines de vulgarisations sur les graphes. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/DH0Hxes2nOo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


En résumé, pour reconstruire une séquence à partir de ses k-mers, nous pouvons chercher un parcours hamiltonien dans un graphe.  Celui ci est simple à comprendre mais n'as pas d'algorithme efficace. En revanche, le parcours eulerien dans un graphe de Debruijn a une solution algorithmique efficace, et c'est cette méthode qui est utilisé par la majorité des assembleurs. 



# Conclusion 
Dans ce billet, j'ai voulu être le plus pédagogique possible en simplifiant à l'extrème. Pour cela, je me suis inspiré grandement du livre "Bioinformatics algoritmics" que je vous conseil. 
Dans la réalité, la reconstruction d'un génome est plus complexe en utilisant les notions des contigs, des scaffolds, des reads pairés. Mais tout cela change déjà avec les séquenceurs de 3ème génération rendant ce billet has-been... 


## References 


