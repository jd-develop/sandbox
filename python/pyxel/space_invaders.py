import pyxel
import random

pyxel.init(128, 128, title="Space Invaders")

vaisseau_x = 60
vaisseau_y = 100
tirs = []
invaders = []
explosions = []

MAX_COOLDOWN = 5
shot_cooldown = 0

life = 1
score = 0


# vaisseau
def deplacement_vaisseau(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT) and x < 120:
        x += 2
    if pyxel.btn(pyxel.KEY_LEFT) and x > 0:
        x -= 2
    if pyxel.btn(pyxel.KEY_DOWN) and y < 120:
        y += 2
    if pyxel.btn(pyxel.KEY_UP) and y > 0:
        y -= 2
    return x, y


# tirs
def creation_tirs(x, y, tirs_: list[list[int, int]]):
    global shot_cooldown
    if pyxel.btn(pyxel.KEY_SPACE) and shot_cooldown == 0:
        tirs_.append([x+4, y-4])
        shot_cooldown = MAX_COOLDOWN
    return tirs_


def deplacement_tirs(tirs_: list[list[int, int]]):
    for tir in tirs_:
        tir[1] -= 2
        if tir[1] < -8:
            tirs_.remove(tir)
    return tirs_


# envahisseurs
def create_invaders(invaders_: list):
    if pyxel.frame_count % 50 == 0:  # un toutes les 30 frames
        invaders_.append([random.randint(0, 120), 0])
    return invaders_


def update_invaders(invaders_: list):
    for invader in invaders_:
        if invader[1] >= 128:
            invaders_.remove(invader)
        else:
            invader[1] += 1
    return invaders_


# collisions
def do_they_collide(x1, y1, w1, h1, x2, y2, w2, h2):
    a1, b1, c1, d1 = (x1, y1), (x1+w1, y1), (x1+w1, y1+h1), (x1, y1+h1)
    a2, b2, c2, d2 = (x2, y2), (x2+w2, y2), (x2+w2, y2+h2), (x2, y2+h2)
    if (a1[0] <= a2[0] <= b1[0] or a1[0] <= b2[0] <= b1[0]) and \
            (a2[1] <= d1[1] <= d2[1] or a2[1] <= a1[1] <= d2[1]):
        return True
    else:
        a1, b1, c1, d1, a2, b2, c2, d2 = a2, b2, c2, d2, a1, b1, c1, d1
        if (a1[0] <= a2[0] <= b1[0] or a1[0] <= b2[0] <= b1[0]) and \
                (a2[1] <= d1[1] <= d2[1] or a2[1] <= a1[1] <= d2[1]):
            return True
        else:
            return False


def collisions():
    global life, score, tirs, invaders, explosions
    # collision entre tirs/envahisseurs
    for invader in invaders:
        continue_ = False
        for tir in tirs:
            if do_they_collide(tir[0], tir[1], 1, 4, invader[0], invader[1], 8, 8):
                tirs.remove(tir)
                invaders.remove(invader)
                continue_ = True
                score += 1
                explosions = create_explosion(invader[0], invader[1], explosions)
        if continue_:
            continue
        # collisions entre envahisseurs/vaisseau
        if do_they_collide(invader[0], invader[1], 8, 8, vaisseau_x, vaisseau_y, 8, 8):
            invaders.remove(invader)
            life -= 1
            explosions = create_explosion(vaisseau_x, vaisseau_y, explosions)


def create_explosion(x, y, explosions_: list):
    explosions_.append([x, y, 0])
    return explosions_


def animate_explosions(explosions_: list):
    for explosion in explosions_:
        explosion[2] += 1
        if explosion[2] == 12:
            explosions_.remove(explosion)
    return explosions_


def draw_explosions(explosions_: list):
    for explosion in explosions_:
        pyxel.circb(explosion[0]+4, explosion[1]+4, explosion[2]//2, 8 + explosion[2] % 3)


# update et draw
def update():
    global vaisseau_x, vaisseau_y, tirs, shot_cooldown, invaders, explosions
    if life != 0:
        vaisseau_x, vaisseau_y = deplacement_vaisseau(vaisseau_x, vaisseau_y)
        tirs = creation_tirs(vaisseau_x, vaisseau_y, tirs)
        tirs = deplacement_tirs(tirs)
        if shot_cooldown != 0:
            shot_cooldown -= 1
        invaders = create_invaders(invaders)
        invaders = update_invaders(invaders)
        collisions()
    explosions = animate_explosions(explosions)


def draw():
    pyxel.cls(0)
    if life != 0:
        pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

    for tir in tirs:
        pyxel.rect(tir[0], tir[1], 1, 4, 10)

    for invader in invaders:
        pyxel.rect(invader[0], invader[1], 8, 8, 2)

    draw_explosions(explosions)

    if life == 0:
        pyxel.text(50, 60, 'Game Over', 12)  # pyxel.frame_count*50 % 16)


pyxel.run(update, draw)
