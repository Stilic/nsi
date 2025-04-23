def miroir(chaine: str) -> str:
    """
    Fonction qui prend en paramètre une chaîne de caractères et qui la renvoie chiffrée suivant de chiffrement miroir.
    """
    assert type(chaine) == str, "chaine doit être une chaîne de caractères"
    resultat = ""
    for caractere in chaine:
        n = ord(caractere)
        estMinuscule = 96 < n < 123
        if estMinuscule or 64 < n < 91:
            if estMinuscule:
                n -= 32
            n = 96 - n
            if estMinuscule:
                n += 32
            resultat += chr(n)
        else:
            resultat += caractere
    return resultat

def test_miroir():
    assert miroir("Vivement la NSI !") == "Erevnmg oz MHR !"
    print("Test passés avec succès")

#test_miroir()
print(miroir("Vivement la NSI !"))