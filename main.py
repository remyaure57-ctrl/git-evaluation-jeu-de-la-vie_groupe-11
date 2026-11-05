import argparse
import random

from lib import write_grid

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Simulation du jeu de la vie de Conway."
    )
    parser.add_argument("-n", "--nb_cells", type=int, default=10,
                        help="nombre de cellules par côté (grille aléatoire)")
    parser.add_argument("-m", "--max_iterations", type=int, default=20,
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

def main():
    nb_cells = 50

    rng = random.Random(4200)

    matrix = [
        [rng.choice([0, 1]) for _ in range(nb_cells)]
        for _ in range(nb_cells)
    ]

    iter = 0
    filename = f"outputs/grid_{iter:04d}.png"
    write_grid(matrix=matrix, filename=filename)

if __name__ == "__main__":
    main()
