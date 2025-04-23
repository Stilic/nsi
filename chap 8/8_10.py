def begaye(tableau: list) -> list:
    """
    Fonction qui prend un tableau en paramètre et qui en renvoie une copie où tous les éléments sont doublés.
    """
    assert type(tableau) == list, "tableau n'est pas un tableau"
    copie = []
    for e in tableau:
        copie.append(e)
        copie.append(e)
    return copie