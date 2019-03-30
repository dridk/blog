Title: Le paradoxe des tests génétiques 
Slug: le-paradoxe-des-tests-génétiques
Date: 2019-03-22 11:35:45
Modified: 2019-03-22 11:35:45
Status: Draft
Tags: 
Category: 
Author: 
Lang: 
Summary:

myheritage, 23andme etc... vous en avez surement tous entendu parlé . Bien qu'interdit france, cest test génétique en libre accès bénéfice pourtant d'une bonne publicité. 
Depuis peu, elle se fait par l'intermediaire de youtubeurs. SmarterEveryDay, Norman, et recemment DrNormzan ont fait ces tests puis ont partager leurs résultats en vidéo. Devant cette engouement, j'ai voulu voir savoir quel informations était rendu à l'utilisateur et si des diagnostic médicales pouvait en être déduit.   

## Le paradoxe
Car il y a un vrai paradoxe avec les tests génétique ,qu'ils soient réalisé dans un cadre médical ou directement sur internet.
En médecine ces tests sont certainement les analyses les plus controlé de toutes les analyses de biologie médicale. Ils sont sous légide de l'agence de la biomédecine et seulement certain médecin peuvent les préscrire (généticien clinique, certaine spécialités encadrés). Un consentement est obligatoirement demandé au patient et dans certain cas, ils sont testé à plusieurs reprise pour être certain de l'identité.
De l'autre coté, il n'a jamais été aussi facile de faire un test génétique sur internet. Le fait de ne pas avoir besoin de faire une prise de sang les rendent même plus facile qu'une examen classique de biochimie ou d'hematologie. On clique sur un bouton, on recoit un kit salivaire par la poste et le tour est joué.
Pourquoi un tel controle en médecine ? 
Je dirai d'abord à cause du caractère de la génétique à pouvoir prédire des maladies chez des patients en bonne santé. Contrairement à un examen classique qui test des malades, les patients testé en génétique sont souvent en bonne santé. C'est une médecine aussi bien de diagnostic que de prédiction. Retirer les seins d'une femmes en bonne santé parce qu'elle est porteuse d'une mutation génétique est une décision délicate à prendre.    
Ensuite il y a l'hérdité. Vous gènes ne vous appartiennent pas, vous les partagez avec votre famille et vos futurs enfants. Faire un diagnostic chez vous implique de le faire aussi chez les membre de votre famille. Si par exemple vous êtes porteurs d'une mutation pour la maladie d'Huntigton, il est possible que votre frère l'ai hérité aussi. 

## Mais il s'agit juste d'un test de généalogie ? 
 Effectivement, la plus part de ces tests sont vendu à petit prix pour vous donner une estimation sur vos origines. La société myheritage réalise cette prouesse en identifiant 700 000 variations de votre ADN en utilisant une puce SNP (Illumina OmniExpress 24).

### C'est quoi un SNP (pronnoncé snips? 
Un génome humain est constitué de 3 milliards de lettres (A,C,G,T) réparti sur 24 chromosomes différents (1,2...X,Y). Chacune de vos cellules est constitué de 2 versions de ce génome herité de votre mère et de votre père. ( 22 paires de chromosomes + XX ou XY selon que vous êtes un homme ou une femme).
Un Snps est une modification d'une lettre sur un de ces génome par rapport à un génome de référence. Si par exemple, vous avez un A sur le chromosome 3 en position 43224 mais que la référence donne un T à cette même position, alors vous avez un snps qui peut s'écrire : chr3:43224 A > T. Toutes ces variations observé sont référéncé dans la base de donnée dbSNP qui attribue à chaqcun de ces snps un identifiant unique (rs7538305).
Le genotype d'un snps indique si vous porter le variant sur un seul ou sur les deux chromosomes de vos parents. Pour un variant, il y a donc 3 génotypes possibles : 

- chr3:43224 AA  # Vous n'etes pas porteur du snps (homozygote sauvage)
- chr3:43224 AT  # Vous portez le snps à l'état hétérozygote
- chr3:43224 TT  # Vous portez le snps à l'état homozygote 

La technologie de Puce à ADN permet d'identifier les génotypes de milliers de snps préalabmelent choisi. Le fichier brut fourni par myheritage donne l'idenfiant du snps, sa localisation (chromosome, position) et le genotype pour le patient. 

    # Exemple data : source
    rs28678693  1   838665  TT  
    rs4475691   1   846808  CT
    rs72631889  1   851390  TT


