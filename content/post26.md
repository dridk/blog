Title: Le génome d'un embryon humain a été édité 
Slug: edition-embryon-humain
Date: 2017-08-06 22:49:20
Tags: crisprcas9,embryon, mutation, MYBPC3,cardiomyopathie
Category: biologie
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/gatacca_banner.png

Si vous êtes passé à côté de la news de la semaine, sachez qu'une équipe américaine a réussi à corriger une mutation génétique lors d'une [fécondation in vitro](https://fr.wikipedia.org/wiki/F%C3%A9condation_in_vitro) à l'aide du couteau suisse moléculaire [CRISPR-Cas9](https://fr.wikipedia.org/wiki/Cas9). 
Une grande étape a été franchie en thérapie génétique avec tous les problèmes éthiques qui en découlent comme l'eugénisme ou le transhumanisme. 
Je me dois de vous faire un résumé rapide de cet article "*Correction of a pathogenic gene mutation in human embryos*" disponible [ici](http://www.nature.com/nature/journal/vaop/ncurrent/full/nature23305.html). 

# Correction d'une maladie autosomique dominante 
L'équipe a choisi de corriger une mutation sur le gène [MYBPC3](https://ghr.nlm.nih.gov/gene/MYBPC3) responsable d'une [cardiomyopathie hypertrophique héréditaire](http://www.rythmo.fr/la-cardiomyopathie-hypertrophique/). C'est la maladie du sportif qui fait une mort subite en plein match.  
C'est une maladie [autosomique dominante](https://fr.wikipedia.org/wiki/Transmission_autosomique_dominante). C'est-à-dire qu'un seul allèle muté suffit pour provoquer la maladie. C'est important pour la suite, car l'édition du gène a besoin de la présence d'un allèle sain. 
La mutation cible est une délétion de 4 nucléotides dans l'exon 16 du gène.

# Édition avec CRISPR-cas9
L'édition du gène a été réalisée  après fécondation in vitro entre le spermatozoïde d'un patient porteur de la mutation et un ovocyte sain. 
Le complexe CRISPR-Cas9 a été injecté dans l'oeuf 18h après fécondation par [micro-injection (vidéo)](https://www.youtube.com/watch?v=_v9xckdeVhU). 
CRISPR-Cas9 fait une coupure double brin pour retirer la région d'ADN contenant la mutation. Puis une [polymérase](https://fr.wikipedia.org/wiki/Polym%C3%A9rase) entre en action et corrige ce trou béant en utilisant l'allèle homologue non muté comme modèle. C'est ce qu'on appelle une [réparation par recombinaison homologue](https://fr.wikipedia.org/wiki/Recombinaison_homologue) ou HDR (Homology Directed Repear). Pour cette raison, seules les mutations hétérozygotes peuvent être corrigées avec ce protocole. 
Un autre mécanisme de réparation non conservatrice peut avoir lieu, la [Jonction d'extrémités non homologues](https://fr.wikipedia.org/wiki/Jonction_d%27extr%C3%A9mit%C3%A9s_non_homologues) ou NHEJ (Non-Homologous End-Joining). Cette dernière ne corrige rien, et l'on cherche à l'eviter autant que possible.

<div class="figure">
    <img src="../images/post26/crispr-homolog.png" /> 
    <div class="legend">réparation par recombinaison homologue</div>
</div>


L'expérience a été répétée plusieurs fois. Au total dans l'étude il y a eu **19** embryons témoins non injectés et **54** embryons injectés. L'ensemble des embryons ont ensuite été séquencés au stade 4-8 cellules pour voir si l'édition a réussi.

<div class="figure">
    <img src="../images/post26/gene_correction.png" /> 
    <div class="legend">1. Fécondation avec un spermatozoïde muté. 2. Injection de CRISPR-CAS9. 3. Plusieurs cas sont alors possibles. ça ne marche pas;ça marche à moitié (mosaïque);ça marche; HDR (Homology directed repair), NHEJ (Non-Homologous End-Joining) </div>
</div>

# bien, mais pas encore au point !
Chez les témoins, comme on s'y attend, la moitié des embryons ont été fécondés par un spermatozoïde muté (hétérozygote: **10/19**) ou par un spermatozoïde non muté (homozygote: **9/19**). Je rappelle que le père est hétérozygote pour la mutation et donc que la moitié de ses spermatozoïdes porte la mutation. 
En revanche, dans les embryons injectés **66.7% (36/54)** sont homozygotes sains et seulement **9.3% (13/54)** sont hétérozygotes mutés. Les **24% (5/54)** restant, corresponde à des embryons en [mosaiques](https://fr.wikipedia.org/wiki/Mosa%C3%AFque_(g%C3%A9n%C3%A9tique)). Ce sont des embryons où certaines cellules ont été corrigées et d'autre non.
En conclusion, ça marche, mais la technique n'est pas encore au point, car il reste pas mal de mosaïssisme. Pour y remédier, l'idée proposée est de faire l'injection CRISPR-cas9 au même moment que l'injection du spermatozoïde. 
Il y a également le risque des mutations induit par CRISPR-Cas9. Les fameuses [mutations off-target](https://www.lequotidiendumedecin.fr/actualites/article/2017/05/29/crispr-des-mutations-targets-encore-plus-inattendues_847911). Aucune n'a été détectée dans cette étude. 

<div class="figure">
    <img src="../images/post26/results.png" /> 
    <div class="legend">Gauche: Témoin sans injection CRISPR-Cas9. 50% des embryons sont mutés  . Droite: Avec injection CRISPR-Cas9. 66.7% des embryons sont sains. </div>
</div>

# Et l'éthique dans tout ça ? 
Pour l'heure, l'[ASHG a donné son autorisation](http://www.cell.com/ajhg/fulltext/S0002-9297(17)30247-1) sur l'édition des embryons tant que les recherches ne conduisent pas à une grossesse et qu'il y a un rationnel scientifique et éthique derrière.   
Mais un pas a tout de même été franchi, et je pense que rapidement, l'édition des génomes deviendra aussi courante que le [diagnostic préimplantatoire](https://fr.wikipedia.org/wiki/Diagnostic_pr%C3%A9implantatoire). 
Avec l'apparition croissante des start-up en génomique, comme [23andMe](https://www.23andme.com/) ou [Helix](https://www.helix.com/) qui s'affranchissent de la barrière médicale, les enjeux éthiques vont vite prendre de l'ampleur. Et les bébés conçus à la carte sur internet seront peut-être monnaie courante.   
D'autre part, l'éradication des maladies génétiques peut paraitre merveilleuse. Mais à l'échelle des populations cela implique la diminution de la diversité génétique et donc une diminution de notre capacité d'aptation dans l'évolution biologique.  
*[Bienvenue à GATTACCA](https://www.youtube.com/watch?v=7u3RrbNpRUQ)* n'a jamais été aussi proche.

<div class="figure">
    <img src="../images/post26/gattaca.gif" /> 
</div>