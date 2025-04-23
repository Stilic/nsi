def ascii(texte: str) -> str:
    """
    Fonction qui prend une chaîne de caractères en paramètre et qui renvoie, séparé par un espace, le code ASCII en décimal de chaque caractère de la chaîne.
    """
    assert type(texte) == str, "texte doit être une chaîne de caractères"
    code = ""
    for caractere in texte:
        code += str(ord(caractere)) + " "
    return code

def test_ascii():
    assert ascii("") == ""
    assert ascii("bonjour") == "98 111 110 106 111 117 114 "
    print("Tous les tests sont passés avec succès")

test_ascii()