Title: Explorer des données cartographiques avec osmium
Slug: osmium-tools
Date: 2020-11-01 19:30:31
Modified: 2020-11-01 19:30:31
Tags: cartographie, bash
Category: informatique
Author: Sacha schutz
SIDEBARIMAGE:images/common/term_banner.jpeg

Récemment j'ai été amené à devoir extraire toutes les cités en France ( que ce soit des villes, des villages ou des hameaux). j'ai d'abord cherché sur internet un dataset prémâché, mais j'ai vite constaté que ces données étaient souvent incomplètes par rapport aux cartes d'[OpenStreetMap](https://www.openstreetmap.fr/). 
J'ai donc voulu directement récupérer les données utilisées par ce site et c'est là que je découvert [osmium-tools](https://osmcode.org/osmium-tool/). Un outil en ligne de commande pour manipuler les fichiers [OSM](https://wiki.openstreetmap.org/wiki/OSM_file_formats) d'Open Street Map.

## Les fichiers OSM et PBF

Les fichiers OSM sont des fichiers au format [XML](https://fr.wikipedia.org/wiki/Extensible_Markup_Language) contenant la description d'une carte avec [3 éléments](https://wiki.openstreetmap.org/wiki/Elements) notables ( **les noeuds**, **les chemins** et **les relations**).     
Les noeuds décrivent une position fixe dans l'espace , comme une ville.
Les chemins décrivent un segment ou un polygone, comme le contour d'un pays. Tandis que les relations sont simplement des groupes d'éléments. 
Chaque élément est décrit par [différents attributs](https://wiki.openstreetmap.org/wiki/Elements#Common_attributes) XML et des [tags](https://wiki.openstreetmap.org/wiki/Tags) permettant d'associer des informations à l'élément sous forme de clef-valeur. 
L'exemple suivant décrit par exemple la ville de Caen sous forme d'un noeud avec sa latitude et sa longitude comme attributs ainsi qu'une liste de tags.

```xml
 <node id="1831881213" version="1" changeset="12370172" lat="49.182863" lon="-0.370679" user="lafkor" uid="75625" visible="true" timestamp="2012-07-20T09:43:19Z">
  <tag k="name" v="Caen"/>
  <tag k="place" v="city"/>
  <tag k="addr:postcode" v="14000"/>

 </node>
```

Le format OSM n'est pas utilisé directement. On lui préfère le format [PBF](https://wiki.openstreetmap.org/wiki/PBF_Format), un format indexé plus léger et plus rapide. 
Tous les fichiers d'openstreetmap sont ainsi disponibles au format PBF sur le site [Geofabrik](https://www.geofabrik.de/). Par exemple, la France et ses régions sont disponibles à [cette adresse](https://download.geofabrik.de/europe/france.html). 


## Osmium-Tool: la boite à outils des fichiers OSM/PBF

[Osmium-tool](https://osmcode.org/osmium-tool/) est un outil en ligne de commande écrit en C++ permettant de manipuler les fichiers OSM/PBF. Vous allez pouvoir extraire des données incluses dans un polygone défini, faire des conversions de format, filtrer les données par tag et bien plus.... 
Je vous propose dans ce billet de juste extraire l'ensemble des commune d'Alsace. 

### Installation 
osmium-tool est disponible dans les dépots d'ubuntu: 

    sudo apt-get install osmium-tools 

### Télécharger la région Alsace 

    wget https://download.geofabrik.de/europe/france/alsace-latest.osm.pbf

### Résumer un fichier pbf
La commande **osmium fileinfo** vous donnera des informations générales sur le fichier avec notamment le nombre de noeuds et de chemins:

```
osmium fileinfo -e alsace-latest.osm.pbf 

File:
  Name: alsace-latest.osm.pbf
  Format: PBF
  Compression: none
  Size: 106931186
Header:
  Bounding boxes:
    (6.83892,47.3845,8.24393,49.0802)
  With history: no
  Options:
    generator=osmium/1.8.0
    osmosis_replication_base_url=http://download.geofabrik.de/europe/france/alsace-updates
    osmosis_replication_sequence_number=2772
    osmosis_replication_timestamp=2020-10-27T21:42:03Z
    pbf_dense_nodes=true
    timestamp=2020-10-27T21:42:03Z
[======================================================================] 100% 
Data:
  Bounding box: (6.11539,47.3342,9.60379,49.7883)
  Timestamps:
    First: 2006-01-11T15:31:39Z
    Last: 2020-10-27T21:29:47Z
  Objects ordered (by type and id): yes
  Multiple versions of same object: no
  CRC32: 6bc2d1a1
  Number of changesets: 0
  Number of nodes: 10880224
  Number of ways: 1751889
  Number of relations: 36547
  Largest changeset ID: 0
  Largest node ID: 8053541452
  Largest way ID: 864360376
  Largest relation ID: 11801460

```

### Filtrer par tags 
La [documentation officielle](https://wiki.openstreetmap.org/wiki/Key:place) nous indique que les cités sont définies par le tag **place** avec 4 valeurs possibles:

- place=city
- place=town
- place=village
- place=hamlet

Pour garder uniquement ces noeuds taggés dans un nouveau fichier *place.pbf*, nous pouvons utiliser la commande **osmium tag-filter** en prefixant par "n/":

```bash
osmium tags-filter alsace-latest.osm.pbf  n/place=city,town,village,hamlet -o place.pbf  
```

### Exporter vers un fichier geojson 
Nous pouvons ensuite convertir le fichier PBF en [GEOJSON](https://fr.wikipedia.org/wiki/GeoJSON) (un format [JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) facile à lire) utilisez pour cela **osmium export** :

```bash
osmium export place.pbf -f geojson > place.geojson
```

```json
"FeatureCollection"
[
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [
        8.0056049,
        48.7521656
      ]
    },
    "properties": {
      "name": "Greffern",
      "place": "village",
      "population": "1943"
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [
        7.9445109,
        49.0365935
      ]
    },
    "properties": {
      "name": "Wissembourg",
      "place": "town",
...

```

Personnellement, j'utilise le formidable outil [jq](https://stedolan.github.io/jq/) pour pouvoir parser du json en ligne de commande. En plus, nous pouvons directement convertir du JSON en [CSV](https://fr.wikipedia.org/wiki/Comma-separated_values) pour avoir une liste propre que l'on pourra consommer avec des outils comme [sed](https://fr.wikipedia.org/wiki/Stream_Editor) ou [awk](https://fr.wikipedia.org/wiki/Awk). 

```bash
cat place.geojson |jq -r '.features[]| [.properties.name, .properties.place,.geometry.coordinates[0],.geometry.coordinates[1]]|@csv'

# "Greffern","village",8.0056049,48.7521656
# "Wissembourg","town",7.9445109,49.0365935
# "Strasbourg","city",7.7507127,48.584614
# "Mulhouse","city",7.3389275,47.7467
# "Saverne","town",7.3625953,48.7419909
# "Wittelsheim","town",7.2402432,47.8091086
# "Kingersheim","town",7.3386856,47.7923002
# "Ostwald","town",7.7102193,48.5425109
# "Cernay","town",7.1787669,47.8086824
# "Wittenheim","town",7.3373681,47.8080799

```

## Conclusion 
Je n'ai pas l'habitude de manipuler ce genre de données et je pense que l'on peut faire bien plus avec. J'ai vu aussi qu'il y a d'autre outil comme [Osmosis](https://wiki.openstreetmap.org/wiki/Osmosis) en java.
Si cela vous intéresse, j'ai mis [ici](https://github.com/dridk/france_place_gps) un fichier contenant l'ensemble des cités par départements français ainsi que la procédure pour le fabriquer.


