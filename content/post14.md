Title: La reconnaissance du soi
Slug: reconnaissance_soi
Date: 2016-02-25 16:45:18
Tags: génétique, immunologie
Category: génétique
Status:draft
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/fingerprint_banner.jpeg

Si vous lisez mon blog, vous avez sûrement constater ma tendance à faire des homologies entre l'informatique et la génétique, et notamment entre une séquence d'ADN et une séquence binaire. Dans ce poste, nous allons voir une nouvelle homologie tout aussi surprenante : La reconnaissance du soi.   
D'un point de vu informatique, Il s'agit de vérifier si un fichier est bien le votre et qu'il n'a pas été modifier par un virus.   
Coté biologique, c'est la même chose, même les mots reste les même! Il s'agit de vérifier si votre cellule est saine et qu'elle n'a pas été infecté par un virus !  
Dans les deux cas nous allons utiliser des "signatures" et toutes anomalies dans celle ci révélera l'imposture.   

## Signature d'un fichier
La signature ou empreinte d'un fichier est une séquence de caractères associée de façon unique à un fichier. par exemple l'empreinte du fichier superMario.exe peut avoir comme empreinte f6c51c6bb1ce72508313dad3dc3c6776. Toutes modifications, même minime du fichier entraînera une modification de l'empreinte.   
Pour réaliser cette prouesse, on utilise des [fonctions de hachages](https://fr.wikipedia.org/wiki/Fonction_de_hachage). Les algorithmes [MD5](https://fr.wikipedia.org/wiki/MD5) et [SHA-1](https://fr.wikipedia.org/wiki/SHA-1) sont certainement les plus connus.    
Depuis un terminal Unix, récupérer l'empreinte de n'importe quel fichier en tappant : 

    md5sum leVraiSuperMario.exe   
    ## Retourne 50e6b5cd621b4f9de2cc78669cd0c350

L'empreinte obtenu est une séquence de 128 bits soit 32 caractères en hexadécimale. La probabilité que deux fichiers aient la même empreinte est très faible. Mais elle existe, et nous appelons ça une "collision".    
Lorsque vous allez vouloir distribuer votre fichier, vous pouvez fournir l'empreinte du fichier sur votre page web, pour que les utilisateurs puissent vérifier de l'authenticité du fichier qu'ils ont récupéré sur bitTorrent. Un exemple, sur la [page de téléchargement de kubuntu](http://cdimage.ubuntu.com/kubuntu/releases/wily/release/), vous pouvez toujours récupérer les empreintes des images ISO depuis le fichier [MD5SUMS](http://cdimage.ubuntu.com/kubuntu/releases/wily/release/MD5SUMS). 
Les antivirus utilisent également cette outil. Ils peuvent par exemple calculer l'empreinte de l'ensemble de vos fichiers. Si un virus contamine l'un fichier, l'empreinte se modifie et notre cher Avast va se mettre à nous gueule dessus !


## Signature d'une cellule 
Quel rapport avec une cellule ? Et bien , une cellule possède également à sa surface une empreinte, grâce au complexe majeur d'histocompatibilité ou encore CMH. Cette empreinte peut être modifier par un virus, ou lorsque la cellule devient cancéreuse. Le système immunitaire peut alors repérer cette modification d'empreinte et entamer la destruction de la cellule. 

Le complexe majeur d'histocompatibilité 
### Le CMH de class 1 
Localisation génétique 
Structures 
Fonction 





## Références 

* [Brief Introduction to STRs](http://www.cstl.nist.gov/biotech/strbase/intro.htm)
* [Les kits commerciaux](http://www.cstl.nist.gov/biotech/strbase/multiplx.htm)
* [Liste des amorces](http://www.cstl.nist.gov/biotech/strbase/primer1.htm)
* [The rarity of DNA profiles](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2585748/)
* [Pour mieux comprendre l'analyse de fragments](https://www.youtube.com/watch?v=43-OQTLtrwQ)

## Remerciement 
* @Piplopp 
* @Oodnadatta 


