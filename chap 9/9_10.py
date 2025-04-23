from random import randint

def creation_mdp(longueur: int) -> str:
    """
    Fonction qui prend en paramètre un entier strictement positif et qui renvoie un mot de passe aléatoire de la longueur définie par le paramètre.
    """
    assert type(longueur) == int, "longueur doit être un entier"
    assert longueur > 0, "longueur doit être strictement positif"
    mdp = ""
    for _ in range(longueur):
        mdp += chr(randint(33, 126))
    return mdp