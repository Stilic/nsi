nombre = int(input("Veuillez entrer un entier positif : "))
nombre_initial = nombre
etapes = 0
maximum = nombre
while nombre != 1:
    if nombre%2 == 0:
        nombre /= 2
    else:
        nombre = nombre*3 + 1
    if nombre > maximum:
        maximum = nombre
    etapes += 1
    print(nombre)
print("Nombre initial :  {}  ; nombre d'étape(s) :  {}  ; nombre maximal atteint :  {}".format(nombre_initial, etapes, maximum))