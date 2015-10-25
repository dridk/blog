Title: Lire un fichier de séquencage Abif
Slug: fichier-binaire
Date: 2015-04-06 16:25:55
Tags: ab1,fsa,sanger
Category: biologie, bioinformatique,Qt
Author: Sacha Schutz
SIDEBARIMAGE:../images/post8/cover.jpg
Status:draft


Le format ABIF est une spécification de fichier binaire crée par Applied Biosystems permettant de stocker les résultats d'un séquençage capillaire. Des données d'électrophorégrammes *(fichier \*.ab1)*  ou d'analyses en fragments *(fichier \*.fsa)*  peuvent être écris à l'aide de ce format. Plusieurs logiciels existent pour lire ces fichiers mais bien sur, la pluspart sont payant. Pour y remédier j'ai décidé de créer mon propre lecteur de fichier ABIF en Qt/C++. 
Le but cette article n'est donc pas de vous expliquer les données d'un séquencage, mais plutôt de manière plus général, comment extraire des données d'un fichier binaire. En gros, comment à partir de ce fichier, j'obtiens ce graphique. 


## Fichier binaire 

Un fichier binaire est un fichier dont les données sont directement codées en binaire contrairement à un fichier texte ou les données sont représente uniquement par des chaînes de caractères lisible par un humain. 
Lorsque que vous ouvrez un fichier binaire, comme une image png, avec votre editeur de texte, vous vous retrouvez avec une liste de caractère incompréhensible. 


<p align="center">
    <img src="../images/raw_data.jpg">
</p>


Pourtant ces données ont un sens. En effet chaque lettre correspond à 1 octet sous sa représentation en caractère ASCII. et c'est la dedans que nous allons devoir trifouiller pour retrouver notre graphique.  
Avant de mettre les mains dans la cambouille, reprennant quelques base fondamental en informatique.

### La Bit

On peut imaginer la mémoire comme une grande liste de trou ou chacun peut être plein ou vide. On appel chacun de ces trous, un **bit** pouvant prendre soit la valeur 1 (plein) soit la valeur 0 (vide).
Pour sauvegarder de l'information dans cette mémoire, nous avons besoin de savoir le type d'information à stocké. Plus précisément le nombre de possibilité que peut prendre une valeur. Prenons le sexe par exemple. Il existe que 2 possibilités Homme ou Femme. Pour stocker cette information, un seul bit suffit. 0 = Homme et 1 = Femme. Il s'agit ici du type boolean codé sur 1 bit.  
Essayons maintenant avec un caractère en considérant qu'il y a 256 caractères possible. Le meilleur possibilité est d'utiliser 8 bit. En effet, avec 8 bit , nous avons 2^8 = 256 combinaison possible. Il s'agit ici du type char codé sur 8 bit avec l'encodage ASCII. Dans ce cas par exemple, La suite "01000001" correspondra à la lettre "A".  


<p align="center">
    <img src="../images/1octet.png">
</p>

### L'octet ou le byte
La mémoire manipule ces bits par paquet de 8 bit qu'on appelle un **octet** ou **byte**. Il s'agit de l'unité atomatique de la mémoire. C'est une unité indivisible. C'est comme acheter des carottes chez votre primeurs. Il vous les vend uniquement par botte de 8. Impossible d'en acheter une seul.  
Le boolean que nous avons vu plus haut codé sur 1 bit, prend en faite 8 bit d'espace mémoire. Le premier bit contient l'information, les 7 autres sont ignoré.  
L'octet peut être écris sous sa représentation binaire en utisant les symboles "1" et "0". Mais il est plus courrant d'écrire l'octet sous sa representation hexadecimal. En effet, un octet s'écris en utilisant 2 symbole parmis les 16 symboles (1,2,3,4,5,6,7,8,9,A,B,C,D,E,F).



<p align="center">
    <img src="../images/4octet.png">
</p>

