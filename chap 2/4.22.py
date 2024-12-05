def inversion(texte):
    newText = ""
    for indice in range(len(texte) - 1, -1, -1):
        newText = newText + texte[indice]
    return newText == texte