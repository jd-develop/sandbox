import pyxel

pyxel.init(128, 128, title="Intro à Pyxel")

vaisseau_x = vaisseau_y = 60
tirs = []


def deplacement_vaisseau(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT) and x < 120:
        x += 1
    if pyxel.btn(pyxel.KEY_LEFT) and x > 0:
        x -= 1
    if pyxel.btn(pyxel.KEY_DOWN) and y < 120:
        y += 1
    if pyxel.btn(pyxel.KEY_UP) and y > 0:
        y -= 1
    return x, y


def creation_tirs(x, y, tirs_: list[list[int, int]]):
    if pyxel.btn(pyxel.KEY_SPACE):
        tirs_.append([x+4, y-4])
    return tirs_


def deplacement_tirs(tirs_: list[list[int, int]]):
    for tir in tirs_:
        tir[1] -= 1
        if tir[1] < -8:
            tirs_.remove(tir)
    return tirs_


def update():
    global vaisseau_x, vaisseau_y, tirs
    vaisseau_x, vaisseau_y = deplacement_vaisseau(vaisseau_x, vaisseau_y)
    tirs = creation_tirs(vaisseau_x, vaisseau_y, tirs)
    tirs = deplacement_tirs(tirs)


def draw():
    pyxel.cls(0)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

    for tir in tirs:
        pyxel.rect(tir[0], tir[1], 1, 4, 10)


pyxel.run(update, draw)
