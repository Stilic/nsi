# Créé par nfercocq, le 12/09/2024 en Python 3.7
def f1(message):
    compteur = 0
    for caractere in message:
        compteur += 1
    print(message)

def f2(message):
    for caractere in message:
        print(caractere)

def f3(message):
    new = ""
    for indice in range(len(message)):
        if indice % 2 == 0:
            new += message[indice]
    print(new)

f1("Bonjour !")
print("---------------------------")
f2("parcours")
print("---------------------------")
f3("parcours")
print("---------------------------")
