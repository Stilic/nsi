def tp_4_28(nombre: int) -> int:
    if nombre == 0:
        return 1
    if nombre < 0:
        return 0
    
    chiffres = 0
    while nombre != 0:
        nombre = nombre//10
        chiffres += 1
    return chiffres