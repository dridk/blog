Title: Renommer ses fichiers avec MMV
Slug: mmv
Date: 2015-07-23 22:55:29
Tags: linux
Category: linux
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/term_banner.jpeg

Cela vous est forcément déjà arrivé de devoir renommer une longue liste de fichiers. Pour les plus fainéant d'entre vous, vous allez cliquer sur un fichier, un par un , puis faire "F2" pour renommer. Bon, ça passe, avec 10 fichiers, mais pour certaine personne, renommer plus de 3 fichiers de cette manière c'est déjà trop! Imaginez que vous voulez renommer toutes votre bibliothèque de série légale sous une forme *serie01e04.avi*, vous risquez de passer un bon bout de temps pour un résultat pas garantie. Heureusement, il existe plein de logiciels graphiques gratuits comme [Rename-it](http://sourceforge.net/projects/renameit/) ou [Bulk Rename](http://www.bulkrenameutility.co.uk/Main_Intro.php) pour vous aidez. Mais voilà, nous, on préfère les techniques de Jedi avec notre console Linux pour en mettre plein les yeux à nos copains. 

##MMV : Mass Rename of files 
Comparé à d'autres outils comme **rename**, **mmv** permet de faire des choses simples sans utiliser d'expression régulière! Elle utilise la syntaxe de **bash** avec des étoiles (\*), des points d'interrogation (?) ou encore des crochets ( [] ). Dans la plus part des cas, vous allez faire des choses simples... 
C'est donc l'outil idéal.   
Par exemple, imaginez que nous ayons des fichiers avec l'extension *jpg* que nous voulons renommer en *jpeg* : 

    file_001_loremipsum.jpg  
    file_002_dolor.jpg  
    file_003_sit.jpg  
    file_004_amet.jpg  
    file_105_randomness.jpg  

On utilise alors la commande **mmv** avec la syntaxe *mmv -n "from" "to"*.   
Le paramètre *"-n"* permet d'ignorer la commande et vous affiche uniquement le résultat escompté. Effacez le, une fois satisfait pour appliquer les changements.  

    >mmv -n "*.jpg" "#1.jpeg" 

    file_001_loremipsum.jpg -> file_001_loremipsum.jpeg
    file_002_dolor.jpg -> file_002_dolor.jpeg
    file_003_sit.jpg -> file_003_sit.jpeg
    file_004_amet.jpg -> file_004_amet.jpeg
    file_105_randomness.jpg -> file_105_randomness.jpeg


Le caractère étoile(\*) du *from* est substitué par l'indice *#1*. Il y a autant d'indice que d'étoile. Cela nous permet de faire des trucs marrants comme : 

    >mmv -n "file_*_*.jpg" "#2-file-#1.jpg"

    file_001_loremipsum.jpg -> loremipsum-file-001.jpg
    file_002_dolor.jpg -> dolor-file-002.jpg
    file_003_sit.jpg -> sit-file-003.jpg
    file_004_amet.jpg -> amet-file-004.jpg
    file_105_randomness.jpg -> randomness-file-105.jpg

##Majuscule / Minuscule 

On peut aussi s'amuser à changer la case en rajoutant avant l'indice, un "l" (lowercase) ou "u (uppercase)". 

    >mmv -n "file_*_*.jpg" "#u2-file-#1.jpg"

    file_001_loremipsum.jpg -> LOREMIPSUM-file-001.jpg
    file_002_dolor.jpg -> DOLOR-file-002.jpg
    file_003_sit.jpg -> SIT-file-003.jpg
    file_004_amet.jpg -> AMET-file-004.jpg
    file_105_randomness.jpg -> RANDOMNESS-file-105.jpg

##Autres expressions 
Vous pouvez également utiliser le caractère "?" pour designer un seul caractère et les crochets "[]" pour faire une sélection.  
Imaginons que nous ayons 4 fichiers : 

    1.png
    2.png
    3.png
    4.png

Et que nous voulons renommer uniquement les 3 premières fichiers. Nous utiliserons alors les crochets de cette façon : 

    >mmv -n '[1-3].png' 'test#1.png'

    1.png -> test1.png
    2.png -> test2.png
    3.png -> test3.png

##Autres méthodes 
Pour des choses plus complexe, comme l'utilisation d'expressions régulières, il faudra se tourner vers l'outil *[rename](http://linux.die.net/man/2/rename)* qui reprend la même syntaxe que perl. 


## Référence 
* [MMV man page](http://ss64.com/bash/mmv.html)   
* [Stackoverflow](http://stackoverflow.com/questions/417916/how-to-do-a-mass-rename)

