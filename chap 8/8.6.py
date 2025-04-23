def memeLongueur(tableau1: list, tableau2: list) -> bool:
    """
    Fonction qui prend 2 tableaux en paramètre et qui retourne True s'il sont de même longueur, ou False dans le cas contraire.
    """
    assert type(tableau1) == list, "tableau1 n'est pas une liste"
    assert type(tableau2) == list, "tableau2 n'est pas une liste"
    return len(tableau1) == len(tableau2)