Title: L'entropie et la théorie de l'information
Slug: shannon-entropy
Status: Draft 
Date: 2019-02-01 22:24:08
Modified: 2019-02-01 22:24:08
Tags: statistique,information
Category: biologie,informatique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/stat_banner.jpg


L'entropie, et plus généralement la théorie de l'information, est un concept essentiel en informatique. Publié par [Claude Shannon](https://fr.wikipedia.org/wiki/Claude_Shannon) en 1948 dans "[A mathematical theory of communication](http://math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)", cette théorie a permis l'essor des communications modernes en passant par la téléphonie jusqu'aux transmissions des données massives par internet. Mais on retrouve également cette théorie dans [les algorithmes de compression](https://fr.wikipedia.org/wiki/Compression_de_donn%C3%A9es), les statistiques ou encore en [intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle). Sans oublier bien-sûr la bio-informatique avec l'analyse de notre support d'information préféré : l'ADN. 
Ce billet a pour objectif de vous faire comprendre ce qu'est l'entropie au sens de Shannon.


## Une mesure de l'incertitude
L'entropie peut être vue comme une mesure de l'incertitude d'un événement en fonction de la connaissance que nous avons. Par exemple, depuis que je suis petit le soleil se lève tous les jours. Je suis donc certain qu'il se lèvera demain. En revanche, il est incertain que je croise aujourd'hui un chat noir dans la rue. Cela m'est déjà arrivé plusieurs fois, mais rien ne garantit que cela arrive aujourd'hui. Pour lever cette incertitude, je dois récupérer une certaine quantité d'**information**...

<div class="figure">     <img src="../images/entropy/draw.png" />      <div class="legend"> Vous ne pouvez recevoir qu'une réponse par oui ou par non. Utiliser votre carnet pour poser le minimum de question </div> </div>


Cette incertitude peut être quantifiée par une valeur H , appelée l'[entropie de Shannon](https://fr.wikipedia.org/wiki/Entropie_de_Shannon).
Pour comprendre, faisons une expérience de pensée:    
Imaginez que vous êtes sur la plage d'une île déserte avec un téléphone qui vous permet de contacter le gardien d'un phare en face de vous. Tous les matins depuis un 1 mois, vous lui demandez la prévision météo du jour que vous notez précieusement dans un carnet. 
Un jour, le micro du gardien casse et impossible pour lui de vous répondre vocalement. Cependant il peut toujours vous entendre. Il choisit alors de répondre à vos questions par oui ou par non en utilisant le signal lumineux de son phare. Lumière verte pour Oui, lumière rouge pour non. 
Combien de questions au minimum allez-vous poser au gardien du phare pour lever l'incertitude sur la météo du jour ?  


### Cas n°1 
En regardant votre carnet, vous constatez qu'il y a eu de la pluie 50% du temps et du soleil 50% du temps. 

<center>
<img src="../images/entropy/bar_plot_1.png" /> 
</center>

Il y a donc 1 chance sur 2 pour qu'il pleuve aujourd'hui. Pour connaître la réponse, vous appelez le phare et lui posez une seule et unique question: 

<center>
*Est ce qu'il va pouvoir aujourd'hui ?*
</center>

Il vous répond **oui** ou **non** en utilisant **1** seul signal lumineux. 
Plus précisément, le phare vous a envoyé **1** [bit](https://fr.wikipedia.org/wiki/Bit) de donnée et cela a suffi à lever votre incertitude. Autrement dit, votre incertitude de 1 chance sur 2 a été divisée par 2.    


### Cas n°2
Imaginez cette fois avoir noté dans votre carnet : Pluie : 100% du temps , Soleil : 0%, Orage : 0% , Neige : 0%. 

<center>
<img src="../images/entropy/bar_plot_4.png" /> 
</center>

Dans ce cas, vous ne poserez aucune question au phare. Vous êtes certain qu'il va pleuvoir. Le phare vous transmet donc 0 bit d'information. L'incertitude est nulle.


### Cas n°3
Cette fois vous avez 4 prévisions différentes notées dans votre carnet. Pluie 25% du temps, Soleil 25% du temps, Neige 25% du temps, Orage 25% du temps. C'est-à-dire 1 chance sur 4 pour chaque prévision.

<center>
<img src="../images/entropy/bar_plot_2.png" /> 
</center>

En réflechissant, vous trouverez qu'il faut suivre un arbre décisionnel en posant 2 questions au minimum pour lever votre incertitude.

<center>
<img src="../images/entropy/decision.png" /> 
</center>

Le phare vous envoie par exemple 2 signaux rouges ( non et non ). Vous en concluez qu'il y aura un orage aujourd'hui.
Vous avez donc reçu 2 bits d'information ce qui divise votre incertitude par 4.   
Une autre façon de faire est de demander au gardien *quel temps fera-t-il aujourd'hui* et de lire sa réponse en fonction du code suivant:

	vert-vert   (11)  = pluie
	vert-rouge  (10)  = neige
	rouge-vert  (01)  = soleil
	rouge-rouge (00)  = orage  

Ce code est défini sur 2 bits pour représenter uniquement les N=4 prévisions possibles. 
De façon générale, le nombre de bits nécessaire pour représenter N prévisions se calcule comme suite. Gardez cette formule en tête pour la suite.

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
Imaginez maintenant que les prévisions de votre carnet ne soient pas équiprobables.    
50% de pluie, 25% de soleil, 12.5% neige et 12.5% orage.

<center>
<img src="../images/entropy/bar_plot_3.png" /> 
</center>


Pour économiser l'énergie du phare à long terme, il vous faut une bonne stratégie pour poser les questions. En effet, si vous lui posez comme question "Va-t-il pleuvoir aujourd'hui?", il y a 1 chance sur 2 qu'il réponde  par **oui**. Et vous n'aurez plus à lui poser d'autre question. Super économique. En revanche, si il répond **non**, il faudra peut-être poser 2 questions supplémentaires, soit 3 questions en tout pour lever l'incertitude. Ce qui est plus que nos 2 bits vu précédemment. 
Mais en raisonnant sur plusieurs jours, l'économie est évidente. Dans 50% des cas il faudra poser 1 question, dans 25% des cas 2 questions et 3 questions dans le dernier quart.
Donc en moyenne, l'arbre décisionnel suivant est le plus économique sur le temps: 

<center>
<img src="../images/entropy/decision2.png" /> 
</center>


Ce code peut donc être utilisé par le phare pour vous transmettre la météo de façon optimale:

	vert              (1)   = pluie
	rouge-vert        (10)  = soleil
	rouge-rouge-vert  (001) = neige
	rouge-rouge-rouge (000) = orange

Vous utiliserez donc 1 bits dans 50% des cas, 2 bits dans 25% des cas, 3 bits dans 25% (12.5% * 2) des cas. Ce qui donne en moyenne 1.75 bits (1x0.5 + 2x0.25 + 3x0.125 + 3x0.125) .
Cette valeur que nous venons de calculer, c'est **l'entropie de Shannon** notée *H*.     
Son équation s'écrit comme ceci avec $p_i$ la probabilité de l'événement i pour la distribution P.

<center>
$$H(P) =  -\sum_i p_i \log_2(p_i)$$ 
</center>

Si vous appliquez cette formule sur les 4 distributions des cas vus précédements, vous devriez retrouver le nombre de question à poser (1 bits, 0 bits, 2 bits et 1.75 bits). 
L'entropie est donc une mesure de l'incertitude calculée en bits. Elle est d'autant plus grande que l'incertitude est grande. Plus exactement, l'entropie est maximale lorsque tous les événements possibles ( pluie, neige ...) sont équiprobables. L'entropie est ainsi une mesure permettant de caractériser une distribution statistique.

## Entropie croisé et divergence de Kullback-Leibler
L'[entropie croisé ](https://fr.wikipedia.org/wiki/Entropie_crois%C3%A9e)(cross entropy) permet de quantifier la dissimilarité entre deux distributions en comparant leurs entropies. Par exemple pour comparer une distribution observée P à une distribution théorique Q.
En reprenant l'exemple précédant, imaginez que vous êtes sur une îles P avec un carnet P mais que vous posez vos questions au phare de l'îles Q qui avait donné d'autre prédictions inscrites sur le carnet Q. Combien de question supplémentaire allez vous poser au phare Q avec votre carnet P ?    
Ce nombre s'obtient en calculant la [divergence de Kullback-Leibler](https://fr.wikipedia.org/wiki/Divergence_de_Kullback-Leibler) (ou divergence K-L ou  entropie relative):

<center>
$$D_{KL}(P||Q) =  -\sum_i p_i \log_2(p_i / q_i)$$ 
</center>

Lorsque les deux distributions sont identiques, alors la divergence est de 0. Vous pouvez aussi calculer ce qu'on appelle l'entropie croisé ( ou cross entropy) qui se calcule de cette façon:

<center>
$$H(P,Q) =  H(p) + D_{KL}(P||Q) $$
<em> ce qui revient à </em>
$$H(P,Q) = -\sum_i p_i \log_2(q_i)$$
</center>

L'entropie croisé est très utilisé en intelligence artificielle, dans les méthode de classifications suppervisées. En effet, elle sert de [fonction objective](https://fr.wikipedia.org/wiki/Optimisation_lin%C3%A9aire) à minimiser. Par exemple, un [réseau de neurones artificiels](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) va être entrainer afin que sa distribution prédite soit le plus proche possible de la distribution réelle observée sur le jeux d'entrainement.  

## Conclusion

L'entropie mesure la quantité d'information minimum nécessaire pour vous transmettre un message.  Ce n'est donc pas étonnant qu'on retrouve ce concept dans les algorithmes de compression comme le [codage de Huffman](https://fr.wikipedia.org/wiki/Codage_de_Huffman) ou en [cryptographie](https://fr.wikipedia.org/wiki/Cryptographie).    
Il y a aussi [le principe d'entropie maximale](https://fr.wikipedia.org/wiki/Principe_d%27entropie_maximale) qui consiste à choisir pour des données, le meilleur modèle qui maximise l'entropie. En encore la décomposition par minimisation de l'entropie, bien illustré sur [cette image](https://media.nature.com/m685/nature-assets/ismej/journal/v9/n4/images/ismej2014195f1.jpg). J'essaierai de discuter tous ces concepts dans des billets dédiés.      
Je n'oublie quand même pas de conclure avec l'ADN, dont la séquence peut être vue comme une suite de 4 événements aléatoires (A,C,G,T) à l'instar de nos prévisions météorologique. Par exemple, nous pouvons aligner plusieurs séquences d'ADN et calculer la fréquence des 4 nucléotides sur chaque position. En calculant l'entropie sur chaque colonne, vous pouvez quantifier une certitude (2-entropie) sur la présence d'un nucléotide dans un motif particulier. C'est ce qui est illustré dans le [logo-plot](https://en.wikipedia.org/wiki/Sequence_logo) ci-dessous. Regardez la légende sur l'axe des ordonnées, et crier avec moi : "La génétique c'est de l'informatique"!


<center>
<img src="../images/entropy/logo_plot.png" /> 
</center>


### Référence 
- [Super vidéo d'Aurélien Géron (en)](https://www.youtube.com/watch?v=ErfnhcEV1O8)
- [Une autre super vidéo (en)](https://www.youtube.com/watch?v=R4OlXb9aTvQ)
- [La théorie de l'information: L'origine de l'entropie](http://www.yann-ollivier.org/entropie/entropie1)

### Merci 
[@andhena](https://github.com/andhena)