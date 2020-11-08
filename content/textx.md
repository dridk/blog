Title: Créer votre propre langage avec textX en Python
Slug: textx
Date: 2020-11-08 15:32:40
Modified: 2020-11-08 15:32:40
Tags: python, langage, parseur
Category:informatique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/term_banner.jpeg

Un [DSL](https://fr.wikipedia.org/wiki/Langage_d%C3%A9di%C3%A9) ( Domain Specific Language ) est un langage de programmation crée pour une tâche spécifique à l'inverse des langages de programmation usuels comme [Python](https://www.python.org/). On peut s'en servir par exemple pour créer des petits langages maisons utilisés au sein d'une application.     
Dans ce billet, je vais vous montrer en Python, comment créer un langage pour contrôler le mouvement d'un robot fictif grâce à la librarie [textX](https://textx.github.io/textX/stable/). 

## Définition de notre grammaire 
Notre langage doit pouvoir permettre de contrôler le déplacement d'un robot sur un échiquier dans les 4 directions ( up, down, left, right).      
Par exemple : 

```
move up     # Bouge d'une case vers le haut      
move up 3   # Bouge de 3 case vers le haut
move left 3 # Bouge de 3 cause vers la gauche 
```
L'idée est de parser ces instructions afin de récupérer les variables pour les consommer dans notre application.      
Nous pourrions très bien résoudre ce problème en parsant les instructions à coup [d'expression régulière](expression-reguliere.html). Mais dès que le langage deviendra plus complexe, l'utilisation d'un outil comme textX vous facilitera grandement la tâche.

## TextX: Un métalangage pour définir notre langage 

La librairie textX en Python dispose d'un [métalangage](https://fr.wikipedia.org/wiki/M%C3%A9talangage) permettant de décrire la grammaire du langage que nous voulons créer (d'ou le prefix méta). Ce métamodel est alors utilisé par textX pour construire [l'arbre syntaxique](https://fr.wikipedia.org/wiki/Arbre_syntaxique) nécessaire pour parser les instructions données à notre robot. Je vous conseil de lire le code et de tester pour comprendre. 

### Installation 
J'utilise Python 3.7, et la version 2.3 de textX : 

    pip install textX

### Le métamodèle décrivant la grammaire

Commençons par créer un fichier *robo.tx* afin de décrire notre grammaire en utilisant différents symboles.      
- **Direction** est un symbole décrivant les 4 directions possibles. C'est un symbole terminal, car il ne peut pas être décomposé en sous-symbole contrairement à MoveCommand.       
- **MoveCommand** est symbole non terminal décrit à l'aide du symbole **Direction** et du symbole **NUMBER**. Ce dernier est un symbole fourni par défaut par textX pour décrire un nombre. La liste des autres types est [disponible ici.](https://textx.github.io/textX/stable/grammar/#textx-base-types). 

```
// robo.tx
MoveCommand:         
    'move' Direction NUMBER
;
Direction:
    'up'|'down'|'left'|'right'
;
```
Utiliser cette commande pour vérifier que le modèle est valide: 

```bash
textx check robot.tx
```

Nous pouvons maintenant affecter les différents valeurs de l'instruction à des variables qui seront accessibles depuis Python. Par la même occasion, je rends l'option step optionnelle grâce à l'opérateur "?". Pour cela, je modifie le code de la façon suivante: 

```
MoveCommand:
    action='move' direction=Direction (step=NUMBER)?
;

Direction:
    'up'|'down'|'left'|'right'     
;
```

Maintenant, pour utiliser cette grammaire en Python, et parser par exemple l'instruction "*move up 4*",  il faut charger le métamodel et parser l'instruction à l'aide de la méthode *[model_from_str](https://github.com/textX/textX/blob/master/textx/model.py#L317)*. Nous obtenons alors l'instance d'une classe **MoveCommand** contenant les 3 variables: **action**, **direction** et **step**.

```python
from textx import metamodel_from_file

metamodel = metamodel_from_file("robot.tx") 
cmd = metamodel.model_from_str("move up 4")

print(type(cmd)) # MoveCommand instance class
print(cmd.action) # "move"
print(cmd.direction) # "up" 
print(cmd.step) # 4

```

### Allez un peu plus loin 
La classe **MoveCommand** peut être personnalisée en amont, pour pouvoir jouer finement sur les variables du modèle. Nous allons modifier la classe afin que le paramètre **step** soit égal à 1 par défaut lorsque celui-ci n'est pas renseigné. 

```python
from textx import metamodel_from_file

class MoveCommand:
    def __init__(self, *args, **kwargs):

        self.action = kwargs.get("action")
        self.direction = kwargs.get("direction")
        self.step = kwargs.get("step")

        if self.step is None or self.step == 0:
            self.step = 1.0


metamodel = metamodel_from_file("robot.tx", classes=[MoveCommand]) 
model = metamodel.model_from_str("move up")

print(model.step) # step = 1 

```

Nous pouvons ajouter également à notre grammaire la possibilité de donner une suite d'instruction séparée par un point virgule. C'est là toute la magie de textX. Car il suffit d'ajouter le nouveau symbole **Command** que textX interprétera comme une liste de **MoveCommand** séparé par des points-virgules.

```
Command:
    commands += MoveCommand[";"]
;
MoveCommand:
    action='move' direction=Direction (step=NUMBER)?
;

Direction:
    'up'|'down'|'left'|'right'
;
```


```python
metamodel = metamodel_from_file("robot.tx", classes=[MoveCommand])
model = metamodel.model_from_str("move up; move left 3; move right")

for cmd in model.commands:
    print(cmd.step)

```

### Visualiser votre modèle
Pour finir, vous pouvez visualiser votre modèle à l'aide de la commande suivante et du fichier robot.txt contenant la suite d'instruction à tester : 

```
# Fichier robot.txt
move up; move left 3; move right
```


```bash
textx visualize robot.tx robot.txt
dot -Tpng -O robot.txt.dot
display robot.txt.dot.png
```

<div class="figure">     <img src="../images/textx/robot.txt.dot.png" />      <div class="legend"> Arbre syntaxique des 3 commandes du fichier robot.txt</div> </div>

## Conclusion 
Dans ce billet, j'ai présenté un cas très simple à visée pédagogique. Mais vous pouvez aller plus loin en créant des parseurs aussi complexe que des parseurs SQL ou JSON. Après, attention, n'utilisez pas ce genre d'outil pour réinventer la roue. Il existe déjà des langages (comme Python) qui font très bien les choses. Personnellement, j'ai créée un DSL dans mon logiciel cutevariant pour pouvoir facilement créer des filtres en ligne de commande sans avoir à passer pas les contrôleurs d'une interface graphique. Vous pouvez jeter un oeil sur ma grammaire [ici](https://github.com/labsquare/cutevariant/blob/master/cutevariant/core/vql.tx).    
Je vous invite à aussi regarder les exemples sur le [site officiel](https://textx.github.io/textX/stable/) dont je me suis largement inspiré. 

## Référence
- [TextX ](https://textx.github.io/textX/stable/) 

Merci à @Aluriak pour m'avoir présenté cette techno ! 
