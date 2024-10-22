Title: Transférer des données avec des captures d'ecrans
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
virtuel munis d'une instance de Jupyter lab pour réaliser ses analyses.  Dans cette bulle, ll 
lui sera impossible de télécharger des données sur son PC. 
Mais en verité, les données qui s'affiche sur nos écrans transitent forcement par votre carte graphique.
Un hacker pourrait très probablement récupérer l'intégralité d'un gros fichier en faisant 
juste des captures d'écran. J'ai donc voulu tester cette théorie en essayant de récupérer un fichier de 10 Mo
disponible depuis un notebook Jupyter en utilisant des QR codes couplé à un algorithme fontaine.  
Voyons voir tout cela de plus près.



## Encoder des données dans un QR Code

J'ai d'abord pensé à encoder l'information dans une image en utilisant tous les pixels et les couleurs 
à disposition. Mais c'est difficilement faisable car les pixels qui s'affichent sur votre écran sont 
différents des pixels encoder dans votre image. En effet, votre moteur de rendu va par exemple ajouter de
l'anti-aliasing qui va modifier la valeur des pixels pour adoucir les contours. 
Du coup, je me suis tourner vers les QR-codes plus simple à mettre en place grâce à un eventail de librarie python.

### Capacité d'un QR Code 
La capacité de stockage d'un QR code varie en fonction de sa version et de son niveau de code d'erreur. 
Dans le meilleurs des cas, nous allons pouvoir stocker 2953 octects en version 40 ( 177 x 177 ) 
en utilisant un niveau de correction d'erreur Low ( 7% ).      
Sauf que moi, j'aimerai bien transférér un fichier de 10 Mo voir plus. Il faut donc généré plein de QR code
et pour cela j'ai fait une animation. Supposions que je génère 30 QR code par secondes, je pourrais récupérér
des données à une vitesse de 720 Kbits/s  (3000 * 30 * 8 * 10**-3) de quoi faire pallir mon bon view modem 56K.
Et voilà ce que ça donne : 

<image> 


## Utilisation du code fontaine
Placons nous maintenant du coté du recepteur. Il suffirait en principe de faire des capture d'ecran toutes 
les 4 ms et décoder chaque QR-Code dans le bon ordre. Mais en réalité, il y a de forte chance d'en rater certain.
Dans des protocoles classiques de communication réseau bi-directionnel comme TCP/IP, chaque capture ou paquet doit 
être confirmer avant de recevoir le prochain. Dans notre cas, ce n'est pas possible 
car la communication est unidirectionnel, nous ne faisons qu'écouter. 
Une solution serait donc de demander à l'emetteur de répéter en boucle son message. Mais attendre un tour complet 
pour récupérer un seul paquet risque d'être long.
Une meilleur idée est d'utiliser un code fontaine, qui consiste à générer aléatoirement des paquets de données labelisé 
et les emettre constamment comme une "fontaine de donnée". Le recepteur aura juste à collecter les paquets 
dans le desordre puis à les réassembler dans l'ordre en utilisant leurs labels.

### Transformation de Luby ou code LT 

Un code LT fonctionne de la façon suivante: 

#### Emetteur 
- Le message à transmettre est d'abord découpé en plusieurs bloc source de la même taille.
- Un tirage aléatoire est ensuite réalisé pour selectionné N bloc source.
- Ce tirage aléatoire suit une distribution de Soliton. ( Voir image )
- Ces N blocs sources sont combiné ensemble avec un operateur XOR pour former un seul bloc . 
- Ce bloc encodé est alors transféré au recepteur en précisant le nombre de bloc source qu'il contient dans un identifiant.
- Dans notre cas, ce bloc est transféré via un QR code en reservant les 12 premiers bytes pour l'identifiant. 

{ Distribution de Solition }


#### Recepteur 
- Le recepteur collecte les paquet encodé en scannant les QR code
- Si le paquet est composé d'un bloc source il le met de coté
- Si le paquet est composé de 2 bloc source, il fera un XOR avec un des paquet déjà recu pour reconstruire le second paquet source.
- Il procède ainsi de suite avec des paquets composés de 3,4..N bloc sources.  
- Lorsqu'il a reçu tout les paquets, il les remet dans l'ordre pour reconstruire le message original.

En combinant les blocs avec un XOR, cela nous permet d'envoyer statistiquement beaucoup moins de bloc que la méthode naïves
qui consisterai à les envoyer un par un.  

## Mise en place 

Nous avons maintenant tous les ingrédients pour construire un canal de communication entre un notebook Jupyter
et mon système de fichier. Nous allons tenter d'exfilter un fichier parquet de N lignes pour un total de 10 Mo. 

### Emetteur 

J'utilise la librarie qrcode pour générer mes QR-code et la librarie lt-code pour le code fontaine. 
Pour l'animation, je fais une boucle for avec une pause de 0.01 secondes.


```python
def send_file(filename:str):
  chunk_size = 2200

  with open(filename , "rb") as file:

      for block in encode.encoder(file, chunk_size):
          qr = qrcode.QRCode(version=40, box_size=3, error_correction=qrcode.ERROR_CORRECT_L, )
          encoded_data = base64.b64encode(block).decode('utf-8')

          
          qr.add_data(encoded_data)
          img = qr.make_image()
          display.clear_output(wait=True)
          display.display(img)
          time.sleep(0.001)
        
```


### Recepteur 
Pour cela, j'ai crée une petite application graphique avec Qt via le la librarie PySide6.
J'utilise QScreen.grabWindow pour faire des screenshots et zbarlight pour la capture des qrcode.
Voici ce que ça donne : 

{ Video }

### Resultats 

Sur mon PC : 
500 ko
1 Mo
10 Mo

### Conclusion 


c'est tout à fait correct pour des petits fichiers. Je pense qu'il serait possible d'augmenter 
le debit en utilisant tout l'espace de l'ecran avec plusieurs QR code en parallele.
Mais on sera toujours limite par la fréquence de rafraichissement et de lecture du QR Code. 








 












