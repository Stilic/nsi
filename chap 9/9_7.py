def majuscule(chaine: str) -> str:
    """
    Fonction qui prend en paramètre une chaîne de caractères en minuscule et qui en renvoie une copie en majuscule.
    """
    assert type(chaine) == str, "chaine doit être une chaîne de caractères"
    majuscules = ""
    for i in range(len(chaine)):
        n = ord(chaine[i])
        assert 96 < n < 123, "Le caractère d'index {} n'est pas en minuscule".format(i)
        majuscules += chr(n - 32)
    return majuscules

def test_majuscule():
    assert majuscule("minuscule") == "MINUSCULE"
    assert majuscule("nsi") == "NSI"
    print("Tous les tests sont passés avec succès")

test_majuscule()