def nomMois(n: int) -> str:
    """
    Fonction qui prend en paramètre un nombre entier entre 1 et 12 et qui renvoie le nom du mois correspondant.
    """
    assert type(n) == int, "n doit être un nombre entier"
    assert 1 <= n <= 12, "Veuillez saisir un nombre entier entre 1 et 12 compris"
    mois = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre")
    return mois[n - 1]

def test_nomMois():
    assert nomMois(1) == "janvier"
    assert nomMois(12) == "décembre"
    print("Tests passés avec succès")

test_nomMois()