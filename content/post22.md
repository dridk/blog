Title: Le séquençage de nouvelle génération
Slug: ngs
Date: 2017-05-16 15:58:18
Tags: biologie
Category: génétique
Author: Sacha Schutz
Status: Draft

Le séquençage de nouvelle génération ( NGS : Next Generation Sequencing) est la révolution biotechnologique de ces dernières années, en permettant de séquencer de grande quantité d'ADN en des temps records.
A titre d'exemple, entre 1990 et 2003, il a fallu 3 milliards de dollars pour séquencer le génome humain en utilisant des séquenceurs de type Sanger répartis dans plusieurs laboratoire à travers le monde. Aujourd'hui, Avec un séquenceur NGS Illumina HiSeq X, en trois jours, on peut séquencer trois génomes humains pour [$1000](http://www.nature.com/news/is-the-1-000-genome-for-real-1.14530) chacun. Le graphique ci-dessous, que vous verez regulièrement, montre l'évolution du coût du séquençage pour par million de nucléotide au cours du temps. Et encore, ce graphique s'arrête en 2013. La société illumina à déjà promis le génome à [$100](https://www.illumina.com/company/news-center/press-releases/press-release-details.html?newsid=2236383) d'ici deux ans avec le nouveau séquenceur Illumina NovaSeq.  
Cet article est un avant-gout très vulgarisé pour découvrir les bases du séquençage haut débit.  

<div class="figure">
    <img src="../images/post22/moore.png" /> 
    <div class="legend">Diminutions du coût du séquençage par nucléotides au cours des dernières années</div>
</div>   


# Principe du séquençage

Imaginons que votre génome s'assimile à un gros livre de plus de 3 milliards de caractères écrit avec les lettres A,C,G et T. Séquencer votre génome, c'est connaitre l'ensemble du texte qu'il contient. Il est impossible avec les technologies actuelles de lire ce livre d'une seul traite, en partant du début jusqu'à la fin. Les séquenceurs se contentent de lire de courtes portions de texte dont la longueur varie suivant la technologie utilisé. 
Par exemple, les anciens séquenceurs de type Sanger, fonctionnant avec un capillaire, sont capable de lire des fragments assez long d'environ 800 caractères en 1 heures. Si vous faites le calcul, vous verez rapidement que pour atteindre les 3 milliards de caractères, il vous faudra plus d'une vie pour reussir à séquencer votre génome (>400 ans). Pour allez plus vite, l'idée est de lire plusieurs fragments en même temps, c'est à dire paralléliser le séquençage. Les plus performant des séquenceurs Sanger, peuvent parallélisé jusqu'à 96 fois en utilisant 96 capillaires. On a donc 96 x 800 caracteres lu en 1 heures. C'est mieux, mais ce n'est pas encore ça.   
Les séquenceurs de nouvelle géneration lisent des fragments plus court, de l'ordre de 150 caractères pour les séquenceurs de type Illumina. En revanche, ils sont capable de lire jusqu'à 20 milliard de fragments à la fois !



# Librairie de séquençage
En génomique, ce qu'on appelle une librarie, est l'ensemble des fragments d'ADN que nous désirons séquencer. Pour créer une librarie, deux méthodes sont à retenir. Soit une méthode globale si l'on souhaite séquencer l'ensemble des ADN. Soit une méthode ciblé lorsque certaine régions seulement de l'ADN nous interesse.
### Méthode globale

Nous lançons le livre de votre génome en l'air et nous tirons au shotgun dessus pour faire une pluie de fragment d'ADN aléatoire. C'est ce qu'on appelle stricto sensu, la stratégie shotgun. 

<div class="figure">
    <img src="../images/post22/shotgun.png" /> 
    <div class="legend">La stratégie shotgun consiste à fragmenter l'ADN en séquence aléatoire puis à les séquencer.</div>
</div>   


Plusieurs méthode exister pour fragmenter l'ADN:

* **Fragmentation par sonication** : En envoyant des ultra-son de façon approprié, on arrive créer des fragments d'ADN de la taille désiré. 

* **Fragmentation enzymatique** : L'utilisation d'enzyme de restriction permet de couper l'ADN au niveau de certain mot précis. Par exemple, avec la metaphore du livre, couper au ciseau dès qu'il y a le mot "la".   


### Méthode ciblé 
Nous ne désirons pas forcément connaître l'ensemble du livre. Nous voulons peut être séquencer uniquement le paragraphe contenant la séquence d'un seul gène, ou tout les paragraphes du livres contenant les gènes associés au retard mentaux. Pour cela nous pouvons enrichir notre librairie en sélectionnant uniquement les fragments d'ADN désiré. Deux techniques sont à retenir:

* **L'enrichissement par capture** : Après fragmentation, les fragments d'ADN sont filtré en s'hybridant sur des séquences complementaire disposé sur une plaque ou en milieu liqude. Les fragments d'ADN qui ne s'hybride pas sont eliminé. 
  

<div class="figure">
    <img src="../images/post22/capture.png" /> 
    <div class="legend">Exemple d'enrichissement en phase liquide grâce à des billes magnétiques</div>
</div>   



* **Enrichissement par PCR** : Les fragments désiré sont amplifié par PCR. Nous pouvons amplifier une seul région avec un coupe d'amorces (simplexe). Ou alors plusieurs régions avec plusieurs couples d'amorces (multiplexe). Dans cette stratégie, toutes les séquences d'un même amplicon seront identique. 


<div class="figure">
    <img src="../images/post22/amplicon.png" /> 
    <div class="legend">La stratégie par amplicon produit des séquences identiques</div>
</div>   



# Sequençage 
Ils existent différentes méthode de séquençage

* Le séquençage par synthèse ( Illumina).
* Le pyroséquençage (Roche 454).
* La ligation (SOLid Thermofisher).
* La détéction des ion H+ (Proton Thermofisher).

Dans l'ensemble, le principe général reste le même. Chaque fragment est d'abord cloné plusieurs fois afin d'amplifier le signal. Puis le brin complémentaire de chaque fragment est synthétisé. A chaque incorporation d'un nucléotide un signal est détécté. De la lumière pour illumina ou une variation de pH sur du Proton. 
A la fin du séquençage, chaque fragment a été séquencé en parallèle. L'ensemble des données est enregistrer dans un fichier Fastq.


## Exemple Proton 

<div class="figure">
    <img src="../images/post22/ion.png" /> 
    <div class="legend">La stratégie par amplicon produit des séquences identiques</div>
</div>   


# Alignement des séquences
A la fin du séquençage, la biologie fait place à la bioinformatique. Les séquences des fragments, que nous appelerons maintenant des "reads", sont sauvegarder dans un fichier fastq contenant les séquences et leurs qualité. Cette qualité est un score (Phred) évaluant à chaque nucléotide sa fidélité de séquençage.
Vous pouvez télécharger ici un exemple pour voir à quoi cela ressemble.   
Mais le travail est loin d'être fini. Ce que nous avons, ce sont uniquement des courtes séquences de 150 p. Ce que nous voulons c'est obtenir la séquence complète d'un gène ou d'un génome entier. Pour cela, nous devons reconstruire un puzzle en réalisant ce qu'on apelle de l'alignement:
Deux méthodes d'alignement sont possible.

- **Alignement de novo** : Il s'agit de résoudre un puzzle sans modèle. Les fragments d'ADN qui sont chevauchant permette petit à petit de reconstruire la séquence. Cette technique est très couteuse en terme de calcul. Des algorithmes bioinformatiques comme les graphe de Debruijn, permettent de résoudre ce problème. Cette méthode est principalement employé pour reconstruire des génomes non connus.
- **Alignement avec reference**: Il s'agit toujours de résoudre un puzzle. Mais cette fois, en s'aidant d'un modèle. Par exemple une version du génome humain (hg19) servira de référence. 
Chaque read est aligné sur cette référence. La complexité de calcul est netement plus simple qu'avec l'allignement de novo. On utilise en général l'algorithme de Burrows Wheeler permettant de rechercher de manière efficace une correspondance entre les reads et la référence. Après cette allignement, on obtient un fichier BAM associant à chaque reads des coordonnées génomique ( chromosome + position). La representation visuel d'un fichier bam ressemble à la figure ci dessous. On appelle la profondeur, le nombre moyen de reads qui se superpose et couverture, l'etalement des reads sur la zone d'interet.  

# Conclusion

Si vous avez tout compris, alors vous êtes capable d'evaluer les capacités d'un séquenceur haut débit. Un séquenceur est défini par :

- La longueur des reads (L)
- Le nombre de reads (n)
- Le nombre de nucléotides lu: (L x n)
- Le temps de séquençage 
- La qualité du séquençage.

Le leader du séquençage haut-débit est pour l'instant Illumina, qui propose une game de séquenceur complète. 


Mais à peine sortie, ces technologies deviennent rapidement obsolète. En effet, je ne vous ai pas parlé des séquenceurs de 3ème générations, qui feront surement l'objet d'un nouvel article. Ce sont des séquenceurs capable de générer de très long reads (jusqu'a x) sans avoir besoin de cloner les reads qui peut être source une source de biais. En revanche, ces nouvelles techniques produisent encore beaucoup d'erreur de séquençage. Les deux leaders de ce Next Next generation sequencing sont Nanopore et PacBio Science qui termine le guerre de brevet. Et rien que voir la miniaturisation de leurs séquenceur, ça me plonge dans un monde futuriste

photo nanopore 