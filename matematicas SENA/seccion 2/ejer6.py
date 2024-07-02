"""
cree un programa que lea una cantidad e imprima un porcentaje a calcular requerido  sobre esa cantidad
"""

cantidad = float(input("ingrese cantidad: "))
porcentaje = float(input("ingrese el porcentajea a calcular: "))

total = (porcentaje/100) * cantidad

print("El porcentaje es: ") + str(total)