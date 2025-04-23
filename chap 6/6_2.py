def calculerEnergieCinetique(m: float, v: float) -> float:
    """
    Fonction qui renvoie l'énergie cinétique d'un objet de masse m (en kg) qui se déplace à la vitesse v (en m / s).
    """
    assert type(m) == float, "m doit être un nombre."
    assert type(v) == float, "v doit être un nombre."

    ec = (1 / 2) * m * (v * v)
    assert ec > 0, "L'énergie cinétique doit être positive."
    return ec
