Title: Code d'erreur de Reed-Solomon 
Slug: reed-solomon
Date: 2024-09-22 19:30:31
Modified: 2024-09-22 19:30:31
Tags: algorithme
Category: informatique
Author: Sacha schutz
SIDEBARIMAGE:images/common/term_banner.jpeg
Status: draft 

Le code de Reed-Solomon est un algorithme qui va vous permettre de corriger des erreurs dans 
une séquence en utilisant des symboles surnuméraires. C'est un système de correction 
d'erreur qui permet par exemple de lire vos vieux CD-ROM tout rayé.
Pour comprendre, imaginiez que je vous transmette lettre par lettre le mot "c-h-a-t" mais que vous n'avez pas 
entendu la 3ème lettre. Vous ne pourrez pas interpréter le message. Il pourrait s'agir aussi bien du mot "chut" que du mot "chot".
Mais en vous communiquant un symbole surnuméraire, par exemple c-h-a-t-z, vous allez pouvoir identifier et corriger l'erreur 
peut importe ou elle se trouve.    
Nous allons donc voir comment fonctionne cette algorithme avec le mot 'c-h-a-t' en évitant tout définition mathémtique complexe. 

 
## Representation du mot chat dans un espace de gallois

Nous allons representer chat lettre du mot chat sur un graphique ou l'axe des ordonnées correspond à la position de la lettre 
dans l'alphabet et l'axes des absisses corespond à la position  dans le mot. Par exemple le C est la première lettre
du mot chat et la 3 ème lettre de l'alphabet. Ses coordonnés seront (0,2). De même on aura H (1,x), A(2,y), T(3,y).


{graph}

2 choses à comprendre sur ce graphique. Tout d'abord le domaine d'application des valeurs. Celui ci est discret.
En effet, les positions sont des nombres entiers car il n'est pas possible d'avoir la position 1.5.     
Regardez ensuite la borne superieur de l'axes des ordonnées qui est egal à 26 . Il s'agit du nombre de symbol dans l'alphabet. 


## Interpolation lagrangienne
L'objectif à présent est de trouver une fonction mathématique passant par ces 4 points. Plus exactement, 
nous allons chercher un polynome de degré 3 ( nombre de lettre - 1 ) en realisant une interpolation lagrangienne. 
Cette méthode, simple à comprendre, peut être réalisé en python avec `scipi.interpolate.lagrange`.


```python

```

Nous obtenons alors le graphique suivant. 


{ graph }


Ce qui est très important à comprendre avec ce polynome, c'est qu'il est unique. Il n'y a qu'un seul polynome de degré 3 qui 
passe par ces 4 points. C'est sur ce principe que se base la correction d'erreur de Reed-solomon.
Si vous connaissez au minimum 3 points vous pouvez déduire le polynome de degré 4 et prédire n'importe  n'importe quel point manquant.


## Ajout des symboles de redondance 

Pour trouver le symbole de rédondance à utiliser à la 5 positions du mot, il suffit de calculer polynome(5) = 102. 
Le symbole de rédondance est donc la 102 lettres de l'alphabet.
Mais attendez, nous avons que 26 lettres dans l'alphabet ? C'est là que vous devez savoir que ce que j'ai dit n'est pas 
tout à fait vrai. En réalité, le polynome est recherché dans un espace de Galois ou régne l'arithmétique modulaire.
C'est comme si vous comptier l'alphabet sur un cercle ou après la lettre Z il y a le A qui est donc la 27 ème lettre de l'alphabet.
La 102 ème lettres de l'alphabet est donc à la position `102 % 26 = 24`, soit la lettre y.     
Vous pouvez ajouter autant de symboles de correction d'erreur que vous le souhaitez. Pour un mot de N lettres avec 1 seul symbol de 
correction d'erreur, vous avez besoin de connaitre N-1 symbol pour valider le code de Reed-solomon. Et si vous rajouter 3 symboles, 
ca veux dire que vous pouvez perdre 3 symboles et les retrouver. 


## En pratique 
En pratique, il y a une librarie python qui fait très bien l'affaire. 









## Remerciements 

- Merci à @lourdes pour la découverte


https://odsc.medium.com/9-open-source-tools-to-generate-synthetic-data-b642cb10dd9a

https://medium.com/@MarkAiCode/linux-ai-data-anonymization-protect-user-privacy-e60a96d2f898


Maskfile 
