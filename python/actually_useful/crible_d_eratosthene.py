# coding:utf-8

def sieve_of_eratosthenes(x=100):
    assert x >= 3
    nombres = list(range(2, x))
    nombres_premiers = []
    while len(nombres) != 0:
        p = nombres.pop(0)
        nombres_premiers.append(p)
        for i, nombre in enumerate(nombres):
            if nombre % p == 0:
                nombres.pop(i)
    return nombres_premiers


print(sieve_of_eratosthenes(1000))
