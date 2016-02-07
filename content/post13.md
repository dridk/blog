Title: Les empreintes génétiques
Slug: codebar_genetique 
Date: 2016-02-07 13:20:34
Tags: génétique,fun
Category: python
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/fingerprint_banner.jpeg

Envie d'identifier le criminiel qui vous a voler votre bic 4 couleurs pendant votre absence au boulo? Alors cette article est fait pour vous! Dans ce billet nous allons voir comment à l'aide de séquences répétées dans le génome humain, il est possible d'identifier une personne en lui attribuant un "codebar génétique".    
Alors on se met tout de suite le [musique des experts Manathan](https://www.youtube.com/watch?v=gY5rztWa1TM) et on commence ! 


# Les séquences répétés
10% du génome humain est constitué de séquence d'ADN répété en tandem. Il s'agit de séquences plus ou moins longues, appelé **noyau**, **motif** ou encore **unité de répétition** (ex: GAAA) qui se répète successivement un certain nombre de fois( ex: GAAAGAAAGAAAGAAAGAAA). 

<p align="center">
    <img src="../images/post13/satellite.png">
</p>

Ces séquences répétés sont présente partout dans le génome. Principalement dans les télomères et les centromères. Parfois ces séquences sont à proximités de gène codant, et la variation du nombre de répétition peut alors entraîner des maladies.La maladie de Huntigton est une maladie neurodegenerative héréditaire caractérisé par une expansion de triplet CAG superieur à 30 dans le gène HTT de l'huntigtine.    
On distingue 2 types de séquences répétés en fonction de la taille du motif. Les minisatellites ou VNTR (variable number tandem repeat) contiennent un motif de 9 à 80 bases et les microsatellites ou STR (Short Tandem Repeat) un motif de 2 à 5 base. Ce sont ces dernières utilisé pour l'identification des personnes ou pour les testes de paternités.

# Le polymorphisme  

La variation du nombre de répétition varie fortement dans la population. Par exemple, pour une position génomique donné, un individu (bleu) pourrait avoir sur son chromosome paternel la répétition(CG)<sub>6</sub> et sur son chromosome maternelle (CG)<sub>8</sub>. Tandis qu'un autre individu (rouge) portera sur son chromosomes les deux allèles (CG)<sub>6</sub> et (CG)<sub>9</sub>.
<p align="center">
    <img src="../images/post13/satellite_poly.png">
</p>

L'identification de plusieurs régions répété au sein du génome, permettra d'associer à un individu une unique combinaison. Une palette de 13 locis contenant des régions répétées est aujourd'hui utilisés dans la police scientifique pour identifier n'importe quel individus. Le caryotype ci-dessous montre la position de ces STRs.   

<p align="center">
    <img src="../images/post13/codis.jpg">
</p>


# Amplification des loci STRs 
Pour créer l'empreinte génétique, il suffit tout simplement de mesurer la taille de ces 13 régions répétés en les amplifiants par PCR. 

Pour cela on réalise une PCR multiplexe suivi d'une analyse en fragment  Pour chaques sites, on utilisera un couple d'amorces flanquant la région variable. Plusieurs kit de PCR multiplexe sont à disposition sur [cette page](http://www.cstl.nist.gov/biotech/strbase/multiplx.htm).   
Une fois la PCR réalisé, on mesurera la tailles de nos 13 amplicons 

## PCR multiplexe 


## Analyse en fragment 

## Etude 


# Conclusion 
# Loi de Bioethique 


#IDEE 
identification des suspects, test de patternité, historical , military
http://www.cstl.nist.gov/biotech/strbase/intro.htm
http://www.cstl.nist.gov/biotech/strbase/intro.htm

https://www.youtube.com/watch?v=43-OQTLtrwQ
## Remerciement 
Merci à @Piplopp pour les corrections 
