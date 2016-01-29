Title: Un message immortel ...
Slug: message_immortel
Date: 2016-01-25 17:00:00
Tags: génétique,fun
Category: python
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/backfutur_banner.jpg

Imaginez que vous vouliez transmettre un message à votre arrière arrière arrière petit-fils, à l'instar du Professeur Brown dans [Retour vers le futur 2](https://fr.wikipedia.org/wiki/Retour_vers_le_futur_2). Quelles solutions envisagez-vous ? Une enveloppe en papier? Aucune chance, risque de perte ou de dégradation, ça ne marche que dans les films.
Un Fichier numérique ? Vous voulez dire comme les photos numériques que nous avons tous perdu? C'est malheureusement encore moins fiable qu'une enveloppe.    
Aujourd'hui, je vous propose mieux: écrire votre message dans votre ADN, et le laisser traverser le temps jusqu'à votre descendance! La réception est garantie à 100% !

#De 10 doigts à 4 doigts
Pour écrire un nombre, nous utilisons les 10 symboles suivants [0,1,2,3,4,5,6,7,8,9]. On appelle ça [un système de numération](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_num%C3%A9ration) en base 10. Mais il est tout à fait possible d'utiliser plus ou moins de symboles. Par exemple, un ordinateur en utilise uniquement 2 ([1 et 0]), le nombre 3 en décimal s'écrit 11 en base 2, on appelle ça du binaire. Il existe d'autres systèmes de numération utilisés, comme l’[hexadécimal](https://fr.wikipedia.org/wiki/Syst%C3%A8me_hexad%C3%A9cimal) 16 symboles [0,1,2,3,4,5,6,7,8,9,A,B,C,D,E] ou encore la [base64](https://fr.wikipedia.org/wiki/Base64) [caractère alphanumérique].   
L'ADN est un support d'information numérique, au même titre qu'un disque dur ou qu'une clef USB. Sauf qu'au lieu d'utiliser du binaire, l'ADN utilise un système en base 4 à l'aide des symboles A,C,G,T. Il est donc tout à fait possible de basculer d'un système décimal vers un système de numération en base 4 et d'utiliser l'ADN comme support de l'information.

