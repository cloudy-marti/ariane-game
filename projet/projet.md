Projet Ariane
=========================


Le projet **Ariane** a été fait dans le cadre du cours d'Outils Logiciels. Il s'agit de l'implémentation d'un jeu en langage Python avec graphisme, moteur de jeu et un solveur naïf.

Le jeu consiste en un labyrinthe peuplé de minotaures hostiles. Ariane, le personnage principale et jouable, doit aller récupérer Thesée, un personnage non jouable, le tout en esquivant les minotaures. Lorsque Ariane récupère Thesée, ils doivent aller jusqu’à la porte toujours en évitant les minotaures.

# Table des matières

1. [Langage et outils](#langage-et-outils)
2. [Fonctionalités et mode d'emploi]
3. [Le projet](#le-projet)\
3.1. [Organisation globale du projet](#organisation-globale-du-projet)\

# Langage et outils

Le jeu a été codé en Python 3.8 et les librairies externes utilisées sont ``sys`` pour la récupération des paramètres de la ligne de commande et ``upemtk`` pour le moteur graphique.

L'environnement de développment principale est Windows 10 et l'éditeur de mon choix est l'IDE de JetBrains pour Python: ``PyCharm``.

Le projet a été entièrement géré sous git. Vous pouvez le retrouver [ici](https://github.com/hyliancloud/INFO_Ariane).

Vous pouvez consulter mon [Python Beginner's Guide](https://github.com/hyliancloud/INFO_Python/blob/master/Guide%20Python/01_python_firsts_steps.md) pour plus d'informations sur l'environnement de développement que j'ai utilisé pour ce projet.

# Fonctionalités implémentées

Les fonctionalités implémentées sont l'affichage graphique du jeu, le moteur de jeu et le solveur naïf.

## Affichage graphique



## Moteur de jeu



## Solver naïf



# Le projet

## Organisation globale du projet

Le code source se trouve dans le dossier [src](./src/).

```bash
projet (racine)
 │
 ├── src
 │   │
 │   ├── assets
 │   │   ├── collectible.py
 │   │   ├── labyrinth.py
 │   │   ├── minotaur.py
 │   │   └── player.py
 │   │
 │   ├── utils
 │   │   ├── graphics.py
 │   │   ├── lab_state.py
 │   │   ├── labyrinth_utils.py
 │   │   └── upemtk.py
 │   │
 │   └── main
 │       ├── game.py
 │       └── solver.py
 │
 ├── maps
 │   ├── big.py
 │   ├── defi.py
 │   └── small.py
 │
 └── media
```

Les fichiers sources sont organisées en trois sous-dossiers:

* **Assets**

Les fichiers sources présents dans Assets sont principalement des classes pour représenter les objets principaux du jeu. Les classes Player, Collectible et Minotaur sont utilisées en guise de structure de données et la classe Labyrinth contient les fonctions principales du moteur de jeu (mouvement des objets).

* **Utils**

Les fichiers suivants possèdent les fonctions

* **Main**

Le package main
