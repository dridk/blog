Title: OpenSlide : La libraire des pathologistes ! 
Slug: openslide
Date: 2014-08-06 19:33:48
Tags: ndpi, python
Category: image processing, python
Author: Sacha Schutz

Il y a quelques temps de cela, un collègue [anatomo-pathologiste](http://fr.wikipedia.org/wiki/Anatomo-pathologie) était venu demander mon aide pour détecter des cellules sur des images histologiques d'amygdales. Ces images étaient issues d'un scanner à lame microscopique et stockées sous un format propriétaire Hamamatsu (.ndpi).  
Bref, c'était mes débuts dans l'analyse et le traitement de l'image! 

<p style="text-align:center">
<img src="/images/histology.jpg">
</p>

<!-- ![Alt text](/images/histology.jpg "Optional title"){float:right;} -->



### Un scanner à lame ? 
Avec un microscope, on peut regarder un échantillon sous toutes ses coutures. Choisir le zoom de l'objectif, se déplacer sur la lame, régler la luminosité, le contraste etc... Tout ça sans jamais perdre en qualité. Une simple photo prise sur le vif, ne peut pas vous montrer l'échantillon dans son ensemble. Si par exemple, vous vouliez demander conseil à un collègue outre atlantique, il fallait lui envoyer la lame par la poste. Et pour les conserver, une grande armoire avec un grand cahier en papier (histoire de rester dans le même registre technologique...:D).   
Mais maintenant, il existe les "**lames virtuelles**" ! Ces lames sont des reproductions numériques du contenu optique d'une lame standard et sont obtenues grâce à un scanner à lame. La lecture se fait sur un ordinateur, et vous pouvez reproduire les mêmes manipulations qu'avec un microscope standard.  Je vous propose de jeter un œil sur cette [démo](http://openslide.org/demo/) depuis votre navigateur. 

####Comment ça marche  ?

Il suffit de faire plein de photos à tous les zooms possibles et sur toute la lame, et d'assembler tout ça dans un fichier. Par exemple, au zoom le plus faible, on aura 4 images de l'ensemble de la lame. Et à plus fort zoom, une centaine. L'ensemble de ces images peut être représenté sous forme d'une pyramide :

![pyramide ndpi](/images/scanner_lame.jpg "représentation schématique d'un fichier ndpi")  

Toutes ces images sont stockées ensemble dans un fichier accompagné de [métadonnée](http://fr.wikipedia.org/wiki/M%C3%A9ta-donn%C3%A9e). Les fichiers que j'utilise sont de [format (.ndpi)](https://www.openmicroscopy.org/site/support/bio-formats5/formats/hamamatsu-ndpi.html).
En contrepartie, ces fichiers sont de taille énorme, comparés aux formats d'images standards et peuvent atteindre sans problème le Gigaoctect. C'est pour ces raisons que rare sont les logiciels qui permettent d'ouvrir ce genre d'image. Même [imageJ](http://imagej.nih.gov/ij/), le saint graal des pathologistes, avait du mal à l'heure où je vous écris. Après c'est une application Java, ça se comprend ... :D [TROLL]!


###OpenSlide :  

[OpenSlide](http://openslide.org/api/python/) est une libraire écrit en C, permettant de gérer ce genre d'image. Il gère un tas de format (.ndpi, .vms, .vmu, .svs, .svslide ... ) et propose un [binding](http://fr.wikipedia.org/wiki/Binding) pour notre langage préféré : python ! 

#### Installation 
Depuis une Debian faite : 

    apt-get install openslide-tools
    apt-get install openslide-python  # Python 2
    apt-get install openslide-python3 # Python 3

Depuis un Mac avec port: 

    port install openslide 
    port install py-openslide 

Depuis un Mac avec brew:

    brew install openslide

Depuis pip : 

    pip install openslide-python 

Pour les autres, allez faire un tour sur [la page officiel](http://openslide.org/download/)

#### Afficher une image ndpi
Téléchargez un exemple d'image .ndpi depuis [cette page](http://openslide.org/demo/) et testez le code qui suit. 

    from openslide import OpenSlide
    img  = OpenSlide("exemple.ndpi")
    img.get_thumbnail((1000,1000)).show() 

Vous devriez voir une belle image d'histologie. Je n'ai pas besoin de commenter le code à part la dernière ligne. **get_thumbnail** retourne un aperçu de votre lame numérique dans sa totalité. L'image est un objet [PIL.Image](http://effbot.org/imagingbook/pil-index.htm),très utilisée pour manipuler des images en python. Cette fonction prend en paramètre la résolution maximum de votre thumbnail. En fait, il va essayer de trouver une image la plus proche de cette résolution. Mettez ce que vous voulez.  
Pour finir, j'appelle la méthode **show** de mon PIL.Image, qui affichera l'image directement dans un viewer. 

#### Récupérer des informations
Plusieurs méthodes sont disponibles afin de connaitre les propriétés de votre lame virtuelle. 

    img.dimensions        # Retourne la dimension global 
    img.properties        # Un tas de métadata 
    img.level_count       # Retourne le nombre d’étage dans la pyramide 
    img.level_dimensions  # Retourne les dimensions de chaque étages
    img.level_downsamples # Retourne le zoom de chaque étages


#### Récupérer une zone de l'image
Et si vous voulez récupérer une zone rectangulaire, faites tout simplement 

    img.read_region(location=(10,10), level=2, size=(500,500))

Ou **location** est le coin supérieur gauche, **level** le numéro de l'étage et **size** les dimensions de votre zone.


#### Conclusion 
Voilà, vous pouvez à présent lancer une discussion sérieuse avec un anatomo-pathologiste en lui expliquant que le microscope c'est *has-been*.  
Dans un prochain article, j'expliquerai différente technique d'analyse d'image.

* * *

#### Référence
[Site officiel de Openslide](http://openslide.org/)  
[Site officiel de Hamamatsu](http://www.hamamatsu.com/jp/en/5007.html)  
[Une autre libraire par Christophe Deroulers](http://www.imnc.in2p3.fr/pagesperso/deroulers/software/ndpitools/)  


