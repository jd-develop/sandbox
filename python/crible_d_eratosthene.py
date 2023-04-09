def criblederatostene(x=100):
    assert x >= 3
    nombres = list(range(2, x))
    nombresPremiers = []
    while len(nombres) != 0:
        p = nombres.pop(0)
        nombresPremiers.append(p)
        for i, nombre in enumerate(nombres):
            if nombre%p == 0:
                nombres.pop(i)
    return nombresPremiers


print(criblederatostene(1000))