### Le boutisme ou byte order
Le boutisme indique le sens de lecture d'un type de donnée. En fonction de l'architecture de l'ordinateur, de type de fichier binaire, les informations peuvent être lu de droite à gauche ou inversement. Imaginez que vous lisez une page d'un livre. Chaques mot représente un type de donné de taille différente. On appelle grand-boutiste (big-endian) lorsque le mot est lu normalement de gauche à droite. Par exemple si nous voulions encoder le mot Leo et l'entier 42, l'organisation des octets seraient le suivant:
<p align="center">
    <img src="../images/bigendian.png">
</p>

A l'inverse, on appelle petit-boutiste (little-endian) lorsque les mots sont lu de droite à gauche. On voit bien dans l'exemple ci dessous, que pour récupéré l'information 42, il est nécessaire de lire l'entier de droite à gauche. Notez également que la notion de byte order n'a de sens que pour les types de donné codé sur plus de 1 octet. Un mot d'une lettre se lit pareil des deux sens, de même qu'avec un type d'un octet comme le char.

<p align="center">
    <img src="../images/littleendian.png">
</p>


### Type de données
Il existe plusieurs type de données avec chacun son codage en mémoire.
Ci dessous un tableau montrant les principaux types utilisés en C++ avec leurs taille en mémoire ainsi que leurs espaces de valeur.  
Si vous êtes curieux, je vous invite à regarder comment un nombre à virgule (float) est stocké sur 32 bit en suivant la norme ISO IEEE754.

<p align="center">
    <img src="../images/typecpp.png">
</p>



### Editeur hexadecimal



Maintenant que les bases sont parfaitement clair, nous allons commencer à decoder notre fichier binaire. Pour cela, nous allons utiliser un éditeur hexadecimal. Il s'agit d'un notepad amélioré, permettant de visualisé clairement les bytes d'un fichier. En plus de voir la représentation des octets sous forme de caractères, comme un notepad classique, l’éditeur hexadécimal va nous permettre de voir les octet sous leurs representation binaire ou hexadecimal. Et nous pourrons également décoder ces octets en fonction d'un type de donnée spécifié (int, float etc...)  
Pour ma part j'utilise le module hexviewer de sublime text. Mais il existe un pleinitude d'autre editeur gratuit :

