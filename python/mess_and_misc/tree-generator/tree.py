#!/usr/bin/env python3
# coding:utf-8
import pygame
import random


class Tree:
    def __init__(self, trunkx) -> None:
        self.trunk = Trunk(trunkx)
        self.branches = Branch(trunkx)
        self.leaves = []
        if random.randint(1, 5) == 1:
            for loop in range(random.randint(500, 1000)):
                self.leaves.append(Leave(self.trunk.rect.x, self.trunk.rect.y, True))
        else:
            for loop in range(random.randint(1000, 2000)):
                self.leaves.append(Leave(self.trunk.rect.x, self.trunk.rect.y))
    
    def return_trunk(self):
        """ Retourne image, rect """
        return self.trunk.image, self.trunk.rect
    
    def return_leaves(self):
        return self.leaves


class Leave:
    def __init__(self, treex, treey, automnal: bool = False) -> None:
        if not automnal:
            if random.randint(1, 10000) == 1:
                self.image = AUTOMN_LEAVE_IMAGE
            else:
                self.image = LEAVE_IMAGE
        else:
            if random.randint(1, 10000) == 1:
                self.image = LEAVE_IMAGE
            else:
                self.image = AUTOMN_LEAVE_IMAGE
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(treex - 50, treex + 100)
        self.rect.y = random.randint(treey - 200, treey + 50)


class Branch:
    def __init__(self, treex) -> None:
        self.branches = pygame.image.load("branches.png")
        self.image = self.get_image(random.randint(0, 2))
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (99, 150))
        self.rect = self.image.get_rect()
        self.rect.x = treex - 25
        self.rect.y = 202
    
    def get_image(self, branches):
        x = branches * 33
        image = pygame.Surface([33, 50])
        image.blit(self.branches, (0, 0), (x, 0, 33, 50))
        return image


class Trunk:
    def __init__(self, x) -> None:
        self.trunks = pygame.image.load('trunk.png')
        self.image = self.get_image(random.randint(0, 2))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 352  # fichu pixel qui dépasse :P
    
    def get_image(self, trunk):
        x = trunk * 50
        image = pygame.Surface([50, 189])
        image.blit(self.trunks, (0, 0), (x, 0, 50, 189))
        return image


class Grass:
    def __init__(self) -> None:
        self.image = pygame.image.load('grass.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 500


LEAVE_IMAGE = pygame.image.load("leave.png")
AUTOMN_LEAVE_IMAGE = pygame.image.load("automnleave.png")
