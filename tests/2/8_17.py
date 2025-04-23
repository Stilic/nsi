def tri(tableau: list) -> tuple:
    """
    Fonction qui prend en paramètre un tableau de nombre entiers et qui renvoie un tableau composé de ses éléments pairs et un tableau composé de ses éléments impairs.
    """
    assert type(tableau) == list, "Le tableau doit être une liste"
    assert len(tableau) > 0, "Le tableau ne doit pas être vide"
    assert type(tableau[0]) == int, "Le tableau ne doit comporter que des nombres entiers"
    
    pair = []
    impair = []

    for nombre in tableau:
        if nombre % 2 == 0:
            pair.append(nombre)
        else:
            impair.append(nombre)

    return pair, impair

def test_tri():
    assert tri([2]) == ([2], []), "Test 1 a échoué"
    assert tri([-144, -88888, -66666, -1111111]) == ([-144, -88888, -66666], [-1111111]), "Test 2 a échoué"
    assert tri([0, 2, 4, 5, 6, 7, 8]) == ([0, 2, 4, 6, 8], [5, 7]), "Test 3 a échoué"
    assert tri([222222, 33333333, 4444, 6666, 999999]) == ([222222, 4444, 6666], [33333333, 999999]), "Test 4 a échoué"
    assert tri([-0, -4, -12, -24, -64, -65]) == ([-0, -4, -12, -24, -64], [-65]), "Test 5 a échoué"
    assert tri([-0, 0, 1, -1, 12, 18, -19]) == ([-0, 0, 12, 18], [1, -1, -19]), "Test 6 a échoué"
    print("Tous les tests ont été passés avec succès")

test_tri()