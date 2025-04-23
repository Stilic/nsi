def maximum(tableau: list) -> float:
    """
    Fonction qui prend un tableau de nombres en paramètre et qui renvoie son maximum et l'indice de la première occurrence du maximum.
    """
    assert type(tableau) == list, "Le tableau doit être une liste"
    assert len(tableau) > 0, "Le tableau ne doit pas être vide"
    assert type(tableau[0]) in (int, float), "Le tableau ne doit comporter que des nombres."

    max = tableau[0]
    indice = 0

    for i in range(len(tableau)):
        nombre = tableau[i]
        if nombre > max:
            max = nombre
            indice = i

    return max, indice