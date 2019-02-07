Title: L'entropie et la théorie de l'information
Slug: shannon-entropy
Status: Draft 
Date: 2019-02-01 22:24:08
Modified: 2019-02-01 22:24:08
Tags: statistique,information
Category: biologie,informatique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/stat_banner.jpg


L'entropie et plus généralement la théorie de l'information est un concepte essentiel en informatique. Publié par [Claude Shannon](https://fr.wikipedia.org/wiki/Claude_Shannon) en 1948 dans "[A mathematical theory of communication](http://math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)", cette théorie a permis l'essort des communications modernes en passant par la téléphonie jusqu'aux transmissions des données massives par internet. Mais on retrouve égallement cette théorie dans les algorithmes de compressions, les statistiques ou encore en intelligence artificielle. Sans oublié bien sûr la bioinformatique avec l'analyse de notre support d'information préféré : l'ADN. 
Ce billet a pour objectif de vous faire comprendre ce qu'est l'entropie au sens de Shannon.


## Une mesure de l'incertitude
L'entropie peut être vue comme une mesure de l'incertiude d'un évenement en fonction de la connaissance que nous avons. Par exemple, depuis que je suis petit le soleil se lève tout les jours. Je suis donc certain qu'il se levera demain. En revanche, il est incertain que je croise aujourd'hui un chat noir dans la rue. Celà m'est déjà arrivé plusieurs fois, mais rien ne garantie que cela arrive aujourd'hui. Pour lever cette incertitude, je dois récupérer une certaine quantité d'**information**...

<div class="figure">     <img src="../images/entropy/draw.png" />      <div class="legend"> Vous ne pouvez recevoir qu'une réponse par oui ou par non. Utiliser votre carnet pour poser le minimum de question </div> </div>


Cette incertitude peut être quantifiée par une valeur H , appelé l'entropie de Shannon.
Pour comprendre, faisons une experience de pensée:    
Imaginer, vous êtes sur la plage d'une île deserte avec un téléphone qui vous permet de contacter le gardien d'un phare en face de vous. Tous les matins depuis un 1 mois, vous lui demandez la prévision météo du jour que vous notez précieusement dans un carnet. 
un jour, le micro du gardien casse et impossible pour lui de vous répondre vocalement. Cependant il peut toujours vous entendre. Il choisi alors de répondre à vos questions par oui ou par non en utilisant le signal lumineux de son phare. Lumière verte pour Oui, lumière rouge pour non. 
Combien de questions au minimum allez-vous poser au gardien du phare pour lever l'incertitude sur la météo du jour ?  


### Cas n°1 
En regardant votre carnet, vous constatez qu'il y a eu de la pluie 50% du temps et du soleil 50% du temps. 

<center>
<img src="../images/entropy/bar_plot_1.png" /> 
</center>

Il y a donc 1 chance sur 2 pour qu'il pleuve aujourd'hui. Pour connaître la réponse, vous appelez le phare et lui poser une seul et unique question: 

<center>
*Est ce qu'il va peuvoir aujourd'hui ?*
</center>

Il vous répond **oui** ou **non** en utilisant **1** seul signal lumineux. 
Plus précisement, le phare vous a envoyé **1** bit de donnée et cela a suffit à lever votre incertitude. Dis autrement, votre incertitude de 1 chance sur 2, a été divisé par 2.    


### Cas n°2
Imaginez cette fois avoir notez dans votre carnet : Pluie : 100% du temps , Soleil : 0%, orange : 0% , Neige : 0%. 

<center>
<img src="../images/entropy/bar_plot_4.png" /> 
</center>

Dans ce cas, vous ne poserez aucune question au phare. Vous êtes certain qu'il va pleuvoir. Le phare vous transmet donc 0 bits d'information. L'incertitude est null.


### Cas n°3
Cette fois vous avez 4 prévisions différentes notées dans votre carnet. Pluie 25% du temps, Soleil 25% du temps, Neige 25% du temps, orage 25% du temps. C'est à dire 1 chance sur 4 pour chaque prévision.

<center>
<img src="../images/entropy/bar_plot_2.png" /> 
</center>

En réflechissant, vous trouverez qu'il faut suivre un arbre désisionnel en poser 2 questions au minimum pour lever votre incertitude.

<center>
<img src="../images/entropy/decision.png" /> 
</center>

le phare vous envoie par exemple 2 signaux rouges ( Non et Non ) . Vous en concluez qu'il y aura un orage aujourd'hui.
Vous avez donc reçu 2 bits d'information ce qui diviser votre incertitude par 4.     
Une autre façon de faire est de demander au gardien *quel temps fera-t'il aujourd'hui* et de lire sa réponse en fonction du code suivant:

	vert-vert   (11)  = pluie
	vert-rouge  (10)  = neige
	rouge-vert  (01)  = soleil
	rouge-rouge (00)  = orage  

Ce code est défini sur 2 bits car nous devons representer uniquement les 4 prévisions possibles. 
De façon général, le nombre de bits nécessaire pour representer N prévision se calcul comme suite. Gardez cette formule en tête pour la suite.

<center>
	$$2^{bits} = N$$
	<em>Soit</em> 
	$$bits = log_2(N) $$
	<em>Ou encore</em> 
	$$bits = -log_2(1/N) $$
	<em>Dans notre cas</em> 
	$$bits = -log_2(1/4) = 2 $$


</center>

### Cas n°4
Imaginez maintenant que les prévisions de votre carnet ne soient pas equiprobable.    
50% de pluie, 25% de soleil, 12.5% neige et 12.5% orage.

<center>
<img src="../images/entropy/bar_plot_3.png" /> 
</center>


Pour économiser l'énérgie du phare à long terme, il y a une stratégie pour poser les questions. En effet, si vous lui poser comme question "Va-t-il pleuvoir aujourd'hui?", il y a 1 chance sur 2 qu'il réponde  par **oui**. Et vous n'aurez plus à lui poser d'autre question. Super économique. En revanche, si il répond **non**, il faudra peut être poser 2 questions supplémentaires, soit 3 questions en tout pour lever l'incertitude. Ce qui est plus que nos 2 bits vu précédement. 
Mais en raisonnant sur plusieurs jours, l'économie est évidente. Dans 50% des cas il faudra poser 1 question, dans 25% des cas 2 questions et 3 questions dans le derniers quarts.
Donc en moyenne, l'arbre décisionnel suivant est idéal : 

<center>
<img src="../images/entropy/decision2.png" /> 
</center>


Ce code peut donc être utiliser par le phare pour vous transmettre la météo de façon optimale:

	vert              (1)   = pluie
	rouge-vert        (10)  = soleil
	rouge-rouge-vert  (001) = neige
	rouge-rouge-rouge (000) = orange

Vous utiliserez donc 1 bits dans 50% des cas, 2 bits dans 25% des cas, 3 bits dans 25% (12.5% * 2) des cas. Ce qui donne en moyenne 1.75 bits (1x0.5 + 2x0.25 + 3x0.125 + 3x0.125) .
Cette valeur que nous venons de calculer, c'est **l'entropie de Shannon** noté *H*. 
Son équation s'écrit comme ceci avec $p_i$ la probabilité de l'évenement i.

<center>
$$H =  -\sum_i p_i \log_2(p_i)$$ 
</center>




## Conclusion
L'entropie est donc une mesure de l'incertitude calculé en bits. Elle est d'autant plus grande que l'incertitude est grande. Plus exactement l'entropie est maximale lorsque tous les évenements possible ( pluie, neige ...) sont équiprobable. C'est d'ailleurs, pour cela que le mot a été repris de la thermodynamique ou l'entropie est une mesure du désordre et de l'imprédictibilité. 
Autrement dit, l'entropie mesure la quantité d'information minimum nécessaire pour vous transmettre un message. D'ou l'utilisation massive de ce concepte dans les algorithmes de compression comme Huffman.    
En statistique, on calcul l'entropie sur une distribution de probabilité. Comme dans ce billet ou les distributions étaient representé par des histogrammes. On peut calculer par exemple l'entropie d'une distribution observé et celle d'une une loi de probabilité. Puis quantifier leurs différences en calculant ce qu'on appelle la divergence de Kullback-Leibler ou encore l'entropie croisé. Cette dernièr est d'ailleurs largement utilisé en intelligence artificielle ou elle joue le rôle de fonction objective à minimiser.
Il y a aussi la décomposition par minimisation d'entropie bien illustré par ce schéma. Et le principe de maximisation d'entropie qui consiste à choisir comme meilleurs modèle expliquant des données, celui qui maximise l'entropie.j'essaiera de discuter tous ces conceptes dans des billets dédiés.      
Etant un blog de bioinfo, je n'oublierai quand même pas de conclure avec l'ADN, dont la séquence peut être vu comme une suite de 4 évenements aléatoire. On peut par exemple aligner plusieurs séquences d'ADN et calculer la fréquences des 4 nucléotides sur chaque position. En calculant l'entropie sur chaque colonnes, vous pouvez alors representer une mesure de la certitude (2-entropie) que tel base est constante dans un motif particulier. C'est ce qu'on appelle un logo-plot. Regardez la légende sur l'axe des ordonnées... Et oui, l'informatique est partout !


<center>
<img src="../images/entropy/logo_plot.png" /> 
</center>


### Référénce 
[Super vidéo d'aurélien Géron](https://www.youtube.com/watch?v=ErfnhcEV1O8)