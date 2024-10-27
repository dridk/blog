Title: Transferer un gros fichier avec une fontaine de QR code
Slug: code-fontain
Date: 2024-09-30 19:30:31
Modified: 2024-09-30 19:30:31
Tags: algorithme
Category: informatique
Author: Sacha schutz
SIDEBARIMAGE:images/common/term_banner.jpeg


Serait il possible d'envoyer un fichier de 10 Mo en utilisant uniquement des QR codes ? 
C'est la question que je me suis posé lorsque l'on m'a affirmé qu'il n'était 
pas possible d'extraire des données d'une instance Jupyter tournant dans un bureau virtuel. 
Dans cette bulle, un datascientist est censé pouvoir faire des analyses mais il lui est impossible 
de récupérer des données.     
Cependant, les données qui s'affiche sur un écran transitent forcement par la carte graphique de l'utilisateur.
Un hacker pourrait donc très probablement récupérer l'intégralité d'un gros fichier en faisant 
juste des captures d'écran. J'ai donc voulu tester cette théorie en essayant de transferer un fichier de 10 Mo
à partir d'une vidéo d QR codes générés grâce à un algorithmes très interessant : Le code fontaine de Luby.


## Encoder des données dans un QR Code

La capacité de stockage d'un QR code varie en fonction de sa version et de son niveau de code d'erreur. 
Dans le meilleurs des cas, nous allons pouvoir stocker 2953 octects en version 40 ( 177 x 177 ) 
en utilisant un niveau de correction d'erreur Low ( 7% ).      
Nous sommes loin des 10 Mo souhaités. Pour y rémedier il va donc falloir généré plein de QR code que l'on 
pourra transmettre dans une vidéo. Supposions que je génère 30 QR code par secondes, je pourrais récupérér
des données à une vitesse de 720 Kbits/s  (3000 * 30 * 8 * 10**-3) de quoi faire pallir mon bon view modem 56K.
Et voilà ce que ça donne pour un fichier de 10 Ko.

<div class="figure"><img src="images/fontain/qrfontain.gif" /><div class="legend">
Animation d'un QR Code en version 40 encodant un fichier de 100 Ko. 
</div> 
</div>


## Utilisation du code fontaine
Placons nous maintenant du coté du recepteur. Il suffirait en principe de faire des capture d'ecran toutes 
les 4 ms et décoder chaque QR Code dans le bon ordre. Mais en réalité, il y a de forte chance d'en rater certain.
Dans des protocoles classiques de communication réseau bi-directionnel comme TCP/IP, chaque capture ou paquet doit 
être confirmer à l'emetteur avant de recevoir le prochain. Dans notre cas, ce n'est pas possible 
car la communication est unidirectionnel, nous ne faisons qu'écouter. 
Une solution serait donc de demander à l'emetteur de répéter en boucle son message. Mais attendre un tour complet 
pour récupérer un seul paquet risque d'être long.
La solution c'est d'utiliser un code fontaine, qui consiste à générer aléatoirement des paquets de données labelisé 
et les emettre constamment comme une "fontaine de paquet". Le recepteur aura juste à collecter les paquets 
dans le desordre puis les réassembler. Une implementation très bien optimisé du code fontaine est le code de transformation
de Luby ou code LT

### Fonctionnement de l'algorithme de Luby

Un code LT fonctionne de la façon suivante: 

#### Emetteur 
- Le message à transmettre est d'abord découpé en plusieurs bloc source de la même taille.
- Un tirage aléatoire est ensuite réalisé pour selectionné N bloc source.
- Ce tirage aléatoire suit une distribution de Soliton. ( Voir image )
- Ces N blocs sources sont combiné ensemble avec un operateur XOR pour former un seul bloc. 
- Ce bloc encodé est alors transféré au recepteur en précisant le nombre de bloc source qu'il contient dans un identifiant.
- Dans notre cas, ce bloc est transféré via un QR code en reservant les 12 premiers bytes pour l'identifiant. 

<div class="figure"><img src="images/fontain/soliton.png" /><div class="legend">
Distribution de Soliton. Notez qu'en suivant cette distribution, il y aura principalement des combinaisons de 2 blocs 
et qque fois des blocs seuls, essentielle pour pouvoir faire les premiers XOR.
</div> 
</div>


#### Recepteur 
- Le recepteur collecte les paquet encodé en scannant les QR code
- Si le paquet est composé d'un bloc source il le met de coté
- Si le paquet est composé de 2 bloc source, il fera un XOR avec un des paquet déjà recu pour reconstruire le second paquet source.
- Il procède ainsi de suite avec des paquets composés de 3,4..N bloc sources.  
- Lorsqu'il a reçu tout les paquets, il les remet dans l'ordre pour reconstruire le message original.

En combinant les blocs avec un XOR, cela nous permet d'envoyer statistiquement beaucoup moins de bloc que la méthode naïves
qui consisterai à les envoyer un par un.  

Une implementation de cette librarie est disponnible pour python à cette adresse. 


## Mise en place 

Avec tous ces ingrédients, j'ai construit une petit librarie me permettant de transférer des données 
via des QR code. Le code source est disponnible sur https://github.com/dridk/qrfontain.

### Pour emettre

```python
import qrfontain 

with open("big.txt", "rb") as file:

  for image in qrfontain.data_to_qrcode(file):
    display(image)

```
### Pour recevoir 

```python
import qrfontain 

with open("output.txt", "wb") as file:

  # Get QR Code images 
  data = qrfontain.data_from_qrcode(image_generator)
  file.write(data)

```

### Recepteur 
Pour le recepteur, j'ai egallement crée une petite application graphique en Qt.
J'utilise QScreen.grabWindow pour faire des screenshots et zbarlight pour la capture des qrcode.
L'application me permet de selectionner une région de mon bureau avec un carré transparent pour 
capturer les QR codes et télécharger les données.

<video width="600px" controls>

<source src="images/fontain/gui_receiver.webm" type="video/webm" />

</video>


### Resultats 

Sur mon PC : 
500 ko
1 Mo
10 Mo

### Conclusion 











 












