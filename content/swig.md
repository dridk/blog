Title: Créer un module C++ pour python
Slug: swig
Date: 2022-01-17 15:31:33
Modified: 2022-01-17 15:31:33
Tags: python 
Category: informatique
Author: Sacha schutz
Status: Draft


Python n'étant pas connu pour sa rapidité, Il existe plusieurs solutions pour executer du code compiler. Je citerai par exemple [numba](https://numba.pydata.org/) qui utilise des decorateurs python ou encore [cython](https://cython.org/) qui utilise un language dédié appelé [PyRex](https://www.csse.canterbury.ac.nz/greg.ewing/python/Pyrex/).
Mais mon regard s'est porté vers la librairie [Swig](http://www.swig.org/Doc1.3/Python.html) permettant facillement d'encapsuler du code C ou C++ en Python.    
Je vous propose dans ce billet, d'écrire à l'aide de Swig, un code permettant de compter le nombre de base A,C,G,T depuis en fichier Fasta.

## Objectif

L'objectif est d'écrire un module python appelé *fastareader* qui nous permettra de compter 
le nombre de base avec le code suivant :

```python
from fastareader import FastaReader
reader = FastaReader("hg19.fa")
print(reader["A"])
print(reader["C"])
print(reader["G"])
print(reader["T"])
```

## Swig

Swig est un programme qui va générer à notre place le code C d'une extension python à partir de notre code c++ (fastareader.cpp fastareader.h) et d'un fichier annexe ( fastreader.i).

### Installation
La version Swig à ce jour est la (4.0) .

- ubuntu 
```sudo apt-get install swig ```

- Arch  
```sudo pacman -S swig ```

- Windows
un binaire est disponible [ici](http://www.swig.org/Doc1.3/Windows.html)


## Code C++

Je crée d'abord 2 fichiers (fastareader.h et fastareader.cpp) ou je défini ma classe C++ avec un algortihme minimaliste pour compter le nombre de chaque base avec la librarie standard.    
J'ajoute egalement la methode magique __getitem__ qui sera interprété par python comme une surcharge d'operateur permettant d'accéder aux résultats via la syntaxe ```reader[base]```.

### Fastareader.h

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
    FastaReader(const string& filename);
    int __getitem__(char base);

protected:
    void read_file();

private:
   string mFilename;
   CountMap mCounter;
};


```

### Fastareader.cpp

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


Verifions rapidement que le code compile avec la commande suivante:

```bash
g++ -c fastareader.cpp 
```

Par la suite, nous utiliserons setuptools pour la compilation. 

## Fichier SWIG

le fichier swig d'extension *\*.i* contient les informations utile à swig pour produire le code C du module python. Dans ce fichier vous pourez detailler comment les objects C++ sont converti en object Python. Il existe par default plusieurs convertisseur. Par exemple, ici j'utiliser *std_string.i* qui prend en charge la conversion de std::string vers python string.

### Fastareader.i

```cpp
%module fastareader   // Nom du module
%include "std_string.i" // permet de convertir les std:::string en Python str

%{
#include "fastareader.h" // Partie qui sera intégré aux fichier de sortie
 %}


 %include "fastareader.h" // interface à encapusler pour Python

```

Vous pouvez à présent générer le code de l'extension python avec la commande suivante:

```bash
swig -c++ -python fastareader.i
```

Si tout ce passe bien, vous devez obtenir un fichier *fastareader.py* et un fichier *fastareader_wrap.cxx*.

### Compilation

La meilleurs façon de compiler notre extension python est d'utiliser setuptools. 
Pour cela, je crée un fichier setup.py avec le code suivant :
Notez bien le nom nom de l'extension prefixé par le caractère (\_) 


```python
from distutils.core import setup, Extension

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

Une fois crée, vous pouvez compiler et installer votre extension. Je vous conseil de créer d'abord un environement virtuel. 

```bash
python -m virtualenv venv 
source venv/bin/activate 

python setup.py build  # Compilation 
python setup.py install # Installation 

```


## C++ versus Python

Si tout c'est bien passé, vous devriez pouvoir executer le code suivant:

### test_cpp.py

```python
from fastareader import FastaReader

reader = FastaReader("chr22.fasta")

print(reader["A"])
print(reader["C"])
print(reader["G"])
print(reader["T"])
```

Sur mon PC portable ( intel I7 ), Je met 73 secondes pour compter l'ensemble des bases du chromosome 22.

```bash
(venv) ➜  fastacounter time python test.py 
9094775
8375985
8369235
9054551
python test.py  0,73s user 0,01s system 99% cpu 0,747 total


```

### test_python.py

Le même code écrit uniquement en python, met comme vous pouvez le voir, beaucoup... beaucoup plus de temps. 

```python
with open("chr22.fasta") as file:

    counter = {}

    counter["A"] = 0
    counter["C"] = 0
    counter["G"] = 0
    counter["T"] = 0

    byte = file.read(1)
    while byte:
        if byte in ("A", "C", "G", "T"):
            counter[byte] += 1
            print(counter[byte])
            byte = file.read(1)

print(counter["A"])
print(counter["C"])
print(counter["G"])
print(counter["T"])

```