def sommesPairs(n: int) -> int:
    """
    Fonction qui renvoie la somme des carrés des nombres pairs allant de 1 à n, où n est un entier entré en paramètre.
    """
    assert type(n) == int, "n n'est pas un entier."
    assert n >= 1, "n doit être supérieur ou égal à 1."

    somme = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            somme = somme + i * i
    return somme
