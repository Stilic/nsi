def enleverE(texte: str) -> str:
    """
    Fonction qui prend en paramètre une chaîne de caractères et qui en renvoie une copie avec tous les "e" (majuscules et accents compris) supprimés.
    """
    assert type(texte) == str, "Le paramètre doit être une chaîne de caractères."
    assert len(texte) > 0, "La chaîne de caractères doit avoir au moins 1 caractère."

    resultat = ""
    for caractere in texte:
        if not caractere.lower() in ("e", "é", "è", "ê", "ë"):
            resultat += caractere
    return resultat

def test_enleverE():
    assert enleverE("e") == ""
    assert enleverE("é") == ""
    assert enleverE("è") == ""
    assert enleverE("ê") == ""
    assert enleverE("ë") == ""
    assert enleverE("E") == ""
    assert enleverE("É") == ""
    assert enleverE("È") == ""
    assert enleverE("Ê") == ""
    assert enleverE("Ë") == ""
    print("Tests passés avec succès.")

test_enleverE()