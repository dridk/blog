Title: La cytométrie en flux
Slug: le-format-lmd-en-cytomtrie
Date: 2014-08-02 14:06:18
Tags: python, cellule
Category:informatique
Author: Sacha Schutz
Status:draft
La cytométrie en flux, comme son nom l'indique, est une technique pour compter et caractériser des cellules. Une à une, les cellules sont passer devant un détecteur qui recueille des données optiques pour les transmettre ensuite vers un ordinateur. Au final, c'est un grand tableau à deux dimensions, ou chaque ligne représente une cellule ou *évènement* avec ses caractéristiques propres. Ce tableau est alors stocké dans un fichier binaire en respectant le [format standard FCS](http://isac-net.org/PDFS/90/9090600d-19be-460d-83fc-f8a8b004e0f9.pdf).  
La cytométrie est par exemple utilisé pour faire votre [formule sanguine](http://fr.wikipedia.org/wiki/H%C3%A9mogramme). Les cellules sanguines sont typées (lymphocyte,monocyte,polynucléaire ...) et comptabilisées . Cette formule sanguine permet ainsi d'aider au diagnostique. [Voir un exemple](/images/post7/nfs.jpg)

### Comment ça marche ? 
#### Cellule par cellule ...



