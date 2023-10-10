#!/usr/bin/env python3
# coding:utf-8
# Fibonnachi2


def fib(n):
    """ Calcule tout les nombres de la suite de Fibonnacci inférieurs à `n` """
    a, b = 0, 1
    fibFile = open("output.out", "w")
    while a < n:
        print(a)
        fibFile.write(f'-  {a}\n')
        a, b = b, a+b


n = 0
mode = str(input("*** CHOIX DU MODE D'ENTRÉE DU NOMBRE JUSQU'AUQUEL CE PROGRAMME CALCULE LA SUITE DE FIBONNACCI ***\n"
                 "'ne' : nombre/exposant\n"
                 "'nm' : nombre/multiplicateur\n"
                 "'ns' : nombre simple\n"
                 "Entrez mode : "))
if mode == 'ne':
    try:
        number = float(input("Entrez le nombre : "))
        power = float(input("Entrez son exposant : "))
        n = number ** power
        if n > 0:
            fib(n)
        else:
            print("Le nombre doit être supérieur à 0.")
    except ValueError:
        print("Saisie invalide.")
elif mode == 'nm':
    try:
        number = float(input("Entrez le nombre : "))
        multiplier = float(input("Entrez son multiplicateur : "))
        n = number * multiplier
        if n > 0:
            fib(n)
        else:
            print("Le nombre doit être supérieur à 0.")
    except ValueError:
        print("Saisie invalide.")
elif mode == 'ns':
    try:
        n = float(input("Entrez le nombre : "))
        if n > 0:
            fib(n)
        else:
            print("Le nombre doit être supérieur à 0.")
    except ValueError:
        print("Saisie invalide.")
else:
    print("Saisie invalide.")
