Title: Module requests : Jouons avec Http et python
Slug:python-requests 
Date: 2014-06-11 23:42:22
Tags: requests, http, get, post
Category:python 
Author: Sacha Schutz

<!-- <p class="img-header">
    <img src="images/post3/header.jpg">
</p> -->

**Requests** est un module python permettant d'utiliser le protocole http de façon ultra simple! Je l'ai découvert en voulant récupérer des données d'une page web au boulot à travers un proxy. Car en effet, il gère vraiment tout ! Les proxy, les cookies, ssl, les uploads multiparts et bien d'autres trucs sympas! Je vous propose dans ce poste, quelques exemples d'utilisations de cette librairie. Pour plus d'informations, il y a la [page officiel en français.](http://fr.python-requests.org/en/latest/)

### Installation 

Comme pour tous les modules python, je vous conseille d'utiliser **[pip](http://pip.readthedocs.org/en/latest/installing.html)**

    pip install requests 

### Créer une requête

Tout d'abord, importons le module Requests: 

    import requests

Maintenant, essayons de récupérer la page de [linuxfr.org](http://linuxfr.org/) et l'afficher dans le terminal. 

    r = requests.get("http://linuxfr.org/")
    print(r.text)

Voila, c'est tout simple ! Pour les autres verbes du protocole HTTP, il suffit de faire : 

        r = requests.put("http://linuxfr.org/")
        r = requests.delete("http://linuxfr.org/")
        r = requests.patch("http://linuxfr.org/")
        r = requests.post("http://linuxfr.org/")
        r = requests.head("http://linuxfr.org/")
        r = requests.options("http://linuxfr.org/")

### Utilisation d'un Proxy

Si vous devez passer par un proxy, comme j'ai du le faire, c'est toujours aussi simple. 

    proxy = {"http":"http://username:password@proxy:port"}
    r = requests.get("http://linuxfr.org/", proxies = proxy)

### Lire la réponse

Pour lire la réponse on a déjà vu *r.text* plus haut. Pour le reste, c'est toujours aussi simple, voici les plus sympas :

    r.text          #Retourne le contenu en unicode
    r.content       #Retourne le contenu en bytes
    r.json          #Retourne le contenu sous forme json
    r.headers       #Retourne le headers sous forme de dictionnaire 
    r.status_code   #Retourne le status code

### Envoyer des données

Pour envoyer des données, toujours aussi simple. Par exemple pour l'envoi des données d'un formulaire : 

    data = {"first_name":"Richard", "second_name":"Stallman"}
    r = request.post("http://linuxfr.org", data = data)

Pour envoyer une image par multipart, encore plus facile : 

    file = {'file': open("photo.png", "rb")}
    r = requests.post("http://linuxfr.org", files = file)


Bon, voila rapidement la base des fonctions du module requests. Qui, il faut l'avouer , est magique !! Je vous conseille vivement la lecture de [cette page](http://fr.python-requests.org/en/latest/user/quickstart.html#creer-une-requete), beaucoup plus détaillée. 


* * *

#### Référence
[fr.python-requests.org](http://fr.python-requests.org)   
[docs.python-requests.org](http://docs.python-requests.org/en/v0.10.6/api/)  
 









