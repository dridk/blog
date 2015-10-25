Title: MongoDB, la base de donnée pour dire adieu à Sql.
Slug: MongoDB
Date: 2014-06-14 16:51:24
Tags: SGBD,sql,database
Category: database
Author: Sacha Schutz
<!-- 
<p class="img-header">
    <img src="/images/post4/header.png">
</p> -->

[MongoDB](http://www.MongoDB.org/) est un système de gestion de base de données ou [SGBD](http://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_de_base_de_donn%C3%A9es), comme [Mysql](http://fr.wikipedia.org/wiki/Mysql) ou [PostgreSql](http://fr.wikipedia.org/wiki/Postgresql), mais dont le mécanisme est complètement différent. Fini le temps ou il fallait créer un schéma de tables relationnelles et créer des requêtes Sql complexes. Grâce à MongoDB vous allez pouvoir stocker vos données un peu comme vous le feriez dans un fichier [JSON](http://fr.wikipedia.org/wiki/JSON). C'est à dire, une sorte de dictionnaire géant composé de clés et de valeurs. Ces données peuvent ensuite être exploitées par du [javascript](http://fr.wikipedia.org/wiki/Javascript), directement intégré dans MongoDB, mais peuvent également être exploitées par d'autre langage comme [python](http://fr.wikipedia.org/wiki/Python_%28langage%29). 

###Collection et Documents 
Avant de commencer à voir en détail le fonctionnement de MongoDB, il faut comprendre différentes notions. MongoDB stocke ses données sous le même format qu'un document JSON. Pour être plus exact, c'est la version binaire du JSON appelé [BSON](http://fr.wikipedia.org/wiki/BSON). Mais alors, c'est quoi un document JSON ? 

####Documents 
Un document JSON, c'est simplement un ensemble de clés et de valeurs dont la notation est la suivante : 

    {
    "first_name": "Richard",
    "last_name": "Dawkins",
    "job":"ethologist",
    "age": 73
    }

Dans cette exemple, *first_name* est la **clé** , *Richard* est la **valeur**.  
Plusieurs documents peuvent être imbriqués ensemble pour former un documents plus complexe : 

    {
    "first_name": "Richard",
    "last_name": "Dawkins",
    "job":"ethologist",
    "age": 73   
    address : {
        "street":"33 panda street",
        "city":"Oxford",
        "country":"UK"
        }
    }

Il est également possible de mettre des listes : 
    
    {
    "first_name": "Richard",
    "last_name": "Dawkins",
    "job":"ethologist",
    "age": 73   
    books: [
    {"title": "Selfish Gene", "date":"1976"},
    {"title": "The blind watchmaker", "date":"1956"},
    {"title":"The magic of Reality", date:"2011", "page_count":200}
    ]
    

Si vous regardez la liste de livres, vous remarquerez qu'il n'est pas nécessaire de respecter la cohérence des champs d'une base Sql. En effet, il y a deux champs *title* et *date* pour les deux premiers livres, et 3 pour le dernier. 

####Collection
Une collection est tous simplement un ensemble de document. On peut la comparer à une table. Par exemple, une collection de 50 auteurs contiendra 50 documents comme défini plus haut. MongoDB intègre des index notés **_id** unique pour chaque document.  

     {
    "_id" : 0
    "first_name": "Richard",
    "last_name": "Dawkins",
     },
     {
    "_id" : 1
    "first_name": "Stephen",
    "last_name": "Jay Gould",
     },
     {
    "_id" : 2
    "first_name": "François",
    "last_name": "Jacob",
     },

Sachez que le format JSON, provient directement du langage Javascript. D'ailleurs JSON veut dire **J**ava**S**cript **O**bject **N**otation. C'est pour cette raison que MongoDB utilise javascript par defaut afin de manipuler sa base. 


#Premier pas avec MongoDB 

###Installation
Si vous êtes sous Linux ubuntu : 

    sudo apt-get install MongoDB

Pour les autres OS, je vous invite à le télécharger depuis [la page officiel](http://www.MongoDB.org/downloads)  
MongoDB est livré avec plusieurs binaires. On retiendra **mongod** le serveur, et **mongo** le client console. 

###Lancement du serveur
Sous linux, un daemon est automatiquement crée. Pour l’exécuter : 

    sudo /etc/init.d/mongod stop

Pour les autres, il suffit d’exécuter **mongod** en spécifiant un chemin de stockage:

    mongod --dbpath C:/mongoData

###Se connecter au serveur
Tout d'abord, exécuter le client **mongo** depuis votre terminal. Par défaut, il se connecte au serveur **mongod** en localhost sur le port 27017. 

    schutz@brest:~/Home$ mongo
    MongoDB shell version: 2.4.9
    connecting to: test
    Server has startup warnings: 
    Sat Jun 14 13:47:38.813 [initandlisten] 
    Sat Jun 14 13:47:38.813 [initandlisten] ** NOTE: This is a 32 bit MongoDB binary.
    Sat Jun 14 13:47:38.813 [initandlisten] **       32 bit builds are limited to less than 2GB of data (or less with --journal).
    Sat Jun 14 13:47:38.813 [initandlisten] **       See http://dochub.MongoDB.org/core/32bit
    Sat Jun 14 13:47:38.813 [initandlisten] 

###Afficher les bases de données 
Pour afficher les bases de données disponibles, utilisez **show dbs**. Normalement vous devriez avoir une base **local** propre à mongo et une base **test**: 
    
    show dbs
    local   0.03125GB
    test    (empty)

###Création d'une base de donnée
Pour continuer ce tutoriel, je veux créer une base de donnée **medical** , et créer une collection de **patients**. Chaque patient sera défini par son **nom**, **prenom** et sa **date de naissance**.
Pour créer notre première base de données :  

    use medical

Vous pouvez faire **db** pour voir la base de donnée courante. Attention, si vous faites **show dbs**, vous ne verrez pas encore votre base. En effet, mongo attend d'avoir du contenu pour créer votre base. 

### Insertion 
Pour créer une collection, il suffit simplement d'ajouter un patient. Par exemple pour: 

    {
        "nom":"Dupond",
        "prenom":"Jean Claude",
        "ddn": new Date('May 18, 1984')
    }

Je fais simplement : 

    db.patients.insert({"nom":"jay gould", "prenom":"stephen", new Date('May 18, 1984')})

La collection *patients* se crée automatiquement lors de la première utilisation. Si vous faite maintenant : 

    db.patients.find()

Vous pouvez voir le document que vous venez d'ajouter. Notez que MongoDB ajoute automatiquement un **_index** si rien n'est spécifié.  
En guise d'exemple, on va remplir notre collections en répétant cette procédure 50 fois. 

    for ( var i = 0 ; i<50; i++){
        db.patients.insert({"nom":"jay gould" , "prenom":"stephen", "age": i})
    }

Vérifions le nombre de patients : 

    db.patients.count()

###Lister la collection

####find(critère, projection)
Utiliser **find()** pour retourner toute la liste de la collection patients.

        db.patients.find() 

Pour récupérer les patients dont l'age = 5 

    db.patients.find({age:5})

On peut aussi utiliser des expressions régulières. Par exemple, tous les prénoms commençant par "*j*"

    db.patients.find({prenom: /^j*/})

Pour récupérer les patients dont l'age est supérieur à 40

     db.patients.find({age:{$gt:40}})

**$gt** est un mot clef de mongo qui veut dire *greater than* (*supérieur à*). Pour voir [la liste complète c'est ici](http://docs.MongoDB.org/manual/reference/operator/query/).  

Pour récupérer un seul élément (le premier) , utiliser **findOne** 

    db.patients.findOne({age:{$gt:40}})

Pour récupérer les patients dont l'âge est 5 ou 10 : 

    db.patients.find({age:{$in:[5,10]}})

Pour récupérer uniquement certaine clé, on utilise l'argument *projection* de find(). Par exemple, récupérer uniquement les noms des patients dont l'âge est supérieur à 40

    db.patients.find({age:{$gt:40}},{"nom":true})

Pour limiter le nombre de résultat à 3 : 
           
    db.patients.find().limit(3)

Pour ordonner la liste par âge décroissant. -1 pour décroissant et 1 pour croissant.

    db.patients.find().sort(age:-1)

###Modifier la collection 
#### update(query, update, options)

Remplacer tous les prénoms *stephen* par *boby*

    db.patients.update({"prenom":"stephen"},{$set:{"prenom":"boby"}},{multi:true})

Ajoute une clé *sexe* à tous les patients 

    db.patients.update({prenom:"boby"}, {$set:{sexe:"male"}}, {multi:true})

Ajoute un patient *olivier* s'il n'existe pas 

    db.patients.update({prenom:"olivier"}, {$set:{sexe:"male"}}, {upsert:true})


#### save(document, writeConcern)
La différence avec **insert** est que **save**, fait un **update** du document s'il existe déjà.

    db.patient.save({"prenom":"jean claude", "nom":"Van Damme"})

### Suppression 
#### remove(query,justOne)

Supprimer tous les patients qui s'appellent *olivier*

    db.patients.remove({prenom:"olivier"})

#### Supprimer la collection

    db.patients.drop()

#### Supprimer la base de donnée

     use medical
     db.runCommand({dropDatabase: 1});


#Conclusion 
Voilà pour les bases de MongoDB. Il y a encore plein de chose à dire sur MongoDB. Comme l'[agrégation](http://docs.MongoDB.org/manual/core/aggregation-introduction/) des données, La [réplication](http://docs.MongoDB.org/manual/core/replication-introduction/) sur plusieurs serveurs ou la [sécurité](http://docs.MongoDB.org/manual/core/security-introduction/). Tous se trouve sur la [documentation officiel](http://docs.MongoDB.org/manual/).
Dans un prochain article, je m’intéresserai cette fois à l'interface entre python et MongoDB via [PyMongo](http://api.MongoDB.org/python/current/). Ce sera forcement un article court :D. Il faut que je jette aussi un coup d’œil à [QtMongo](https://github.com/manuels/QtMongo), une interface vers Qt/C++. 

* * *

#### Référence
[MongoDB site officiel](http://www.MongoDB.org/)  
[MongoDB Documentation](http://docs.MongoDB.org/manual/)  
[Syrinxoon Tuts](http://tuts.syrinxoon.net/tuts/installation-et-bases-de-MongoDB)  
[PyMongo](http://api.MongoDB.org/p)













    
   






