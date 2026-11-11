import argparse
import random
import sys

from lib import write_grid

def positive_int(value):
    """Entier strictement positif (pour --nb_cells)."""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' n'est pas un entier")
    if number <= 0:
        raise argparse.ArgumentTypeError(
            f"la valeur doit être strictement positive (reçu : {number})"
        )
    return number


def non_negative_int(value):
    """Entier positif ou nul (pour --max_iterations)."""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' n'est pas un entier")
    if number < 0:
        raise argparse.ArgumentTypeError(
            f"la valeur doit être positive ou nulle (reçu : {number})"
        )
    return number

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Simulation du jeu de la vie de Conway."
    )
    parser.add_argument("-n", "--nb_cells", type=positive_int, default=10,
                        help="nombre de cellules par côté (grille aléatoire)")
    parser.add_argument("-m", "--max_iterations", type=non_negative_int, default=20,
                        help="numéro de la dernière itération à calculer")
    parser.add_argument("-s", "--seed", type=int, default=42,
                        help="graine du générateur aléatoire")
    parser.add_argument("-o", "--output_directory", default="outputs",
                        help="dossier de sortie des images")
    parser.add_argument("-t", "--output_type", choices=["image", "text"],
                        default="image", help="type de sortie")
    parser.add_argument("-p", "--periodic", action="store_true",
                        help="conditions aux limites périodiques")
    return parser.parse_args(argv)

def grille_aleatoire(nb_cells, seed):
    """Crée une grille carrée aléatoire, identique pour une même graine."""
    rng = random.Random(seed)
    return [
        [rng.choice([0, 1]) for _ in range(nb_cells)]
        for _ in range(nb_cells)
    ]

def erreur(message):
    """Affiche un message sur STDERR et arrête le programme."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


def lire_grille(texte):
    """Transforme le texte reçu sur STDIN en grille, en vérifiant le format."""
    # On garde seulement les lignes qui ne sont pas vides
    lignes = []
    for ligne in texte.splitlines():
        if ligne.strip() != "":
            lignes.append(ligne)

    if len(lignes) == 0:
        erreur("la grille est vide")

    # La première ligne donne la taille
    try:
        taille = int(lignes[0])
    except ValueError:
        erreur(f"la première ligne doit être la taille : {lignes[0]}")
    if taille <= 0:
        erreur(f"la taille doit être strictement positive : {taille}")

    # Il doit y avoir autant de lignes que la taille
    if len(lignes) - 1 != taille:
        erreur(f"il faut {taille} lignes, il y en a {len(lignes) - 1}")

    # On lit chaque ligne de la grille
    grille = []
    numero = 1
    for ligne in lignes[1:]:
        cases = ligne.split()
        if len(cases) != taille:
            erreur(f"la ligne {numero} doit avoir {taille} cases, elle en a {len(cases)}")
        ligne_grille = []
        for case in cases:
            if case != "0" and case != "1":
                erreur(f"la ligne {numero} contient une case invalide : {case}")
            ligne_grille.append(int(case))
        grille.append(ligne_grille)
        numero += 1
    return grille

def calcul_generation_fixe(matrix):
    nouv_mat=[]
    l=len(matrix)
    for i in range(l):
        ligne=[]
        #parcours des voisins en évitant les hors bords.
        for j in range(l):
            nb_voisines=0
            if i!=0:
                if matrix[i-1][j]==1:
                    nb_voisines+=1
            if j!=0:
                if matrix[i][j-1]==1:
                    nb_voisines+=1
            if (i!=0 and j!=0):
                if matrix[i-1][j-1]==1:
                    nb_voisines+=1
            if (i!=l-1 and j!=l-1):
                if matrix[i+1][j+1]==1:
                    nb_voisines+=1
            if (i!=l-1):
                if matrix[i+1][j]==1:
                    nb_voisines+=1
            if (j!=l-1):
                if matrix[i][j+1]==1:
                    nb_voisines+=1
            if (i!=l-1 and j!=0):
                if matrix[i+1][j-1]==1:
                    nb_voisines+=1
            if (j!=l-1 and i!=0):
                if matrix[i-1][j+1]==1:
                    nb_voisines+=1
            #ajout de la cellule en fonction de si la cellule est vivante ou morte et de son nombre de voisins.
            if matrix[i][j]==0:
                if nb_voisines==3:
                    ligne.append(1)
                else:
                    ligne.append(0)
            else:
                if (nb_voisines==2 or nb_voisines==3):
                    ligne.append(1)
                else:
                    ligne.append(0)
        nouv_mat.append(ligne)
    return nouv_mat

def main():
    args = parse_args()
   
    if sys.stdin.isatty():
        # Personne n'a envoyé de grille : on en crée une au hasard
        matrix = grille_aleatoire(args.nb_cells, args.seed)
    else:
        # Une grille a été envoyée avec | ou < : on la lit
        matrix = lire_grille(sys.stdin.read())
        
    iter = 0
    filename = f"{args.output_directory}/grid_{iter:04d}.png"
    write_grid(matrix=matrix, filename=filename)

if __name__ == "__main__":
    main()
