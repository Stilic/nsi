# Créé par nfercocq, le 13/09/2024 en Python 3.7

from turtle import *

def rectangle(largeur, longueur):
    goto(longueur, 0)
    goto(longueur, -largeur)
    goto(0, -largeur)
    goto(0, 0)

rectangle(float(input("Largeur du rectangle ? ")), float(input("Longueur du rectangle ? ")))
exitonclick()
