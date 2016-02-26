Title: La reconnaissance du soi
Slug: reconnaissance_soi
Date: 2016-02-25 16:45:18
Tags: génétique, immunologie
Category: génétique
Status:draft
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/immuno_banner.jpg

Si vous lisez mon blog, vous avez sûrement constater ma tendance à faire des homologies entre l'informatique et la génétique, notamment entre séquence d'ADN et séquence binaire. Dans ce post, nous allons voir une nouvelle homologie tout aussi surprenante : **La reconnaissance du soi**.   
D'un point de vu informatique, Il s'agit de vérifier si un fichier est bien le votre et qu'il n'a pas été modifier par un virus.   
Coté biologique, c'est la même chose. Il s'agit de vérifier si votre cellule est saine et qu'elle n'a pas été infecté par un virus !  
Dans les deux cas nous allons utiliser des "**signatures**" et toutes anomalies dans celle-ci révélera l'imposture.   

## Signature d'un fichier
La *signature* ou *empreinte* d'un fichier est une séquence de caractères associée de façon unique à un fichier. par exemple l'empreinte du fichier **superMario.exe** peut avoir comme empreinte *f6c51c6bb1ce72508313dad3dc3c6776*. Toutes modifications, même minime du fichier entraînera une modification de l'empreinte.   
Pour réaliser cette prouesse, on utilise des [fonctions de hachages](https://fr.wikipedia.org/wiki/Fonction_de_hachage). Les algorithmes [MD5](https://fr.wikipedia.org/wiki/MD5) et [SHA-1](https://fr.wikipedia.org/wiki/SHA-1) sont certainement les plus connus.    
Depuis un terminal [Unix](https://fr.wikipedia.org/wiki/Unix), récupérer l'empreinte de n'importe quel fichier en tapant : 

    md5sum leVraiSuperMario.exe   
    ## Retourne 50e6b5cd621b4f9de2cc78669cd0c350

L'empreinte obtenue est une séquence de 128 bits soit 32 caractères en hexadécimale. La probabilité que deux fichiers aient la même empreinte est très faible. Mais elle existe, ç'est une "*collision*".    
Lorsque vous allez distribuer votre fichier, vous pouvez fournir son empreinte depuis votre page web, pour que les utilisateurs puissent en vérifier  l'authenticité. Par exemple, jeter un œil sur la [page de téléchargement de kubuntu](http://cdimage.ubuntu.com/kubuntu/releases/wily/release/), vous pouvez récupérer les empreintes des images ISO depuis le fichier [MD5SUMS](http://cdimage.ubuntu.com/kubuntu/releases/wily/release/MD5SUMS). 
Les antivirus utilisent également cette outil. Ils peuvent par exemple calculer l'empreinte de l'ensemble de vos fichiers. Si un virus contamine l'un des fichiers, l'empreinte est modifiée et ce cher [Avast](https://fr.wikipedia.org/wiki/Avast!) va se mettre à nous crier dessus !


## Signature d'une cellule 
Quel rapport avec une cellule ? Et bien, la majorité de vos cellules possèdent à leurs surfaces une empreinte formé par le **[complexe majeur d'histocompatibilité](https://fr.wikipedia.org/wiki/Complexe_majeur_d'histocompatibilit%C3%A9)** qu'on appelle plus couramment **CMH**. Toute modification de cette empreinte (par un virus par exemple), sera reconnue par le système immunitaire et déclenchera la mort pour la cellule. C'est également par ce mécanisme que les greffes d'organes sont rejetées, car reconnu comme étrangère. 

### Les molécules du CMH. 
Les molécules du CMH sont des [glycoprotéines](https://fr.wikipedia.org/wiki/Glycoprot%C3%A9ine) situées sur la membrane de la quasi totalité de vos cellules. Leurs rôles est de présenter des courts fragments peptidiques au système immunitaire. Il en existe différentes codées par des gènes localisés sur le bras court du chromosome 6 et regroupés en plusieurs classes. Dans ce post, nous nous intéressons uniquement à la [classe I](https://fr.wikipedia.org/wiki/Complexe_majeur_d'histocompatibilit%C3%A9#CMH_de_classe_I), composée des 3 gènes: [HLA-A](http://www.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000206503;r=6:29941260-29945884), [HLA-B](http://www.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000234745;r=6:31353872-31357188) et [HLA-C](http://www.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000204525;r=6:31268749-31272130).  
Ces gènes codent chacun pour une glycoprotéine membranaire composé d'un pochoir ou se lie un peptide par complémentarité. Il s'agit donc d'une liaison spécifique, c'est à dire que les molécule HLA-A ne fixe pas les mêmes peptides que les molécule HLA-B. 

### La fonction de hachage cellulaire 
Une cellule est définie par ses constituants. Dans notre cas, c'est l'ensemble des protéines synthétisées par la cellule qui participera à la création d'une empreinte. Ces protéines sont découpées en petit fragment de 9 acides-aminées par le [protéasome](https://fr.wikipedia.org/wiki/Prot%C3%A9asome). Ceux-ci se fixe ensuite par complémentarité sur les molécules du CMH à destination de la membrane cellulaire.    
La combinaison des peptides présentée à la surface est la signature ou l'empreinte de la cellule.  

<p align="center">
    <img src="../images/post14/cell_hla.png">
</p>

### La reconnaissance du CMH
Les [lymphocytes T cytotoxiques](https://fr.wikipedia.org/wiki/Lymphocyte_T_cytotoxique) (TCD8) sont des globules blancs dont la mission est de tester l'intégrité des cellules en vérifiant leurs CMH par leurs récepteurs TCR. Ils reconnaissent à la fois la molécule du CMH et le peptide associé.   
Au cours de la formation du système immunitaire, par un mécanisme encore non élucidé, les lymphocytes T deviennent tolèrent aux peptides du soi. C'est à dire aux peptides présentés normalement par le CMH.   
Plus tard, lors d'une infection par un virus, celui-ci génère de nouvelles protéines dans la cellule, dont les fragments se retrouvent présentés aux lymphocytes T via le CMH. Les lymphocytes reconnaissent alors l'intrusion, et peuvent sonner l'alarme déclenchant tout une cascade de processus aboutissant à la destruction des cellules infectées.   


<p align="center">
    <img src="../images/post14/lymphoT.png">
</p>


### Le polymorphisme du CMH 
Du point de vue d'un virus, la meilleur façon de réussir son intrusion, c'est de le faire incognito. C'est à dire en produisant des protéines non reconnues par les molécules du CMH, qui ne peuvent donc plus présenter les [antigènes](https://fr.wikipedia.org/wiki/Antig%C3%A8ne) viraux (peptide) aux lymphocytes. Pour contrecarrer ces plans, C'est à l’échelle des populations qu'il faut raisonner. C'est la population qui s'adapte au virus et non l'individu.   
La variation allélique du CMH dans la population est la plus grande du génome. Il existe [tableau] 1519 allèles du gène HLA-A, 2069 HLA-B et 1016 HLA-C. En rajoutant les allèles maternelles et paternelles, le nombre de combinaison pour chaque individus est énorme. C'est à dire que deux individus non-apparentés ont une chance infime d'avoir l'ensemble de leurs molécules du CMH identique. En prenant l'ensemble des molécules HLA de toute la population, aucune protéine virale ne peux se cacher.    
Tel une armé de soldat possédant chacun une arme différente, chaque individu possède une combinaison unique capable potentiellement de reconnaître les protéines virales. Ça passe ou ça casse ! Les individus qui réussisse à reconnaître le virus sont sélectionnés avec leurs allèles, et vont à leur tour enrichir le patrimoine des gènes du CMH.  

<p align="center">
    <img src="../images/post14/frequence.jpg">
</p>

### Greffe et rejet 
La variation allélique des gènes du CMH permette à une population de lutter contre un virus. En contrepartie, cela pose problème lors des greffes d'organes. Nous l'avons vu plus haut, les lymphocytes T reconnaissent aussi bien le peptide que la molécule du CMH. Un organe d'un donneur, ne possède pas les même molécules HLA que le receveur. Il en va que cette greffe sera reconnu comme étrangère par les lymphocytes T du receveur. Pour y remédier, on peut utiliser des immunosuppresseurs qui vont museler le système immunitaire. Mais c'est surtout la recherche d'une [compatibilité HLA](http://biblio.hmr.qc.ca/ciup/Publications_pdf/T/typage_hla_onc011.pdf) qui est systématiquement recherché lors d'une greffe. Plus les allèles sont proche et moins le rejet sera sévère. On cherche donc à typer le profil HLA du donneur et du greffé. On s'aide d'une nomenclature international défini sur [hla.alleles.org](http://hla.alleles.org/) et qui donne un identifiant pour chaque gène HLA. La figure suivante identifie un allèle pour le gène HLA-A. 

<p align="center">
    <img src="../images/post14/nomenclature.png">
</p>

## Conclusion 
J'espère que vous avez saisi quelque chose, même partiellement en lisant ce post. L'immunologie est une discipline assez complexe, et il m'est difficile de tout résumer en quelque ligne.   
Retenez que chaque cellule dispose d'une empreinte composé de peptide et de molécule HLA. Toutes modifications soi du peptide ( virus ) soit du HLA ( greffe) est reconnu comme étranger et entraîne l'activation du système immunitaire.   

## Références 
* [Le complexe majeur d'histocompatibilité](http://www.assim.refer.org/raisil/raisil/L02_files/page82-4.-complexe-majeur-d0027histocompatibilite.pdf)
* [The antibody, T cell receptor and MHC loci](http://nfs.unipv.it/nfs/minf/dispense/immunology/lectures/files/loci_abs_tcr_mhc.html
)
* [HLA nomenclature](http://hla.alleles.org/)
* [Typage HLA pour tous](http://biblio.hmr.qc.ca/ciup/Publications_pdf/T/typage_hla_onc011.pdf)


## Remerciement 


