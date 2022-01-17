Title: Créer un module python en C++ avec SWIG
Slug: swig
Date: 2022-01-17 23:18:57
Modified: 2022-01-17 23:18:57
Tags: python,C++
Category: informatique
Author: Sacha Schutz


[Python](https://fr.wikipedia.org/wiki/Python_(langage)) n'étant pas connu pour sa rapidité, il existe plusieurs solutions pour exécuter du code compilé. Je citerai par exemple [numba](https://numba.pydata.org/) qui utilise des décorateurs dédiés ou encore [cython](https://cython.org/) qui permet d'écrire un module avec un langage mélangeant du python et du [C](https://fr.wikipedia.org/wiki/C_(langage)).   
Mais mon regard s'est porté récemment vers la librairie [SWIG](http://www.swig.org/Doc1.3/Python.html) qui permet facilement d'encapsuler du code [C++](https://fr.wikipedia.org/wiki/C%2B%2B) dans un module Python. Je vous propose donc dans ce billet, d'écrire à l'aide de *SWIG*, un module en C++ permettant de compter le nombre de base A,C,G,T présent dans un fichier [Fasta](https://fr.wikipedia.org/wiki/FASTA_(format_de_fichier)). 

## Objectif

L'objectif est d'écrire un module python appelé *fastareader* qui s’exécute de la façon suivante : 

```python
from fastareader import FastaReader

# Instanciation : Compte le nombre de base A,C,G,T dans le fichier chr22.fa
reader = FastaReader("chr22.fa")

# Affiche le nombre de chaque base
print(reader["A"])
print(reader["C"])
print(reader["G"])
print(reader["T"])
```

## Installation de SWIG

Swig est un programme en ligne de commande qui permet de générer automatiquement le code d'un module python à partir de notre code C++.    
Pour installer Swig dans sa version (4.0):

- **ubuntu**  
```sudo apt-get install swig ```


- **Windows**      
Télécharger le binaire [ici](http://www.swig.org/Doc1.3/Windows.html)


## Création du module en C++

Je crée d'abord 2 fichiers (*fastareader.h* et *fastareader.cpp*) contenant la classe C++ qui nous calculera le nombre de base après avoir parcouru le fichier.    
Je lui ajoute la [méthode magique](https://www.geeksforgeeks.org/dunder-magic-methods-python/) **```__getitem__```** qui sera interprétée par python comme  surcharge d’opérateur pour accéder aux résultats via la syntaxe **```reader['A']```**.

#### Fastareader.h

```cpp
#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <cctype>

using namespace std;

using CountMap = map<char,int> ; 

class FastaReader
{
public:
    // Constructeur 
    FastaReader(const string& filename);
    
    // Fonction magique pour pouvoir faire reader['A']
    int __getitem__(char base);

protected:
    // Lis le fichier lors de la construction
    void read_file();

private:
   string mFilename;
   CountMap mCounter;
};


```

#### Fastareader.cpp

```cpp 
#include "fastareader.h"

FastaReader::FastaReader(const string& filename)
:mFilename(filename)
{

    read_file();
}

int FastaReader::__getitem__(char base)
{
    return mCounter[base];
}

void FastaReader::read_file()
{
    // Nous parcourons le fichier et nous comptons les bases A,C,G,T
    ifstream infile(mFilename);
    string line;

    mCounter['A'] = 0;
    mCounter['C'] = 0;
    mCounter['G'] = 0;
    mCounter['T'] = 0;

    while (infile.good())
    {
        char c = toupper(infile.get());
        if ((c == 'A') || (c =='C') ||( c=='G') || (c == 'T'))
            mCounter[c]++;
    }
}
```


Vous pouvez vérifier rapidement que le code compile avec le commande suivante. Mais par la suite, nous utiliserons [setuptools](https://setuptools.pypa.io/en/latest/) pour la compilation et l'installation du module.

```bash
g++ -c fastareader.cpp 
```


## Le fichier d'interface SWIG

L'interfaçage entre python et le C++ est paramétrée depuis le fichier *fastareader.i*. C'est ce fichier qu'il faudra modifier si vous voulez détailler comment convertir des objets C++ en objets Python. Cette conversion existe déjà pour la plus part des types. Par exemple, ici j'importe **```std_string.i ```** afin de mapper les strings C++ en string Python. Allez voir la documentation sur les *[typemaps](http://www.swig.org/Doc1.3/Typemaps.html)* pour plus de détails.

#### Fastareader.i

```cpp
%module fastareader   // Nom du module python généré
%include "std_string.i" // permet de convertir les std:::string en Python string

%{
// Le code de cette section sera intégré au fichier produit
#include "fastareader.h" 
 %}

 // Cette section contient la liste des interfaces C++ à encapsuler
 %include "fastareader.h"

```

Vous pouvez à présent générer le code de l'extension python avec la commande suivante:

```bash
swig -c++ -python fastareader.i
```

Si tout se passe bien, vous devez obtenir 2 fichiers:

- un fichier **fastareader.py** contenant le module python à importer.
- un fichier **fastareader_wrap.cxx** contenant l'encapsulation de votre code C++.

## Compilation avec setuptools

Une fois le code de l'extension généré, il faut le compiler et l'installer. 
Pour cela, vous pouvez utiliser [setuptools](https://setuptools.pypa.io/en/latest/) disponible dans la librairie standard de python.    
Créer le fichier *setup.py* avec le code suivant:

```python
from distutils.core import setup, Extension

# Description de l'extension et du code à compiler.
# Notez bien le nom de l'extension `_fastareader` préfixé par le caractère `_` 

fastareader_module = Extension(
    "_fastareader", sources=["fastareader.cpp", "fastareader_wrap.cxx"]
)


setup(
    name="fastareader",
    version="0.1",
    author="Sacha Schutz",
    ext_modules=[fastareader_module],
    py_modules=["fastareader"],
)

```

Compiler et installer maintenant votre module avec les commandes suivantes:       

```bash
python -m virtualenv venv 
source venv/bin/activate 

python setup.py build  # Compilation 
python setup.py install # Installation 

```

Si tout c'est bien passé, vous devriez pouvoir lancer le code python vu au début de ce billet.

>**Note**: Sous windows, vous aurez besoin d'installer [Visual studio](https://docs.microsoft.com/fr-fr/visualstudio/install/install-visual-studio?view=vs-2022) pour compiler une extension Python. Attention, à bien vérifier les architectures (x64, x86) et quel versions de python vous utilisez.      







## Le benchmark

Sur mon PC portable, Je met **0.63 secondes** pour compter l'ensemble des bases du chromosome 22 avec la module C++. Et encore, le code n'est pas optimisé.

#### bench_cpp.py
```python
from fastareader import FastaReader

reader = FastaReader("chr22.fasta")

print(reader["A"])
print(reader["C"])
print(reader["G"])
print(reader["T"])
```

```bash
(venv) ➜ time python bench_cpp.py
9094775
8375985
8369235
9054551
python test.py  0,63s user 0,02s system 99% cpu 0,645 total

```


Le même code écrit uniquement avec python prend **12 secondes**. Soit 20 fois plus longtemps.  

#### bench_python.py
```python
with open("chr22.fasta") as file:

    counter = {}

    counter["A"] = 0
    counter["C"] = 0
    counter["G"] = 0
    counter["T"] = 0

    byte = file.read(1)
    while byte:
        byte = str.upper(byte)
        if byte in ("A", "C", "G", "T"):
            counter[byte] += 1

        byte = file.read(1)


print(counter["A"])
print(counter["C"])
print(counter["G"])
print(counter["T"])

```

```bash
(venv) ➜ time python bench_python.py
9094775
8375985
8369235
9054551
python test_py.py  12,67s user 0,02s system 99% cpu 12,791 total
```

## Si vous voulez m'aider !

J'ai commencé à écrire un simple parseur de fichier VCF, qui contrairement à [cyvcf2](https://github.com/brentp/cyvcf2), ne dépend pas de htslib et compile facilement sous windows. 
[https://github.com/dridk/vcfreader](https://github.com/dridk/vcfreader)


## Référence 

- [Documentation de SWIG](http://www.swig.org/doc.html)