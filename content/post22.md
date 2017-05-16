Title: Le séquençage de nouvelle génération
Slug: ngs
Date: 2017-05-16 15:58:18
Tags: biologie
Category: génétique
Author: Sacha Schutz
Status: Draft

Le séquençage de nouvelle génération ( NGS : Next Generation Sequencing) est la révolution biotechnologique de ces dernières années, en permettant de séquencer de grande quantité d'ADN en des temps records.
A titre d'exemple, il a fallu 13 ans et 3 milliards de dollars pour séquencer le génome humain en utilisant des séquenceurs de type Sanger répartis dans plusieurs laboratoire à travers le monde. Aujourd'hui, Avec un séquenceur NGS Illumina HiSeq X, en trois jours, on arrive à séquencer trois génomes humains pour [$1000](http://www.nature.com/news/is-the-1-000-genome-for-real-1.14530) chacun. Le graphique ci-dessous, que vous verez regulièrement, montre l'évolution de coût du séquençage pour par million de nucléotide. Et encore, ce graphique s'arrête en 2013. La société illumina à déjà promis le génome à [$100](https://www.illumina.com/company/news-center/press-releases/press-release-details.html?newsid=2236383) d'ici deux ans avec le nouveau séquenceur Illumina NovaSeq.  
Cet article est un avant-gout pour découvrir les nases du séquençage haut débit.  

<div class="figure">
    <img src="../images/post22/moore.png" /> 
    <div class="legend">Diminutions du coût du séquençage par nucléotides au cours des dernières années</div>
</div>   



# Principe du séquençage
Imaginons que votre génome s'assimile à un gros livre de plus de 3 milliard de caractères écrit avec les lettres A,C,G et T. Séquencer votre génome, c'est connaitre l'ensemble du texte de ce livre.
Aujourd'hui, on ne peut pas pas lire ce livre d'une seul traite, du début jusqu'à la fin. Les séquenceurs lisent seulement des bouts de phrases dont la longueur varie suivant la technologie utilisé. 
Par exemple, les anciens séquenceurs de type Sanger sont capable de lire des fragments assez long d'environ 800 caractères en 1 heures. Si vous faites le calcul, vous verez rapidement que pour atteindre les 3 milliards de caractères, il vous faudra plus d'une vie pour reussir séquencer votre génome (>400 ans). Pour allez plus vite, l'idée est de lire plusieurs fragments en même temps, c'est à dire paralléliser le séquençage. Pour ceux qui connaisse le fonctionnement d'un processeur graphique GPU, c'est la même chose. Les plus performant des séquenceurs classiques, peuvent parallélisé jusqu'à 96 fois le séquençage (en utilisant 96 capillaires). On a donc 96 x 800 caracteres lu en 1 heures. C'est mieux, mais ce n'est pas encore ça.   
Les séquenceurs de deuxième géneration lisent des fragments plus court, de l'ordre de 150 caractères pour les séquenceurs Illumina. En revanche, ils sont capable de lire jusqu'à 20 milliard de fragments à la fois!!!!!



# Librairie de séquençage
En génomique, ce qu'on appelle une librarie, est l'ensemble des fragments de d'ADN que nous désirons séquencer. Pour créer une librarie, deux méthodes sont à retenir.

### Méthode globale

Nous lançons le livre de votre génome en l'air et nous tirons au shotgun dessus pour faire une pluie de fragment d'ADN aléatoire. C'est ce qu'on appelle stricto sensu, la stratégie shotgun. Plusieurs méthode exister pour fragmenter l'ADN en petit morceau:

* **Fragmentation par sonication** : En envoyant des ultra-son de façon approprié, on arrive créer des fragments d'ADN de la taille désiré. 

* **Fragmentation enzymatique** : L'utilisation d'enzyme de restriction permet de couper l'ADN au niveau de certain mot précis. Par exemple, avec la metaphore du livre, couper au ciseau dès qu'il y a le mot "la".   


### Méthode ciblé 
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