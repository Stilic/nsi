def supprime(nuplet: tuple, i: int) -> tuple:
    """
    Fonction qui prend en paramètre un tuple et un nombre entier et qui renvoie un tuple qui contient tous les éléments du tuple de départ sauf celui d'indice i.
    """
    assert type(nuplet) == tuple, "nuplet doit être un tuple"
    assert type(i) == int, "i doit être un nombre entier"
    assert 0 <= i < len(nuplet), "i doit être positif et strictement inférieur à la longueur du nuplet"
    newUplet = ()
    for j in range(len(nuplet)):
        if j != i:
            newUplet = newUplet + (nuplet[j],)
    return newUplet