Title: Ce que peut révéler un test génétique sur internet
Slug: tests-genetiques
Date: 2019-03-22 11:35:45
Modified: 2019-03-22 11:35:45
Status: Draft
Tags: génétique
Category: bioinformatique 
Author: Sacha Schutz
SIDEBARIMAGE:../images/common/dnaquestion_banner.jpg

[MyHeritage](https://www.myheritage.fr/), [23andme](https://www.23andme.com), [Ancestry](https://www.ancestry.fr/)... Vous en avez sûrement tous entendu parler. Bien qu'interdits en france [(Article 16-10)](https://www.legifrance.gouv.fr/affichCodeArticle.do?cidTexte=LEGITEXT000006070721&idArticle=LEGIARTI000006419305&dateTexte=&categorieLien=cid), ces tests génétiques en libre accès, bénéficient pourtant d'une bonne publicité.
Depuis peu, elle se fait par l'intermédiaire de youtube. [Amixem](https://www.youtube.com/watch?v=by168cgLmw0), [Squeezie](https://www.youtube.com/watch?v=xrkmdXyOaHg), et récemment [DrNormzan](https://www.youtube.com/watch?v=rEY-smTTLto) ont fait ces tests puis ont partagé leurs résultats en vidéo. Devant cet engouement, j'ai voulu savoir quelles informations étaient rendues à l'utilisateur et si des diagnostics médicaux pouvait être faits avec.   

<div class="figure">     <img src="../images/test_genetique/23andme.png" />      <div class="legend">Promotion 23andMe pour la fête des pères. "Des liens qui unissent vraiment"</div> </div>



## La génétique à deux vitesses
Avant tout, j'aimerais vous montrer le paradoxe avec ces tests génétiques qu'ils soient réalisés dans un cadre médical ou directement sur internet.
En médecine, ces tests sont certainement les analyses les plus contrôlées de toutes les analyses de [biologie médicale](https://fr.wikipedia.org/wiki/Biologie_m%C3%A9dicale). Ils sont sous l'égide de l'[agence de la biomédecine](https://fr.wikipedia.org/wiki/Agence_de_la_biom%C3%A9decine) et sont prescrits uniquement par des [médecins généticiens](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9tique_m%C3%A9dicale) ou par des médecins non généticiens, mais en relation avec une équipe de génétique clinique. Un consentement([exemple](http://robertdebre.aphp.fr/wp-content/blogs.dir/137/files/2013/08/Consentement_genetique-2.pdf)) est obligatoirement demandé au patient-e. En oncogénétique, les analyses sont toujours réalisées deux fois pour éviter une erreur sur l'identité. Pour signer des résultats, même après mon doctorat de médecine, j'ai du attendre d'avoir [les aggréments](https://www.agence-biomedecine.fr/agrement-praticiens-genetique?lang=fr) de l'agence de la biomédecine....      
De l'autre côté, il n'a jamais été aussi facile de faire un test génétique sur internet. Le fait de ne pas avoir besoin de faire une prise de sang les rend même plus faciles et plus accessibles qu'un examen classique de [biochimie](https://fr.wikipedia.org/wiki/Biochimie_clinique) ou d'[hématologie](https://fr.wikipedia.org/wiki/H%C3%A9matologie). On clique sur un bouton, on reçoit un kit salivaire par la poste et le tour est joué.     
Pourquoi un tel contrôle en médecine ? 
D'abord à cause du caractère de la génétique à pouvoir prédire des maladies chez des patients en bonne santé. Contrairement à un examen classique qui teste des patients malades, les examens de génétique concernent souvent des individus sains. C'est une médecine aussi bien de diagnostic que de prédiction. Retirer les seins d'une femme en bonne santé parce qu'elle est porteuse d'une mutation prédisposant au cancer est une décision délicate à prendre.      
Ensuite il y a l'hérédité. Vos gènes ne vous appartiennent pas, vous les partagez avec votre famille et vos futurs enfants. Faire un diagnostic chez vous implique de le faire aussi chez les membres de votre famille, vos frères, vos soeurs, vos enfants. Si vous êtes porteur-se d'une mutation, elle n'impliquera donc pas que vous.

## Un test de généalogie qui en dit plus ?
La plupart de ces tests sont vendus comme une analyse sur vos origines ethniques. La société MyHeritage utilise pour cela une [puce à ADN](https://fr.wikipedia.org/wiki/Puce_%C3%A0_ADN) permettant d'identifier [710 000](https://www.illumina.com/products/by-type/microarray-kits/infinium-omni-express.html) [SNPs](https://fr.wikipedia.org/wiki/Polymorphisme_nucl%C3%A9otidique) absents ou présents de votre génome qu'elle compare à des populations de référence. Une des méthodes est d'identifier des groupes de SNPs ([haplogroups](https://fr.wikipedia.org/wiki/Haplogroupe)) permettant d'associer un individu à sa population d'origine. 
Mais, alors c'est quoi ces "SNPs" et que peuvent ils dire de plus ? 

###Single Nucleotide Polymorphism (SNP)
Un génome humain est constitué de 3 milliards de lettres (A,C,G,T) réparties sur 24 chromosomes différents (1,2...X,Y). Chacune de vos cellules est constituée de 2 versions de ce génome hérité de votre mère et de votre père. (22 paires de chromosomes + XX ou XY selon que vous êtes un homme ou une femme).   
Un **SNP** (prononcé snip) est une modification d'une lettre d'un génome par rapport à un génome de référence. Si par exemple, vous avez un A sur le chromosome 9 en position 101594229, mais que la référence est un G à cette même position, alors vous avez un snps qui peut s'écrire : [chr9-101594229-G-A](http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr9%3A101594229%2D101594229&hgsid=718306327_QCaQikXTcs5svbD4i9HYmPnkk40x). Toutes ces variations observées sont référencées dans la base de données [dbSNP](https://en.wikipedia.org/wiki/DbSNP) qui attribue à chacun de ces snps un identifiant unique ([rs145236923](https://www.ncbi.nlm.nih.gov/snp/rs145236923)).
Quant au [génotype](https://fr.wikipedia.org/wiki/G%C3%A9notype) d'un snp, il indique si vous portez le variant sur un seul ou sur les deux chromosomes de vos parents. Pour un variant donné, il y a donc 3 génotypes possibles. [Homozygote](https://fr.wikipedia.org/wiki/Homozygote) sauvage, [Hétérozygote](https://fr.wikipedia.org/wiki/H%C3%A9t%C3%A9rozygote) et Hétérozygote muté. 

- AA: Vous n'êtes pas porteur-se du SNP
- AG: Vous portez le SNP à l'état hétérozygote
- GG: Vous portez le SNP à l'état homozygote 


<div class="figure">     <img src="../images/test_genetique/genotype.png" />      <div class="legend">Source: <a href="https://en.wikipedia.org/wiki/Zygosity">wikipedia Zygosity</a></div> </div>



La technologie de Puce à ADN permet d'identifier les génotypes de milliers de snps préalablement choisis. Le fichier brut fourni par MyHeritage donne l'idenfiant du snp, sa localisation (chromosome, position) et le génotype pour le p̶a̶t̶i̶e̶n̶t̶ client. 

    # Exemple fichier brut 
    rs28678693  1   838665  TT  
    rs4475691   1   846808  CT
    rs72631889  1   851390  TT


### Comment interpréter ces snps ? 
Sur les 3 milliards du génome, il y a chez un individu environs 1 snp tous les 1000 bases qui vous distingue d'un autre individu. La majorité d'entre eux sont benins, mais certains peuvent être pathogènes. 
En génétique médicale on classe ces snps en 5 classes différentes:

* Classe 1: Benin (benin)
* Classe 2: Probablement benin (likely benin)
* Classe 3: Variant de signification indéterminé (VSI)
* Classe 4: Probablement pathogène (likely pathogenic)
* Classe 5: Pathogène (pathogenic)

Cette classification se fait à l'aide d'arguments scientifiques plus ou moins fort résumés dans ce qu'on appelle les règles de l'[ACMG](https://www.acmg.net/docs/standards_guidelines_for_the_interpretation_of_sequence_variants.pdf). Par exemple, on peut se poser comme question: 

* Le variant est-il déjà décrit dans la littérature ?  
* Le variant est-il rare ou fréquent dans la population?
* Est-il situé dans un gène ou non?
* Si oui, impacte-t'il la protéine codée par ce gène?
* Entraine l'apparition d'un codon stop dans la séquence protéique?
* etc ...

Être porteur-se d'un variant classé pathogène ne suffit pas pour prédire ou diagnostiquer une maladie. Par exemple, dans les [maladies récessives](https://fr.wikipedia.org/wiki/Transmission_autosomique_r%C3%A9cessive), il faut être homozygote muté pour être atteint ([Mucoviscidose](https://fr.wikipedia.org/wiki/Mucoviscidose), [Drépnaocytose](https://fr.wikipedia.org/wiki/Dr%C3%A9panocytose) ... ). Dans les maladies [à pénétrance](https://fr.wikipedia.org/wiki/P%C3%A9n%C3%A9trance) incomplètes ([hémochromatose](https://fr.wikipedia.org/wiki/H%C3%A9mochromatose), vous pouvez être porteur-se de la mutation sans présenter un seul signe de la maladie. Et pour toutes les maladies non mendéliennes, c'est la combinaison de plusieurs variants qui indique un risque pour une maladie. 

## Y a-t-il des variants pathogène dans ces tests ?  
Pour répondre à cette question, j'ai récupéré depuis la base de données [Clinvar](https://www.ncbi.nlm.nih.gov/clinvar/), tous les variants pathogène connus de classe 5 et j'ai fait l'intersection avec les 700 000 snps de la puce [illumina OmniExpress 24](https://www.illumina.com/products/by-type/microarray-kits/infinium-omni-express.html) utilisé par myheritage. Un notebook python est [disponible ici](https://github.com/dridk/notebook/blob/master/myheritage/myheritage.ipynb).
Il en ressort une centaine de SNP classés pathogènes:

<script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.3.1.js"></script>
<script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">

<table id="example" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Pathologie</th>
                <th>rsid</th>
            </tr>
        </thead>
    </table>

<script>
$(document).ready(function() {
    $('#example').DataTable( {
        "ajax": "https://raw.githubusercontent.com/dridk/notebook/master/myheritage/clinvar_omniexpress24.json"
    } );
} );
</script>

Parmi ces maladies génétiques, je me contenterai de commenter 2 d'entre elles.

### La mucoviscidose 
22 snps présents sont identifiés comme pathogènes pour la mucoviscidose. Il s'agit d'une [maladie récessive](https://fr.wikipedia.org/wiki/Transmission_autosomique_r%C3%A9cessive) très fréquente impliquant le gène [CFTR](https://fr.wikipedia.org/wiki/G%C3%A8ne_et_prot%C3%A9ine_CFTR) situé sur le chromosome 7. C'est-à-dire que le snp doit être à l'état homozygote pour entrainer la maladie. Un-e patient-e hétérozygote est porteur-se sain-e, et a un risque d'1 sur 2 de transmettre le snps à son enfant. 
On trouve dans la liste, le snp [rs75961395 ou VG07S29458](https://www.snpedia.com/index.php/Rs75961395) correspondant à la mutation [c.254G>A Gly85Glu](https://cftr.iurc.montp.inserm.fr/cgi-bin/affiche.cgi?variant=c.254G%3EA&provenance=0) décrit dans la base de donnée [CFTR-France](https://cftr.iurc.montp.inserm.fr/cgi-bin/home.cgi?).
Elle fait partie des 30 mutations les plus fréquentes que l'on recherche systématiquement en routine. Mais elle représente moins de 1% des mutations, loin derrière la  mutation DF508, la plus connue et la plus fréquente.

<div class="figure">     <img src="../images/test_genetique/cftr_pie.png" />      <div class="legend">La G85E represence 0.6% des causes de mucoviscidoses. <br/>Source: Cystic Fibrosis Foundation Patient Registry 2014.</div> </div>

### Prédisposition au cancer 
S’il y a bien des tests génétiques contrôlés plus que tous, ce sont les tests d'oncogénétique indiquant la prédisposition au cancer avec une forte pénétrante. C'est-à-dire qu'en étant porteur-se de ce type de variant, il y a une forte probabilité de développer un cancer. La liste de ces gènes est détaillée sur la [page de l'INCA ](https://www.e-cancer.fr/Professionnels-de-sante/L-organisation-de-l-offre-de-soins/Oncogenetique-et-plateformes-de-genetique-moleculaire/Les-predispositions-genetiques)que je vous conseille de lire.

On y trouve le [Syndrome héréditaire de prédisposition au cancer du sein et de l'ovaire](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=FR&Expert=145) [médiatisé par l'actrice Angelina Jolie](https://fr.wikipedia.org/wiki/Angelina_Jolie#Cancer), porteuse probablement d'une mutation dans le gène BRCA1 et qui a eu recours à la chirurgie prophylactique.
Sur la puce, j'ai aussi trouvé le snp [rs28897743 ou i5009343](https://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?rs=rs28897743) situé sur le gène BRCA2. Ce variant est identifié comme probablement pathogène. Je n'ai pas trouvé de papier sur cette mutation. 
Il y a également le snp [rs721048](https://www.snpedia.com/index.php/Rs721048) associé au cancer de la prostate qui d'après [ce papier](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4500625/) est fortement impliqué.

## En conclusion
À première vue, il n'y a pas vraiment de quoi s'alarmer. Parmi ces 700 000 snps, très peu sont répertoriés dans clinvar comme pathogènes. Cependant, gardez en tête que les bases de données de snps sont très loin d'être exhaustives. Chaque jour, de nouveaux variants sont découverts comme pouvant être impliqués dans une maladie. Pour cela d'ailleurs que ces puces sont très utiles à la recherche. Vous n'êtes donc pas à l'abri que, dans 10 ans, ces données révèleront une information importante sur votre santé. 
Je pense en particulier au [score de risque polygénique](https://en.wikipedia.org/wiki/Polygenic_score) associant la présence de plusieurs SNPs à une maladie. On trouve déjà sur internet ce genre de test pour la maladie d'Alzheimer par exemple. Bref, tous ces tests sont, à mon sens, éthiquement borderline. Surtout quand de la publicité est faite sur Youtube sachant que la dirigente [Susan Wojcicki](https://fr.wikipedia.org/wiki/Susan_Wojcicki) est la soeur de [Anne Wojcicki](https://fr.wikipedia.org/wiki/Anne_Wojcicki), elle même dirigente de.... 23andMe.    
Je vous conseille donc de réfléchir à deux fois avant de faire ce genre de test, de bien lire le consentement et de le faire de façon anonyme. J'en ai pas parlé, mais vous n'êtes pas l'abri que ces données arriveront un jour entre de mauvaises mains. L'argument *c'est ultra sécurisé* on l'a déjà entendu avec tous les services webs qui se sont fait piratés.       
Je tiens enfin à signaler à toutes celles et ceux qui ont réalisé le test d'éviter de s'essayer à l'autodiagnostic. Si vous avez la moindre inquiétude quant à vos résultats, consulter un conseiller en génétique médicale en demandant à votre médecin généraliste. 


#Reference
- [Règles de bonne pratique génétique](https://www.has-sante.fr/portail/upload/docs/application/pdf/2013-02/regles_de_bonne_pratique_en_genetique_constitutionnelle_a_des_fins_medicales.pdf
)
- [ACMG](https://www.acmg.net/ACMG/Medical-Genetics-Practice-Resources/Practice-Guidelines.aspx)
- [Etats généraux de bioéthique](https://etatsgenerauxdelabioethique.fr/)
- [Prédisposition oncogénétique - INCA](https://www.e-cancer.fr/Professionnels-de-sante/L-organisation-de-l-offre-de-soins/Oncogenetique-et-plateformes-de-genetique-moleculaire/Les-predispositions-genetiques)