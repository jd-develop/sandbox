#!/urs/bin/env python3
# -*- coding:utf-8 -*-
import random


def generate_sujet() -> str:
    start: list[tuple[str, int, list[str]]] = [
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
    end2 = [
        ("être considéré comme", "être considérée comme"),
        ("être", "être")
    ]
    adjective = [
        ("considéré", "considérée", ["comme une énigme", "comme une réflexion", "de façon métaphysique"]),
        ("en tant que", "en tant que", ["valeur", "notion fondamentale"]),
        ("", "", [""]),
        ("", "", [""]),
        ("", "", [""])
    ]
    s = start.pop(random.randint(0, len(start)-1))
    whichend = random.randint(1, 2)
    if whichend == 1:
        e1 = random.choice(end1)
    else:
        e1 = random.choice(end2)
    randomend = random.choice(start)
    randomadj = random.choice(adjective)
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

    if whichend == 1:
        if s[1] == 0 or s[1] == 2:
            result += "est-il "
        elif s[1] == 1 or s[1] == 3:
            result += "est-elle "
    else:
        if s[1] == 0 or s[1] == 2:
            result += "peut-il "
        elif s[1] == 1 or s[1] == 3:
            result += "peut-elle "

    if random.randint(0, 5) == 0:
        result += "toujours "

    if whichend == 1:
        if e1[1] is None:
            pass
        elif e1[1]:
            result += "une "
        else:
            result += "un "
        result += e1[0] + " "
    else:
        if s[1] == 0 or s[1] == 2:
            result += e1[0] + " "
        else:
            result += e1[1] + " "


    if randomend[1] == 0:
        if e1[1] is None:
            result += "au "
        else:
            result += "du "
    elif randomend[1] == 1:
        if e1[1] is None:
            result += "à la "
        else:
            result += "de la "
    else:
        if e1[1] is None:
            result += "à l’"
        else:
            result += "de l’"
    result += randomend[0] + " "
    if len(randomend[2]) != 0:
        if random.randint(0, 1) == 0:
            result += random.choice(randomend[2]) + " "

    index_in_e3 = int(randomend[1])%2
    result += randomadj[index_in_e3] + " "
    result += random.choice(randomadj[2])
    while result.endswith(" "):
        result = result[:-1]
    result += "\N{NBSP}?"

    return result


print(generate_sujet())


