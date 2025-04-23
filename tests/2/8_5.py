def reverse(nuplet: tuple) -> tuple:
    """
    Fonction qui prend en paramètre un tuple et qui renvoie un tuple qui contient tous les éléments du tuple de départ dans l'ordre inverse.
    """
    assert type(nuplet) == tuple, "nuplet doit être un tuple"
    nupletInverse = ()
    for element in nuplet:
        nupletInverse = (element,) + nupletInverse
    return nupletInverse

def test_reverse():
    assert reverse((1, 2, 3)) == (3, 2, 1), "Test 1 a échoué"
    assert reverse((1,)) == (1,), "Test 2 a échoué"
    assert reverse((4, 5, 6, 7)) == (7, 6, 5, 4), "Test 3 a échoué"
    assert reverse(("vivre", "la", "nsi")) == ("nsi", "la", "vivre"), "Test 4 a échoué"
    print("Tous les test ont été passés avec succès")

test_reverse()