*  [un editeur libre pour windows : frhed](http://frhed.sourceforge.net/fr/)
*  [l'editeur de KDE Okteta](https://utils.kde.org/projects/okteta/)
*  [Si vous adorez la commande line hexdump](http://brendanzagaeski.appspot.com/0006.html)
*  [xxd]()


<p align="center">
    <img src="../images/hexviewer.png">
</p>



## Spécification du format ABIF 

Avant de se jeter dans les entrailles de notre fichier ABIF, il nous faut le document de spécification du format. Si vous ne l'avez pas, il faudra alors faire de la retro ingénierie et ça risque de prendre de temps. Heuresement elle est [disponible ici.](http://www6.appliedbiosystems.com/support/software_community/ABIF_File_Format.pdf).  
En résumé, les fichier abif sont composé de 3 blocks **HEADER** , **DIRECTORIES** et **DATA** contenant des données binaires avec un sens de lecture de type gros-boutiste. 

<p align="center">
    <img src="../images/abif_spec.png">
</p>

### Header
Le header, toujours en début de fichier, contient une signature sur 4 bytes contenant la valeur 'ABIF' suivi d'un numéro de version sur 2 bytes. Ces deux informations permettent de rapidement vérifier quel type de fichier vous êtes en train de manipuler. Quasiment tous les fichiers binaires utilisent les premiers bytes pour cette tache. Essayer d'ouvrir une image PNG avec votre éditeur hexadécimal, et regarder les premiers bytes.  
Les 28 bytes suivant contiennent une structure **DirEntry** défini plus bas. Elle contient principalement la position (ou offset) du prochain block Directory.

### Directory 
Ce bloque contient une liste de structure **DirEntry** codé sur 28 bytes.
Les fichiers ABIF stock leurs données sous une forme clef valeur. La clef est composé d'un nom et d'un numero. Par exemple en ayant "Dye" comme nom et 2 comme numero, on pourrait accéder à la valeur correspondent avec une fonction comme *getData("Dye",2)*.  
Chaques donnée est représenté à partir d'une structure **DirEntry** définit comme suite : 

        SInt32 name;          //Le nom de la clef. ex: Dye
        SInt32 number;        //Le numero de la clef. ex: 2
        SInt16 elementtype;   //Le type de valeur. ex : char
        SInt16 elementsize;   //la taille du type. ex: char = 1 octect
        SInt32 numelements;   //Le nombre d'élément. ex: 4 lettres = 4 éléments
        SInt32 datasize;      //La taille total de la valeur. ex:4*1 = 4octet
        SInt32 dataoffset;    //La position de la donné dans le fichier ou 
                              //la donné elle meme si sa datasize est 
                              //inferieur a 4 octet
        SInt32 datahandle;    //reservé...

 **name** et **number** corresponde à la clef .  
**elementtype** est le type de variable comme définit dans la spécification. Par exemple le type 7 correspond à un type float 32 bit.  
**elementsize** est une information redondante,(car déjà défini implicitement par le type) donnant la taille du type. Par example le type float à une taille de 4 octet.  
**numelements** indique le nombre d'element. En effet, DirEntry peut faire référence à une unique valeur ou à une liste de valeur. Dans ce dernier cas, le nombre d'element sera superieur à 1. 
**datasize** indique la taille total de la valeur. C'est à dire numelements x elementsize.  
**dataoffset** indique la position de la valeur dans le fichier. En connaissant le nombre d’élément et leurs tailles, nous pouvons extraire un block de donnée précis. Pour économiser de l'espace, lorsque la valeur est plus petite que 4 octets, dataoffset ne contient pas la position mais directement la valeur elle même.

### Data
Tout le reste du fichier contient les données dont la taille est superieurs à 4 octets. C'est à dire , principalement les chaines de caractères et les listes de valeur. La seul facon d'y accéder c'est de connaitre l'offset de depart , le type et le nombre d'element contigu à partir du block Directory.


## Extraction des données en C++ avec Qt5

Place à la pratique! Nous allons extraire une donnée depuis un fichier fsa et l'afficher sous forme d'un graphique. En lisant la documentation, la variable ayant comme nom "DATA" et comme numéro  1 contient le "Channel 1 raw data". C'est cette donnée que nous allons récupéré. Pour cela, on va utiliser du C++ avec Qt5. 


### Création d'une structure AbifDict 
On va avoir besoin d'une structure pour stocker nos directories. Pour éviter de mauvaise surprise, au lieu d'utiliser les type "int", "short .. On va utiliser les type fourni par stdint.h ou la taille reste la même sur n'importe quel plateforme.

    :::c++
    struct AbifDir{
        char name[4];
        int32_t number;
        int16_t elementType;
        int16_t elementsize;
        int32_t numElements;
        int32_t dataSize;
        int32_t dataOffset;
        int32_t dataHandle;
    };

### Ouverture du fichier en mode binaire
On ouvre le fichier dans un QFile en mode lecture seul 

    :::c++

    QFile file("tmp/example.fsa", QIODevice::ReadOnly);
    if (file.isOpen())
    {
            // do stuff
    }




### Extration de l'offset du directories
Comme vu plus haut, il y a un AbifDir dans le header, à partir du 6ème byte , sur 28 bytes. On va simplement se positionner au 6 ème bytes avec ifstream::seekg et lire 28 bytes dans une structure AbifDir avec ifstream::read.
       
    :::c++
    AbifDir headerDir;
    file.seekg(6);
    file->read((char*)(&headerDir), sizeof(AbifDir));

### Le fichier est en gros boutisme....






# references
http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2722627/
http://mylinuxbook.com/hexdump/,      