Title: L'entropie et la théorie de l'information
Slug: shannon-entropy
Status: Draft 
Date: 2019-02-01 22:24:08
Modified: 2019-02-01 22:24:08
Tags: statistique,information
Category: biologie,informatique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/stat_banner.jpg


L'etropie et plus généralement la théorie de l'information est un concepte essentiel en informatique. Publié par Claude Shannon en 1948 dans "A mathematical theory of communication", cette théorie a permis l'essort des communications modernes de la téléphonie jusqu'au transmission des données massives par internet. L'equaton de l'entropie est également utilisé dans les algorithmes de compressions, les statistiques ou encore en intelligence artificielle. Sans oublié bien sûr la bioinformatique avec l'analyse de notre support d'information préféré : l'ADN. 
Ce billet a pour objectif de vous faire comprendre ce qu'est l'entropie au sens de Shannon.


## une mesure de l'incertitude
L'entropie peut être vue comme une mesure de l'incertiude d'un évenement en fonction de la connaissance que nous avons. Par exemple, depuis que je suis petit le soleil se lève tout les jours. Je suis donc certain qu'il se levera demain. En revanche, il est incertain que je croise aujourd'hui un chat noir dans la rue. Celà m'est déjà arrivé plusieurs, mais rien de garantie que cela arrive aujourd'hui. Pour lever cette incertitude, je dois récupérer une certaine quantité d'information...

<div class="figure">     <img src="../images/entropy/draw.png" />      <div class="legend"> Vous ne pouvez recevoir qu'une réponse par oui ou par non. Utiliser votre carnet pour poser le minimum de question </div> </div>


Pour comprendre comment quantifier cette incertitude avec des chiffres, faisons une experience de pensée:    
Imaginer, vous êtes sur la plage d'une île deserte avec un téléphone qui vous permet de contacter le gardien du phare en face de vous. Chaque jour depuis un 1 mois, vous lui demandez la prévision météo que vous notez précieusement dans un carnet. 
Un jour, le micro du gardien casse et impossible pour lui de vous répondre vocalement. Cependant il peut toujours vous entendre. Il choisi alors de répondre à vos questions par oui ou par non en utilisant le signal lumineux de son phare. Lumière verte pour Oui, lumière rouge pour non. 
Sachant qu'allumer le phare est couteux, combien de questions allez-vous poser au gardien du phare ? 



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
Plus précisement, le phare vous a envoyé **1** bit de donnée et cela a suffit pour lever votre incertitude.

### Cas n°2
Cette fois vous avez 4 prévisions différentes dans votre carnet. Pluie 25% du temps, Soleil 25% du temps, Neige 25% du temps, orage 25% du temps. C'est à dire 1 chance sur 4 pour chaque prévision.

<center>
<img src="../images/entropy/bar_plot_2.png" /> 
</center>

Combien de questions  allez vous poser au phare pour lever votre incertitude ? Réfléchissez bien ....    
La réponse est de **2 questions**, et pas 3 ni 4. Par exemple : 

<center> Faire un arbre ? 
*Il va neiger ou pleuvoir aujourd'hui?*   
*Il y aura un orage aujourd'hui ?  *   
</center>

Il vous répond alors par 2 signaux rouges ( Non et Non ) . Vous en concluez qu'il y aura du soleil aujourd'hui.
Le phare vous a donc transmis 2 bits d'information pour lever votre incertitude.      
Une autre façon de faire est d'utiliser un code entre vous et le gardien du phare. Il suffit alors de demander *quel temps fera-t'il* et de décoder le message.

	vert-vert   (11)  = Soleil
	vert-rouge  (10)  = Pluie
	rouge-vert  (01)  = Neige
	rouge-rouge (00)  = Orage  

La encore, 2 bits sont nécessaire pour lever votre incertitude. 


### Cas n°3
Imaginez maintenant que les prévisions de votre carnet ne soient pas equiprobable.    
Pluie 80% du temps, Soleil 5%, orage 5%, Neige 5%.

<center>
<img src="../images/entropy/bar_plot_3.png" /> 
</center>


Vous pouvez toujours préparer 2 questions. Mais cette fois l'ordre va être important. En effet, si vous lui poser d'abord la question: 

<center>
*Est ce qu'il va pleuvoir aujourd'hui?*
</center>

il y a de grande chance qu'il réponde **oui** et il ne sera plus nécessaire de lui poser la deuxième question. 
En faisant ainsi chaque jour, vous avez 80% de chance qu'un seul bit suffise pour lever votre incertitude. Dans les 20% restant il faudra 2 bits. 
Il faut donc calculer le nombre de question **en moyenne** qui est nécessaire pour lever votre incertitude. Dans notre cas : 80% * 1  + 20% * 2 soit 1.2 bits.

### Cas n°4
Pour finir, imaginez cette fois avoir notez dans votre carnet : Pluie : 100% du temps , Soleil : 0%, orange : 0% , Neige : 0%. 

