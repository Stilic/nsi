# Créé par nfercocq, le 03/10/2024 en Python 3.7

nom = input("Quel est votre nom ?")
sexe = input("Quel est votre sexe ? (Veuillez saisir soit M soit F)")
if sexe == "M":
    print("Cher Monsieur", nom)
elif sexe == "F":
    print("Chère Madame", nom)
else:
    print("Saisie invalide")