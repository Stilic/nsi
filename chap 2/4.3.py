# Créé par nfercocq, le 03/10/2024 en Python 3.7

def bowling(boule1):
    if boule1 == 10:
        message = "STRIKE"
    else:
        boule2 = int(input("Combien de quilles avez-vous renversées avec la deuxième boule ? "))
        quilles = boule1 + boule2
        if quilles == 10:
            message = "SPARE"
        elif quilles > 10:
            message = "Erreur: nombre de quilles renversées supérieur à 10"
        else:
            message = "Vous avez renversé " + str(boule1 + boule2) + " quilles"
    return message
