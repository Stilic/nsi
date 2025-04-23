# Créé par nfercocq, le 13/09/2024 en Python 3.7
def inter(mot: str) -> str:
    new = ""
    for indice in range(len(mot)):
        new = new + mot[indice] + "*"
    return new
