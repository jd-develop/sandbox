#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Heap:  # MaxHeap
    def __init__(self):
        self.table: list[int | float] = list()
        self.taille_actuelle = 0

    def est_vide(self):
        return self.taille_actuelle == 0

    def _tasser(self, i: int = -1):
        if i == -1:
            i = self.taille_actuelle - 1
        parent = i//2
        while i > 0 and self.table[i] > self.table[parent]:
            self.table[i], self.table[parent] = self.table[parent], self.table[i]
            i //= 2
            parent = i//2

    def ajout(self, x: int | float):
        self.table.insert(self.taille_actuelle-1, x)
        self._tasser()
        self.taille_actuelle += 1

    def _tamiser(self, i: int = 0):
        # doesn’t work
        enfant_gauche = 2*i+1
        enfant_droit = 2*i+2
        while 2*i+2 < self.taille_actuelle-1 and (self.table[i] < self.table[enfant_gauche] or self.table[i] < self.table[enfant_droit]):
            if enfant_gauche > enfant_droit:
                enfant = enfant_gauche
            else:
                enfant = enfant_droit
            self.table[i], self.table[enfant] = self.table[enfant], self.table[i]
            i = enfant
            enfant_gauche = 2*i+1
            enfant_droit = 2*i+2

    def extraire_max(self):
        assert self.taille_actuelle > 0

        r, self.table[0] = self.table[0], self.table[self.taille_actuelle-1]

        self.taille_actuelle -= 1

        self._tamiser()

        return r


def heap_sort(l: list[int|float]):
    # doesn’t work
    heap = Heap()
    for elt in l:
        heap.ajout(elt)
        print(heap.table)

    print()
    while not heap.est_vide():
        heap.extraire_max()
        print(heap.table)

    print()
    return heap.table

