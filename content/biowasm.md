Title: Biowasm: Vos outils bioinformatiques sur une page web static
Slug: biowasm
Date: 2024-09-22 19:30:31
Modified: 2024-09-22 19:30:31
Tags: web
Category: informatique
Author: Sacha schutz
SIDEBARIMAGE:images/common/term_banner.jpeg


Récemment, une collègue m'a fait découvrir [Biowasm](https://biowasm.com/). C'est une collection d'outils bioinformatiques bien connus, compilés en [WebAssembly](https://fr.wikipedia.org/wiki/WebAssembly). Concrètement, cela signifie que nous pouvons créer des interfaces graphiques pour nos collègues non-spécialistes en bioinformatique, directement sur une simple page web statique, sans avoir besoin de serveur. Et Justement, un biologiste m'a demandé s'il était possible de générer un fichier [FASTQ](https://fr.wikipedia.org/wiki/FASTQ) réduit, autrement dit de faire un échantillonnage aléatoire (downsampling). C'était donc une excellente occasion de tester Biowasm en construisant une page web qui fait le travail.

## Créer la page web static 

L'interface graphique se résume à l'essentiel : un bouton pour charger le fichier FASTQ, un champ pour saisir le nombre de reads souhaités, et un gros bouton pour lancer la transformation. Impossible de faire plus simple !
J'ai construit cette interface en HTML pur, en utilisant la bibliothèque CSS [PicoCSS](https://picocss.com/). Pour être honnête, je n'ai pas trop aimé coder tout ça à la main. Après avoir gouté à plusieurs frameworks web, et à [TailwindCSS](https://tailwindcss.com/), c'était laborieux. Mais pour ce projet simple, ça faisait largement l'affaire.
Pour ceux qui sont allergique au HTML, je recommande de jeter un œil à [Dominate](https://github.com/Knio/dominate), un outil qui permet de générer du HTML directement en Python. C'est même moins verbeux que le HTML classique, et personnellement, je trouve ça génial !

## Utilisation de biowasm 

Biowasm est distribué via une bibliothèque JavaScript appelée [Aioli](https://github.com/biowasm/aioli), qui vous permet d'exécuter divers outils bioinformatiques en seulement quelques lignes de code. Actuellement, il s'agit principalement d'applications écrites en C/C++, telles que [samtools](http://www.htslib.org/), [bedtools](https://bedtools.readthedocs.io/en/latest/) et [bwa](https://github.com/lh3/bwa). Vous pouvez consulter la liste complète des outils [disponibles ici](https://biowasm.com/cdn/v3/).

Par exemple, pour exécuter bedtools, il vous suffit d'ajouter ce code à votre page HTML :

```html 

<script src="https://biowasm.com/cdn/v3/aioli.js"></script>
<script type="module">
const CLI = await new Aioli(["bedtools/2.31.0"]);

const output = await CLI.exec(`bedtools --version`);


</script>

```

Incroyable, non ? En plus, Aioli propose [une API](https://biowasm.com/documentation/) qui permet de gérer un système de fichiers virtuel local. Comme vous le savez, un navigateur ne peut pas accéder directement à votre système de fichiers pour des raisons évidentes de sécurité. Vous vous demandez sûrement comment peut on alors charger de gros fichiers, comme un fichier [BAM](https://fr.wikipedia.org/wiki/Binary_Alignment_Map) ?

Eh bien, c’est possible ! Le système de fichiers virtuel ne fait que pointer vers votre fichier réel, sans le charger intégralement en mémoire. Cependant, il y a une limitation : la sortie que vous générez doit elle être entièrement stockée en mémoire avant d'être téléchargée sous forme de fichier. Cela pose problème si vous devez générer un fichier de 100 Go alors que votre machine ne dispose que de 8 Go de RAM.


## Bioweb : Fastq sampling

J'ai donc mis tout cela en pratique en créant une page web statique permettant de réaliser le downsampling d'un fichier FASTQ avec [seqtk](https://github.com/lh3/seqtk) et sa commande ```seqtk sample```. Je l'ai publié sur une page github [**disponnible ici**](https://dridk.github.io/bioweb/sampling_fastq.html) Cet exemple est particulièrement intéressant car il implique la gestion du chargement d'un fichier FASTQ ainsi que la sauvegarde du fichier généré.
Le processus fonctionne plutôt bien. J'ai testé avec un fichier FASTQ de 5 Go : c'était un peu long, mais j'ai obtenu le résultat en moins d'une minute.

## Conclusion 

Biowasm est un outil très pratique qui vous permet de déployer rapidement de petits outils bioinformatiques pour vos biologistes, sans avoir besoin de serveur. Il est extrêmement simple à utiliser, bien que probablement limité pour des tâches plus complexes ou pour l'exécution de pipelines plus lourds.
Ironiquement, la partie la plus difficile de ce projet a été... de personnaliser le bouton "upload" du formulaire. D'ailleurs je n'ai pas reussi, question de sécurité.       
Si vous aussi vous voulez faire un outil, hesitez pas à l'ajouter sur mon repo via une [pull-request](https://docs.github.com/fr/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

*PS : Dites bonjour dans les commentaires, cela me motivera pour publier plus  !*


## Remerciements 

- Merci à @lourdes pour la découverte
