Title: Transférer des données avec un code fontaine
Slug: code-fontain
Date: 2024-09-30 19:30:31
Modified: 2024-09-30 19:30:31
Tags: algorithme
Category: informatique
Author: Sacha schutz
SIDEBARIMAGE:images/common/term_banner.jpeg


Avec toutes les attaques informatiques que l'on connait aujourd'hui, 
les environnements de travail pour accéder à des données sensible sont devenu très restreint.
Un datascientist qui doit manipuler ce genre de données aura par exemple accès uniquement à un bureau 
virtuel disposant d'une instance de Jupyter. Il ne pourra travailler que dans cette environement 
sans pouvoir télécharger ces données sur sa machine. 
Du coup, je me suis posé la question suivante : Est ce qu'un hacker pourrait récupérer
l'intégralité d'un gros fichier CSV depuis un bureau virtuel uniquement en faisant des captures
d'ecran ? La réponse est bien sur oui, et nous allons voir comment faire cela en utilisant 
des QR codes animées et un code fontaine.

## Encoder des données dans un QR Code

J'ai d'abord essayer de voir si il était possible d'encoder de l'information dans une grosse 
image avec plein de couleur que l'on récupererait avec un screenshot. Mais ce n'est pas possible,
ou difficilement, car les données derrière l'image s'affichant sur votre écran sont différentes 
des données de l'image original. En effet, votre moteur de rendu va changer la valeurs des pixels 
en rajoutant par exemple de l'anti-aliasing ou en utilisant une autre palette de couleur.     
Du coup, je me suis tourner vers les QR-codes plus simple à mettre en place.   
Au maximum, il est possible de stocker 2853 octets dans un QR Code en version 40, c'est à dire avec une 
résolution de 177x177 modules carrés et un faible niveau de correction d'erreur.
Pour encoder un fichier de 10 Mo, ça va être difficile. Sauf, si on crée une animation de QR-code. 
C'est ce que vous pouvez voir dans l'animation suivante : 



## Transférer des données de manière unidirectionnelle avec  un code fontaine
Placons nous maintenant du coté du recepteur. Il suffirait en principe de faire des capture d'ecran toutes les 0.01 ms , de décoder 
chaque QR-Code et de reconstruire le fichier. Sauf que ça, c'est dans un monde idéal ou aucun QR code n'est perdu et arrivent tous
dans le bon ordre. Dans des protocoles classiques de communication réseau comme TCP/IP, pour éviter cela, 
le recepteur envoie une confirmation à l'emetteur qui lui retransmettra les paquet perdu si besoin. Dans notre cas, ce n'est pas 
possible car le signal est unidirectionnel. Une solution serait de demander à l'emetteur de répéter sans arret tout en labelisant 
ses paquets pour que le recepteur puisse tous les récupérer dans le bon ordre. Mais ca risque d'être long. En perdant le paquet 
numéro 2200 , il faudra attendre que l'emetteur rejoue toute la serie pour le récupérer. 
C'est la qu'intervienne les codes fontaines et notamment le code LT ( Luby Transform codes ) que nous allons utilisé. 

### Fonctionnement de l'algorithme 
- Le fichier binaire que vous souhaitez transférére est divisé en bloc de N bytes.
- Pusieurs blocs sont ensuite choisi aléatoirement. Le nombre de bloc (d) est défini par une distribution de probabilité ( Soliton distribution)
- Les blocs sont combiné ensemble par un operateur XOR. SI le recepteur possède assez de bloc, il peut reconstruire les blocs manquants.

Je ne me suis pas embeter à réimplementer l'algorithme. Il est disponnible dans va la librarie rt. Le code pour encoder 
et decoder  une chaine chaine de bytes est le suivant : 

/decoder/encoder


## Mise en place 

Nous avons tous les ingrédients pour réaliser une exfiltration de données depuis un notebook Jupyter avec des captures d'ecran ;

### Emetteur 

Je souhaite transférér un fichier de 10 Mo. Je le lis par block de N bytes que je vais donner à manger à mon encodeur
LT. Ce dernier me restitue des nouveaux blocs que je peux alors encoder dans un QR Code.



### Recepteur 
Pour cela, j'ai crée une petite application Qt, qui me permet de capturer une region spécifique de mon ecrant 
pour détécter le QRCode, le décoder avec le code LT et me sauvegarder le tout dans un fichier. 

screenshot 



### Resultats 

1 Mo
10 mo
100 Mo 


### Conclusion 
Bien que les débits sont faibles, c'est tout à fait correct pour des petits fichiers. Je pense qu'il serait possible d'augmenter 
le debit en utilisant tout l'espace de l'ecran avec plusieurs QR code en parallele.
Mais on sera toujours limite par la fréquence de rafraichissement et de lecture du QR Code. 








 












