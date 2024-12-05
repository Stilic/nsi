# Créé par nfercocq, le 13/09/2024 en Python 3.7

from turtle import *

def mystere(pixel):
    """
    Dessine une maison de la taille `pixel`.
    """
    goto(pixel, 0)
    goto(0, pixel)
    goto(pixel, pixel)
    goto(0, 0)
    goto(0, pixel)
    goto(0.5 * pixel, 1.5 * pixel)
    goto(pixel, pixel)
    goto(pixel, 0)

mystere(40)
exitonclick()
