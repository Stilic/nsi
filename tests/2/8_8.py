def presence(tableau: list, element) -> bool:
    """
    Fonction qui prend un tableau et un élément en paramètre et qui renvoie True si l'élément est présent dans le tableau, ou False sinon.
    """
    assert type(tableau) == list, "Le tableau doit être de type list"
    i = 0
    longueur = len(tableau)
    resultat = False
    while not resultat and i < longueur:
        if element == tableau[i]:
            resultat = True
        i = i + 1
    return resultat

def test_presence():
    assert presence([1, 2, 3], 1) == True, "Test 1 a échoué"
    assert presence([1, 2, 3], 4) == False, "Test 2 a échoué"
    assert presence([], 4) == False, "Test 3 a échoué"
    assert presence([4, 4, 4, 4], 4) == True, "Test 4 a échoué"
    assert presence(['abc', 'def', 'hij', 'klm'], 'a') == False, "Test 5 a échoué"
    assert presence(['abc', 'def', 'hij', 'klm'], 'klm') == True, "Test 6 a échoué"
    print("Tous les tests ont été passés avec succès")

test_presence()