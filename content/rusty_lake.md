Title: L'enigme du rusty lake hostel
Slug: the-rusty-lake-hostel
Date: 2018-09-30 00:34:27
Modified: 2018-09-30 12:53:15
Tags: graphe
Category: informatique
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/graph_banner.png

Cela fait plusieurs jours que je m'éclate sur un jeu [android](https://fr.wikipedia.org/wiki/Android) appelé « [The rusty lake hostel](https://store.steampowered.com/app/435120/Rusty_Lake_Hotel/) ». Il s'agit d'une sorte d'escape game en [point & click ](https://fr.wikipedia.org/wiki/Pointer-et-cliquer) ou vous devez résoudre des énigmes. Parmi celles-ci, il y en a une qui m'a donné du fil à retordre et qui m'a contraint à écrire du code pour la résoudre. 
Il s'agit d'une énigme composée de 3 bouteilles de volumes différents : la première de **10** litres , la deuxième de **5** litres et la troisième de **6** litres. En début de partie,  la première bouteille contient 10 litres d'eau sur les 10, la deuxième 1 litre sur les 5 et la troisième est vide.    
Le but du jeu est de réussir à avoir 8 litres dans la première en vidant les bouteilles les unes dans les autres successivement. 

<div class="figure">     <img src="../images/rusty_lake/base.jpg" />      <div class="legend">3 bouteilles ..</div> </div>   

En essayant à tâtons et en réfléchissant, vous trouverez surement la réponse en un temps raisonnable. Mais j'ai préféré écrire du code qui réfléchisse pour moi afin d'être plus systématique et parce que c'est plus rigolo. J'ai d'abord pensé à de la programmation logique avec [Prolog](https://fr.wikipedia.org/wiki/Prolog) ou [Answer Set Programming](https://fr.wikipedia.org/wiki/Answer_set_programming). Mais n'étant pas à l'aise dans ces langages, j'ai demandé à un copain, Aluriak, qui s'est fait une joie de résoudre ce problème en ASP et dont les résultats [sont dispo sur son blog](https://lucas.bourneuf.net/blog/asp-temporal.html).       
De mon côté, j'ai choisi une approche algorithmique en construisant un graphe résumant tous les états possibles associés à leurs transitions. Le notebook est disponible [ici](https://github.com/dridk/notebook/blob/master/rusty_lake/rusty_lake.ipynb) .

## un graphe d'état

On peut résumer ce problème comme une succession d'état reliés par des transitions. Un état est défini par les 3 volumes dans chaque bouteille. Par exemple le premier état **(10,1,0)** correspond à la première bouteille remplie à 10L, la deuxième à 1L et la troisième à 0L. 
À partir de cet état, il existe 3 transitions possibles.   
Si vous videz la première bouteille dans la seconde vous obtenez l'état **(6,5,1)**.   
Si vous videz la deuxième bouteille dans la troisième, vous obtenez l'état **(10,0,1)**.   
Si vous videz la première bouteille dans la troisième vous obtenez l'état **(4,1,6)**.    
Il n'y a pas d'autre possibilité comme illustrée ci-dessous:

<div class="figure">     <img src="../images/rusty_lake/graphe_base.png" />      <div class="legend">à partir de l'état (10,1,0) il y a trois façons différentes de transvaser l'eau</div> </div>   

Nous pouvons alors recommencer ce processus à partir de chacun des nouveaux états et construire sur plusieurs itérations les autres états dans un [graphe orienté](https://fr.wikipedia.org/wiki/Graphe_orient%C3%A9).      
Pour cela, j'ai utilisé [Python](https://www.python.org/download/releases/3.0/) et la librairie [networkx](https://networkx.github.io/) en représentant chaque état par un [tuple](http://apprendre-python.com/page-apprendre-tuples-tuple-python) de dimension 3.   
la fonction suivante permet de passer d'un état à un autre : 

```python
# Vider la bouteille x dans la bouteille y connaissant l'état (state) et
#le volume maximum pour chaque bouteille (vmax). Retourne None si impossible 
def change_state(x:int, y:int, state:tuple, vmax=(10,5,6)) -> (int, int, int) or None:
    
    new_state = list(state)
    
    # Calcul de e : le volume de liquide à déplacer

    e_in = (vmax[y] - new_state[y])
    e_out = state[x] 
    e = min(e_in, e_out)
    
    
    if e == 0 : 
        return None
    
    if new_state[x] - e < 0:
        return None
    
    if new_state[x] == 0:
        return None
    
    if new_state[y] + e > vmax[y]:
        return None
         
    new_state[x] -= e
    new_state[y] += e
    
    return tuple(new_state)
    
# exemple 
print(change_state(0,1,(10,1,0)))
```

En partant de l'état **(10,1,0)**, j'ai alors construit en 7 itérations le graphe de tous les états successifs possibles: 

```python

# Creation d'un graphe dirigé # Creat 
graph = nx.DiGraph()

# Liste de toutes les transitions possibles
# Bouteilles 0 dans 1, Bouteille 1 dans 2 etc ...
choices = list(itertools.permutations([0, 1, 2], 2))

# Creation du premier noeud avec l'état 10, 1, 0
parent = (10, 1, 0)
graph.add_node(parent)

# Construction du graphe sur 7 itérations 
for depth in range(7):
    parents = list(graph.nodes())
    for parent in parents: 
        for choice in choices:
            child = change_state(*choice, parent)
            if child is not None:
                graph.add_node(child)
                graph.add_edges_from([(parent, child)], label=str(i))

nx.draw(graph, with_labels=True)

```

Voilà ce qu'on obtient comme graphe. Et comme vous pouvez l'observer en jaune, il y a un état **(8,0,3)** contenant 8L dans la première bouteille. C'est l'état que nous voulons atteindre.

<div class="figure">     <img src="../images/rusty_lake/graphe.png" />      <div class="legend">Graphe de l'ensemble des états possibles avec 7 mouvements</div> </div> 

## La solution

Il suffit alors de trouver dans le graphe le chemin le plus court partant de l'état initial **(10,0,1)** vers l'état final **(8,0,3)** en utilisant [l'algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra). (Allez faire un tour sur la chaine YouTube « [A la découverte des graphe](https://www.youtube.com/watch?v=JPeCmKFrKio) » pour comprendre cet algorithme). Networkx nous fournit directement l'implémentation via la fonction [shortest_path](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path.html#networkx.algorithms.shortest_paths.generic.shortest_path):

```python     
states = nx.shortest_path(graph,source=(10, 1, 0), target=(8, 0, 3))

#State 1 (10, 1, 0)
#State 2 (4, 1, 6)
#State 3 (4, 5, 2)
#State 4 (9, 0, 2)
#State 5 (9, 2, 0)
#State 6 (3, 2, 6)
#State 7 (3, 5, 3)
#State 8 (8, 0, 3)

```

7 transitions sont donc nécessaires pour passer de l'état **(10,1,0)** à l'état **(8,0,1)**. La solution de l'énigme est donc la suivante. Merci les graphes !!

- State (10,1,0)
    + Vider la première bouteille dans la deuxième
- State (4,1,6)
    + Vider la troisième bouteille dans la deuxième
- State (4,5,2)
    + Vider la deuxième bouteille dans la première
- State (9,0,2)
    + Vider la troisième bouteille dans la deuxième
- State (9,2,0)
    + Vider la première bouteille dans la troisième
- State (3,2,6)
    + Vider la troisième bouteille dans la deuxième
- State (3,5,3)
    + Vider la deuxième bouteille dans la première
- State (8,0,3) 

<iframe width="560" height="315" src="https://www.youtube.com/embed/AqylpTp1sNs?start=423" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

