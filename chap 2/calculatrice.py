OPERATEURS = ["+", "-", "*", "/"]
CARACTERES_NOMBRE = ["-", "."]
#calcul = input("Entrez votre calcul : ")
calcul = "1.5"
ast = []
texte_en_analyse = ""
operateur = None
for c in calcul:
    if not c.isspace():
        if operateur == None and c in OPERATEURS:
            ast.append(c)
            texte_en_analyse = ""
        elif c.isdigit() or c in CARACTERES_NOMBRE:
            texte_en_analyse += c

        if texte_en_analyse != "":
            try:
                if texte_en_analyse.isnumeric():
                    print(texte_en_analyse)
                    ast.append(int(texte_en_analyse))
                else:
                    ast.append(float(texte_en_analyse))
            except:
                pass
print(ast)