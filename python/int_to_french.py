#!/usr/bin/env python3
# coding:utf-8
# Enter an int, you have the French transcription!

chiffres = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze",
            "treize", "quatorze", "quinze", "seize"]

dizaines = [None, "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt",
            "quatre-vingt"]
a_besoin_de_et_pour_un = [None, False, True, True, True, True, True, True, False, False]
use_plus_dix = [None, False, False, False, False, False, False, True, False, True]

prefixes = ["cent", "mille", "million", "milliard"]


def int_to_french(nombre, do_not_print_0=False):
    assert isinstance(nombre, int)

    nombre = str(nombre)
    result = ""
    if nombre.startswith("-"):
        nombre = nombre[1:]
        result += "moins "
    if len(nombre) == 1:
        if nombre == "0" and do_not_print_0:
            return ""
        else:
            return chiffres[int(nombre)]
    if len(nombre) == 2:
        if nombre[0] == "0":
            return chiffres[int(nombre[1])]
        if int(nombre) < 17:
            return chiffres[int(nombre)]
        dizaine = dizaines[int(nombre[0])]
        result += dizaine
        if a_besoin_de_et_pour_un[int(nombre[0])] and nombre[1] == "1":
            if use_plus_dix[int(nombre[0])]:
                result += "-et-onze"
            else:
                result += "-et-un"
            return result
        elif nombre[1] == "0":
            if use_plus_dix[int(nombre[0])]:
                return result + "-dix"
            if nombre == "80":
                return result + "s"
            return result
        else:
            if use_plus_dix[int(nombre[0])]:
                result += "-" + int_to_french(int("1" + nombre[1]))
            else:
                result += "-" + int_to_french(int(nombre[1]))
            return result
    if len(nombre) == 3:
        if nombre[0] == "1":
            if nombre[1] == "0" and nombre[2] == "0":
                return "cent"
            else:
                return "cent " + int_to_french(int(nombre[1:]))
        else:
            centaine = int_to_french(int(nombre[0]), True)
            if centaine != "":
                centaine += " "
            dizaine_et_unite = int_to_french(int(nombre[1:]))
            if dizaine_et_unite != "zéro":
                return centaine + "cent " + dizaine_et_unite
            else:
                return centaine + "cents"


for i in range(1000):
    print(int_to_french(i))
