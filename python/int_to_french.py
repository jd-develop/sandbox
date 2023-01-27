#!/usr/bin/env python3
# coding:utf-8
# Enter an int, you have the French transcription!

chiffres = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze",
            "treize", "quatorze", "quinze", "seize"]

dizaines = [None, "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt",
            "quatre-vingt"]
a_besoin_de_et_pour_un = [None, False, True, True, True, True, True, True, False, False]
use_plus_dix = [None, False, False, False, False, False, False, True, False, True]


def float_to_french(nombre):
    assert isinstance(nombre, float)
    nombre = str(nombre).split(".")
    int_ = int_to_french(int(nombre[0]))
    float_ = int_to_french(int(nombre[1]))
    if float_ != "zéro":
        if int_.endswith(" "):
            return int_ + "virgule " + float_
        else:
            return int_ + " virgule " + float_
    else:
        return int_


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
        elif nombre == "0":
            return chiffres[int(nombre)]
        else:
            return result + chiffres[int(nombre)]
    if len(nombre) == 2:
        if nombre[0] == "0":
            if nombre[1] == "0":
                return chiffres[int(nombre[1])]
            else:
                return result + chiffres[int(nombre[1])]
        if int(nombre) < 17:
            return result + chiffres[int(nombre)]
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
                return result + "cent"
            else:
                return result + "cent " + int_to_french(int(nombre[1:]))
        else:
            centaine = int_to_french(int(nombre[0]), True)
            if centaine != "":
                centaine += " "
            dizaine_et_unite = int_to_french(int(nombre[1:]))
            if dizaine_et_unite != "zéro":
                return result + centaine + "cent " + dizaine_et_unite
            else:
                return result + centaine + "cents"
    else:
        result_list = []  # do not forget to add result at the end ("moins")
        if len(nombre) % 3 == 1:  # 1 digit then lot of 3-digits groups
            result_list.append(int_to_french(int(nombre[0]), True))
            nombre = nombre[1:]
        elif len(nombre) % 3 == 2:  # 2 digits then lot of 3-digits groups
            result_list.append(int_to_french(int(nombre[:2])))
            nombre = nombre[2:]

        # then len(nombre) % 3 == 0
        while len(nombre) != 0:
            if nombre[:3] == "000":
                result_list.append(None)
            else:
                result_list.append(int_to_french(int(nombre[:3])))
            nombre = nombre[3:]

        for i, res in enumerate(result_list):
            if res == "un" and ((len(result_list[i:])+1) % 3) == 0:  # mille
                result += "mille "
            elif ((len(result_list[i:])+1) % 3) == 0:  # milliers
                if res is not None:
                    result += res + " mille "
                else:
                    pass
            elif (len(result_list[i:]) % 3) == 0:  # millions
                if res is not None:
                    result += res + " million"
                    if res != "un":
                        result += "s"
                    result += " "
                else:
                    pass
            elif ((len(result_list[i:])-1) % 3) == 0 and i != (len(result_list)-1):  # milliards:
                if res is not None:
                    result += res + " milliard"
                    if res != "un":
                        result += "s"
                    result += " "
                else:
                    if result.endswith("million ") or result.endswith("millions ") or \
                                    result.endswith("milliards ") or result.endswith("milliard "):
                        result += "de milliards "
                    else:
                        result += "milliards "
            elif i == len(result_list)-1:
                if res is not None:
                    result += res

        return result


for n in range(-1500, 1500):
    print(int_to_french(n))

print(int_to_french(1_274_625))
print(int_to_french(23_274_625_000_245_628_000))
print(int_to_french(3_274_000_000_245_628_020))
print(int_to_french(6_000_000_000_000_000_001))
print(int_to_french(-999999999999999999999999999999999999999999999999999999999))
print(float_to_french(66642.8098409958))
print(float_to_french(-3.14))
