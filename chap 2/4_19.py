def appartenance(lettre, texte):
    for caractere in texte:
        if caractere == lettre:
            return True
    return False