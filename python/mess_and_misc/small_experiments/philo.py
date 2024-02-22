#!/urs/bin/env python3
# -*- coding:utf-8 -*-
import random


def generate_sujet():
    start = [
        ("conscience", 1, ["de soi"]),
        ("temps", 0, ["pour soi"]),
        ("liberté", 1, ["de penser", "d’opinion", "d’agir"]),
        ("recherche", 1, ["de soi", "de liberté", "de vérité"]),
        ("inconscient", 2, ["psychique"]),
        ("vérité", 1, ["scientifique"]),
        ("religion", 1, []),
        ("travail", 0, ["selon Marx"]),
        ("philosophie", 1, ["de Descartes"])
    ]
    end1 = [
        ("extension", True),
        ("partie", True),
        ("état d’esprit", False),
        ("selon vous assimilable", None)
    ]
    adjective = [
        ("considéré", "considérée", ["comme une énigme", "comme une réflexion", "de façon métaphysique"]),
        ("en tant que", "en tant que", ["valeur"]),
        ("", "", [""])
    ]
    s = start.pop(random.randint(0, len(start)-1))
    e1 = random.choice(end1)
    e2 = random.choice(start)
    e3 = random.choice(adjective)
    if s[1] == 0:
        result = "Le "
    elif s[1] == 1:
        result = "La "
    else:
        result = "L’"
    result += s[0] + " "
    if len(s[2]) != 0:
        if random.randint(0, 1) == 0:
            result += random.choice(s[2]) + " "

    if s[1] == 0 or s[1] == 2:
        result += "est-il "
    elif s[1] == 1 or s[1] == 3:
        result += "est-elle "

    if e1[1] is None:
        pass
    elif e1[1]:
        result += "une "
    else:
        result += "un "
    result += e1[0] + " "

    if e2[1] == 0:
        if e1[1] is None:
            result += "au "
        else:
            result += "du "
    elif e2[1] == 1:
        if e1[1] is None:
            result += "à la "
        else:
            result += "de la "
    else:
        if e1[1] is None:
            result += "à l’"
        else:
            result += "de l’"
    result += e2[0] + " "
    if len(e2[2]) != 0:
        if random.randint(0, 1) == 0:
            result += random.choice(e2[2]) + " "

    index_in_e3 = int(e2[1])%2
    result += e3[index_in_e3] + " "
    result += random.choice(e3[2])
    while result.endswith(" "):
        result = result[:-1]
    result += "\N{NBSP}?"

    return result


print(generate_sujet())


