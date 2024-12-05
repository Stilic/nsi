def multiplication(nombre: int) -> int:
    print("Voici la table de multiplication de {0}".format(nombre))
    for i in range(10):
        calcul = nombre * (i + 1)
        print("{0} x {1} = {2}".format(nombre, i + 1, calcul))
    return None # pas obligé