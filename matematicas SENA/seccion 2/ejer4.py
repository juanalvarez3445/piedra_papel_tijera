"""juan caarlos ceballos"""
# Solicitar al usuario que ingrese el precio del producto
precio_producto = float(input("Ingrese el precio del producto: "))

# Calcular el precio final al agregar el IVA del 19%
precio_final = precio_producto * 1.19

# Imprimir el precio final al consumidor
print(f"El precio final al consumidor con un IVA del 19% es: {precio_final:.2f}")