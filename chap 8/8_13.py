def moyenne(tableau: list) -> float:
    """
    Fonction qui renvoie la moyenne d'un tableau non vide de flottants entré en paramètre.
    """

    assert type(tableau) == list, "Le tableau n'est pas une liste"
    assert len(tableau) > 0, "Le tableau ne doit pas être vide"
    assert type(tableau[0]) == float, "Les éléments du tableau doivent être des flottants"

    somme = 0
    for e in tableau:
        somme += e
    return somme / len(tableau)

# TP 8.19
def test_moyenne():
    assert moyenne([2.2, 2.4, 2.6]) == 2.4
    print("Tous les tests sont passés avec succès.")

test_moyenne()