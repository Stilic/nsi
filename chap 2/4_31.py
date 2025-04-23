def prog(nombre):
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
    return etapes, maximum

max_etapes = (0, 0)
max_maximum = (0, 0)
for i in range(1, 21):
    etapes, maximum = prog(i)
    if max_etapes[1] < etapes:
        max_etapes = (i, etapes)
    if max_maximum[1] < maximum:
        max_maximum = (i, maximum)
    print()
print("Nombre de départ donnant le plus grand nombre d'étapes : " + str(max_etapes[0]))
print("Nombre de départ donnant le plus grand maximum : " + str(max_maximum[0]))