from math import sqrt

def attente(p: float) -> float:
    """
    Fonction qui renvoie le temps d'attente du "plouf" (en seconde) pour la longueur p (en mètre) du puits.
    """
    assert type(p) == float, "p doit être un nombre."
    assert p > 0, "p doit être supérieur à 0."

    temps = sqrt(p / 4.9) + p / 330
    assert temps > 0, "Le temps d'attente doit être supérieur à 0."
    return temps
