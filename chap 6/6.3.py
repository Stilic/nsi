def divisionEuclidienne(a: int, b: int) -> tuple:
    """
    Renvoie un tuple (quotient, reste) pour la division euclidienne de a par b.
    """
    assert type(a) == int, "a doit être un entier."
    assert type(b) == int, "b doit être un entier."

    quotient = a / b
    reste = a % b
    couple = (quotient, reste)

    assert type(quotient) == int, "Le quotient doit être un entier."
    assert type(reste) == int, "Le reste doit être un entier."
    assert quotient != 0, "Le quotient est égal à 0."
    assert reste <= quotient, "Le reste est supérieur au quotient."
    return couple
