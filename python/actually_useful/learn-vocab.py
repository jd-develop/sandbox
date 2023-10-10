#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random

# this is véri goude ancient greek transcription, isn’t it?
VOCAB_1 = ["khalkeúoo",
           "daídalos, os, on",
           "pórpee, ees (hee)",
           "gnamptós, ée, ón",
           "hélix, ikos (hee)",
           "kálux, ukos (hee)",
           "hórmos, ou (ho)",
           "phûsa, ees (hee)",
           "péloor (tò)",
           "ħaíntos, os, on",
           "khaleúoo",
           "ħamphípolos, os, on",
           "tekhnítees, ou (ho)",
           "tékhnee, ees (hee)",
           "deemiourgós, oû (ho)",
           "ħautómatos, ee, on"]

VOCAB_2 = ["forger, travailler le métal",
           "travaillé avec art",
           "agrafe pour tenir un vêtement",
           "courbé, qui dessine une courbe",
           "spirale",
           "calice de fleur, bouton de fleur",
           "collier, guirlande",
           "soufflet de forge",
           "être prodigieux, prodige, monstre",
           "au souffle bruyant",
           "boîter",
           "serviteur, servante",
           "artisan, artiste",
           "art",
           "qui travaille pour le public",
           "qui se meut de soi-même"]
assert len(VOCAB_1) == len(VOCAB_2)

MODE = 2  # 1 to learn vocab 1, 2 to learn vocab 2

done = []
while True:
    if len(done) == len(VOCAB_1):
        break

    element = random.randint(0, len(VOCAB_1)-1)
    while element in done:
        element = random.randint(0, len(VOCAB_1) - 1)

    if MODE == 1:
        question = VOCAB_2[element]
        correct_ans = VOCAB_1[element]
    else:
        question = VOCAB_1[element]
        correct_ans = VOCAB_2[element]

    ans = input(f"{question}: ")

    if ans == correct_ans:
        print("VRAI")
        done.append(element)
    else:
        print(f"FAUX. Réponse correcte: {correct_ans}")
