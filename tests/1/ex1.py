def presence(mot: str, lettre: str) -> bool:
    """
    Fonction qui renvoie True si "lettre" apparaît au moins une fois dans la chaîne de caractères "mot", ou False dans le cas contraire.
    """
    assert type(mot) == str, "mot doit être une chaîne de caractères."
    assert type(lettre) == str, "lettre doit être une chaîne de caractères."
    assert len(lettre) == 1, "lettre doit être composé de 1 caractère."

    i = 0
    longueur = len(mot)
    estPresent = False
    while not estPresent and i < longueur:
        if mot[i] == lettre:
            estPresent = True
        i = i + 1
    return estPresent
