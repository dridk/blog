Title: La thérapie cellulaire adoptive 
Slug: therapie-cellulaire-adoptive
Date: 2017-09-07 23:34:32
Tags: thérapie génique,immunologie
Category: biologie
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/editing_banner.jpg
Status: Draft

C'était [la news](https://www.novartis.com/news/media-releases/novartis-receives-first-ever-fda-approval-car-t-cell-therapy-kymriahtm-ctl019) de la semaine dernière. La première thérapie génique appelée **Kymriah™** a été autorisée aux États-Unis par la [FDA](https://fr.wikipedia.org/wiki/Food_and_Drug_Administration) dans le traitement d'un cancer, en l'occurrence la [leucémie aiguë lymphoblastique](https://fr.wikipedia.org/wiki/Leuc%C3%A9mie#Leuc.C3.A9mies_aigu.C3.ABs_lymphoblastiques). 
Ce traitement est une [immunothérapie](https://fr.wikipedia.org/wiki/Immunoth%C3%A9rapie) et va plus loin que l'immunothérapie classique à base d'anticorps [anti-CTLA4](https://fr.wikipedia.org/wiki/Ipilimumab)/[anti-PD1](https://fr.wikipedia.org/wiki/Nivolumab) ([Voir la vidéo sur le cancer](https://www.youtube.com/watch?v=gxtqGhhomQE) de [@scienceEtonnante](https://www.youtube.com/user/ScienceEtonnante), il en parle dans sa conclusion).    
Elle repose sur ce qu'on appelle un « [transfert adoptif de cellules](https://fr.wikipedia.org/wiki/Transfert_adoptif_de_cellules) »: 

- on prend les cellules immunitaires du patient ([lymphocyte T](https://fr.wikipedia.org/wiki/Lymphocyte_T))
- on les modifie génétiquement pour qu'ils ciblent les cellules cancéreuses 
- puis on les réinjecte au patient. 

Génial non ? Alors, voyons de plus près comment fonctionne cette thérapie étape par étape.

<div class="figure">     <img src="../images/post28/etapes.jpg" />      <div class="legend">Schéma résumant les étapes de la thérapies. Chaque étape est décrit dans le texte <br/> <a href='http://clincancerres.aacrjournals.org/content/22/8/1875'>source de l'image</a></div> </div>

## Étape 1 : Leucophérèse et récuperation des lymphocytes T
La première étape consiste à extraire du sang, les lymphocytes T.
On réalise pour cela une [leucophérèse](https://en.wikipedia.org/wiki/Leukapheresis). C'est un peu comme une prise de sang, sauf qu'ici tous les globules blancs ([leucocytes](https://fr.wikipedia.org/wiki/Leucocyte)) sont filtrés et le reste (globule rouge, plaquettes ...) retourne directement dans la circulation sanguine.   
De ces leucocytes, on récupère les lymphocytes T en utilisant [différentes techniques](http://e-sante.futura-sciences.com/_forum/separation-cellules-sang.html) de séparation comme la centrifugation ou encore des [billes magnétiques couplées à des anticorps spécifiques](https://www.ncbi.nlm.nih.gov/pubmed/17680228).

## Étape 2 : Culture cellulaire
À partir de là, on a besoin de mettre les cellules en culture pour qu'elles se divisent . Un pré-requis pour la [transfection virale](https://fr.wikipedia.org/wiki/Transfection) qui fera suite.   
À l'état normal, les cellules T se divisent après activation par des [cellules présentatrices d'antigènes](https://fr.wikipedia.org/wiki/Cellule_pr%C3%A9sentatrice_d%27antig%C3%A8ne) ou [dendrocytes](https://fr.wikipedia.org/wiki/Cellule_dendritique) (voir [les supers vidéos de @unPeuPointu](https://www.youtube.com/watch?v=Mpn87TQbRJE)). On pourrait en ajouter, mais le risque c'est qu'au moment de la réinjection au patient, ces cellules étrangères déclenchent un rejet immunitaire. On préfère alors utiliser des billes magnétiques recouvertes d'anticorps qui se font passer pour des dendrocytes artificielles. Après l'activation, il suffira de les enlever avec un aimant. 

## Étape 3 : Transfection virale et récepteurs chimériques 
C'est maintenant que la manipulation génétique commence. [Un virus ARN](https://fr.wikipedia.org/wiki/Virus_%C3%A0_ARN) utilisé comme vecteur, va venir intégrer un gène dans le génome du lymphocytes T pour qu'il exprime à sa surface un récepteur chimérique appelé [CAR (Chimeric antigen recepteur)](https://fr.wikipedia.org/wiki/R%C3%A9cepteur_antig%C3%A9nique_chim%C3%A9rique) capable de reconnaitre les cellules tumorales. C'est le même mécanisme qu'avec n'importe quel virus ARN comme le [VIH](https://fr.wikipedia.org/wiki/Syndrome_d%27immunod%C3%A9ficience_acquise). 

<div class="figure">     <img src="../images/post28/biobiz.jpg" />      <div class="legend">Transfection virale de l'ADN du récepteur chimérique CAR<br/><a href='http://www.the-scientist.com/?articles.view/articleNo/42462/title/The-CAR-T-Cell-Race/'>source de l'image</a></div></div> 

Les *CAR* ou *CAR-T* sont dit chimérique car ils sont constitués artificiellement d'un domaine extramembranaire similaire à la portion variable des anticorps. Et d'une partie intracytoplasmique similiaire aux [recepteurs des cellules T](https://fr.wikipedia.org/wiki/R%C3%A9cepteur_des_cellules_T)  permettant de déclencher le signal d'activation du lymphocyte (un motif [ITAM](https://fr.wikipedia.org/wiki/Motif_d%E2%80%99activation_des_r%C3%A9cepteurs_immuns_bas%C3%A9_sur_la_tyrosine) pour les connaisseurs).   


<div class="figure">     <img src="../images/post28/CAR-t.jpg" />      <div class="legend">Representation d'un CAR (Chimeric antigen recepteur). En orange le domaine variable (scFC : single chain variable fragment) qui reconnait l'antigène tumoral. Et en bleu la partie intra-cellulaire qui déclenche l'activation du lymphocyte.<br/><a href='http://www.the-scientist.com/?articles.view/articleNo/42462/title/The-CAR-T-Cell-Race/'>source de l'image</a></div> </div>


<div class="figure"> <img src="../images/post28/car.gif" />      <div class="legend"> Il existe différents types de CAR-t<br/><a href='https://jitc.biomedcentral.com/articles/10.1186/s40425-017-0230-9'>source de l'image</a></div></div>

Dans le cas du **Kymriah™**, les *CAR-T* sont conçus pour qu'ils reconnaissent spécifiquement les antigènes [CD-19](https://en.wikipedia.org/wiki/CD19) présent à la surface des cellules cancéreuses (mais aussi des [lymphocytes B normaux](https://fr.wikipedia.org/wiki/Lymphocyte_B)). Lorsque ces nouveaux lymphocytes T génétiquements modifiés seront en contacte avec les cellules cancereuses, ils s'activerons et entrainerons une réponse immunitaire ciblée. 

## Étape 4 : Préparation du produit  
Il ne reste plus qu'à préparer nos cellules pour l'injection. Les billes magnétiques sont retirées. Les microbes éliminés en utilisant des rayons UV. Etape critique, car on s'apprete à réinjecter un produit dans la circulation du patient. 

## Étape 5 : Adminstration au patient
Les lymphocytes T génétiquement modifiés sont administrés au patient. En général, le patient est préparé à recevoir le traitement avec une chimiothérapie lympho-déplétive. L'activation des cellules T est aussi soutenue par l'administration d'[interleukine-2](https://fr.wikipedia.org/wiki/Interleukine_2), une molécule stimulant les lymphocytes T.     
Quant aux effets indésirables, ils existent. Le relargage excessif des cytokines par les lymphocytes T activés est responsable du [syndrome de relargage des cytokines](http://dictionnaire.doctissimo.fr/definition-syndrome-de-relargage-des-cytokines.htm). Et n'oublions pas que ces CAR-T anti-CD19 cible également les lymphocytes B avec le risque d'un déficit de l'immunité.


<div class="figure">     <img src="../images/post28/juno-leukapherisis.jpg" />      <div class="legend">Résumé général</div> </div>


# Et l'efficacité du traitement ? 
D'après [cette étude](, https://jhoonline.biomedcentral.com/articles/10.1186/s13045-017-0423-1, ), l'efficacité des *CAR-T* anti-CD19 est vraiment bonne avec **90%** de rémission complète dans la leucémie lymphoïde aiguë.     
D'autres chercheurs ont déjà essayé la thérapie cellulaire adoptive sur d'autres cancers, notamment les cancers solides. Des résultats concluants ont déjà été obtenu dans le mélanome metastatique. Dans ce cas, les lymphocytes expriment un récepteur reconnaissant des antigènes spécifiques du mélanome ([MART-1](https://en.wikipedia.org/wiki/MLANA)).      


Malheureusement la complexité technique de ces thérapies personnalisées rend inaccessible le traitement. Le Kymiria couterait environ 475 000 dollars!!!
Avec ce nouveau traitement sur le marché, il y a de quoi creuser les inégalités dans la santé... surtout aux Etats-unis.



# Reference

- [Principes de la thérapie cellulaire par transfert adoptif à base de Tumor Infiltrating Lymphocytes](https://www.revmed.ch/RMS/2016/RMS-N-519/Principes-de-la-therapie-cellulaire-par-transfert-adoptif-a-base-de-Tumor-Infiltrating-Lymphocytes)
- [CAR T Cells: Engineering Patients’ Immune Cells to Treat Their Cancers](https://www.cancer.gov/about-cancer/treatment/research/car-t-cells)
- [Current approaches to increase CAR T cell potency in solid tumors: targeting the tumor microenvironment](https://jitc.biomedcentral.com/articles/10.1186/s40425-017-0230-9)
- [Safe engineering of CAR T cells for adoptive cell therapy of cancer using long‐term episomal gene transfer](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4931286/)
- [Chimeric antigen receptor T cells: a novel therapy for solid tumors](https://jhoonline.biomedcentral.com/articles/10.1186/s13045-017-0444-9)

@Merci aux relecteurs