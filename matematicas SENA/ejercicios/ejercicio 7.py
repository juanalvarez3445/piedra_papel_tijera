"""
    suma de los angulos de un triangulo
    dados por el ususario 
    Autor: juan carlos ceballos
    Fecha: 20 de octubre de 2023   
"""

angulo1 = float (input ('ingrese primer angulo :'))

angulo2 = float (input ('ingrese segundo angulo :'))

angulo3 = float (input ('ingrese tercer angulo :'))

suma = angulo1 + angulo2 + angulo3

if suma == 180 :
    print (" si corresponden a un triangulo")
else :
    print (" no corresponden a un triangulo")

