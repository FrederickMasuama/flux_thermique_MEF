
# Résolution de l'équation de la chaleur par la méthode des éléments finis (MEF)

## Brève description

Dans ce projet nous avons implémenté une solution numérique de l'équation de la chaleur stationnaire en 2D sur une plaque carrée en utilisant la méthode des éléments finis (MEF). La plaque est soumise à une source de chaleur uniforme et possède des conditions aux limites de Dirichlet avec une température fixée à zéro sur les bords.

## A propos du code

Ce script peut être scindé en 3 grandes parties: 

1re partie: 
- Implémentation de la méthode itérative de résolution des équations matricielles : Gauss-Seidel
- Les paramètres physiques: dimensions de la plaque, valeurs de la source de chaleur et de la conductivité. 

2e partie: 
- Discrétisation de la plaque en un maillage régulier
- Assemblage de la matrice de conductivité thermique et du vecteur des forces
- Imposition de conditions aux limites de Dirichlet

3e partie:
- Résolution du système linéaire :
    1. Par inversion matricielle en faisant appel à linalg.solve
    2. Par la méthode de Gauss-Seidel avec une tolérance de 1e-6, max_iter = 1000 et le vecteur initial est le vecteur nul
- Visualisation de la distribution de température grace à matplotlib

## Dépendances

Le script nécessite les bibliothèques suivantes :

- `numpy` pour les calculs numériques et l'assemblage du système linéaire
- `matplotlib` pour la visualisation des résultats

## Installation

Assurez-vous d'avoir Python installé, ainsi que les dépendances nécessaires. Sinon vous pouvez facilement les installer via pip :

```sh
pip install numpy matplotlib
```

## Utilisation

Exécutez simplement le script avec :

```sh
python script.py
```

Cela affichera la distribution de température sur la plaque.

Nous avons pris un maillage de 25 X 25 noeuds pour la rapidité des calculs avec Gauss-Seidel mais n'hésitez pas de prendre plus et utiliser linalg.solve pour plus de rapidité. 
Plus il y a des noeuds, plus le rendu de l'image est fluide. 
  

## Paramètres

Les paramètres suivants peuvent être modifiés dans le script :

- `k` : Conductivité thermique
- `q` : Source de chaleur
- `Lx`, `Ly` : Dimensions de la plaque
- `Nx`, `Ny` : Nombre de nœuds dans chaque direction

## Résultats

Le script génère une carte de chaleur représentant la distribution de température sur la plaque. La température est fixée à zéro sur les bords et la chaleur se diffuse depuis la source intérieure selon la conductivité thermique.


## Licence et documentation

Ce projet a été réalisé avec l'aide: 
- Des cours magistraux pour la licence 3 Mathématiques de Monsieur Christophe Berton
- La chaine You Tube https://www.youtube.com/@FredericBruyeremeca
- Un code open source de MIT 





