# Le jeu de la vie de John Conway
***

Le jeu de la vie est un automate cellulaire imaginé par John Horton Conway en 1970
et qui est probablement le plus connu de tous les automates cellulaires. 
Malgré des règles très simples, le jeu de la vie est [Turing-complet](https://fr.wikipedia.org/wiki/Turing-complet).

## 
1. [Règles](#règles)
2. [Code](#code)
4. [Structure](#structure)
5. [Turing-complet](#Turing-complet)


## Règles
***

Le jeu de la vie est particulièrement intéressant car il est facile à comprendre et à coder 
mais nous permet d'amener une grande grande variété de structures plus ou moins complexes

![canon](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)

Le jeu se déroule sur une grille à deux dimensions, dont les cases — qu’on appelle des « cellules », 
par analogie avec les cellules vivantes — peuvent prendre deux états distincts : « vivante » ou « morte ».

À chaque étape, l’évolution d’une cellule est entièrement déterminée par l’état de ses huit voisines de la façon suivante :

- une cellule morte possédant exactement trois voisines vivantes devient vivante (elle naît) ;
- une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt.

On peut également formuler cette évolution ainsi :

- si une cellule a exactement trois voisines vivantes, elle est vivante à l’étape suivante.
- si une cellule a exactement deux voisines vivantes, elle reste dans son état actuel à l’étape suivante.
- si une cellule a strictement moins de deux ou strictement plus de trois voisines vivantes, elle est morte à l’étape suivante.

## Code
***

Objectifs : 

- Coder en python le jeu de la vie et afficher dans la console
- Adapter pour que le jeu fonctionne avec notre matrice de led -> Réutiliser LED_display.py

## Structure
***
Des structures, constituées de plusieurs cellules, peuvent apparaître dans l’univers ; les plus classiques sont :

- les structures stables ![carré](https://upload.wikimedia.org/wikipedia/commons/6/63/Gol-block.png)
- les structures périodiques, ou oscillateurs ![grenouille](https://upload.wikimedia.org/wikipedia/commons/5/5f/Gol-toad.gif)
- les vaisseaux ![planeur](https://upload.wikimedia.org/wikipedia/commons/4/4f/Gol-glider.gif)

## Turing-complet
***
Le jeu de la vie est complet. [Il est donc possible de programmer n'importe quelle machine de Turing dans celui-ci.](https://www.youtube.com/watch?v=xP5-iIeKXE8)

[Portes Logiques](https://www.youtube.com/watch?v=Kk2MH9O4pXY)


