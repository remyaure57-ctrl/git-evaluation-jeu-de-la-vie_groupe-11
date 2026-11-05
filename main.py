import random

from lib import write_grid

def calcul_generation(matrix):
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
            #ajout de la cellule en fonction de si la cellule est vivante ou morte et de son nombre #de voisins.
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
    nb_cells = 50

    rng = random.Random(4200)

    matrix = [
        [rng.choice([0, 1]) for _ in range(nb_cells)]
        for _ in range(nb_cells)
    ]

    iter = 0
    for i in range(21):
        filename = f"outputs/grid_{iter:04d}.png"
        write_grid(matrix=matrix, filename=filename)
        iter+=1
        matrix=calcul_generation(matrix)
        #ne pas oublier la condition sur le mode avec argparse
    print("Generation of 21 images in directory outputs")

if __name__ == "__main__":
    main()
