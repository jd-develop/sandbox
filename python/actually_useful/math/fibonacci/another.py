#!/usr/bin/env python3
# no imports
""" Suite de Fibonacci """
a = 1
b = 1
actuallyTimes = 0


def ask():
    mode = str(input("Modes : toute la liste (t), valeur seulement(v). Entrez votre choix (t, v) : "))
    if mode == "t":
        try:
            times = int(input("Entrez le nombre de valeurs à calculer suivant la suite de Fibonacci : "))
        except ValueError:
            print("Erreur : le nombre de valeurs sera 10.")
            times = 10
    elif mode == "v":
        try:
            times = int(input("Entrez la valeur à calculer suivant la suite de Fibonacci : "))
        except ValueError:
            print("Erreur : la valeur sera 10.")
            times = 10
    elif mode == "easteregg":
        while True:
            try:
                print("EASTER EGG!!!!!!!!!!!!")
            except KeyboardInterrupt:
                break
        print("Le mode sera t et la valeur 10.")
        mode = "t"
        times = 10
    else:
        print("Le mode sera t et la valeur 10.")
        mode = "t"
        times = 10
    return [mode, times]


ask = ask()
toDoTimes = ask[1]
chooseMode = ask[0]

if chooseMode == "v" and toDoTimes > 100000:
    print("Calcul en cours, veuillez patienter...")

if toDoTimes > 0:
    if toDoTimes >= 1:
        actuallyTimes += 1
        if chooseMode == "t":
            print(actuallyTimes, ": ", a)
    if toDoTimes >= 2:
        actuallyTimes += 1
        if chooseMode == "t":
            print(actuallyTimes, ": ", b)

    for loop in range(toDoTimes - 2):
        try:
            actuallyTimes += 1
            number = a + b
            if chooseMode == "t":
                print(actuallyTimes, ": ", number)
            b = a
            a = number
        except KeyboardInterrupt:
            print("\nProgramme terminé")
            quit(0)

    if chooseMode == "v":
        print(actuallyTimes, ": ", number)
else:
    print("Le nombre de valeurs à calculer doit être strictement supérieur à 0.")
