# coding:utf-8
import pyxel
import time
import random

pyxel.init(128, 128, title="Snake")

game_board = [[0]*16 for i in range(16)]

head_x = 7
head_y = 7
tail_x = 7
tail_y = 7

LEFT = 2
RIGHT = 3
UP = 4
DOWN = 5

game_board[head_x][head_y] = 1
direction = RIGHT
cooldown = 3
game_over = False

apple_x = apple_y = 0
score = 0


def randomize_apple():
    global apple_x, apple_y
    apple_x, apple_y = random.randint(0, 15), random.randint(0, 15)
    while game_board[apple_x][apple_y] != 0:
        apple_x, apple_y = random.randint(0, 15), random.randint(0, 15)


randomize_apple()
game_board[apple_x][apple_y] = 9


def update_direction():
    global direction
    if (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z)) and direction != DOWN:
        direction = UP
    elif (pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S)) and direction != UP:
        direction = DOWN
    elif (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q)) and direction != RIGHT:
        direction = LEFT
    elif (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)) and direction != LEFT:
        direction = RIGHT


def update():
    global head_x, head_y, tail_x, tail_y, cooldown, game_board, game_over, score
    if not game_over:
        update_direction()

        game_board[head_x][head_y] = direction
        if direction == LEFT:
            head_x -= 1
        elif direction == RIGHT:
            head_x += 1
        elif direction == UP:
            head_y -= 1
        else:
            head_y += 1

        if head_y < 0 or head_y > 15 or head_x < 0 or head_x > 15:
            game_over = True
            return

        if game_board[head_x][head_y] == 9:
            print("miam")
            score += 1
            randomize_apple()
            game_board[apple_x][apple_y] = 9
            cooldown = 1

        if cooldown <= 0:
            tail_direction = game_board[tail_x][tail_y]
            game_board[tail_x][tail_y] = 0
            if tail_direction == LEFT:
                tail_x -= 1
            elif tail_direction == RIGHT:
                tail_x += 1
            elif tail_direction == UP:
                tail_y -= 1
            else:
                tail_y += 1

        cooldown -= 1
        game_board[head_x][head_y] = 1
        print(head_x, head_y, direction)
        time.sleep(.5)


def draw():
    pyxel.cls(0)
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                pyxel.rect(i*8, j*8, 8, 8, pyxel.COLOR_GREEN)
            elif game_board[i][j] in (LEFT, RIGHT, UP, DOWN):
                pyxel.rect(i*8, j*8, 8, 8, pyxel.COLOR_LIME)
            elif game_board[i][j] == 9:
                pyxel.rect(i*8, j*8, 8, 8, pyxel.COLOR_RED)
    if game_over:
        pyxel.text(50, 60, 'Game Over', 12)


pyxel.run(update, draw)
