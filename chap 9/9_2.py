def caractereASCII(n: int) -> str:
    """
    Fonction qui prend un nombre entier n compris entre 1 et 26 en paramètre et qui renvoie le n-ième caractère de l'alphabet minuscule.
    """
    assert type(n) == int, "Le nombre doit être un entier"
    assert 0 < n < 27, "Le nombre doit être compris entre 1 et 26"
    return chr(96 + n)

def test_caractereASCII():
    assert caractereASCII(1) == "a"
    assert caractereASCII(26) == "z"
    print("Tous les tests ont été passés avec succès")

test_caractereASCII()