# Créé par nfercocq, le 03/10/2024 en Python 3.7

def bowling(boule1, boule2):
    if boule1 == 10:
        message = "STRIKE"
    elif boule1 + boule2 == 10:
        message = "SPARE"
    else:
        message = "Vous avez renversé " + str(boule1 + boule2) + " quilles"
    return message