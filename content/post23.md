Title: Un hook git pour mon blog 
Slug: un-hook-git-pour-mon-blog 
Date: 2017-07-13 00:53:37
Tags:informatique, linux, git
Category: informatique
Author: Sacha Schutz
SIDEBARIMAGE:images/common/term_banner.jpeg

Vous l'avez sûrement remarqué, j'écris mon blog avec [pelican](http://docs.getpelican.com/en/stable/). 
Lorsque je suis prêt à publier, je commit mon blog sur [github](https://github.com/), puis dans un second temps je synchronise mon dossier html généré sur mon serveur web. 
Et comme je suis fainéant, je veux que ces deux étapes se fassent en même temps. Pour cela j'utilise les [hooks](https://git-scm.com/book/gr/v2/Customizing-Git-Git-Hooks) de git coté client. 

# Les hooks 
Les hooks sont des scripts qui peuvent s’exécuter côté client (mais aussi côté serveur) après un événement git. 
Dans mon cas, je veux uploader mon dossier html sur mon serveur web à chaque fois que je fais un *git push*. La commande a exécuté et fourni dans le *Makefile* de pelican. Elle synchronise les fichiers html sur mon serveur web avec *rsync* et ma clef ssh. 

    make rsync_upload 

Pour exécuter cette commande à chaque *git push*, il me suffit d'écrire un script dans le dossier *.git/hooks* et de lui donner le bon nom de fichier. Tous les fichiers d'extensions *.sample* déjà présent sont des exemples avec les noms appropriés correspondant à l'étape d'exécution. Supprimer l'extension *.sample* pour que le script s’exécute. Dans mon cas, je veux lancer ma synchronisation avant chaque *push*. J'écris tout simplement la commande précédente dans le fichier *.git/hooks/pre-push*. 

    echo "make rsync_upload" > .git/hooks/pre-push

# zsh et ssh-agent 
Afin d'éviter de retaper mes mots de passe plusieurs fois, aussi bien pour github que pour la synchro sur mon serveur web, j'utilise des clefs ssh. 
Par default, *ssh-agent* ne marche pas avec [zsh](https://fr.wikipedia.org/wiki/Z_Shell). Il faut modifier le script ~/.zshrc et modifier la ligne plugin et relancer zsh:

    vim ~/.zshrc
    plugins=(git ssh-agent)


Voilà. Maintenant à chaque *push* et sans me demander mon mot de passe, mon blog est envoyé sur github puis sur mon serveur web.

PS : Je vais essayer de publier plus de notes courtes de ce type, si ça ne vous embête pas. C'est moins long à faire, et comme ça je peux partager ce que j'apprends plus rapidement. 