## Interpration des variants 
Sur les 3 milliards du génome, il y a chez un individu environs 1 snps tous les 1000 bases qui vous distingue d'un autre individu. La majorité d'eutre eux sont benin, on les appelles polymorphismes. Mais certains peuvent être pathogène. 
En génétique médical on classe ces snps en 5 classes différentes (benin, probablement benin, signification indéterminée, probablement pathogène, pathogène). Cela se fait à l'aide d'arguments plus ou moin fort résumé dans ce qu'on appelle les règle de l'ACMG. Vous pouvez aller jeter un oeil sur le site varsome, pour voir cette classification. Par exemple, les questions à se poser: Est ce que ce variant est déjà décrit dans la littérature ?  Est ce que variant est rare ou fréquent dans la population?  Est ce qu'il est situé dans un gène? Impacte t'il la protéine? Est ce qu'il entraine l'apparition d'un codon stop ? 

# Alors Y a t'il des variants pathogène dans ces tests ?  
Pour répondre à cette questions, j'ai récupéré depuis la base de donnée Clinvar, tous les variants pathogène de classe 5 connu et j'ai fait l'intersection avec les 700 000 snps de la puce illumina OmniExpress 24. Un notebook python est disponnible ici. 
Il en ressort 128 snps. La liste est disponible ici. Parmis ces maladies génétique mais je me contenterai de commenter 2 d'entre elles : 

## La mucoviscidose 
22 snps présent sont identifié comme pathogène pour la mucoviscidose. Il s'agit d'une maladie récessive très fréquente impliquant le gène CFTR situé sur le chromosome 7. C'est à dire que le snp doit être à l'état homozygote pour entrainer la maladie. Un patient hétérozygote est porteur sain et a un risque d'1 sur 2 de transmettre le snps à son enfant. 
On trouve par exemple le snp rs75961395 correspondant à la mutation c.254G>A Gly85Glu décrit dans la base de donnée CFTR-France.https://cftr.iurc.montp.inserm.fr/cgi-bin/affiche.cgi?variant=c.254G%3EA&provenance=0
Elle fait partis des 30 mutations les plus fréquente que l'on recherche systématiquement en routine. Mais elle represente moin de 1% des mutations, loin derrière la  mutation DF508, la plus connu et la plus fréquente.

## Prédisposition au cancer 
Si il y a bien des test génétique controlé plus que tous, ce sont les tests d'oncogénétique indiquant la prédisposition au cancer avec une forte pénétrance. C'est à dire qu'en étant porteur de ce type de variant, il y a de forte probabilité pour faire un cancer. La liste de ces gènes sont disponible sur le site de l'Inca. On y trouve le gène le plus médiatisé, à savoir BRCA1/2 impliqué dans le Cancer du sein et de l'ovaire. L'actrice Angelina jolie, porteuse du variant, a eu recour à la chirugie prophylactique.
Sur la puce, j'ai trouvé le snp rs28897743 situé sur le gène BRCA2. Ce variant est identifié comme probablement pathogène, mais sur d'autre base il est identifié comme variant de signification indéterminé.
Il y a également le snps rs721048 associé au cancer de la prostate d'après ce papier. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4500625/. 

## En conclusion
A première vue, il n'y a pas de quoi s'alarmer. Parmis ces 700 000 snps, très peu sont pathogène. Cependant, garder en tête que les bases de données de snps sont très loin d'être exaustif. Chaque jour de nouveau variant sont découvert comme pouvant être impliqué dans une maladie. C'est pour ça, d'ailleurs que ces puces sont utile à la recherche. Vous n'êtes pas à l'abri, que dans 10 ans, ces données révèleront une information importante sur votre santé. 
Je pense en particulier au score de risque polygénique associant la présence de plusieurs SNPs à une maladie. On trouve déjà sur internet ce genre de test pour la maladie d'Alzheimer par exemple. 
Je tiens également signaler à tous ceux qui ont réalisé le test d'éviter de s'essayer à l'autodiagnostique. Si vous avez la moindre inquietude quand à vos résultats, consulter un conseiller un génétique médicale en demandant à votre médecin généraliste. 