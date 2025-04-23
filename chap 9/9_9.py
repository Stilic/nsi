def majusculebis(chaine: str) -> str:
    """
    Fonction qui prend en paramètre une chaîne de caractères et qui en renvoie une copie en majuscule.
    """
    assert type(chaine) == str, "chaine doit être une chaîne de caractères"
    majuscules = ""
    for caractere in chaine:
        n = ord(caractere)
        if 96 < n < 123:
            majuscules += chr(n - 32)
        else:
            majuscules += caractere
    return majuscules

def test_majusculebis():
    assert majusculebis("Vivement la NSI !") == "VIVEMENT LA NSI !"
    print("Tous les tests sont passés avec succès")

test_majusculebis()