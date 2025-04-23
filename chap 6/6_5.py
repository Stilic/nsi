def enleverVoyelle(texte: str, voyelle: str) -> str:
    """
    Fonction qui prend en paramètre une chaîne de caractères `texte` et un caractère `voyelle`.
    Renvoie une copie de `texte` avec toutes les occurrences de `voyelle` retirées.
    """
    assert type(texte) == str, "`texte` doit être une chaîne de caractères."
    assert len(texte) > 0, "La chaîne de caractères doit avoir au moins un caractère."
    assert voyelle in ["a", "e", "i", "o", "u", "y"], "`voyelle` doit être une voyelle."

    resultat = ""
    for caractere in texte:
        minuscule = caractere.lower()
        if minuscule != voyelle:
            resultat += caractere
    return resultat

def test_enleverE():
    assert enleverE("e") == ""
    assert enleverE("é") == ""
    assert enleverE("è") == ""
    assert enleverE("ê") == ""
    assert enleverE("Nathanaël") == "Nathanal"
    assert enleverE("ÉGiOste") == "GiOst"
    print("Tous les tests ont été passés avec succès.")

test_enleverE()