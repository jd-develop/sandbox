#!/usr/bin/env python3
# coding:utf-8
import pygame.font
from tree import Tree, Grass

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Tahoma", 20)
pygame.display.set_caption("Tree generator")

screen = pygame.display.set_mode((800, 600))
screen.fill((127, 221, 76))


def generate_trees() -> tuple:
    return Tree(100), Tree(375), Tree(650)


tree, tree1, tree2 = generate_trees()
grass = Grass()

screen.fill((127, 221, 76))

screen.blit(tree.return_trunk()[0], tree.return_trunk()[1])
screen.blit(tree.branches.image, tree.branches.rect)

for leave in tree.leaves:
    screen.blit(leave.image, leave.rect)

screen.blit(tree1.return_trunk()[0], tree1.return_trunk()[1])
screen.blit(tree1.branches.image, tree1.branches.rect)

for leave in tree1.leaves:
    screen.blit(leave.image, leave.rect)

screen.blit(tree2.return_trunk()[0], tree2.return_trunk()[1])
screen.blit(tree2.branches.image, tree2.branches.rect)

for leave in tree2.leaves:
    screen.blit(leave.image, leave.rect)

screen.blit(grass.image, grass.rect)

pygame.display.flip()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(font.render("Génération des arbres...", False, (0, 0, 0)), (0, 0))
            pygame.display.flip()
            
            tree, tree1, tree2 = generate_trees()
            screen.fill((127, 221, 76))

            screen.blit(tree.return_trunk()[0], tree.return_trunk()[1])
            screen.blit(tree.branches.image, tree.branches.rect)
            for leave in tree.leaves:
                screen.blit(leave.image, leave.rect)

            screen.blit(tree1.return_trunk()[0], tree1.return_trunk()[1])
            screen.blit(tree1.branches.image, tree1.branches.rect)
            for leave in tree1.leaves:
                screen.blit(leave.image, leave.rect)

            screen.blit(tree2.return_trunk()[0], tree2.return_trunk()[1])
            screen.blit(tree2.branches.image, tree2.branches.rect)
            for leave in tree2.leaves:
                screen.blit(leave.image, leave.rect)

            screen.blit(grass.image, grass.rect)

            pygame.display.flip()
