def minuscule(chaine: str) -> str:
    """
    Fonction qui prend en paramètre une chaîne de caractères en majuscule et qui en renvoie une copie en minuscule.
    """
    assert type(chaine) == str, "chaine doit être une chaîne de caractères"
    minuscules = ""
    for i in range(len(chaine)):
        n = ord(chaine[i])
        assert 64 < n < 91, "Le caractère d'index {} n'est pas en majuscule".format(i)
        minuscules += chr(n + 32)
    return minuscules

def test_minuscule():
    assert minuscule("MAJUSCULE") == "majuscule"
    assert minuscule("NSI") == "nsi"
    print("Tous les tests sont passés avec succès")

test_minuscule()