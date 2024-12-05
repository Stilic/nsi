# Créé par nfercocq, le 12/09/2024 en Python 3.7
def reduction(articles: float, prix: float):
    if articles <= 0 or prix <= 0:
        message = "Veuillez saisir un nombre d'articles et un prix strictement positifs."
    else:
        if articles >= 10:
            nouveauPrix = prix * 0.9 * articles
        else:
            nouveauPrix = prix * 0.8 * articles
        message = "Le nouveau prix est de " + str(nouveauPrix) + " euros."
    return message

print(reduction(1, 0))
print(reduction(0, 1))
print(reduction(1, 5))
print(reduction(8, 5))
