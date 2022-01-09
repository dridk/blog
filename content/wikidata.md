Title: Du Rock, Wikidata et du SPARQL
Slug: wikidata
Date: 2022-01-09 23:03:06
Modified: 2022-01-09 23:03:06
Tags: datascience
Category:informatique
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/stat_banner.jpg

Citez moi toutes les personnes ayant eu un oscar et le prix Nobel ? Quelles sont les lieux de naissance de toutes les célébrités se prénommant Antoine ? Trouvez moi tous les médicaments qui cible des gènes liés à la prolifération cellulaire ?     
Ce genre de question peut être difficile à répondre si vous utiliser seulement un moteur de recherche comme [google](https://www.google.com/). Mais en utilisant une [ontologie](https://fr.wikipedia.org/wiki/Ontologie_(informatique)) et un langage dédié appelé [SPARQL
](https://fr.wikipedia.org/wiki/SPARQL), vous allez pouvoir répondre à toutes ces questions en un éclair.  
Dans ce billet, je vous propose d'explorer l'ontologie de [wikipedia](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal) ([wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page)) et utiliser SPARQL pour construire une carte du monde montrant le nombre de groupe de [rock](https://fr.wikipedia.org/wiki/Rock) par habitant de chaque pays.

## Qu'est ce qu'une ontologie ?

Une ontologie est une façon d'organiser le savoir en reliant de nombreux concepts entre eux. Plus exactement, c'est un [graphe](https://fr.wikipedia.org/wiki/Graphe) construit à partir d'un ensemble de [triplets](https://fr.wikipedia.org/wiki/Triplet_RDF) composé chacun  d'un *sujet*, d'un *prédicat* et d'un *objet*.
Par exemple, les 3 triplets suivant permette de relier les [Rolling Stones](https://www.wikidata.org/wiki/Q11036) au [Fish and Chips](https://www.wikidata.org/wiki/Q203925). 

	<The Rolling Stones>   <est d'origine du>   <Royaume uni>
	<The Rolling Stones>   <est un groupe de>   <Rock>
	<Le Fish and Chips>    <est d'origine du>   <Royaume uni>

Dans une ontologie, les concepts sont définis par un identifiant unique. 
Par exemple, sur wikidata, Le concepte "*Rolling Stones*" porte l'identifiant [Q11036](https://www.wikidata.org/wiki/Q11036) et le concepte "*Fish and Chips*" porte l'identifiant [Q203925](https://www.wikidata.org/wiki/Q203925). Il en est de même pour les prédicats et les objets. Ainsi, les triplets précédents peuvent s'écrire de la manière suivante:

```
	wd:Q11036  wdt:P17	wd:Q145  
	wd:Q11036  wdt:P31  wd:Q5741069
	wd:Q203925 wdt:P17  wd:Q145
```

Ces triplets sont généralement stockés dans un fichier texte au [format RDF](https://fr.wikipedia.org/wiki/Resource_Description_Framework) ou dans une base de donnée dédiée appelée [triple store](https://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_orient%C3%A9e_graphe#Triple_store). 
Vous trouverez sur internet de nombreuses ontologies, notamment en biologie avec par exemple [GO](http://geneontology.org/) ( Gene ontology ) décrivant les éléments cellulaires ou [HPO](https://hpo.jax.org/) (Human Phenotype Ontology) décrivant les signes cliniques. L'ensemble des ontologies disponible sur web visent à former ce qu'on appelle [le web sémantique](https://fr.wikipedia.org/wiki/Web_s%C3%A9mantique).

## Le language SPARQL

[SPARQL](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial/fr) est un langage dédié à l'extraction d'information depuis une ontologie. Je vous invite à  exécuter les requêtes SPARQL avec [l'outil en ligne](https://query.wikidata.org/) mis à disposition par wikidata.      
Le principe est assez simple. Il faut écrire des triplets en remplaçant les concepts inconnus qui nous intéresse par des variables.        
Par exemple pour trouver tous les groupes de rocks anglais, nous cherchons :

- ?x qui est d'origine anglais 
- ?x qui est un groupe de rock 

En SPARQL, ça donne : 

```sql
SELECT ?x 
WHERE {
?x wdt:P17 wd:Q145.
?x wdt:P31 wd:Q5741069.
}
```

Pour avoir le noms des concepts en français: 

```sql
SELECT ?x ?xLabel 
WHERE 
{
?x wdt:P17 wd:Q145.
?x wdt:P31 wd:Q5741069.
SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```

Et pour récupérer tous les groupes de rocks, leurs pays d'origine et le nombre d'habitant du pays, je fais : 

```sql
SELECT ?groupeLabel ?paysLabel ?population
WHERE 
{
  ?groupe wdt:P31 wd:Q5741069;
          wdt:P495 ?pays.
  ?pays   wdt:P1082 ?population.
 
 SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } 
}"""
```

Je vous invite à lire [ce tutoriel](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial/fr) pour plus de précision et à bien utiliser l'autocompletion (ctrl+espace) pour éviter à devoir chercher les concepts un par un.


## Exécution depuis Python

L’éditeur SPARQL de wikidata propose un bouton magique pour générer du code dans différents langages.


<div class="figure">
<img src="../images/wikidata/editor.png" />
<div class="legend"> Editeur SPARQL de wikidata </div>
</div>



 Ainsi vous pouvez exécuter en python une requête SPARQL pour récupérer le résultat en [JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation). Vous aurez besoin du package [sparqlwrapper](https://pypi.org/project/SPARQLWrapper/).     
Vous pouvez ensuite construire un [Dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) avec [pandas](https://pandas.pydata.org/docs/index.html).

```python

# Installer sparqlwrapper
#!pip install sparqlwrapper
import sys
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

endpoint_url = "https://query.wikidata.org/sparql"

query = """
SELECT ?groupeLabel ?paysLabel ?population
WHERE 
{
  ?groupe wdt:P31 wd:Q5741069;
          wdt:P495 ?pays.
  ?pays wdt:P1082 ?population.
 
 SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # Helps get the label in your language, if not, then en language
}"""

def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

# construction d'un dataframe
df = pd.io.json.json_normalize(results['results']['bindings'])
df = df[["groupeLabel.value","paysLabel.value", "population.value"]]
df.columns = ["groupe","pays","population"]

```
## La carte ! 

Il suffit de mouliner le tout avec [geopandas](https://geopandas.org/en/stable/) sur un notebook jupyter disponible [ici](https://colab.research.google.com/drive/1PzdvHAeCxed9FtrAzpCRF5lKSmKGnfnQ?usp=sharing), et le tour est jouer.

<div class="figure">
<img src="../images/wikidata/map.png" />
<div class="legend"> Nombre de groupes de rock par pays</div>
</div>

Les pays ayant le plus de groupes de rocks par habitant, sont les pays nordique ( Finlande, Norvège, Groenland, islande, suède) . 1 groupe référencé en Iran, 86 groupe pour la France et 270 pour le Royaume-unis !


#### Note 

Toutes les questions dans l'introduction sont disponible dans le menu example de [l’éditeur sparql de wikidata.](https://query.wikidata.org/)

### Référence 

- [Wikidata Query service](https://query.wikidata.org/)
- [Un tutoriel sur SPARQL/WIKIDATA en Français](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial/fr)