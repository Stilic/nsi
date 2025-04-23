def mix(tableau1: list, tableau2: list) -> list:
    """
    Fonction qui prend 2 tableaux déjà triés en paramètre et qui renvoie un tableau composé des éléments des 2 tableaux ordonnés.
    """

    assert type(tableau1) == list, "tableau1 doit être une liste"
    assert type(tableau2) == list, "tableau2 doit être une liste"
    assert len(tableau1) > 0, "tableau1 ne doit pas être vide"
    assert len(tableau2) > 0, "tableau2 ne doit pas être vide"

    if tableau1[-1] > tableau2[-1]:
        return tableau2 + tableau1
    else:
        return tableau1 + tableau2