"""
    programa que suma los numeros 
    dados por el ususario 
    Autor: kevin Aguirre
    Fecha: 10 de octubre de 2023    
"""

producto = int (input("ingrese el precio de el producto: "))
iva = producto * 1.19
total = producto + iva
print("el total del producto es:  " + str (total))