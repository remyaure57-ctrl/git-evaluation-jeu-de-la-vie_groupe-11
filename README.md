# Jeu de la vie

Simulation du [jeu de la vie de Conway](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) en Python 3, réalisée par le groupe 11 dans le cadre du module outils de développement logiciel.

## Installation

Le programme utilise uniquement Python 3 et sa bibliothèque standard : aucune dépendance Python à installer.

Pour générer les vidéos, il faut en plus `ffmpeg` et `gource`.

### Ubuntu ou Debian

```
sudo apt update
sudo apt install python3 git gource ffmpeg
```

### macOS

```
brew install gource ffmpeg
```

### Windows

Installer [WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install) (`wsl --install` dans PowerShell en administrateur), puis suivre la procédure Ubuntu ci-dessus dans le terminal WSL.

### Vérification

```
python3 --version
ffmpeg -version
gource --version
```

## Exécution

Le programme se lance depuis la racine du dépôt.

### Sans option

```
$ python3 main.py
Generation of 21 images in directory outputs
```

Crée 21 images (`grid_0000.png` à `grid_0020.png`) dans `outputs`, à partir d'une grille aléatoire de 10 cellules par côté (graine 42).

### Grille aléatoire personnalisée

```
$ python3 main.py -n 50 -m 200 -s 4200
Generation of 201 images in directory outputs
```

### Évolution d'une grille lue sur l'entrée standard

La première ligne donne la taille, puis les lignes de la grille. Bords fixes (par défaut) :

```
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -t text
iteration: 1
0 1 0
0 0 1
0 1 0
```

### Conditions aux limites périodiques

```
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -p -t text
iteration: 1
0 0 0
0 0 0
0 0 0
```

### Erreurs

Une entrée invalide produit un message sur la sortie d'erreur et un code de sortie différent de 0 :

```
$ printf '2\n1 0\n1 2\n' | python3 main.py -t text
Error: la ligne 2 contient une case invalide : 2
```

## Arguments

| Option courte | Option longue | Description | Valeur par défaut |
|---|---|---|---|
| `-n N` | `--nb_cells N` | nombre de cellules par côté pour une grille aléatoire (entier strictement positif) | `10` |
| `-m N` | `--max_iterations N` | numéro de la dernière itération à calculer (entier positif ou nul) | `20` |
| `-s N` | `--seed N` | graine du générateur aléatoire (entier quelconque) | `42` |
| `-o DOSSIER` | `--output_directory DOSSIER` | dossier dans lequel écrire les images | `outputs` |
| `-t TYPE` | `--output_type TYPE` | type de sortie : `image` ou `text` | `image` |
| `-p` | `--periodic` | active les conditions aux limites périodiques | désactivée |
| `-h` | `--help` | affiche l'aide du programme | — |

## Vidéos

## Auteurs

Groupe 11 :

- MAILLOT Benoît, n° étudiant : 45004199
- AURE Remy, n° étudiant : 45005317
- SIMONIN Clément, n° étudiant : 45002492
- ESSOB Alexandre, n° étudiant : 41009089

## Liens utiles

- [Workshop 3 : rebase et historique final](https://github.com/frozar/git-workshop-3) : organisation Git attendue pour ce projet,
- [Historique final du workshop 3](https://github.com/frozar/git-workshop-3/blob/main/img/historique-final.png) : exemple du graphe à obtenir,
- [Jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) : présentation des règles du jeu de Conway,
- [Documentation argparse](https://docs.python.org/fr/3/library/argparse.html) : analyse des arguments d'un script Python,
- [Documentation random](https://docs.python.org/fr/3/library/random.html) : génération de grilles aléatoires reproductibles,
- [Philosophie d'Unix](https://fr.wikipedia.org/wiki/Philosophie_d%27Unix) : description de la philosophie Unix,
- [Pipeline (Unix)](https://en.wikipedia.org/wiki/Pipeline_%28Unix%29) : description du pipe,
- [Installation de WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install) : procédure officielle pour Windows,
- [Documentation ffmpeg](https://ffmpeg.org/documentation.html) : installation et utilisation de ffmpeg,
- [Site officiel de Gource](https://gource.io/) : présentation et téléchargement de Gource,
- [My Gource video production pipeline](https://dev.to/voieducode/my-gource-video-production-pipeline-5eb0) : exemple de création d'une vidéo Gource,
- [Documentation officielle de git rebase](https://git-scm.com/book/fr/v2/Les-branches-avec-Git-Rebaser-Rebasing) : fonctionnement du rebase.