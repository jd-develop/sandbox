from random import randint
import py5

global n, p
global currentGrid
global tempGrid
cellSize = 15
alive = 1
dead = 0
pause = True
gen = 0
frame_rate_ = 20


def setup():
    global n, p

    # fenêtre d'affichage pour les motifs de test
    py5.size(1000, 650)
    # plein écran pour la version définitive
    # py5.full_screen()

    py5.background(0)  # fond noir
    py5.frame_rate(frame_rate_)

    # Calcul du nombre de lignes n et du nombre de colonnes p
    n = int(py5.width / cellSize)
    p = int(py5.height / cellSize)

    # Initialisation des grilles courante et temporaire
    init_grids("empty")
    # Affichage initial de la grille
    display_grid()

    py5.text_size(20)
    py5.fill(255)
    py5.text("gen: " + str(gen), 0, 20)
    py5.fill(0)


def draw():
    if not pause:
        # Actualiser la grille
        update_grids()
        # Afficher la grille
        display_grid()

        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)


def mouse_pressed():
    if py5.mouse_button == py5.LEFT:
        # Réinitialise la grille
        init_grids()
        # Afficher la grille
        display_grid()

        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)
    else:
        global currentGrid
        # changer l'état d'une cellule
        cell_x = int(py5.mouse_x / cellSize)
        cell_y = int(py5.mouse_y / cellSize)

        try:
            if currentGrid[cell_x][cell_y] == alive:
                currentGrid[cell_x][cell_y] = dead
            else:
                currentGrid[cell_x][cell_y] = alive
            # Afficher la grille
            display_grid()
            py5.fill(255)
            py5.text("gen: " + str(gen), 0, 20)
            py5.fill(0)
        except IndexError:
            pass


def key_pressed():
    global frame_rate_
    # Appuyer sur la touche espace suspend ou reprend l'exécution
    global pause
    if py5.key == " ":
        pause = not pause
    elif py5.key_code == py5.RIGHT and pause:
        # Actualiser la grille
        update_grids()
        # Afficher la grille
        display_grid()

        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)
    elif py5.key_code == py5.UP:
        frame_rate_ += 5
        py5.frame_rate(frame_rate_)
    elif py5.key_code == py5.DOWN:
        frame_rate_ -= 5
        if frame_rate_ < 5:
            frame_rate_ = 5
        py5.frame_rate(frame_rate_)
    elif py5.key == 'r':
        init_grids("random")
        display_grid()
        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)
    elif py5.key == 'b':
        init_grids("blinker")
        display_grid()
        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)
    elif py5.key == 't':
        init_grids("tub")
        display_grid()
        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)
    elif py5.key == 's':
        init_grids("ship")
        display_grid()
        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)
    elif py5.key == 'g':
        init_grids("glider")
        display_grid()
        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)
    elif py5.key == 'u':
        init_grids("glider_gun")
        display_grid()
        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)
    elif py5.key == 'd':
        init_grids("the_4812_diamond")
        display_grid()
        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)
    elif py5.key == 'e':
        init_grids("random_more")
        display_grid()
        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)
    elif py5.key == "p":
        init_grids("space_ship")
        display_grid()
        py5.fill(255)
        py5.text("gen: " + str(gen), 0, 20)
        py5.fill(0)


def init_grids(which_grid="empty"):
    """
    La fonction init_grids initialise les grilles courantes currentGrid et temporaire tempGrid.
    Les grilles sont codées par des listes de colonnes, par cohérence avec l'abscisse x en colonne et l'ordonnée y en 
    ligne
    """

    global currentGrid, tempGrid, gen

    # Grilles avec motifs de test
    empty = [[0]]

    blinker = [[1, 1, 1]]

    tub = [[0, 1, 0],
           [1, 0, 1],
           [0, 1, 0]]

    ship = [[1, 1, 0],
            [1, 0, 1],
            [0, 1, 1]]

    glider = [[0, 0, 1],
              [1, 0, 1],
              [0, 1, 1]]

    glider_gun = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    the_4812_diamond = [[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]]

    space_ship = [[0, 1, 1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 1, 0],
                  [0, 0, 1, 1, 0, 0, 0]]

    adapt_to_screen = True
    chosen_grid = blinker
    if which_grid == "blinker":
        chosen_grid = blinker
    elif which_grid == "tub":
        chosen_grid = tub
    elif which_grid == "ship":
        chosen_grid = ship
    elif which_grid == "glider":
        chosen_grid = glider
    elif which_grid == "glider_gun":
        chosen_grid = glider_gun
    elif which_grid == "the_4812_diamond":
        chosen_grid = the_4812_diamond
    elif which_grid == "empty":
        chosen_grid = empty
    elif which_grid == "space_ship":
        chosen_grid = space_ship
    elif which_grid == "random_more":
        currentGrid = [[randint(1, 5) // 5 for y in range(p)] for x in range(n)]
        adapt_to_screen = False
    else:
        currentGrid = [[randint(1, 12) // 12 for y in range(p)] for x in range(n)]
        adapt_to_screen = False

    if adapt_to_screen:
        chosen_grid2 = [[0 for y in range(p)] for x in range(n)]
        for i, line_ in enumerate(chosen_grid):
            for j, cell_ in enumerate(line_):
                chosen_grid2[j + int(n / 2) - int(len(line_) / 2)][i + int(p / 2) - int(len(chosen_grid) / 2)] = cell_
        currentGrid = chosen_grid2

    # initialise la grille temporaire avec des zéros
    tempGrid = [[0 for y in range(p)] for x in range(n)]
    gen = 0


def display_grid():
    """
    Affiche chaque cellule (x;y), sous la forme d'un rectangle
    """
    for x in range(n):
        for y in range(p):
            # Si la cellule est vivante, colorier en bleu
            if currentGrid[x][y] == alive:
                py5.fill(255)
            # Sinon la cellule est morte, colorier en noir
            elif currentGrid[x][y] == dead:
                py5.fill(0)
            # Tracer la cellule carrée de taille cellSize et de cordonnées (x*cellSize; y*cellSize)
            py5.square(x * cellSize, y * cellSize, cellSize)


def update_grids():
    """
    Actualise la grille en :
        - parcourant toutes les cellules de la grille
        - calculant le nombre de voisins vivants de la cellule en cours
        - appliquant alors les règles de transition pour actualiser la cellule en cours
    """
    global currentGrid
    global tempGrid, gen

    # Boucles de parcours de la grille courante, par colonne x, puis par ligne y

    for x in range(n):
        for y in range(p):
            # nombre de voisins vivants de la cellule (x;y)
            neighbors = alive_neighbors(currentGrid, x, y)
            # état de la cellule (x;y)
            state = currentGrid[x][y]
            # Actualisation de la cellule (x;y)
            if state == dead and neighbors == 3:  # birth
                tempGrid[x][y] = alive
            elif state == alive and neighbors < 2:  # isolation
                tempGrid[x][y] = dead
            elif state == alive and neighbors > 3:  # overpopulated
                tempGrid[x][y] = dead
            else:  # stable
                tempGrid[x][y] = currentGrid[x][y]

    # boucles de recopiage des valeurs de tempGrid dans  currentGrid
    for x in range(n):
        for y in range(p):
            currentGrid[x][y] = tempGrid[x][y]
    gen += 1


def alive_neighbors(current_grid, x, y):
    """
    Calcule et retourne le nombre de voisins vivants de la cellule de coordonnées (x;y).
    Doit tenir compte du voisinage
    """

    nb = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            nb += current_grid[(x + i + n) % n][(y + j + p) % p]

    nb -= current_grid[x][y]
    return nb


py5.run_sketch()