<center>
<img src="../images/entropy/bar_plot_4.png" /> 
</center>


Dans ce dernier cas, vous ne poserez aucune question au phare. Vous êtes certain qu'il va pleuvoir. Le phare vous transmet donc 0 bits d'information. 


## L'entropie de Shannon
Le nombre de bit moyen transmis par le phare pour lever votre votre incertitude se calcul via l'entropie de Shannon $H$ ou $p_i$ est la probabilité de l'évenement $i$.

$$H =  -\sum_i p_i \log_2(p_i)$$ 

Testons pour voir ...     
Dans le **cas n°1**, il y avait 2 évenements avec des probabilités de 50%. 
Soit : 

$$H = - 0.5 * log_2(0.5) + 0.5 * log_2(0.5) =  1 bit $$

Dans le **cas n°2**, il y avait 4 évenements avec des probablités de 25%. Soit :   

$$H = - (0.25 * log_2(0.25)) * 4  = 2 bit $$

 
Dans le cas n°3, il y avaiat 4 évenments avec des probabilités respectives de 80%,5%,5%,5% . Soit : 

$$H = - (0.8 * log_2(0.8)  + 0.05 * log_2(0.05))    = 2 bit $$



Dans le cas 4 , il y a 4 évenements dont une a une probabilité de 100%. 
E = 0 .

L'entropie augmente donc avec votre incertitude. Autrement dit, c'est une mesure de la quantité d'information de votre carnet à prédir les prochaines météos. C'est dans ce sens, que l'entropie est une mesure de l'information. 
Pourquoi utiliser ce terme, qui en physique mesure le désordre? Tout simplement parce que lorsque les évenements sont parfaitement aléatoires, c'est à dire désordonnée,l'entropie est maximale.


## un exemple en génétique : Le logo plot 
Si vous faite un peu de génétique, vous avez certainement déjà remarqué ce genre de graphique appelé logo plot. En y regardant de plus près, vous constaterez que l'axe des ordonnées est donnée en nombre de bits! 

remplacer soleil, pluie, neige, orage par A,C,G,T .. 

<div class="figure">     <img src="../images/entropy/logo_plot.png" />      <div class="legend"> Vous ne pouvez poser que des questions avec réponse par oui ou par non pour connaître la météo du jour. Utiliser votre carnet pour en poser un minimum </div> </div>



ce graphique est construit en allignant plusieurs séquences nucléotidique afin d'identifier un motif conservé

	ACGTATA
	ACGTATA
	TCGTACG
	ACATATA
	ACGTTTA
	ACGTATA
	CCGTCTA
	ACGTATG

En prenant chaque colonne, on peut alors estimer la probabilité d'avoir tel nucléotide que l'on reporte dans un tableau appelé PWM (Position Weight Matrix) : 

|       | 1     | 2    | 3     | 4    | 5     | 6     | 7   |
|-------|-------|------|-------|------|-------|-------|-----|
| **A** | 75%   | 0%   | 12,5% | 0%   | 75%   | 0%    | 75% |
| **C** | 12,5% | 100% | 0%    | 0%   | 12,5% | 12,5% | 0%  |
| **G** | 0%    | 0%   | 87,5% | 0%   | 0%    | 0%    | 25% |
| **T** | 12,5% | 0%   | 0%    | 100% | 12,5% | 87,5% | 0%  |



Ce tableau peut être representer par un logo plot et pour chaque colonne nous pouvons calculer l'entropie comme nous l'avons détaillé. Plus exactement, sur l'axe vertical du logo plot, il s'agit de mesurer la certitude que nous avons pour chaque position en calculant l'inverse de l'entropie, c'est à dire entropie maximum - entropie. Il y a 4 évenements possible( A,C,G,T) l'entropie maximum est donc égal à 2. 
Par exemple, en position 4, l'alignement montre qu'il n'y a que des A. L'entropie est à 0, et votre certitude est maximal.
Voilà donc, un exemple simple d'utilisation de l'entropie avec l'ADN .  
Une point suplémentaire tant qu'on y est. La matrice PPM est aussi un modèle d'apprentissage. Vous pouvez répondre à la question : "Est ce que cette séquence est un promoteur" en calculant le score suivant. 
Formule
Plus ce score score est élevé, plus il y a de chance que la séquence testé soit un promoteur.



## Conclusion
il y a de nombreuses applications de l'entropie en bioinformatique. Par exemple la clusterisation d'un alignement multiple en décomposant par minimisation de l'entropie. ( résumé en image : Minimum decomposition entropie).
Ou encore Le principe d'entropie maximal, utilisé en statistique pour prédire le modèle d'une distribution comme étant celle qui a le maximum d'entropie.
Enfin si le sujet vous interesse, je vous conseille fortement de regarder comment fonctionne le codage de Huffman qui est à la base de la compression des fichiers zip. 
