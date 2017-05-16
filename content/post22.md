Title: Introduction au séquençage haut débit
Slug: ngs
Date: 2017-05-16 15:58:18
Tags: biologie
Category: génétique
Author: Sacha Schutz
Status: Draft

Le séquençage de nouvelle génération ( NGS : Next Generation Sequencing) est la révolution biotechnologique de ces dernières années. C'est une technologie qui permet de séquencer des molécule d'ADN à très haut débit.  
A titre d'exemple, il a fallu 13 ans et 3 milliards de dollars pour séquencer le génome humain en utilisant des séquenceurs Sanger répartis dans plusieurs laboratoire à travers le monde. Aujourd'hui, Avec un séquenceur NGS et 1000 dollars, on peut réaliser le même travail en 3 jours.

# Principe du séquençage
Imaginons que votre ADN s'assimile à un gros livre de 3 milliard de caractères écrit avec les lettres A,C,G et T. 
Avec les séquenceurs actuels, on ne peut pas pas lire ce livre d'une seul traite, du début jusqu'à la fin. Les séquenceurs ne peuvent lire que des petits fragments de papiers,contenant une phrase, dont la longueur varie suivant le séquenceur. 
Les anciens séquenceurs de type Sanger peuvent lire des fragments assez long d'environ 800 caractères en 1 heures. Si vous faites le calcul, vous verez rapidement que pour atteindre les 3 milliards de caractères, il vous faudra plus d'une vie pour reussir (>400 ans). Pour allez plus vite, l'idée c'est de lire plusieurs fragments en même temps, c'est à dire parallélisé le séquençage. Le plus performant des séquenceurs classiques, peuvent parallélisé jusqu'à 96 fois (en utilisant 96 capillaires) le séquençage. On a donc 96 x 800 caracteres lu en 1 heures. C'est mieux, mais ce n'est pas encore ça.   
Les séquenceurs de deuxième géneration lisent des fragments plus court, de l'ordre de 150 caractères pour les séquenceurs Illumina. En revanche, ils sont capable de lire jusqu'à 20 milliard de fragments à la fois pour le NovaSeq. Et la ce n'est pas un génome humain, mais plusieurs génome que l'on peu séquencer sur une même machine.  

# Creation d'une librarie 
En génomique, ce qu'on appelle une librarie, est l'ensemble des fragments de d'ADN que nous désirons séquencer. Pour créer cette librarie, deux méthodes sont à retenir.

## Méthode globale
Nous allons lancer le livre en l'air et tirer au shotgun dessus pour faire une pluie de fragment d'ADN. C'est ce qu'on appelle stricto sensu, la stratégie shotgun. En réalité, on utilise une méthode mécanique ou enzymatique pour fragmenter l'ADN en petit morceau.  
* La sonication : En envoyant des ultra-son de façon approprié, on arrive créer des fragments d'ADN de la taille désiré. 
* Enzyme de restriction : L'utilisation d'enzyme de restriction permette de couper l'ADN au niveau de certain mot précis. Par exemple, avec la metaphore du livre, couper au ciseau dès qu'il y a le mot "la".   

## Méthode ciblé 
On a pas forcément envie de séquencer l'ensemble du livre. Nous voulons peut être séquencer uniquement le paragraphe contenant la séquence d'un seul gène, ou tout les paragraphes du livres contenant les gènes associés au retard mentaux. Pour cela nous pouvons enrichir notre librarire en sélectionnant uniquement les fragments d'ADN désiré. Deux techniques sont à retenir:

* L'enrichissement par capture : Après fragmentation, les fragments d'ADN sont filtré en s'hybridant sur des séquences complementaire disposé sur une plaque ou sur des billes. Les fragments d'ADN qui ne s'hybride pas sont eliminé. 
  
* Enrichissement par PCR : Les fragments désiré sont amplifié par PCR multipliexe, c'est à dire en utilisant plusieurs couples d'amorces en même temps.

# Sequençage 
Ils existent là aussi différentes méthode de séquençage. Le séquençage par synthèse, le pyroséquençage, la ligation, par détéction des ion H+. 
Mais dans l'ensemble, le principe reste le même. Chaque fragment d'ADN est d'abord cloner un certain nombre de fois afin d'amplifier un signal de detection. Puis chaque groupe cloné, est deposé sur un support ou aura lieu la synthèse du brin complémentaire. Chaque incorporation de nucléotide est detecté, permettant ainsi de lire la séquence de chaque fragment.

## Exemple Proton 
### PCR emulsion 
### Amplification 

# Alignement des séquences
A la fin du séquençage, la biologie fait place à la bioinformatique. Les séquences des fragments, que nous appelerons maintenant des "reads", sont sauvegarder dans un fichier fastq. Vous pouvez telecharger ce fichier pour voir à quoi cela ressemble. 
Mais ce ne sont que des phrases de 150 caracteres. Ce que nous voulons c'est la séquence complète d'un chapitre ou du livre entier. Pour cela, nous devons aligner les séquences comme un puzzle pour reconstruire le texte d'origine. 
Deux méthodes d'alignement sont possible.
- Alignement de novo : Il s'agit de résoudre un puzzle sans modèle. Les fragments d'ADN qui sont chevauchant permette petit à petit de reconstruire la séquence. Cette technique est très couteuse en calcul. 
- Alignement avec reference: Il s'agit toujours de résoudre un puzzle. Mais cette fois, nous disposons d'un modèle. Par exemple une version du génome humain peut faire office de modèle. Le cout en calcul est netement moindre que la méthode d'alignement précédent . 
Après l'alignement ne notre fichier fastq, nous obtenons un fichier BAM dont la representation visuel ressemble à ca : 
On appelle la profondeur, le nombre moyen de reads qui se superpose . 
On appelle recouvrement, l'etalement des reads sur la zone d'interet 

# Qualification d'un séquenceur 
Si jusqu'ici vous avez compris, alors vous êtes capable d'evaluer les capacités d'un séquenceur haut débit. Un séquenceur est défini : 
- La longueur des reads 
- Le nombre de reads 
- Le nombre de nucléotides lu : longueur des reads * nombre de reads
Les grandes marques des séquenceurs sont Illumina, ThermoFisher .


# Conclusion vers la 3eme generation
Je ne vous ai pas parler des séquenceurs de 3ème générations, qui feront surement l'objet d'un nouvel article. Ce sont des séquenceurs capable de générer de très long reads, et sans avoir besoin d'amplifier le signal en clonant les reads. Les deux leaders actuellent, qui se fond des procès sont Nanopore et PacBio Science. 