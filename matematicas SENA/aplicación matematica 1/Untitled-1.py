"""
    dados por el ususario 
    Autor: kevin Aguirre
    Fecha: 10 de octubre de 2023    
"""

def calcular_porcentaje(numero, porcentaje):
    porcentaje_decimal = porcentaje / 100
    resultado = numero * porcentaje_decimal
    return resultado

numero = float(input("Ingresa el número: "))

porcentaje_str = input("Ingresa el porcentaje que deseas calcular: ")

porcentaje_str = porcentaje_str.rstrip('%')
porcentaje = float(porcentaje_str)

resultado = calcular_porcentaje(numero, porcentaje)

print(f"{porcentaje}% de {numero} es igual a {resultado}")