# Créé par nfercocq, le 13/09/2024 en Python 3.7
def occurence(mot: str, lettre: str) -> int:
    compteur = 0
    for element in mot:
        if element == lettre:
            compteur += 1
    return compteur
