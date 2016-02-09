Title: Les empreintes génétiques
Slug: empreinte_genetique 
Date: 2016-02-07 13:20:34
Tags: génétique
Category: python
Author: Sacha Schutz
Status: Draft
SIDEBARIMAGE:../images/common/fingerprint_banner.jpeg


Envie d'identifier le criminel qui vous a volé votre bic 4 couleurs pendant votre absence au boulot ? Dans ce cas, cet article est fait pour vous ! Dans ce billet nous allons voir comment, à l'aide des séquences répétées dans le génome humain, il est possible d'identifier une personne en lui attribuant un « code-barres génétique ».    
On se met tout de suite la [musique des experts Manhatthan](https://www.youtube.com/watch?v=gY5rztWa1TM) et on commence ! 


# Les séquences répétées
10 % du génome humain est constitué de séquences d'ADN répétées en tandem. Il s'agit de séquences plus ou moins longues, appelées « **noyaux** », « **motifs** » ou encore « **unités de répétition** » (ex : GAAA), qui se répètent successivement un certain nombre de fois (ex : GAAAGAAAGAAAGAAAGAAA). 

<p align="center">
    <img src="../images/post13/satellite.png">
</p>


Ces séquences répétées sont présentes partout dans le génome, principalement dans les [télomères](https://fr.wikipedia.org/wiki/T%C3%A9lom%C3%A8re) et les [centromères](https://fr.wikipedia.org/wiki/Centrom%C3%A8re). Parfois, ces séquences sont à proximité de gènes codants et une modification du nombre de répétitions peut alors entraîner des répercussions cliniques. L'exemple type est la [maladie de Huntington](https://fr.wikipedia.org/wiki/Maladie_de_Huntington). Cette atteinte neurodégénérative héréditaire est caractérisée par une expansion de triplets CAG supérieure à 30 dans le gène HTT de l'[huntingtine](https://fr.wikipedia.org/wiki/Huntingtine).  
On distingue 2 types de séquences répétées en fonction de la taille du motif. Les [minisatellites](https://fr.wikipedia.org/wiki/Minisatellite) ou VNTR (*Variable Number Tandem Repeat*) contiennent un motif de 9 à 80 bases et les [microsatellites](https://fr.wikipedia.org/wiki/Microsatellite_%28biologie%29) ou STR (*Short Tandem Repeat*) un motif de 2 à 5 bases. Ce sont ces dernières qui sont utilisées pour l'identification des personnes par empreinte génétique.

# Le polymorphisme  

La variation du nombre de répétitions varie fortement dans la population. Par exemple, pour une position génomique donnée, un individu (bleu) pourrait avoir sur son chromosome paternel la répétition (CG)<sub>6</sub> et sur son chromosome maternel la répétition (CG)<sub>8</sub>. Un autre individu (rouge) pourrait porter sur ses chromosomes les allèles (CG)<sub>6</sub> et (CG)<sub>9</sub>.

<p align="center">
    <img src="../images/post13/satellite_poly.png">
</p>


L'identification de plusieurs régions répétées au sein du génome permet d'associer à un individu une unique combinaison. Une palette de 13 loci contenant des régions répétées est aujourd'hui utilisée par la police scientifique pour identifier n'importe quel individu. Le caryotype ci-dessous montre la position et le nom de ces STR sur les chromosomes.

<p align="center">
    <img src="../images/post13/codis.jpg">
</p>

# Identification des STR 
Pour créer une empreinte génétique, il suffit tout simplement de mesurer la taille de ces 13 régions répétées en les amplifiant par PCR. Pour cela, pour chaque STR, on utilise un couple d'amorces flanquant le STR en question. Une des deux amorces est couplée à un fluorochrome qui permet ensuite l'identification de la séquence par [électrophorèse capillaire](https://fr.wikipedia.org/wiki/%C3%89lectrophor%C3%A8se_capillaire). Les séquences des amorces sont disponibles [ici](http://www.cstl.nist.gov/biotech/strbase/multiplx.htm).

<p align="center">
    <img src="../images/post13/PCR_multiplexe.png">
</p>


À la fin de la PCR, on obtient des [amplicons](https://fr.wikipedia.org/wiki/Amplicon) dont la taille est proportionnelle à celle du STR. Une [analyse de fragments](https://cmgg.be/fr/content/analyse-de-fragments) est ensuite réalisée à l'aide d'un séquenceur capillaire. En d'autres termes, les amplicons migrent dans un capillaire plus ou moins vite et leur temps de passage est mesuré lors de la détection du fluorochrome par un laser. Les résultats sont représentés par des pics de fluorescence dont la position sur l'axe des abscisses correspond à la taille du STR.   
Prenons par exemple un individu homozygote pour le locus [vWA](http://www.sciencedirect.com/science/article/pii/S0531513103017746). À ce locus, cet individu possède 4 répétitions TCTG à la fois sur le chromosome maternel et sur le chromosome paternel. Son génotype pourrait s'écrire : (TCTG)<sub>4</sub> / (TCTG)<sub>4</sub>. Dans ce cas, la PCR amplifie des amplicons faisant tous la même taille et un seul pic est détecté avec l'analyse de fragments.   

 <p align="center">
    <img src="../images/post13/homozygote.png">
</p>

En revanche, si le patient est hétérozygote avec le génotype suivant : (TCTG)<sub>4</sub> / (TCTG)<sub>5</sub>, on observe 2 pics et une diminution des amplitudes.  

 <p align="center">
    <img src="../images/post13/heterozygote.png">
</p>


Pour créer une empreinte génétique, il suffit de refaire la même chose pour les 13 loci. On fait une [PCR multiplexe](http://www.ozyme.fr/documentation/techozyme/techozyme20-pcr-multiplexe.asp) en mélangeant tous les couples d'amorces et en discriminant chaque locus à l'aide de 4 fluorochromes différents ainsi que par des tailles de STR différentes. En traçant l'ensemble des pics, on obtient l'empreinte génétique. La probabilité que deux individus (non jumeaux) aient le même profil est extrêmement faible, de l'ordre de  10<sup>-10</sup>.    
Voici le profil d'un individu que j'ai trouvé sur Google ! Je vous laisse le soin de l'interpréter ! 

 <p align="center">
    <img src="../images/post13/fingerprint.jpg">
</p>

* Question : Que signifie le pic bleu avec l'unique valeur 24 ? 
* Question : S'agit-il d'un homme ou d'une femme ? 
* Question : Que pourriez-vous proposer comme empreinte génétique pour la mère ?
* Question : Peut-on se servir de l'empreinte génétique pour faire un test de paternité ? 

#Conclusion 
C'est aux États-Unis en 1994 que la première banque de données d'empreintes génétiques a été créée sous l'égide du FBI, sous le label [CODIS](https://fr.wikipedia.org/wiki/Combined_DNA_index_system). En France, suite à l'affaire du tueur parisien [Guy Georges](https://fr.wikipedia.org/wiki/Guy_Georges), la loi du 17 juin 1998 acte la création du fichier national ([FNAEG](https://fr.wikipedia.org/wiki/Fichier_national_automatis%C3%A9_des_empreintes_g%C3%A9n%C3%A9tiques)). Il recense aujourd'hui 2 655 381 personnes.  


## Références 

* [Brief Introduction to STRs](http://www.cstl.nist.gov/biotech/strbase/intro.htm)
* [Les kits commerciaux](http://www.cstl.nist.gov/biotech/strbase/multiplx.htm)
* [Liste des amorces](http://www.cstl.nist.gov/biotech/strbase/primer1.htm)
* [The rarity of DNA profiles](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2585748/)
* [Pour mieux comprendre l'analyse de fragments](https://www.youtube.com/watch?v=43-OQTLtrwQ)

## Remerciement 
* @Piplopp 
* @Oodnadatta 


