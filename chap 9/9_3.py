def rang(c: str) -> int:
    """
    Fonction qui prend pour paramètre un caractère et qui renvoie son rang dans l'alphabet minuscule.
    """
    assert type(c) == str, "c doit être une chaîne de caractères"
    assert len(c) == 1, "c ne doit comporter qu'un seul caractère"
    return ord(c) - 96

def test_rang():
    assert rang("a") == 1
    assert rang("z") == 26
    print("Tous les tests sont passés avec succès")

test_rang()