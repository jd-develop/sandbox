# Soit un carré de côté L et un cercle de rayon R et de centre le croisement des diagonales du carré avec R<L.
# Plaçons aléatoirement des points dans le carré et déterminons s’ils sont à l’intérieur (in) ou à l’extérieur (out)
# du cercle.
# Après avoir placé une infinité de points, on a théoriquement (in+out)/in = L²/πR² soit π = R²(in+out)/L²·in
# Ici, on fixe L=1 et R=0.3
import random
import math
import py5

L = 1
R = 0.3
total_points = 0

in_points = 0


def is_in_circle(x, y):
    return math.sqrt((x - L/2)**2 + (y - L/2)**2) <= R


def setup():
    py5.size(L*500, L*500+40)
    py5.background(255)
    py5.text_size(20)
    py5.fill(255)
    py5.stroke(0)
    py5.circle(250, 250, 500*R*2)
    py5.stroke(0, 0, 255)
    py5.frame_rate(99999999999)


def draw():
    global in_points, total_points
    x, y = random.random(), random.random()
    total_points += 1

    if is_in_circle(x, y):
        in_points += 1
        py5.stroke(255, 0, 0)

    py5.circle(500 * x, 500 * y, 1)
    py5.stroke(0, 0, 255)

    if in_points != 0:
        py5.rect(0, 500, 500, 20)
        py5.fill(0)
        pi_estimation = (R**2 * total_points * 10) / (L**2 * in_points)
        # print(pi_estimation)
        py5.text(f"π ≈ {str(pi_estimation)}", 10, 515)
        py5.text("π = 3.141592653589793", 300, 515)

    py5.stroke(255)
    py5.fill(255)
    py5.rect(0, 520, 500, 20)
    py5.stroke(0, 0, 255)
    py5.fill(0)
    py5.text(f"Points: {total_points}. Points in circle: {in_points} ({int(in_points*100/total_points)}%).", 10, 535)
    py5.fill(255)


py5.run_sketch()
