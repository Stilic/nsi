def occurence(lettre, message):
    compteur = 0
    for i in range(len(message)):
        if message[i] == lettre:
            compteur = compteur + 1
    return compteur