#l'ASCII génomique
Pour écrire un message on peut utiliser la [table ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange#Table_des_128_caract.C3.A8res_ASCII). Celle-ci attribue à chaque lettre un nombre qui peut s'écrire en décimal, binaire, hexadécimal ... et en génomique, c'est-à-dire en base 4.   
J'ai utilisé la librarie [python-baseconv](https://pypi.python.org/pypi/python-baseconv/1.1.3) pour faire les conversions entre les différents systèmes de numération. Par exemple, la lettre Z s'écrit 90 en décimal, 5A en hexadécimal, 1011010 en binaire et enfin CCGG en génomique.
A partir de là, il suffit pour un message donné, de remplacer chaque lettre par sa représentation génomique et obtenir la séquence de nucléotide que nous allons intégrer dans votre génome!   
Je vous ai fait un script JS pour que vous pussiez tester directement en ligne ! Cliquer sur *Décoder* pour convertir la séquence en texte. Vous pouvez aussi encoder du texte en séquence en cliquant sur *Encoder*.  Attention, n'utilisez que des lettres de l'alphabet ! Pas de nombre ni de caractère spéciaux! 

## ASCII genomic convertor

<form>
 <textarea id="area" rows="4" cols="50">CAGGCGCCCCTTCTATCTCCCGGCCTATCCTTCTCACGTTCGTGCCTTCGACCGTGCGATTGGGCTCACTAGCGCCCCTTCGCCCTCACCTTCGGGCGCCCCTTCGTGCGACCGGCCCTTCTAGCGGCCGCCCGTGCCTTTGAACCTTCTCACGCCCCTTCGCACGGCCTAGCGCCCCTTCGCACGCCCCTTCTAACGTACTCCCTAT
</textarea> <br/>
<input type="button" value="encoder" onClick="start_encode()">
<input type="button" value="decoder" onClick="start_decode()">
<script>

function start_encode()
{
    var textArea = document.getElementById("area");
    // On remplace les caracteres space, car ils s'encode sur 3 et pas 4 symboles
    textArea.value = encode(textArea.value.replace(/\s/g,"_"));
}

function start_decode()
{
    var textArea = document.getElementById("area");
    textArea.value = decode(textArea.value).replace(/_/g," ");

}


function encode(txt){
var code = ['A','C','G','T'];
var output = "";
    for (var i in txt)
    {
    var raw = txt[i].charCodeAt(0).toString(4);
    acgt = raw.replace(/0|1|2|3/g, function lambda(x){return code[x];});
    output+=acgt;
  }
return output;
}
//===========================================================================
function decode(txt){
var code = {'A':0,'C':1,'G':2,'T':3};
var output = "";
    for (var i=0; i<txt.length; i+=4)
    {
    acgt  = txt.substring(i,i+4);
    bases = acgt.replace(/A|C|G|T/g, function lambda(x){return code[x];});
    output+=String.fromCharCode(parseInt(bases,4));

    }
    return output;
}
</script>
</form>


#Copier, Couper, Coller
Nous avons la séquence. Comment l'insérer dans notre ADN ? Bon on ne va pas l'insérer dans toutes vos cellules, car uniquement les spermatozoïdes/ovocytes vont transmettre l'information à votre descendance. On aurait pu partir sur une stratégie de transfection virale. C'est-à-dire utiliser un virus dans lequel votre message est inséré, et infecter vos cellules germinales. Sur ce coup, je pense que ça va être difficile de trouver le virus! Peut être le virus ourlien qui provoque les oreillons et qui touche les testicules, mais pas sûr...
Je vous propose plutôt d'utiliser le tout dernier outil de biotechnologie, qui aboutira sûrement au prochain prix Nobel français, je parle bien sur du complexe enzymatique [CRISPR-CAS9](https://fr.wikipedia.org/wiki/Cas9), le couteau suisse de l'ADN. Ce complexe est capable de découper l'ADN à un endroit précis et d'y insérer n'importe quelle séquence d'ADN. C'est un outil assez révolutionnaire, un article entier y sera bientôt consacré. Contentez vous de cette vidéo pour l'instant:

<iframe width="560" height="315" src="https://www.youtube.com/embed/2pp17E4E-O8" frameborder="0" allowfullscreen></iframe>


Pour modifier nos spermatozoïdes, nous pourrions d'abord faire une biopsie testiculaire, extraire les cellules souches (spermatogonies) et insérer le message dans leurs ADN à l'aide de CRISPR-CAS9, comme l'illustre [cet article](http://www.ncbi.nlm.nih.gov/pubmed/25772367) avec un premier succès chez le rat. Enfin, ces spermatogonies pourront être mis en culture pour devenir des spermatozoïdes compétents, grâce au succès récent d'[une équipe française](http://www.cell.com/cell-stem-cell/abstract/S1934-5909%2812%2900587-5) qui a réussi la culture des spermatogonies.   
Voila, Il ne reste plus qu'à réaliser une fécondation in-vitro, et votre enfant disposera du message dans toutes ses cellules y compris dans ses spermatoizoïdes. A la prochaine génération, la moitié de son génome se diluera avec le génome de sa compagne ( votre belle-fille). Vous avez donc intérêt à dupliquer le message un peu partout sur son génome. Par exemple, en insérant le message sur le chromosome Y, vous êtes certain que votre arrière arrière arrière petit-fils héritera du message car le chromosome Y se transmet de père à fils.  
De même si vous arrivez à modifier l'ADN mitonchondriale d'un ovocyte chez votre compagne, c'est votre descendance féminine qui heritera du message. 

# Et les mutations ?
Bon on a oublié de prendre en compte les mutations. Plus on descend dans les générations, plus grand sera le risque de mutation. Par exemple des [crossing-over](https://fr.wikipedia.org/wiki/Enjambement_%28g%C3%A9n%C3%A9tique%29).ou des mutations ponctuelles. 
En augmentant le nombre de messages, votre descendant pourra retrouver le message originel en faisant des alignements multiples entre tous les séquences. Mais bon, d'ici que le message ait disparu complètement, il faudra un certain temps! Je vais me pencher sur ce calcul d’ailleurs!

#Conclusion
Bon, j'ai un peu déliré dans ce poste. Mais pourtant, derrière cette histoire se cache une réalité qui à le goût de [Bienvenue à Gattaca](https://fr.wikipedia.org/wiki/Bienvenue_%C3%A0_Gattaca). En effet, on peut ajouter un message, mais pourquoi pas modifier vos gènes. Supprimez toutes les maladies génétiques jusqu'à garder uniquement les grands bruns au yeux bleus. Une équipe chinoise a d'ailleurs franchi le pas en modifiant des [embryons humains](http://www.ncbi.nlm.nih.gov/pubmed/25894090).  Nous ne sommes pas encore au niveau de ce film mais la technologie semble disponible! Gardez juste à l'esprit que l'[eugénisme](https://fr.wikipedia.org/wiki/Eug%C3%A9nisme) en diminuant la variabilité des individus est un puissant frein à l'évolution du vivant...


## Référence
* [python-baseconv](https://pypi.python.org/pypi/python-baseconv/1.1.3)
* [Stem Cell Therapy for Male Infertility Takes a Step Forward](http://www.cell.com/cell-stem-cell/abstract/S1934-5909%2812%2900587-5)
* [Targeted Germline Modifications in Rats Using CRISPR/Cas9 and Spermatogonial Stem Cells.](http://www.ncbi.nlm.nih.gov/pubmed/25772367)
* [Cas9 as a versatile tool for engineering biology](http://www.nature.com/nmeth/journal/v10/n10/full/nmeth.2649.html)
* [Chine scientists genetically modify human embryos](http://www.nature.com/news/chinese-scientists-genetically-modify-human-embryos-1.17378)

## Correction 
Merci à @Piplopp pour les corrections 
