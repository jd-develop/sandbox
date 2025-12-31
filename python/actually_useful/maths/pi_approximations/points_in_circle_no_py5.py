# Soit un carré de côté L et un cercle de rayon R et de centre le croisement des diagonales du carré avec R<L.
# Plaçons aléatoirement des points dans le carré et déterminons s’ils sont à l’intérieur (in) ou à l’extérieur (out)
# du cercle.
# Après avoir placé une infinité de points, on a théoriquement (in+out)/in = L²/πR² soit π = R²(in+out)/L²·in
# Ici, on fixe L=1 et R=0.3
import random
import math

L = 1
R = 0.3

in_points = 0


def is_in_circle(x: float, y: float):
    return math.sqrt((x - L/2)**2 + (y - L/2)**2) <= R


total_points = int(input("Nombre total de points à placer : "))


for i in range(total_points):
    x, y = random.random(), random.random()
    if is_in_circle(x, y):
        in_points += 1


pi_estimation = (R**2 * total_points * 10) / (L**2 * in_points)
print(pi_estimation)

