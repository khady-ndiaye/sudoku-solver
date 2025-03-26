# Résolution du Sudoku par Force Brute

## Introduction
La force brute est une approche de résolution du Sudoku qui consiste à tester toutes les combinaisons possibles jusqu'à trouver une solution valide. Bien que cette méthode soit inefficace pour les grilles complexes, elle garantit une solution si elle existe.

## Principe de la Force Brute
L'algorithme fonctionne en suivant ces étapes :
1. Identifier les cases vides de la grille.
2. Essayer chaque chiffre possible (1-9) dans une case vide.
3. Vérifier si le chiffre respecte les règles du Sudoku (lignes, colonnes, sous-grilles 3x3).
4. Si valide, passer à la case suivante.
5. Si un blocage est rencontré, revenir à la case précédente (backtracking) et essayer une autre valeur.
6. Répéter jusqu'à ce que la grille soit complète ou que toutes les possibilités aient été testées.

## Performance
La méthode de force brute est extrêmement lente pour les grilles complexes car elle explore un grand nombre de combinaisons. Son temps d'exécution augmente exponentiellement avec le nombre de cases vides.

**Complexité approximative :** O(9^N), où N est le nombre de cases vides.

## Conclusion
Bien que la force brute ne soit pas la méthode la plus efficace, elle constitue une solution simple et garantit une résolution si la grille est valide. Pour une meilleure performance, il est recommandé d'utiliser des algorithmes plus optimisés comme le backtracking avec des heuristiques d'optimisation.

