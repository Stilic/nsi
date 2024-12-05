def occurence(lettre, message):
    compteur = 0
    for caractere in message:
        if caractere == lettre:
            compteur = compteur + 1
    return compteur