def range_pair(n: int) -> None:
    """
    Procédure qui prend en paramètre un nombre entier n, qui affiche tous les nombres entre 1 et n, et qui indique pour chacun si celui-ci est pair ou impair.
    """
    for i in range(n):
        vrai_nombre = i + 1
        if vrai_nombre % 2 == 0:
            print("{0} est pair.".format(vrai_nombre))
        else:
            print("{0} est impair.".format(vrai_nombre))