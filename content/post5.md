Title: Pygal, pour faire des graphiques en vectoriel ! 
Slug: pygal
Date: 2014-06-23 18:25:30
Tags: chart,plot,graph,svg
Category: python
Author: Sacha Schutz

<!-- <p class="img-header">
    <img src="../images/post5/header.png">
</p>
 -->

Il existe plusieurs façons de créer de jolis graphiques avec python. La plus connue est bien entendu [matplotlib](http://matplotlib.org/) qui permet de faire du simple camembert au super graphique 3D isobarique spéctromotogramique. (je vous rassure ça veux rien dire). Il y en a aussi d'autres, moins connus que je cite en exemple : [pyQwt](http://pyqwt.sourceforge.net/), [plotly](https://plot.ly/api/), [Vincent](https://pypi.python.org/pypi/vincent/0.1.6) ( J'en parlerai dans un prochain post), [pyla](http://pyla.codeplex.com/), [chartDirector](http://www.advsofteng.com/) etc... 
Sans utiliser python, il y a aussi le [langage R](http://www.r-project.org/) qui est un outil extrêmement puissant pour faire des statistiques et des graphiques scientifiques. Et enfin, [gnuplot](http://www.gnuplot.info/), logiciel à part entière, que vous exécutez directement depuis la console.
Dans ce poste, on va parler d'une n-ième *chart library*, que j'affectionne tout particulièrement, tant son rendu est stylé! Il s'agit de [pygal](http://pygal.org/), une librairie qui va non seulement nous générer des graphiques super classes, mais va les générer dans un format vectoriel! 

### Des images vectorielles  ?

Bon, au cas ou vous ne savez pas ce qu'est du vectoriel, je vous l'explique rapidement. 

#### Image matricielle
Les images aux formats *.png *.bmp, *.jpeg etc... sont des images matricielles. C'est à dire qu'elles sont définies par un tableau contenant la couleur des pixels. Par exemple une image de 3x3 pixels contiendra : 
    
    bleu - blanc - rouge 
    bleu - blanc - rouge 
    bleu - blanc - rouge

Les différents formats (*.png *.bmp, *.jpeg), représentent différents algorithmes pour stocker et compresser ces informations. 

#### Image vectorielle 
Les images aux formats *.svg sont des images vectorielles. Il existe d'autres formats propriétaires comme *.ai (Adobe illustrator). mais retenez *.svg qui est un standard libre.  
Ces images sont définies par leurs *façons d'être dessiné* grâce à des objets géométriques simples. A contrario des images matricielles, l'image vectorielle sera constituée d'une série d'action. 

    Rectangle(couleur=bleu, largeur=3, longueur = 2)
    Rectangle(couleur=blanc,largeur=3, longueur = 2)
    Rectangle(couleur=rouge, largeur=3, longueur = 2)

Toutes ces règles sont en fait écrites en xml, et ça donne plutôt ça :

    <?xml version="1.0" encoding="utf-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="300" height="200">
    <rect width="100" height="80" x="0" y="70" fill="green" />
    </svg>

Les images vectorielles ont ainsi plusieurs avantages par rapport au images matricielles. Tout d'abord elle n'ont pas de résolution. A partir d'une image vectorielle, vous pouvez faire un icône ou un poster de 10 mètres sans jamais perdre de résolution. Également, de part leurs syntaxes xml, ils sont facilement éditables. Et devinez quoi ? Vous pouvez même y mettre du javascript pour faire des animations. 
Ci-dessous, deux images, l'une vectorielle et l'autre matricielle. Vous pouvez les ouvrir séparément et zoomer dessus pour voir la différence. Enfin, vous la voyez déjà ! 

<p align="center">
    
  <img src="/images/post5/vectoriel.svg"  width="100px" alt="vectoriel" />
  <img src="/images/post5/matriciel.png"  width="100px" alt="matriciel"/>
</p>


### Premier pas avec pygal 

#### Installation 
Comme d'habitude ...

    pip install pygal 

Attention, pour pouvoir exporter vos données vectorielles en *.png via **render_to_png**, vous devez installer : 

    pip install CairoSVG tinycss cssselect

#### Création d'un <del>Livarot</del> Camembert 

    import pygal
    pie_chart = pygal.Pie()
    pie_chart.title = 'Activity'
    pie_chart.add('Sleep', 60)
    pie_chart.add('blog', 20)
    pie_chart.add('code', 30)
    pie_chart.add('study', 9)

Faites maintenant **pie_chart.render()** Pour générer le code xml de votre image vectorielle... Bon, c'est juste du code xml qui s'affiche... Mais heureusement, pygal propose plusieurs méthodes : 

    - pie_chart.render_in_browser()         //Vous l'ouvrira dans le browser
    - pie_chart.render_to_file("mypie.svg") //Création du fichier mypie.svg
    - pie_chart.render_to_png("mypie.png")  //Création du fichier mypie.png 

Voilà le résultat final quand je l'insère dans mon code html de cette façon : 

      <embed src="/images/post5/mypie.svg" type="image/svg+xml" width="100px" />

  <embed src="/images/post5/mypie.svg" type="image/svg+xml" />


Oui c'est beau ! J'espère que vous avez remarqué l'interactivité du graphique lorsque vous passez la souris dessus.   
Mais sinon, à part des camemberts, on peut faire tout un tas d'autres graphiques. 

####Autres graphiques 
Je vous met dans cette section, une série de graphique réalisable avec pygal. Il y en a plein d'autre! Allez faire un tour sur cette page : [pygal charts type](http://pygal.org/chart_types/#idbar-charts-histograms)
###### Line Charts

    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    line_chart.render_to_file("line_chart.svg")

[Afficher le graphique](/images/post5/line_chart.svg)

####Bar Charts

    bar_chart = pygal.Bar()
    bar_chart.title = 'Browser usage evolution (in %)'
    bar_chart.x_labels = map(str, range(2002, 2013))
    bar_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    bar_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    bar_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    bar_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    bar_chart.render_to_file("bar_chart.svg")

[Afficher le graphique](images/post5/bar_chart.svg)

####Scatter plot

    xy_chart = pygal.XY(stroke=False)
    xy_chart.title = 'Correlation'
    xy_chart.add('A', [(0, 0), (.1, .2), (.3, .1), (.5, 1), (.8, .6), (1, 1.08), (1.3, 1.1), (2, 3.23), (2.43, 2)])
    xy_chart.add('B', [(.1, .15), (.12, .23), (.4, .3), (.6, .4), (.21, .21), (.5, .3), (.6, .8), (.7, .8)])
    xy_chart.add('C', [(.05, .01), (.13, .02), (1.5, 1.7), (1.52, 1.6), (1.8, 1.63), (1.5, 1.82), (1.7, 1.23), (2.1, 2.23), (2.3, 1.98)])
    xy_chart.render_to_file("scatter_plot.svg")

[Afficher le graphique](images/post5/scatter_plot.svg)

####Box plot

    box_plot = pygal.Box()
    box_plot.title = 'V8 benchmark results'
    box_plot.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
    box_plot.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
    box_plot.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
    box_plot.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
    box_plot.render_to_file("box_plot.svg")

[Afficher le graphique](images/post5/box_plot.svg)

Voilà, fini pour cette article! Je vais pas me casser la tête à faire plus, car la [documentation officiel](http://pygal.org/documentation/) est parfaitement réalisée. Vous pouvez par exemple, customiser vos graphiques en changeant de thème, ou créer des thèmes personnalisés. Ou encore modifier le rendu en jouant sur les marges, les labels , les dimensions etc...


* * *

#### Référence
[pygal.org](http://pygal.org/)   
[pygal Documentation](http://pygal.org/documentation/)   
[teste en ligne de pygal](http://cabaret.pygal.org/)   





