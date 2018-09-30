Title: the rusty lake hostel
Slug: the-rusty-lake-hostel
Date: 2018-09-30 00:34:27
Modified: 2018-09-30 00:34:27
Tags: 
Category: 
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/graph_banner.png

Cela fait plusieurs jour que je m'éclate sur un jeux android appelé "The rusty lake hostel". Il s'agit d'une sorte d'escape game en point & click ou vous devez résoudre des enigmes. Parmi celle-ci, il y en a une qui m'a donné du fil à retordre et qui m'a contraint à écrire du code pour la résoudre. 
Cette énigme est composé de 3 bouteilles de volumes differents : La première de 10L , la deuxième de 5L et la troisème de 6L. Lorsqu'on commence le jeu, la première bouteille contient 10L d'eau sur 10, la deuxième 1L sur 5 et la troisième est vide. 
Le but du jeu est de reussir à avoir la première bouteille rempli à 8L en transvasant l'eau de bouteille à bouteille. Une bouteille est vidé dans une autre jusqu'à la remplir. 

<div class="figure">
    <img src="../images/rusty_lake/base.jpg" /> 
    <div class="legend">3 bouteilles ..</div>
</div>   

En essayant à taton et en réfléchissant, vous trouverez surement la réponse en un temps raisonnable. Mais j'ai préféré écrire du code qui réfléchisse pour moi. J'ai d'abord pensé à de la programmation logique avec Prolog ou ASP. Mais n'étant pas habile dans ces languages, j'ai demandé à un copain qui a résolu ce problème et qui a publié sur son blog ses résultats.    
De mon coté, je me suis contenter de construire un graphe résumant tous les cas possibles avec leurs transitions. 

## un graphe à état 

On peut résumer ce problème comme une succession d'état relié par des transitions. Un état est défini par le volume dans chaque bouteille. Par exemple le premièr état (10,1,0) correspond à 10L pour la premère bouteille, 1L pour la deuxième et 0L pour la troisème. A partir de cette état, nous pouvons passer dans differents. l'état (10,0,1) ou l'état (6,5,1).

<div class="figure">
    <img src="../images/rusty_lake/graphe_base.png" /> 
    <div class="legend">3 bouteilles ..</div>
</div>   

 En continuant ainsi, nous pouvons construire à chaque itération un graphe dirigé de plus en plus complexe. Pour cela, j'ai utilisé networkx en python. Le notebook jupyter est disponible ici. Après 7 itérations, on voit apparaitre l'état (8,0,3) qui est celui que nous cherchons à atteindre. 

<div class="figure">
    <img src="../images/rusty_lake/graphe.png" /> 
    <div class="legend">3 bouteilles ..</div>
</div> 

Il suffit alors de trouver dans le graphe le chemin le plus court partant de l'état initial (10,0,1) vers (8,0,3).


    nx.shortest_path(graph,source=(10,1,0),target=(8,0,3))
    
    #Etat 1 (10, 1, 0)
    #Etat 2 (4, 1, 6)
    #Etat 3 (4, 5, 2)
    #Etat 4 (9, 0, 2)
    #Etat 5 (9, 2, 0)
    #Etat 6 (3, 2, 6)
    #Etat 7 (3, 5, 3)
    #Etat 8 (8, 0, 3)



