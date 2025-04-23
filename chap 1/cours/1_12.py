# Créé par nfercocq, le 13/09/2024 en Python 3.7
from math import pi
def infosDisque(rayon):
    perimetre = 2 * pi * rayon
    aire = pi * (rayon * rayon)
    return perimetre, aire

print(infosDisque(10))
