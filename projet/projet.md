Projet Ariane
=========================

Le projet **Ariane** a été fait dans le cadre du cours d'Outils Logiciels. Il s'agit de l'implémentation d'un jeu en langage Python avec graphisme, moteur de jeu et un solveur naïf.

Le jeu consiste en un labyrinthe peuplé de minotaures hostiles. Ariane, le personnage principal et jouable, doit aller récupérer Thesée, un personnage non jouable, le tout en esquivant les minotaures. Lorsque Ariane récupère Thesée, ils doivent aller jusqu’à la porte toujours en évitant les minotaures.

# Table des matières

1. [Langage et outils](#langage-et-outils)
2. [Fonctionalités](#fonctionalits)
3. [Mode d'emploi](#mode-demploi)\
3.1. [Exécution sur Console](#excution-sur-console)\
3.2. [Exécution depuis PyCharm](#excution-depuis-pycharm)
4. [Le projet](#le-projet)\
4.1. [Organisation globale du projet](#organisation-globale-du-projet)

# Langage et outils

Le jeu a été codé en Python 3.8 et les librairies externes utilisées sont ``sys`` pour la récupération des paramètres de la ligne de commande et ``upemtk`` pour le moteur graphique.

L'environnement de développment principale est Windows 10 et l'éditeur de mon choix est l'IDE de JetBrains pour Python: ``PyCharm``.

Le projet a été entièrement géré sous git. Vous pouvez le retrouver [ici](https://github.com/hyliancloud/INFO_Ariane).

# Fonctionalités

Les fonctionalités implémentées sont l'**affichage graphique du jeu** réalisé avec ``upemtk``, le **moteur de jeu** pour le mode solo et le **solveur naïf**, qui est un solver qui fait une recherche en profondeur et donne la première solution trouvée.

# Mode d'emploi

## Exécution sur Console

Pour exécuter le programme il faut se placer dans le dossier ``src`` et la forme générique de la commande est la suivante:

```bash
python3 -m main.fichier chemin_vers_map.txt
```

L'argument ``-m`` est nécessaire car le projet est organisé en modules et en se plaçant dans le dossier racine des sources on indique que les dossiers visibles sont les packages du projet.

Le "chemin_vers_map.txt" est le chemin de la configuration de base à partir du dossier ``maps``.

### Le jeu

Si on veut jouer sur la carte définie par ``labyrinthe1.txt`` et présente dans ``maps`` on va écrire:

```bash
python3 -m main.game labyrinthe1.txt
``` 

### Le solver

Si on veut la solution pour la carte définie par ``labyrinthe1.txt`` et présente dans ``maps`` on va écrire:

```bash
python3 -m main.solver labyrinthe1.txt
```

Le programme va proposer une interface graphique si l'utilisateur le souhaite et va afficher la solution.

*Cette méthode a été testée sur le PowerShell de Windows 10, car je n'ai pas Linux chez moi. Si cela ne marche pas, vous pouvez essayer d'exécuter depuis PyCharm.*

## Exécution depuis PyCharm

Pour un souci de contextes différents selon si on exécute depuis la console ou depuis l'IDE, il faut aller récupérer la version sur master sur le projet:

```bash
git clone https://github.com/hyliancloud/INFO_Ariane.git
```

Cette version présente de légères différences sur les chemins d'accès aux assets graphiques.

Après avoir importé le projet sur PyCharm, il faut aller sur ``Add Configuration`` et cliquer sur ``+`` puis ``Python``.

Dans ``Script path`` on choisit le fichier ``game.py`` et dans ``Parameters`` on rajoute le chemin du fichier depuis le dossier ``maps`` (comme précédemment). Cliquer sur ``OK``.

Pour le solver, faire la même chose en pointant le chemin du script vers ``solver.py``.

On peut ensuite lancer l'un des deux fichiers en cliquant sur le bouton play en vert.

# Le projet

## Organisation globale du projet

Le code source se trouve dans le dossier [src](./src/) et est organisé en modules.

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
 │   ├── big
 │   ├── defi
 │   └── small
 │
 └── media
```

Les fichiers sources sont organisées en trois packages:

* **Assets**

Les fichiers sources présents dans ``assets`` sont des classes pour représenter les objets principaux du jeu. Labyrinth est l'objet qui regroupe tous les membres du jeu et possède les fonctions du moteur de jeu.

* **Utils**

Les fichiers de ``utils`` possèdent les fonctions qui aident au fonctionnement du jeu et du solver, tel que la lecture des fichiers de base ou encore les fonctions graphiques.

* **Main**

Dans le package ``main`` on trouve les fichiers qui ont la boucle principale du jeu et du solver. Ce sont les fichiers qui devront être executés par l'utilisateur.
