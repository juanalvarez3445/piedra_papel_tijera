"""
    di el numero es divisible entre 5
    dados por el ususario 
    Autor: juan carlos ceballos
    Fecha: 21 de octubre de 2023   
"""

numero = float(input('ingresa el numero :'))

if numero % 5 == 0 :
    print("el numero",numero,"es divisble entre 5")
else :
    print('el numero',numero, 'no es divisble entre 5')