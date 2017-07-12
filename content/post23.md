Title: Note sur les hook de git 
Slug: git-hook
Date: 2017-07-15 00:23:31
Tags:informatique
Category: informatique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/term_banner.jpg
Status: Draft

Vous l'avez surement remarquer, j'écris mon blog avec pelican. 
Lorsque je suis prêt à publier je commit mon blog sur github, puis dans un second temps je synchronise le dossier html généré sur mon serveur. 
Et comme je suis fainéant, je veux que ces deux étapes se fassent en même temps. Pour cela j'utilise les hooks git. 

# Les hooks git
Pour synchroniser mon dossier html avec pelican, je dois taper la commande suivante, qui synchronise mon dossier html local sur mon serveur en utilisant rsync et ma clef ssh. 

    make rsync_upload 

Pour executer cette commande à chaque git push, il me suffit d'écrire un script dans le dossiers .git/hooks et de lui donner le bon nom. Tous les fichiers d'extensions *.sample déjà présent sont des exemples. Dans mon cas, je veux lancer ma synchronisation pour avant chaque push. J'écris tout simplement la commande précédante dans le fichier pre-push. 

    echo "make rsync_upload" > .git/hooks/pre-push

# zsh et ssh-agent 
Afin d'éviter de retaper mes mots de passe plusieurs fois, aussi bien pour github que pour mon serveur, j'utilise des clefs ssh. 
Par default, ça ne marche pas avec zsh. Il faut modifier le script ~/.zshrc et modifier la ligne plugin et relancer zsh:

    vim ~/.zshrc
    plugins=(git ssh-agent)


Voilà. Maintenant à chaque push et sans me demander de mot de passe, mon blog est envoyé sur github puis sur mon serveur web... 

PS : Je vais essayer de publier plus de note de type. c'est pas long à faire, et c'est parfois plus interessant !  






