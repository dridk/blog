Title: Le transfert adoptif de cellules immunitaires génétiquement modifié
Slug: transfert-adoptif
Date: 2017-09-01 21:36:32
Tags: rna-seq,single-cell,microfluidique
Category: biologie
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg
Status: Draft

C'etait [la news](https://www.novartis.com/news/media-releases/novartis-receives-first-ever-fda-approval-car-t-cell-therapy-kymriahtm-ctl019) de la semaine dernière. La première thérapie génique appelé *Kymriah(TM)* à été autorisé au états-unis par la [FDA](https://fr.wikipedia.org/wiki/Food_and_Drug_Administration) dans le traitement d'un cancer, en l'occurence la [leucémies aiguës lymphoblastiques](https://fr.wikipedia.org/wiki/Leuc%C3%A9mie#Leuc.C3.A9mies_aigu.C3.ABs_lymphoblastiques). 
Ce traitement est une [immunothérapie](https://fr.wikipedia.org/wiki/Immunoth%C3%A9rapie) qui va plus loin que la simple utilisation d'anticorps [anti-CTLA4](https://fr.wikipedia.org/wiki/Ipilimumab)/[anti-PD1](https://fr.wikipedia.org/wiki/Nivolumab). ([Voir la vidéo](https://www.youtube.com/watch?v=gxtqGhhomQE) de [@scienceEtonnante](https://www.youtube.com/user/ScienceEtonnante), il en parle dans sa conclusion).
Elle repose sur ce qu'on appelle un "[transfert adoptif de cellules](https://fr.wikipedia.org/wiki/Transfert_adoptif_de_cellules)". On prend vos cellules immunitaires ([lymphocyte T](https://fr.wikipedia.org/wiki/Lymphocyte_T)), on les modifient génétiquement pour qu'ils ciblent les cellules cancereuses, et on vous les reinjecte directement. Génial non ?     
Alors voyons de plus près comment fonctionne cette thérapie étapes par étapes.

# Thérapie cellulaire adoptive 


<div class="figure">     <img src="../images/post28/etapes.jpg" />      <div class="legend">Etapes...</div> </div>

## Etape 1 : Leucophérèse et enrichissement des lymphocytes
La première étape consiste à extraire du sang les lymphocytes T.
On réalise alors une [leucophérèse](https://en.wikipedia.org/wiki/Leukapheresis). C'est un peu comme une prise de sang, sauf qu'ici tous les globules blancs ([leucocytes](https://fr.wikipedia.org/wiki/Leucocyte)) sont filtré et le reste (globule rouge, plaquettes ...) repasse directement dans la circulation sanguine.   
De ces leucocytes, on récupère les lymphocytes T en utilisant [différentes techniques](http://e-sante.futura-sciences.com/_forum/separation-cellules-sang.html) comme la centrifugation ou des [billes magnétiques couplé à des anticorps spécifiques](https://www.ncbi.nlm.nih.gov/pubmed/17680228).

## Etape 2 : Activation et culture des cellules 
A partir de là, on a besoin que les cellules se divisent. Un pré-requis pour la [transfection virale](https://fr.wikipedia.org/wiki/Transfection) qui viendra ensuite.   
A l'état normale, les cellules T se divisent après activation par des [cellules presentatrices d'antigènes](https://fr.wikipedia.org/wiki/Cellule_pr%C3%A9sentatrice_d%27antig%C3%A8ne) ou [dendrocytes](https://fr.wikipedia.org/wiki/Cellule_dendritique) (Voir [les supers vidéos de @unPeuPointu](https://www.youtube.com/watch?v=Mpn87TQbRJE)). on pourrait en ajouter, mais le risque c'est qu'au moment de la réinjection au patient, ces cellules étrangère déclenchent un rejet immunitaire. On préfère alors utiliser des billes magnétique recouvert d'anticorps qui se font passer pour des dendrocytes artificielles. Après l'activation, il suffit de les enlever avec un aimant. 

## Etape 3 : Transfection virale de recepteur chimerique 
C'est maintenant que la manipulation génétique intervient. [Un virus ARN](https://fr.wikipedia.org/wiki/Virus_%C3%A0_ARN) utilisé comme vecteur, va venir infecter tous ces lymphocytes T pour qu'ils expriment à leurs surface un recepteur chimerique appelé [CAR (Chimeric antigen recepteur)](https://fr.wikipedia.org/wiki/R%C3%A9cepteur_antig%C3%A9nique_chim%C3%A9rique). Ces virus contiennent le gène du recepteur CAR qui vont venir s'intégré au génome de la même manière que le ferai le Virus du [SIDA](https://fr.wikipedia.org/wiki/Syndrome_d%27immunod%C3%A9ficience_acquise). 

<div class="figure">     <img src="../images/post28/biobiz.jpg" />      <div class="legend">Etapes...</div> </div>


Les CARs sont constitué artificielement d'un domaine extramembranaire similaire à la portion variable des anticorps et d'une partie intracytoplasmique permettant de déclencher le signal d'activation des lymphocytes T ( un motif [ITAM](https://fr.wikipedia.org/wiki/Motif_d%E2%80%99activation_des_r%C3%A9cepteurs_immuns_bas%C3%A9_sur_la_tyrosine) pour les connaisseurs).   


<div class="figure">     <img src="../images/post28/CAR-t.jpg" />      <div class="legend">Etapes...</div> </div>

<div class="figure">     <img src="../images/post28/car.gif" />      <div class="legend">Etapes...</div> </div>

Dans le cas du *Kymriah(TM)*, les CAR-T sont concu pour qu'ils reconnaissent spécifiquement les antigènes [CD-19](https://en.wikipedia.org/wiki/CD19) présent à la surface des cellules cancereuses ... mais aussi des [lymphocytes B normaux](https://fr.wikipedia.org/wiki/Lymphocyte_B). 

## Etape 4 : Netoyage et préparation 
Il ne reste plus qu'à préparer nos cellules pour l'injection. Les billes magnétiques sont retiré. Les microbes éliminés par des rayons UV. 
Le tout emballé pesé prêt pour la livraison. 

## Etape 5 : Adminstration au patient
Les lymphocytes T génétiquement modifié sont administré au patient. En général le patient est préparé à recevoir le traitement avec une chimiothérapie lympho-déplétive. L'activation des cellules T est aussi soutenu par l'administration d'[interleukine-2](https://fr.wikipedia.org/wiki/Interleukine_2) une molécule stimulant les lymphocytes T.     
Quand aux effets indésirable, ils existent. Le relargage excessifs des cytokines par les lymphocytes T activé est responsable du [syndrome de relargage des cytokines](http://dictionnaire.doctissimo.fr/definition-syndrome-de-relargage-des-cytokines.htm). Et n'oublions pas que CAR-T anti-CD19 ciblent egallement les lymphocytes B avec un risque de déficit immunitaire. 


# Et alors ça marche ? 
D'après [cette étude](, https://jhoonline.biomedcentral.com/articles/10.1186/s13045-017-0423-1, ) l'efficacité des CAR-T anti-CD19 est vraiment bonne avec 90% de remission complete dans la leucemie lymphoïde aigu.     
D'autre chercheurs ont déjà essayer la thérapie cellulaire adoptive sur d'autre cancer notamment les cancers solide. Des résultats concluant sont déjà obtenu dans le mélanome metastatique. Dans ce cas, les lymphocytes expriment unun recepteur reconnaissant des antigènes spécifique au mélanome ([MART-1](https://en.wikipedia.org/wiki/MLANA)).   
Malheuresement la complexité technique de ces thérapies personnalisés rend innaccessible le traitement. Le Kymiria couterait environs 475 000 dollars!! De quoi creuser les innégalités dans la santé. 




<div class="figure">     <img src="../images/post28/juno-leukapherisis.jpg" />      <div class="legend">Résumé général</div> </div>





# Culture et transfection de CAR-T 
## Les CAR-T et les anti 19 

# Traitement 

side effect 
relargage en execes de cytokines ( cytokine release syndrome)
mort de plein de lymphocyte  ( voir aplasie).
oeudeme cerebrale


Ca parlait d'immunothérapie dans la video de .. 

La thérapie cellulaire adoptive est une forme d'immunothérapie tout récente. 
Isolement, expansion clonale in vitro, reinfusion 
Les premiere test concluant était pour le mélanome metastqtiaue.
Un recepteur chimérique antigénique ( CAR ) .

La therapie cellulaire adaptive : 

Lentivirus ++ / gamma retrovirus 

etape 1 : leukopherese : On enleve les globule blanc et on reinjecte le reste 
etape 2 : enrichissement en cellule T ( centrifugeuse celle by size density)
etape 3 : seperation des CD4/CD8




Immunothérapie
transfert adoptif de cellule: transferer des fonction immunitaire
CAR-t

Adoptive cell therapy (ACT) is a novel tool in the fight against cancer. In particular T-cells engineered to express Chimeric Antigen Receptors (CARs) have demonstrated recent significant clinical efficacy with improvements in patient outcomes for a number of hematological malignancies [1, 2, 3, 4]. CARs are synthetic molecules composed of an extracellular binding domain, a transmembrane domain and an intracellular signaling/activation domain. The extracellular component consists of the light and heavy chain regions derived from an antibody to form a single chain variable fragment (scFv), and serves to recognize and bind specific tumor-associated antigens (TAAs) in a MHC-independent manner. A hinge domain, typically derived from CD8 or IgG4 molecules, connects this module with the intracellular one. This last portion is formed by CD3ζ segment which is responsible to trigger T-cell activation. The first generation of CAR vectors was designed with CD3ζ domain alone. Second and third generations added to CD3ζ one or two costimulatory domains (CD28 and/or 4-1BB) respectively (Fig. 1). All these components are typically inserted using γ-retroviral or lentiviral transduction systems. Although silencing of LTR-driven transgenes has been known to occur in other tissues, vector silencing was not observed in one study of human lymphocytes [5]. Interestingly, one study showed that efficacy of CAR T cells in vivo is a function of the density of CAR expression, and that this can have a substantial impact on antitumor efficacy and persistence of CAR T cells both systemically and at the tumor site [6].

therapeutic outcome depends on long‐term expression of CAR transgene in T cells, which is achieved by delivering transgene using integrating gamma retrovirus (RV) or lentivirus (LV). 

 There are several types of ACT (see “ACT: TILs, TCRs, and CARs”), but the one that is closest to producing a treatment approved by the Food and Drug Administration (FDA) is called CAR T-cell therapy.


linique des anticorps monoclonaux anti-CTLA-4 (ipilimumab) et anti-PD-1 (pembrolizumab et nivolumab), 


antitumor activity, and cytokine secretion (such as IL-2, TNFα, and IFN-γ) of T cell (Fig. 1) [7, 8]. Currently, anti-CD19 CAR-T cells were demonstrated to be effective in the treatment of B cell non-Hodgkin lymphoma (NHL), acute lymphoblastic leukemia (ALL), and chronic lymphocytic leukemia (CLL) [9, 10, 11, 12, 13]. Anti-CD116 has been developed for treating myelomonocytic leukemia [14].


# Conclusion 
La complexité technique , thérapie personnalisé rend innaccessible le traitement.

https://www.revmed.ch/RMS/2016/RMS-N-519/Principes-de-la-therapie-cellulaire-par-transfert-adoptif-a-base-de-Tumor-Infiltrating-Lymphocytes

https://www.cancer.gov/about-cancer/treatment/research/car-t-cells

https://jitc.biomedcentral.com/articles/10.1186/s40425-017-0230-9

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4931286/

https://jhoonline.biomedcentral.com/articles/10.1186/s13045-017-0444-9

http://ac.els-cdn.com/S2329050116302029/1-s2.0-S2329050116302029-main.pdf?_tid=b7c71706-93e6-11e7-b31a-00000aab0f6b&acdnat=1504800659_a0480d07f356b279ef7ef77bd923c234

SOURCE images : 
http://clincancerres.aacrjournals.org/content/22/8/1875

efficacité 
https://jhoonline.biomedcentral.com/articles/10.1186/s13045-017-0423-1