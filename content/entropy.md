Title: L'entropie et la théorie de l'information
Slug: entropy
Status: Draft 
Date: 2019-02-01 22:24:08
Modified: 2019-02-01 22:24:08
Tags: statistique,information
Category: biologie,informatique
Author: Sacha Schutz

J'ai plusieurs fois été confronté en informatique à la notion d'entropie sans vraiment la comprendre. 
J'avais une vague idée, inspiré de mes cours de physiques, d'une sorte de "mesure" du "désordre" pour "quantifer" de l'information. 
Il s'agit pourtant d'un concept fondamental en informatique que tout informaticien doit connaître et qu'on appelle : la théorie de l'information. 

Cette théorie publié par Claude Shannon dans "A mathematical theory of communication" a permis l'essort de nos communications modernes, de la téléphonie jusqu'au transmission des données massives par internet. On la trouve égallement dans les algorithmes de compressions, les statistiques ou encore en intelligence artificielle. Sans oublié bien sûr en bioinformatique avec l'analyse de notre support d'information préféré : l'ADN. 


## une mesure de l'incertitude
L'entropie mesure l'incertiude d'un évenement en fonction de la connaissance que nous avons. Par exemple, depuis que je suis petit le soleil se lève tout les jours. Je suis certain qu'il se levera demain. En revanche, je ne suis pas certain de croisé un ami en ville aujourd'hui, car par experience cela ne m'arrive pas tous les jours. 
Pour comprendre comment quantifer avec des chiffres cette incertitude, nous allons faire une experience de pensée. Imaginez vous êtes sur la plage d'une île deserte avec un téléphone qui vous permet de contacter le gardien du phare en face de vous. Chaque jour depuis un 1 mois, vous lui demandez la prévision météo que vous notez dans un carnet. 
Un jour, le micro du gardien casse et impossible pour lui de vous répondre vocalement mais il vous entend très bien. Il choisi alors de vous répondre par oui ou par non en utilisant le signal lumineux de son phare. Lumière verte pour Oui, lumière rouge pour non. Sachant qu'allumer le phare coûte très cher au gardien, essayer de trouver, dans les cas suivants, combien de questions minimum vous allez poser au gardien pour lever votre incertitude sur la météo du jour.

<div class="figure">     <img src="../images/entropy/draw.png" />      <div class="legend"> Vous ne pouvez poser que des questions avec réponse par oui ou par non pour connaître la météo du jour. Utiliser votre carnet pour en poser un minimum </div> </div>



### Cas 1 
En regardant votre carnet, vous constatez qu'il y a eu de la pluie 50% du temps et du soleil 50% du temps. 

<center>
<img src="../images/entropy/bar_plot_1.png" /> 
</center>

Aujourd'hui il y a donc 1 chance sur 2 pour qu'il pleuve. Pour avoir la réponse, vous appelez le phare et lui poser 1 seul question: 

- Est ce qu'il pleut aujourd'hui ? **OUI**

 Il vous répond "oui" par un seul signal lumineux. Plus précisement, le phare vous a envoyé 1 bits ( oui / non) de donnée et cela a suffit pour lever votre incertitude.

### Cas 2 
Cette fois vous lisez dans votre carnet 4 prévisions différentes. Pluie 25% du temps, Soleil 25% temps, Neige 25% du temps, orage 25% du temps. Donc une chance sur 4 pour chaque prévision.

<center>
<img src="../images/entropy/bar_plot_2.png" /> 
</center>

Combien de question au minimum allez vous poser au phare pour lever votre incertitude ? Réfléchissez .... 

La réponse est de 2 questions, par exemple :

- Est ce que demain ce sera de la neige ou de la pluie ? ( NON )
- Est ce que demain ce sera un orage ? ( NON)
- Donc il y aura du soleil. 

Cette fois-ci, le phare vous a transmis 2 bits d'information pour lever votre incertitude. 

### Cas 3
Imaginez maintenant que les prévisions de votre carnet ne sont pas equiprobable. Pluie 80% du temps, Soleil 5% , orage 5%, Neige 5%.

<center>
<img src="../images/entropy/bar_plot_3.png" /> 
</center>


Vous pouvez toujours lui poser 2 questions. Mais cette fois l'ordre va être important. En effet, si vous lui poser d'abord la question: 

- "Est ce qu'il pleut ? ( OUI)

il y a de grande chance qu'il réponde oui et il ne sera plus nécessaire de lui poser la deuxième question. 
En faisant ainsi chaque jour, dans 80%, un seul bit d'information suffira pour lever votre incertitude. Dans les 20% restant il faudra 2 bits. Soit en moyenne :80% * 1  + 20% * 2  = 1.2 bits. 

### Cas 4
Pour finir, imaginez cette fois avoir notez dans votre carnet : Pluie : 100% du temps , Soleil : 0%, orange : 0% , Neige : 0%. 

<center>
<img src="../images/entropy/bar_plot_4.png" /> 
</center>


Dans ce cas, vous ne poserez aucune question au phare. Vous êtes certain qu'il va pleuvoir. Le phare vous transmet donc 0 bits d'information. 



## L'entropie de Shannon
Le nombre de bit minimum transmis par le phare pour lever votre votre incertitude se calcul via l'entropie de Shannon : 

[ formule commenté]

Dans le cas 1, il y a 2 évenements avec des probabilités de 50%. Soit : 
E = 1 
Dans le cas 2, il y a 4 évenements avec des probablités de 25%. Soit : 
E = 
Dans le cas 3, il y a 4 évenments avec des probabilités respectives de 80%, 5%,5%,5% . Soit : 
E = 1.2 bits 
Dans le cas 4 , il y a 4 évenements dont une a une probabilité de 100%. 
E = 0 .

L'entropie augmente donc avec votre incertitude. Autrement dit, c'est une mesure de la quantité d'information de votre carnet à prédir les prochaines météos. C'est dans ce sens, que l'entropie est une mesure de l'information. 
Pourquoi utiliser ce terme, qui en physique mesure le désordre? Tout simplement parce que lorsque les évenements sont parfaitement aléatoires, c'est à dire désordonnée,l'entropie est maximale.


## un exemple en génétique : Le logo plot 
Si vous faite un peu de génétique, vous avez certainement déjà remarqué ce genre de graphique appelé logo plot. En y regardant de plus près, vous constaterez que l'axe des ordonnées est donnée en nombre de bits! 


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
