Title: Les algorithmes avec la STL 
Slug: cpp-stl-1
Date: 2017-12-11 17:16:31
Tags: c++,stl
Category: informatique
Author: Sacha schutz

J'utilise de plus en plus dans mon code C++, les [algorithmes](http://en.cppreference.com/w/cpp/algorithm) de la [librairie standard](https://fr.wikipedia.org/wiki/Standard_Template_Library). Couplés avec les [lambdas expression](http://fr.cppreference.com/w/cpp/language/lambda), j'évite d'écrire des tas de boucles for, et mon code est plus lisible. Sans oublier que cette programmation générique est compatible avec les containers [Qt](https://www.qt.io/). Donc forcément, j'adore.     
Voici donc quelques fonctions que j'utilise à foison: 

## Copier un vecteur A dans un vecteur B 

    std::vector<int> a = {1,2,3,4,5,6};
    std::vector<int> b;
    std::copy(a.begin(), a.end(), std::back_inserter(b));
    // b est égal à {1,2,3,4,5,6}

## Insérer un vecteur B dans un vecteur A à la position 3 

    std::vector<int> a = {1,2,3,4,5,6};
    std::vector<int> b = {0,0,0};
    std::copy(b.begin(), b.end(), std::inserter(a, a.begin() + 3));
    // a est égal à {1, 2, 3, 0, 0, 0, 4, 5, 6}

## Calculer la dérivée d'une fonction

    std::vector<double> a = {0,1,4,9,16,25,36};
    std::vector<double> b;
    std::adjacent_difference(a.begin(),a.end(),
                             std::back_inserter(b),
                             [](double a,double b){return (a-b)/2;});
    // a est une parabole x^2 = {0,1,4,9,16,25,36};
    // b est la dérivé de x^2, soit une droite = {0, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5}

## Supprimer toutes les valeurs superieurs à 4 

    std::vector<int> a = {0,1,4,9,16,25,36};
    a.erase(std::remove_if(a.begin(),a.end(),[](int v){return v > 4;}), a.end());
    // a = {0,1,4}

## Elever les valeurs d'un vecteur à la puissance 2 

    std::vector<int> a = {1,2,3,4,5,6,7};
    std::transform(a.begin(),a.end(), a.begin(), [](int v){return v*v;});
    // a = {1, 4, 9, 16, 25, 36, 49}

## Faire la somme d'un vecteur 

    std::vector<int> a = {1,1,1,1,1};
    int result = std::accumulate(a.begin(),a.end(),0);
    // result = 5

## Toutes mes valeurs sont elles superieurs à 0 ?

    std::vector<int> a = {1,2,3,4,5};
    bool success = std::all_of(a.begin(), a.end(), [](int x){return x>0;});
    // success = True 
