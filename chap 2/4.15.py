def occurence(message):
    compteur = 0
    for caractere in message:
        if caractere == "e":
            compteur = compteur + 1
    return compteur