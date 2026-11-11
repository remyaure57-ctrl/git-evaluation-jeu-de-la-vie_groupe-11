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

## Liens utiles