def tri(tableau: list) -> tuple:
    """
    Fonction qui prend en paramètre un tableau de nombre entiers et qui renvoie un tableau composé de ses éléments pairs et un tableau composé de ses éléments impairs.
    """
    assert type(tableau) == list, "Le tableau doit être une liste"
    assert len(tableau) > 0, "Le tableau ne doit pas être vide"
    assert type(tableau[0]) == int, "Le tableau ne doit comporter que des nombres entiers"
    
    pair = []
    impair = []

    for nombre in tableau:
        if nombre % 2 == 0:
            pair.append(nombre)
        else:
            impair.append(nombre)

    return pair, impair