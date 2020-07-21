Title: Premier Blog avec Pelican
Date: 2014-04-12 10:20
Tags: pelican, blog, python
Category: informatique
Slug: first-post
Author: Sacha Schutz

<!-- <p class="img-header">
    <img src="../images/post1/header.jpg">
</p> -->

Hello, à tous ! 
Bon, j'ai enfin passé le cap de la création de blog. A vrai dire, j'avais déjà essayé auparavent d'autres systèmes de blog comme [wordpress](http://fr.wordpress.org/) ou [blogger](https://www.blogger.com/). Mais j'ai pas tenu longtemps car je perdais vraiment tout mon temps à écrire du html et à checker le rendu en ligne. Donc, j'ai enfin trouvé un système pour blogger idéalement! Il s'agit de [Pelican 3.3](http://docs.getpelican.com/en/3.3.0/), un générateur de page web static écrit en python. Il suffit d'écrire un article en [Markdown](http://fr.wikipedia.org/wiki/Markdown) dans son éditeur préféré ( Vim pour les africanos ou [Sublime Text](http://www.sublimetext.com/) comme moi) et Pelican se charge de créer toutes les pages html. Il ne reste alors plus qu'à automatiser l'envoi de ces pages sur un serveur nginx ou apache , et le tour est joué ! Vous n'avez même pas idée a quel point c'est agréable d'écrire sans html avec son éditeur préféré.
Je vous propose donc, dans ce premier poste, de vous détailler la création d'un blog avec Pelican.

###Installation 

L'installation suivante, a été faite sous Linux/ubuntu. Mais les exemples suivants devraient marcher sur tous les OS supportant python. Si vous êtes sous windows, je vous invite quand même à installer un vrai OS de développement :D 
Vérifiez d'avoir une version de python compatible 2.7.x .  Depuis votre terminal tapez : 

	python --version
	Python 2.7.5+

Si vous n'avez pas python, installez le en suivant ce [tutorial](http://fr.openclassrooms.com/informatique/cours/apprenez-a-programmer-en-python/installer-python-1).
Ensuite, assurez vous d'avoir le gestionnaire de package de python **pip**. Vous pouvez l'installer en suivant les indications de la [page officiel](http://www.pip-installer.org/en/latest/installing.html).  
Installer alors le package Pelican et le package Markdown que nous utiliserons par la suite. 

	sudo pip install pelican
	sudo pip install Markdown  


###Création du blog 
Tout d'abord, créez le dossier de votre blog. Une fois à l’intérieur, lancer la commande **pelican-quickstart**. 

	mkdir monBlog
	cd monBlog
	pelican-quickstart

Suivez les indications. Voici ce que j'ai mis. Si comme moi, vous avez un serveur accessible par ftp ou ssh, répondez 'Oui' et suivez les instructions. Ceci nous permettra d'envoyer automatiquement les fichiers html générés, vers un serveur. 

	Where do you want to create your new web site? [.] 
	What will be the title of this web site? MonBlog
	Who will be the author of this web site? sacha schutz
	What will be the default language of this web site? [en] fr
	Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)         
	What is your URL prefix? (see above example; no trailing slash) https://dridk.me    
	Do you want to enable article pagination? (Y/n)                                         
	How many articles per page do you want? [10]                                                  
	Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)       
	Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)      
	Do you want to upload your website using FTP? (y/N)                                                                   
	Do you want to upload your website using SSH? (y/N)                                                                   
	Do you want to upload your website using Dropbox? (y/N)                                                               
	Do you want to upload your website using S3? (y/N)                                                                               
	Do you want to upload your website using Rackspace Cloud Files? (y/N) 
	Done. Your new project is available at /home/schutz/dev/monblog

Les fichiers et dossiers intéressants sont les suivants :  

**content/** *Tous vos articles et pages doivent être ranger ici*   
**output/** *Les pages html static se trouverons ici*  
**pelicanconf.py** *La fichier de configuration de votre site*   
**publishconf.py** *Le fichier de configuration pour la publication.*  
**Makefile** *Un make nous permettant de faire plein de manipulation automatique*  





### Tester votre blog
Vous pouvez maintenant générer vos pages static via la commande suivante : 

	make html

Puis testez votre blog en lançant un serveur via la commande suivante : 

	make serve 

N’hésitez pas à taper **make help** pour avoir plus d'information sur ces commandes.   
Si tout se passe bien, vous devriez obtenir cette page en vous rendant à l'adresse : [http://localhost:8000](http://localhost:8000). 


![Capture](/images/post1.png)   


### Créez votre premier poste. 
Maintenant, rien de plus simple! Depuis votre éditeur de texte préféré, créez un fichier *mon_premier_post.md* dans le dossier *content* et sauvegarder.  


	Title: Mon blog avec pelican
	Date: 2010-12-03 10:20
	Tags: linux, python, pelican
	Category: python
	Slug: first-post
	Author: Sacha Schutz

	Ceci est le contenu de mon premier poste     


Régénérer votre code comme précédemment et voilà: 

	make html
	make serve 

Une astuce, au lieu de faire à chaque fois make html et make serve, vous pouvez directement faire une seul fois:

	make devserver 

Ceci créera un serveur en arrière plan se mettant à jour à chaque modification de vos fichiers. 


### Publier votre blog
Pour finir, la publication de vos pages statiques peut se faire soit manuellement, en envoyant le contenu du dossier output. Soit via une de ces commandes en fonction des paramètres de votre serveur.

	make ssh_upload                  upload the web site via SSH        
	make rsync_upload                upload the web site via rsync+ssh  
	make dropbox_upload              upload the web site via Dropbox    
	make ftp_upload                  upload the web site via FTP        
	make s3_upload                   upload the web site via S3         
	make cf_upload                   upload the web site via Cloud Files
	make github                      upload the web site via gh-pages   


### Conclusion 
Voilà, j'espère que ce poste vous a aidé à comprendre le fonctionnement de Pelican. Je n'ai pas détaillé le reste. Mais sachez qu'il est possible d'ajouter plein [d'options intéressantes](http://pelican.readthedocs.org/en/latest/settings.html) depuis le fichier de configuration. Vous pouvez installer des thèmes et des plugins que vous récupérez [ici depuis github](https://github.com/getpelican). Vous pouvez également créer des pages fixes en les sauvegardant dans contents/pages. 

* * *

#### Référence
[Site officiel du project Pelican](http://docs.getpelican.com/en/3.3.0/)  
[Github du project Pelican (Theme et plugins)](https://github.com/getpelican)  
[Markdown Syntax Guide](http://daringfireball.net/projects/markdown/)  
[Pelican Settings doc](http://pelican.readthedocs.org/en/latest/settings.html)

